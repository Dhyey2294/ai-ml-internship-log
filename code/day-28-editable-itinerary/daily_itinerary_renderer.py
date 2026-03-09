import streamlit as st
from utils.distance_calculator import calculate_daily_distances
from services.place_service import enrich_place_details
from utils.chat_renderer import render_chat


def generate_google_maps_link(place_name, lat, lon):
    query = place_name.replace(" ", "+")
    return f"https://www.google.com/maps/search/?api=1&query={query}+{lat},{lon}"


def render_daily_itinerary(data):

    daily_distances, _, segment_distances, segment_times = calculate_daily_distances(
        data.get("itinerary", [])
    )

    st.markdown("## 🗓️ Itinerary")

    for day_index, day in enumerate(data.get("itinerary", [])):

        day_number = day.get("day")
        activities = day.get("activities", [])

        segments = segment_distances.get(day_number, [])
        times = segment_times.get(day_number, [])

        with st.expander(
            f"Day {day_number} • {daily_distances.get(day_number, 0)} km travel",
            expanded=True
        ):

            for i, activity in enumerate(activities):

                place = activity.get("place")
                lat = activity.get("latitude")
                lon = activity.get("longitude")

                maps_link = generate_google_maps_link(place, lat, lon)

                col1, col2 = st.columns([8, 1])

                with col1:
                    st.markdown(
                        f"""
<h4>⏰ {activity.get('time')}</h4>
📍 <b><a href="{maps_link}" target="_blank">{place}</a></b><br>
Category: {activity.get('category')}<br>
Location: {lat}, {lon}<br><br>
{activity.get('description')}
""",
                        unsafe_allow_html=True
                    )

                    if activity.get("estimated_cost"):
                        st.markdown(
                            f"💵 Estimated Cost: {activity.get('estimated_cost')}"
                        )

                    if i < len(segments):
                        st.markdown(
                            f"➡️ Distance to next stop: **{segments[i]} km**"
                        )
                        st.markdown(
                            f"🚗 Estimated Travel Time: **{times[i]} minutes**"
                        )
                        st.markdown("---")

                with col2:
                    if st.button("❌", key=f"remove_{day_index}_{i}"):
                        st.session_state["itinerary_data"]["itinerary"][day_index]["activities"].pop(i)
                        st.rerun()

                render_chat(activity, data.get("city_selected"), day_index, i)

            with st.expander(f"➕ Add Place to Day {day_number}"):

                new_place = st.text_input(
                    "Place Name",
                    key=f"new_place_{day_index}"
                )

                if st.button("Add Place", key=f"add_btn_{day_index}"):

                    if not new_place:
                        st.warning("Please enter a place name.")
                    else:
                        with st.spinner("Fetching place details..."):
                            try:
                                place_data = enrich_place_details(
                                    new_place,
                                    data.get("city_selected")
                                )

                                new_activity = {
                                    "time": "Custom Time",
                                    "place": place_data.get("place"),
                                    "category": place_data.get("category"),
                                    "latitude": place_data.get("latitude"),
                                    "longitude": place_data.get("longitude"),
                                    "description": place_data.get("description"),
                                    "estimated_cost": place_data.get("estimated_cost")
                                }

                                st.session_state["itinerary_data"]["itinerary"][day_index]["activities"].append(new_activity)
                                st.rerun()

                            except:
                                st.error("Could not fetch place details.")

        st.divider()
