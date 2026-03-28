import streamlit as st
import requests

st.title("🎓 Student Marks Predictor")

# Input from user
hours = st.number_input("Enter study hours")

if st.button("Predict"):

    url = "https://fastapi-app-5gt0.onrender.com/predict"

    try:
        response = requests.post(url, json={"hours": hours})

        # Show status for debugging
        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Marks: {result['marks']}")
        else:
            st.error("API Error")
            st.write(response.text)

    except Exception as e:
        st.error("Server is sleeping 😴 or network issue")
        st.write(e)

