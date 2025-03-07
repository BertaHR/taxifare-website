import streamlit as st
from geopy.geocoders import Nominatim


st.title("📍 Convert Coordinates to Address")

latitude = st.number_input("Enter Latitude", format="%.6f")
longitude = st.number_input("Enter Longitude", format="%.6f")


if st.button("📡 Convert"):
    geolocator = Nominatim(user_agent="geoapp")
    location = geolocator.reverse((latitude, longitude), language="en")

    if location:
        st.success(f"🏠 Address: {location.address}")
    else:
        st.error("❌ Address not found. Try other coordinates.")
