import streamlit as st
import urllib.parse


def generate_google_maps_link(place_name, lat, lon):
    query = urllib.parse.quote_plus(f"{place_name} {lat},{lon}")
    return f"https://www.google.com/maps/search/?api=1&query={query}"


def render_hotels(data):

    hotels = data.get("recommended_hotels", [])

    if not hotels:
        return

    st.markdown("## 🏨 Recommended Hotels")

    for hotel in hotels:

        name = hotel.get("name", "Hotel")
        category = hotel.get("category", "N/A")
        price = hotel.get("price_range", "N/A")
        lat = hotel.get("latitude")
        lon = hotel.get("longitude")

        maps_link = None

        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                maps_link = generate_google_maps_link(name, lat, lon)
            except:
                maps_link = None

        if maps_link:
            st.markdown(
                f"### 🔗 <a href='{maps_link}' target='_blank'>{name}</a>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(f"### {name}")

        st.markdown(f"Category: {category}")

        st.markdown(
            f"<div style='font-size:15px;'>Price per night: {price}</div>",
            unsafe_allow_html=True
        )

        if lat and lon:
            st.markdown(f"📍 Location: {lat}, {lon}")

        st.divider()
