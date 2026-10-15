import os
import traceback
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="AI Real Estate Platform")

# Setup templates directory
templates = Jinja2Templates(directory="app/templates")

# Model path check & load
MODEL_PATH = "models/house_price_model.pkl"

if os.path.exists(MODEL_PATH):
  try:
    model = joblib.load(MODEL_PATH)
  except Exception as e:
    model = None
    print(f"Error loading model: {e}")
else:
  model = None


class HouseFeatures(BaseModel):
  country: str
  city: str
  OverallQual: int
  GrLivArea: int
  GarageCars: int
  TotalBsmtSF: int
  FirstFlrSF: int
  FullBath: int
  TotRmsAbvGrd: int
  YearBuilt: int


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
  try:
    return templates.TemplateResponse(request, "index.html", {})
  except Exception as e:
    error_trace = traceback.format_exc()
    return PlainTextResponse(
        f"Detailed Template Error:\n\n{error_trace}", status_code=500
    )


@app.post("/predict")
def predict_price(features: HouseFeatures):
  if model is None:
    raise HTTPException(status_code=500, detail="Model file not found!")

  # Input data for the ML model (using the 8 numerical features)
  input_data = np.array([[
      features.OverallQual,
      features.GrLivArea,
      features.GarageCars,
      features.TotalBsmtSF,
      features.FirstFlrSF,
      features.FullBath,
      features.TotRmsAbvGrd,
      features.YearBuilt,
  ]])

  base_prediction = model.predict(input_data)[0]

  # Optional location-based multiplier logic to make it realistic per city/country
  multiplier = 1.0
  if features.city.lower() in ["karachi", "lahore", "islamabad"]:
    multiplier = 0.85  # Regional adjustment example
  elif features.city.lower() in ["new york", "london", "dubai"]:
    multiplier = 1.35

  final_price = base_prediction * multiplier

  return {
      "predicted_price_usd": round(float(final_price), 2),
      "location": f"{features.city}, {features.country}",
      "status": "Success",
  }