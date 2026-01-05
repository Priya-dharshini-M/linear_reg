import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("weather_datas.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🌤️ Weather Temperature Prediction App")
st.write("Predict Daily Temperature using Linear Regression")

# User inputs
hours_sunlight = st.number_input(
    "Enter Hours of Sunlight",
    min_value=0.0,
    max_value=24.0,
    step=0.1
)

humidity_level = st.number_input(
    "Enter Humidity Level (%)",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

# Prediction button
if st.button("Predict Temperature"):
    input_data = np.array([[hours_sunlight, humidity_level]])
    prediction = model.predict(input_data)

    st.success(f"🌡️ Predicted Daily Temperature: {prediction[0]:.2f} °C")
