<div align="center">

# 🏡 AI Real Estate Intelligence Platform
### *Global Machine Learning Property Valuation & Market Analytics Engine*

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://ai-realestate-platform-seven.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>An advanced worldwide property valuation engine supporting international countries, dynamic cascading cities, multi-currency conversion, and real-time Chart.js market analytics.</b>
</p>

</div>

---

## 🌐 Live Application
- **Access the Live Platform here**: [ai-realestate-platform-seven.vercel.app](https://ai-realestate-platform-seven.vercel.app)

---

## ✨ Key Highlights & Features

- **🤖 High-Precision ML Engine**: Powered by a trained `scikit-learn` regression model (`house_price_model.pkl`) for reliable property valuation.
- **🌍 Worldwide Location Selector**: Dynamic cascading dropdowns supporting major global countries (Pakistan, UAE, USA, UK, Canada, Australia, Saudi Arabia, Turkey, Germany, France, India) and their key cities.
- **📊 Interactive Visual Analytics**: Real-time **Chart.js** graphs displaying price trends by quality rating and regional city valuation multipliers.
- **💎 Glassmorphism Dashboard UI**: Modern responsive side-by-side dashboard layout styled with custom CSS gradients and Google Fonts (*Plus Jakarta Sans*).
- **💱 Global Multi-Currency Converter**: Real-time conversion engine supporting **USD ($), Pakistani Rupees (PKR ₨), British Pounds (£), UAE Dirhams (AED), Euros (€), Canadian Dollars (CAD), Australian Dollars (AUD), Saudi Riyals (SAR), and Indian Rupees (INR ₹)**.
- **⚡ Quick Property Presets**: One-click preset loaders (*Cozy Home*, *Modern Family*, *Luxury Villa*) for rapid evaluation.

---

## 🏗️ System Architecture & Project Structure

```text
ai-realestate-platform/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application core & route controllers
│   └── templates/
│       └── index.html       # Responsive frontend dashboard UI & Chart.js integration
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