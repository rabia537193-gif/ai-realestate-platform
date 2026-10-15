<div align="center">

# 🏡 AI Real Estate Intelligence Platform
### *Enterprise-Grade Machine Learning Property Valuation & Analytics Engine*

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>Instant property market valuations powered by advanced Machine Learning regression models and a modern glassmorphism web interface.</b>
</p>

</div>

---

## ✨ Key Highlights & Features

- **🤖 High-Precision ML Model**: Powered by a trained `scikit-learn` regression model (`house_price_model.pkl`) optimized for real estate appraisal.
- **💎 Glassmorphism Dashboard UI**: A breathtaking, responsive user interface styled with custom CSS gradients, Google Fonts (*Plus Jakarta Sans*), and FontAwesome icons.
- **💱 Multi-Currency Converter**: Dynamic, real-time conversion engine supporting **USD ($), Pakistani Rupees (PKR ₨), Euros (€), British Pounds (£), UAE Dirham (AED), and Indian Rupees (INR ₹)**.
- **⚡ Quick Property Presets**: One-click preset selectors (*Cozy Home*, *Modern Family*, *Luxury Villa*) for instantaneous testing and evaluation.
- **🚀 Interactive API Documentation**: Fully automated OpenAPI endpoints and Swagger UI integrated directly via FastAPI (`/docs`).

---

## 🏗️ System Architecture & Project Structure

```text
ai-realestate-platform/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application core & route controllers
│   └── templates/
│       └── index.html       # Responsive frontend dashboard UI
│
├── models/
│   └── house_price_model.pkl # Trained Scikit-Learn regression model
│
├── data/                    # Raw housing datasets & preprocessing files
├── notebooks/               # Jupyter notebooks for Exploratory Data Analysis (EDA)
├── scripts/
│   └── train_model.py       # Pipeline script for training the ML model
│
├── requirements.txt         # Project Python dependencies
└── README.md                # Project documentation