from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from prediction import PredictionInput, predict

app = FastAPI()


# Define the prediction route
@app.post("/predict/")
def get_prediction(data: PredictionInput):
    try:
        # Validate input values before making a prediction
        if not (0 <= data.age <= 120):
            raise HTTPException(status_code=400, detail="Age must be between 0 and 120.")
        if data.sex not in [0, 1]:
            raise HTTPException(status_code=400, detail="Sex must be 0 (Female) or 1 (Male).")
        if not (0 <= data.cp <= 3):
            raise HTTPException(status_code=400, detail="Chest Pain Type must be between 0 and 3.")
        if not (80 <= data.trestbps <= 200):
            raise HTTPException(status_code=400, detail="Resting Blood Pressure must be between 80 and 200.")
        if not (100 <= data.chol <= 400):
            raise HTTPException(status_code=400, detail="Cholesterol must be between 100 and 400.")
        if data.fbs not in [0, 1]:
            raise HTTPException(status_code=400, detail="Fasting Blood Sugar must be 0 (No) or 1 (Yes).")
        if not (0 <= data.restecg <= 2):
            raise HTTPException(status_code=400, detail="Resting Electrocardiographic Results must be between 0 and 2.")
        if not (60 <= data.thalach <= 200):
            raise HTTPException(status_code=400, detail="Maximum Heart Rate Achieved must be between 60 and 200.")
        if data.exang not in [0, 1]:
            raise HTTPException(status_code=400, detail="Exercise Induced Angina must be 0 (No) or 1 (Yes).")
        if not (0.0 <= data.oldpeak <= 6.0):
            raise HTTPException(status_code=400, detail="Oldpeak must be between 0.0 and 6.0.")
        if not (0 <= data.slope <= 2):
            raise HTTPException(status_code=400, detail="Slope must be between 0 and 2.")
        if not (0 <= data.ca <= 3):
            raise HTTPException(status_code=400, detail="Number of Major Vessels must be between 0 and 3.")
        if not (1 <= data.thal <= 3):
            raise HTTPException(status_code=400,
                                detail="Thalassemia must be 1 (Normal), 2 (Fixed defect), or 3 (Reversible defect).")

        # Make the prediction
        return predict(data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# New GET endpoint to retrieve expected parameters
@app.get("/parameters/")
def get_parameters():
    parameters = {
        "age": "int: Age of the patient (0-120)",
        "sex": "int: Gender (0 = Female, 1 = Male)",
        "cp": "int: Chest Pain Type (0-3)",
        "trestbps": "int: Resting Blood Pressure (80-200)",
        "chol": "int: Cholesterol (100-400)",
        "fbs": "int: Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)",
        "restecg": "int: Resting Electrocardiographic Results (0-2)",
        "thalach": "int: Maximum Heart Rate Achieved (60-200)",
        "exang": "int: Exercise Induced Angina (0 = No, 1 = Yes)",
        "oldpeak": "float: Oldpeak (depression induced by exercise relative to rest, 0.0-6.0)",
        "slope": "int: Slope of the Peak Exercise ST Segment (0-2)",
        "ca": "int: Number of Major Vessels (0-3)",
        "thal": "int: Thalassemia (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)"
    }
    return JSONResponse(content=parameters)

# Run the application with: uvicorn main:app --reload
