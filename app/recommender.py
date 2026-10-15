import pandas as pd


class PropertyRecommender:

  def __init__(self, dataset_path: str):
    self.df = pd.read_csv(dataset_path)

  def recommend(
      self,
      max_budget: float,
      neighborhood: str,
      min_baths: int = 1,
      top_n: int = 3,
  ) -> list:
    filtered = self.df[
        (self.df["SalePrice"] <= max_budget)
        & (self.df["Neighborhood"] == neighborhood)
        & (self.df["FullBath"] >= min_baths)
    ].copy()

    # Relax location constraint if zero initial hits are found
    if filtered.empty:
      filtered = self.df[
          (self.df["SalePrice"] <= max_budget)
          & (self.df["FullBath"] >= min_baths)
      ].copy()

    if filtered.empty:
      return []

    # Score properties by quality density relative to listing price
    filtered["score"] = (filtered["OverallQual"] * 100000) / filtered[
        "SalePrice"
    ]
    ranked = filtered.sort_values(by="score", ascending=False).head(top_n)

    recommendations = []
    for _, row in ranked.iterrows():
      recommendations.append({
          "Id": int(row["Id"]),
          "Neighborhood": row["Neighborhood"],
          "Price": float(row["SalePrice"]),
          "GrLivArea": float(row["GrLivArea"]),
          "OverallQual": int(row["OverallQual"]),
          "FullBath": int(row["FullBath"]),
          "Explanation": (
              f"Priced at ${row['SalePrice']:,.0f} (within budget threshold"
              f" ${max_budget:,.0f}). Delivers an overall quality index of"
              f" {row['OverallQual']}/10, {row['GrLivArea']} sqft living area,"
              f" built in {row['YearBuilt']}."
          ),
      })

    return recommendations