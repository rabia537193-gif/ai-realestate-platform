import os
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBRegressor


class RealEstateMLPipeline:

  def __init__(self, model_path="models/xgboost_house_price.pkl"):
    self.model_path = model_path
    self.pipeline = None
    self.num_cols = [
        "OverallQual",
        "GrLivArea",
        "TotalBsmtSF",
        "GarageCars",
        "1stFlrSF",
        "FullBath",
        "YearBuilt",
        "YearRemodAdd",
    ]
    self.cat_cols = ["Neighborhood", "HouseStyle", "SaleCondition"]

  def build_and_train(self, df_path: str):
    df = pd.read_csv(df_path)

    # Clean extreme outliers (as recommended in Kaggle kernel analyses)
    df = df.drop(
        df[(df["GrLivArea"] > 4000) & (df["SalePrice"] < 300000)].index
    )

    X = df[self.num_cols + self.cat_cols]
    y = np.log1p(df["SalePrice"])

    num_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    cat_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_transformer, self.num_cols),
            ("cat", cat_transformer, self.cat_cols),
        ]
    )

    self.pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "regressor",
                XGBRegressor(
                    n_estimators=300,
                    learning_rate=0.05,
                    max_depth=5,
                    random_state=42,
                ),
            ),
        ]
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    self.pipeline.fit(X_train, y_train)

    preds = self.pipeline.predict(X_val)
    rmsle = np.sqrt(mean_squared_error(y_val, preds))
    r2 = r2_score(y_val, preds)
    print(f"[ML Model Trained] Validation RMSLE: {rmsle:.4f} | R²: {r2:.4f}")

    os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
    joblib.dump(self.pipeline, self.model_path)

  def load_model(self):
    self.pipeline = joblib.load(self.model_path)

  def predict_price(self, input_dict: dict) -> float:
    df_in = pd.DataFrame([input_dict])
    log_pred = self.pipeline.predict(df_in)[0]
    return float(np.expm1(log_pred))