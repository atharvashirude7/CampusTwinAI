from typing import Optional

from pydantic import BaseModel


class StudentProfile(BaseModel):
    student_id: str
    name: str
    department: str
    year: int
    attendance: float
    internal_marks: float
    assignment_score: float
    coding_score: float
    aptitude_score: float
    projects: int
    backlogs: int


class StudentUpdateRequest(BaseModel):
    student_id: Optional[str] = None
    name: Optional[str] = None
    department: Optional[str] = None
    year: Optional[int] = None
    attendance: Optional[float] = None
    internal_marks: Optional[float] = None
    assignment_score: Optional[float] = None
    coding_score: Optional[float] = None
    aptitude_score: Optional[float] = None
    projects: Optional[int] = None
    backlogs: Optional[int] = None


class PredictionResponse(BaseModel):
    academic_risk: str
    risk_probability: float
