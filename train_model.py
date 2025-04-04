import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Define the features and load your dataset
feature_names = [
    'Size_m', 'Velocity_km_s', 'Altitude_km', 'Mass_kg',
    'Solar_Activity_Index', 'Radiation_Exposure_Level', 'Debris_Density_in_Region'
]

# Adjust the CSV path as needed
df = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\college projects\space-debris-risk-predictor\data\space_debris_binary_risk.csv")

# Select features and target (replace 'Risk_Category' with your target column name)
X = df[feature_names]
y = df['Risk_Category']

# Train the RandomForest model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the model and feature names together in a tuple
joblib.dump((model, feature_names), "rf_model.pkl")
print("Model trained and saved!")
