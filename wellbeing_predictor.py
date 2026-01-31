from joblib import load
import numpy as np

# Load the trained model
model = load("wellbeing_model.pkl")

def predict_wellbeing(features):
    prediction = model.predict(features)[0]
    if prediction == 2:
        return "Good Wellbeing 😊"
    elif prediction == 1:
        return "Average Wellbeing 😐"
    else:
        return "Needs Attention ⚠️"
