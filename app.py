import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("admission_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Masters Admission Prediction App")
st.write("Enter your details to estimate your **Chance of Admission**")

# Input fields
gre = st.number_input("GRE Score", min_value=260, max_value=340, value=320)
toefl = st.number_input("TOEFL Score", min_value=0, max_value=120, value=110)
uni_rating = st.slider("University Rating", 1, 5, 3)
sop = st.slider("SOP Strength", 1.0, 5.0, 3.0)
lor = st.slider("LOR Strength", 1.0, 5.0, 3.0)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=8.5, step=0.01)
research = st.radio("Research Experience", [0, 1])

# Prediction
if st.button("Predict Admission Chance"):
    input_data = np.array([[gre, toefl, uni_rating, sop, lor, cgpa, research]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Chance of Admission: {prediction:.2f}")
