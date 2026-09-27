from fastapi import FastAPI
from pydantic import BaseModel

from backend.models import StudentUpdateRequest
from backend.services.prediction import predict_risk

app = FastAPI(
    title="CampusTwin AI",
    description="AI-powered student intelligence system",
    version="1.0.0",
)


class StudentInput(BaseModel):
    student_name: str | None = None
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
def predict(payload: StudentInput):
    data = payload.model_dump(exclude={"student_name"})
    result = predict_risk(data)
    if payload.student_name:
        result["student_name"] = payload.student_name
    return result


@app.get("/students")
def get_students():
    return [
        {
            "student_id": "STU-1001",
            "name": "Aisha Sharma",
            "department": "Computer Science",
            "year": 3,
            "attendance": 88,
            "internal_marks": 81,
            "assignment_score": 76,
            "coding_score": 90,
            "aptitude_score": 72,
            "projects": 3,
            "backlogs": 1,
        },
        {
            "student_id": "STU-1002",
            "name": "Rahul Verma",
            "department": "Information Technology",
            "year": 2,
            "attendance": 71,
            "internal_marks": 65,
            "assignment_score": 69,
            "coding_score": 62,
            "aptitude_score": 58,
            "projects": 1,
            "backlogs": 2,
        },
    ]


@app.post("/students")
def create_student(student: StudentUpdateRequest):
    return {
        "message": "Student profile received",
        "student": student.model_dump(exclude_none=True),
    }
