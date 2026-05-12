import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

# Title
st.title("Student Performance Prediction System")

st.write("Enter Student Details")

# Input fields
study_time = st.number_input(
    "Study Hours",
    min_value=0.0
)

absences = st.number_input(
    "Absences",
    min_value=0
)

gpa = st.number_input(
    "GPA",
    min_value=0.0,
    max_value=4.0
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0,
    max_value=100
)

# Predict button
if st.button("Predict"):

    input_data = np.array([[
        study_time,
        absences,
        gpa,
        attendance
    ]])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Grade: {prediction[0]}"
    )

    # Risk detection
    if prediction[0] <= 1:
        st.error("Student is At Risk")
    else:
        st.success(
            "Student Performance is Good"
        )

    # Recommendations
    st.subheader("Recommendations")

    st.write("- Increase study hours")
    st.write("- Improve attendance")
    st.write("- Complete assignments regularly")