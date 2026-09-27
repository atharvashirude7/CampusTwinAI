import os

import requests
import streamlit as st


API_URL = os.getenv("CAMPUS_TWIN_API_URL", "https://campustwinai.onrender.com")


st.set_page_config(page_title="CampusTwin AI", page_icon="🎓", layout="wide")
st.title("🎓 CampusTwin AI")
st.subheader("AI-Powered Student Intelligence System")

st.markdown("### Dashboard Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Students", 1200)
with col2:
    st.metric("At Risk", 148)
with col3:
    st.metric("Average Attendance", "86%")

st.divider()

st.markdown("### Top Priority Students")
priority = [
    {"name": "Aisha Sharma", "risk": "Low Risk", "score": "18%"},
    {"name": "Rahul Verma", "risk": "High Risk", "score": "72%"},
    {"name": "Meera Iyer", "risk": "Medium Risk", "score": "42%"},
]
for student in priority:
    st.write(f"- {student['name']}: {student['risk']} ({student['score']})")

st.divider()

st.header("👨‍🎓 Student Risk Prediction")
student_name = st.text_input("Student Name", value="Aisha Sharma")

col1, col2 = st.columns(2)
with col1:
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    internal_marks = st.slider("Internal Marks (%)", 0, 100, 70)
    assignment_score = st.slider("Assignment Score (%)", 0, 100, 70)
    coding_score = st.slider("Coding Score (%)", 0, 100, 60)
with col2:
    aptitude_score = st.slider("Aptitude Score (%)", 0, 100, 60)
    projects = st.number_input("Number of Projects", min_value=0, max_value=10, value=2)
    backlogs = st.number_input("Number of Backlogs", min_value=0, max_value=10, value=0)

if st.button("🚀 Analyze Student", use_container_width=True):
    payload = {
        "student_name": student_name,
        "attendance": attendance,
        "internal_marks": internal_marks,
        "assignment_score": assignment_score,
        "coding_score": coding_score,
        "aptitude_score": aptitude_score,
        "projects": projects,
        "backlogs": backlogs,
    }

    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Analysis completed for {student_name}!")
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Academic Risk", result["academic_risk"])
            with col_b:
                st.metric("Risk Probability", f'{result["risk_probability"]}%')
        else:
            st.error(f"FastAPI returned an error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error(f"❌ Could not connect to backend at {API_URL}.")