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


# pickup_datetime: str,  # 2014-07-06 19:18:00
        # pickup_longitude: float,    # -73.950655
        # pickup_latitude: float,     # 40.783282
        # dropoff_longitude: float,   # -73.984365
        # dropoff_latitude: float,    # 40.769802
        # passenger_count: 
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')



'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''