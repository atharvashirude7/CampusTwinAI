from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "academic_model.pkl"


if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found at {MODEL_PATH}. Please train the model first."
    )

MODEL = joblib.load(MODEL_PATH)


def predict_risk(student_data: dict) -> dict:
    features = np.array([
        [
            student_data["attendance"],
            student_data["internal_marks"],
            student_data["assignment_score"],
            student_data["coding_score"],
            student_data["aptitude_score"],
            student_data["projects"],
            student_data["backlogs"],
        ]
    ])

    prediction = MODEL.predict(features)[0]
    probability = MODEL.predict_proba(features)[0][1]

    risk = "High Risk" if prediction == 1 else "Low Risk"

    return {
        "academic_risk": risk,
        "risk_probability": round(float(probability * 100), 2),
    }
