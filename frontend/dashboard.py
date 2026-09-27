import streamlit as st

st.title("🎓 CampusTwin Dashboard")

st.subheader("Student Overview")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Students", 1200)
with col2:
    st.metric("At Risk", 148)
with col3:
    st.metric("Avg Attendance", "86%")

st.divider()

st.markdown("### Top Priority Students")

students = [
    {"name": "Aisha Sharma", "risk": "Low Risk", "score": "18%"},
    {"name": "Rahul Verma", "risk": "High Risk", "score": "72%"},
    {"name": "Meera Iyer", "risk": "Medium Risk", "score": "42%"},
]

for student in students:
    st.write(f"- {student['name']}: {student['risk']} ({student['score']})")
