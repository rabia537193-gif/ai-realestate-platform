import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


class RAGEngine:

  def __init__(self, docs_dir: str = "data/knowledge_base"):
    self.docs_dir = docs_dir
    self.vector_store = None
    self.rag_chain = None

  def initialize_rag(self):
    os.makedirs(self.docs_dir, exist_ok=True)
    sample_doc = os.path.join(self.docs_dir, "real_estate_guide.txt")

    if not os.path.exists(sample_doc):
      with open(sample_doc, "w") as f:
        f.write(
            "Ames Property Tax Guide: Property taxes in Ames average 1.5% of"
            " market valuation annually. Zoning Regulations: Residential High"
            " Density (RH) permits multi-family apartment complexes. Residential"
            " Low Density (RL) requires single-family detached homes with a"
            " minimum 50ft lot frontage. Financing Tips: Down payments below 20%"
            " typically trigger Private Mortgage Insurance (PMI) requirements."
        )

    loader = DirectoryLoader(self.docs_dir, glob="*.txt", loader_cls=TextLoader)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40)
    splits = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    self.vector_store = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        collection_name="real_estate_knowledge",
    )

    retriever = self.vector_store.as_retriever(search_kwargs={"k": 2})

    template = """Answer the question based only on the provided context:
{context}

Question: {question}
Answer:"""
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

    self.rag_chain = (
        {
            "context": retriever
            | (lambda docs: "\n\n".join(d.page_content for d in docs)),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

  def ask(self, query: str) -> str:
    if not self.rag_chain:
      return "RAG Knowledge engine is offline or uninitialized."
    try:
      return self.rag_chain.invoke(query)
    except Exception as e:
      return f"Error executing RAG pipeline: {str(e)}"