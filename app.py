import streamlit as st

import requests
import datetime

# Page title
st.title("🚖 Taxi Fare Prediction")

st.markdown("""
### Enter ride details:
""")

# 1️⃣ User input fields
pickup_datetime = st.text_input("📅 Date and Time (YYYY-MM-DD HH:MM:SS)", str(datetime.datetime.now()))
pickup_longitude = st.number_input("📍 Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("📍 Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("🎯 Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("🎯 Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("🧑‍🤝‍🧑 Number of Passengers", min_value=1, max_value=8, value=1, step=1)

# 2️⃣ API request setup
url = 'https://taxifare.lewagon.ai/predict'  # Replace with your API if needed

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'

# 3️⃣ API call button
if st.button("📡 Get Fare Prediction"):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            fare = response.json().get("fare", "Prediction Error")
            st.success(f"💰 Predicted Fare: ${fare:.2f}")
        else:
            st.error("Error calling the API")
    except Exception as e:
        st.error(f"Request error: {e}")

# Final message
st.markdown("🚀 Try entering different values and get your fare prediction!")
