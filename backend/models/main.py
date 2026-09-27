from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="CampusTwin AI",
    description="AI-powered student risk prediction API",
    version="1.0",
)


MODEL_PATH = Path(__file__).resolve().with_name("academic_model.pkl")
if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. Please train the model first using ml/train_models.py."
    )
model = joblib.load(MODEL_PATH)


class StudentData(BaseModel):
    attendance: float
    internal_marks: float
    assignment_score: float
    coding_score: float
    aptitude_score: float
    projects: int
    backlogs: int


@app.get("/")
def home():
    return {"message": "CampusTwin AI API is running!"}


@app.post("/predict")
def predict(data: StudentData):
    features = np.array(
        [[
            data.attendance,
            data.internal_marks,
            data.assignment_score,
            data.coding_score,
            data.aptitude_score,
            data.projects,
            data.backlogs,
        ]]
    )

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    risk = "High Risk" if prediction == 1 else "Low Risk"

    return {
        "academic_risk": risk,
        "risk_probability": round(float(probability * 100), 2),
    }


from backend.app import app

__all__ = ["app"]