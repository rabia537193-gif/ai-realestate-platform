import os
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Directories setup
os.makedirs("models", exist_ok=True)

# 2. Load dataset
data_path = "data/raw/train.csv"
if not os.path.exists(data_path):
    print(f"Error: {data_path} file nahi mili!")
    exit()

df = pd.read_csv(data_path)
print("Data successfully loaded!")

# 3. Select important numerical features for House Price Prediction
features = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "TotalBsmtSF",
    "1stFlrSF",
    "FullBath",
    "TotRmsAbvGrd",
    "YearBuilt",
]
target = "SalePrice"

# Missing values handle karein
X = df[features].copy()
y = df[target].copy()

X = X.fillna(X.median())

# 4. Train/Test split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate Model
y_pred = model.predict(X_val)
rmse = np.sqrt(mean_squared_error(y_val, y_pred))
r2 = r2_score(y_val, y_pred)

print(f"Model Training Complete!")
print(f"Validation RMSE: ${rmse:,.2f}")
print(f"Validation R2 Score: {r2:.4f}")

# 7. Save model
model_path = "models/house_price_model.pkl"
joblib.dump(model, model_path)
print(f"Model successfully saved at: {model_path}")