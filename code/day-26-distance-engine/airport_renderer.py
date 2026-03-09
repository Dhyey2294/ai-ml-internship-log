import streamlit as st
from utils.distance_calculator import (
    calculate_distance_km,
    estimate_travel_time_minutes,
    estimate_taxi_fare_range,
)


def render_airport_transfer(data):

    if not data.get("nearest_airport") or not data.get("itinerary"):
        return

    airport = data["nearest_airport"]

    try:
        first_activity = data["itinerary"][0]["activities"][0]

        distance = calculate_distance_km(
            airport.get("latitude"),
            airport.get("longitude"),
            first_activity.get("latitude"),
            first_activity.get("longitude")
        )

        travel_time = estimate_travel_time_minutes(distance)
        fare_range = estimate_taxi_fare_range(distance)

        st.markdown("## ✈️ Airport Transfer")

        st.markdown(f"""
**Nearest Airport:** {airport.get('airport_name')} ({airport.get('airport_code')})

📍 Location: {airport.get('latitude')}, {airport.get('longitude')}

🚕 Distance to First Stop: {distance} km  
🕒 Estimated Travel Time: {travel_time} minutes  
💰 Estimated Taxi Fare Range: {fare_range}
""")

        maps_link = (
            f"https://www.google.com/maps/dir/"
            f"{airport.get('latitude')},{airport.get('longitude')}/"
            f"{first_activity.get('latitude')},{first_activity.get('longitude')}"
        )

        st.markdown(f"[🗺️ Open Taxi Route in Google Maps]({maps_link})")
        st.divider()

    except:
        st.warning("Airport transfer details unavailable.")
