import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# ✅ Set page config as the very first Streamlit command
st.set_page_config(page_title="Space Debris ML App", layout="wide")

# Load the model
with open("models/rf_model.pkl", "rb") as file:
    model, feature_names = joblib.load(file)

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\college projects\space-debris-risk-predictor\data\space_debris_data.csv")

df = load_data()

# App title
st.title("🚀 Space Debris Risk Prediction")

# Sidebar inputs
st.sidebar.header("Input Debris Parameters")

size = st.sidebar.slider("Size (m)", 0.0, 10.0, 1.0)
velocity = st.sidebar.slider("Velocity (km/s)", 0.0, 20.0, 7.5)
altitude = st.sidebar.slider("Altitude (km)", 100.0, 2000.0, 500.0)
mass = st.sidebar.slider("Mass (kg)", 0.0, 1000.0, 100.0)
solar_index = st.sidebar.slider("Solar Activity Index", 0.0, 300.0, 100.0)
radiation = st.sidebar.slider("Radiation Exposure Level", 0.0, 100.0, 25.0)
density = st.sidebar.slider("Debris Density in Region", 0.0, 100.0, 10.0)

# Collect user input
user_input = pd.DataFrame({
    'Size_m': [size],
    'Velocity_km_s': [velocity],
    'Altitude_km': [altitude],
    'Mass_kg': [mass],
    'Solar_Activity_Index': [solar_index],
    'Radiation_Exposure_Level': [radiation],
    'Debris_Density_in_Region': [density]
})

# Predict button
if st.sidebar.button("Predict Risk Category"):
    prediction = model.predict(user_input)[0]  # Make sure model input matches column names
    st.success(f"Predicted Risk Category: {prediction}")

# Show raw dataset
with st.expander("🔍 Show Raw Dataset"):
    st.dataframe(df)

# Correlation Heatmap
st.subheader("📊 Feature Correlation")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
