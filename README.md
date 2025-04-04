# 🚀 Space Debris Risk Predictor 🌌  
Predict the risk level of space debris using machine learning!

[![Streamlit App](https://img.shields.io/badge/Made%20with-Streamlit-orange?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)

---

## 🌠 Overview

This project leverages a **Random Forest Classifier** to predict the **risk category** (e.g., Low, Medium, High) of space debris based on physical and environmental parameters. It features an intuitive **Streamlit web app** interface where users can input data and get real-time risk assessments.

> Think of it as your mini **NASA control panel** to monitor threats in orbit! 🌍🛰️

---

## ✨ Features

- 🎯 **Accurate ML Model** trained on realistic debris data  
- 📊 **Interactive Heatmaps** for correlation exploration  
- 🧠 **Live Predictions** from a trained Random Forest model  
- 💡 **Real-time UI** powered by Streamlit  
- 📁 Organized project structure with modular components

---

## 📂 Project Structure

```
space-debris-risk-predictor/
│
├── data/
│   └── space_debris_binary_risk.csv       # Dataset used
│
├── models/
│   └── rf_model.pkl                       # Trained model (Random Forest)
│
├── main.py                                # Streamlit app code
├── train_model.py                         # Model training script
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```
---

## 🔍 Parameters Used for Prediction

- `Size_m` – Size of debris in meters  
- `Velocity_km_s` – Orbital velocity  
- `Altitude_km` – Altitude from Earth  
- `Mass_kg` – Mass of debris  
- `Solar_Activity_Index` – Solar conditions affecting orbits  
- `Radiation_Exposure_Level` – Space radiation around the object  
- `Debris_Density_in_Region` – Crowdedness in space sector

---

## ⚙️ Installation & Usage

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/psykickguy/space-debris-risk-predictor.git
cd space-debris-risk-predictor

```
### 📦 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 🚀 3. Run the App

```bash
streamlit run main.py
```

Then open the local URL (usually `http://localhost:8501`) in your browser.

