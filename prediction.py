# model.py
import joblib
import pandas as pd
from pydantic import BaseModel

# Load your trained model
model = joblib.load("model/random_forest.joblib")


# Define the input data model
class PredictionInput(BaseModel):
    age: int
    sex: int  # 0 = Female, 1 = Male
    cp: int  # Chest Pain Type (0-3)
    trestbps: int  # Resting Blood Pressure
    chol: int  # Cholesterol
    fbs: int  # Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)
    restecg: int  # Resting Electrocardiographic Results (0-2)
    thalach: int  # Maximum Heart Rate Achieved
    exang: int  # Exercise Induced Angina (0 = No, 1 = Yes)
    oldpeak: float  # Oldpeak (depression induced by exercise relative to rest)
    slope: int  # Slope of the Peak Exercise ST Segment (0-2)
    ca: int  # Number of Major Vessels (0-3)
    thal: int  # Thalassemia (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)


# Optional: Create a function to handle predictions
def predict(input_data: PredictionInput):
    data_array = [[
        input_data.age,
        input_data.sex,
        input_data.cp,
        input_data.trestbps,
        input_data.chol,
        input_data.fbs,
        input_data.restecg,
        input_data.thalach,
        input_data.exang,
        input_data.oldpeak,
        input_data.slope,
        input_data.ca,
        input_data.thal
    ]]

    input_df = pd.DataFrame(data_array, columns=[
        "age", "sex", "cp", "trestbps", "chol", "fbs",
        "restecg", "thalach", "exang", "oldpeak",
        "slope", "ca", "thal"
    ])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    return {
        "Prediction": "Disease" if prediction == 1 else "No Disease",
        "Probability of No Disease": round(probability[0], 4),
        "Probability of Disease": round(probability[1], 4)
    }
