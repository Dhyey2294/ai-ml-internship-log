import streamlit as st
import folium
from streamlit_folium import st_folium


def render_route_map(data):

    st.markdown("## 🗺️ Route Overview")

    points = []
    counter = 1

    for day_index, day in enumerate(data.get("itinerary", [])):
        for activity_index, activity in enumerate(day.get("activities", [])):

            lat = activity.get("latitude")
            lon = activity.get("longitude")

            if not lat or not lon:
                continue

            try:
                lat = round(float(lat), 5)
                lon = round(float(lon), 5)
            except (ValueError, TypeError):
                continue

            points.append({
                "name": activity.get("place", "Unknown"),
                "lat": lat,
                "lon": lon,
                "order": counter,
                "day_index": day_index,
                "activity_index": activity_index
            })

            counter += 1

    if not points:
        st.info("Map not available for this itinerary.")
        return

    # Create map centered on first point
    m = folium.Map(
        location=[points[0]["lat"], points[0]["lon"]],
        zoom_start=12
    )

    # Draw route line
    route_coords = [[p["lat"], p["lon"]] for p in points]
    folium.PolyLine(route_coords, color="red", weight=4).add_to(m)

    # Add numbered markers (restore original UI)
    for idx, point in enumerate(points):

        if idx == 0:
            color = "green"
        elif idx == len(points) - 1:
            color = "blue"
        else:
            color = "red"

        folium.Marker(
            location=[point["lat"], point["lon"]],
            tooltip=f"{point['order']}. {point['name']}",
            icon=folium.Icon(color=color, icon="info-sign"),
        ).add_to(m)

    # Render map
    map_data = st_folium(m, width=1000, height=500)

    # Detect clicked marker using lat/lon (stable after rounding)
    if map_data and map_data.get("last_object_clicked"):

        clicked_lat = round(map_data["last_object_clicked"]["lat"], 5)
        clicked_lon = round(map_data["last_object_clicked"]["lng"], 5)

        for point in points:
            if point["lat"] == clicked_lat and point["lon"] == clicked_lon:
                st.session_state["scroll_to"] = (
                    point["day_index"],
                    point["activity_index"]
                )
                st.rerun()

    st.divider()
