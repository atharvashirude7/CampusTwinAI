from pathlib import Path

import joblib
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Resolve project paths reliably from this script's location
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "backend" / "models"
MODEL_PATH = MODEL_DIR / "academic_model.pkl"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# For reproducible results
np.random.seed(42)

# Number of students in our demo dataset
n = 1000


# -----------------------------
# 1. CREATE STUDENT DATA
# -----------------------------

attendance = np.random.randint(40, 101, n)

internal_marks = np.random.randint(30, 101, n)

assignment_score = np.random.randint(30, 101, n)

coding_score = np.random.randint(20, 101, n)

aptitude_score = np.random.randint(20, 101, n)

projects = np.random.randint(0, 5, n)

backlogs = np.random.randint(0, 4, n)


# -----------------------------
# 2. CREATE ACADEMIC RISK
# -----------------------------

risk_score = (
    (100 - attendance) * 0.30
    + (100 - internal_marks) * 0.25
    + (100 - assignment_score) * 0.15
    + backlogs * 10
)


# 1 = High Risk
# 0 = Low Risk

academic_risk = np.where(
    risk_score > 45,
    1,
    0
)


# -----------------------------
# 3. CREATE FEATURES
# -----------------------------

X = np.column_stack([
    attendance,
    internal_marks,
    assignment_score,
    coding_score,
    aptitude_score,
    projects,
    backlogs
])


# -----------------------------
# 4. SPLIT DATA
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    academic_risk,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# 5. TRAIN MODEL
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)


# -----------------------------
# 6. TEST MODEL
# -----------------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

print(
    f"Academic Risk Model Accuracy: {accuracy * 100:.2f}%"
)


# -----------------------------
# 7. SAVE MODEL
# -----------------------------

joblib.dump(
    model,
    MODEL_PATH
)

print(f"Academic model saved successfully to {MODEL_PATH}!")