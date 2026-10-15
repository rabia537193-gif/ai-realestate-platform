import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("assets", exist_ok=True)

df = pd.read_csv("data/raw/train.csv")
print("Data successfully load ho gaya!")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")

plt.figure(figsize=(8, 5))
sns.histplot(df['SalePrice'], kde=True, color='blue')
plt.title("House Price Distribution")
plt.savefig("assets/target_distribution.png")
plt.close()

print("Graph saved: assets/target_distribution.png")