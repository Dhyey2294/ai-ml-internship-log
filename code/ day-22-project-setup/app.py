import streamlit as st
from services.itinerary_service import generate_itinerary
from utils.header_renderer import render_header
from utils.map_renderer import render_route_map
from utils.hotel_renderer import render_hotels
from utils.itinerary_renderer import render_itinerary
from utils.tips_renderer import render_tips
from utils.pdf_generator import generate_pdf

st.set_page_config(
    page_title="AI Travel Planner",
    layout="wide",
    page_icon="🌍"
)

st.markdown(
    "<h1 style='margin-bottom:0;'>🌍 AI Travel Itinerary Planner</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color:gray; margin-top:0;'>Plan smarter. Travel better.</p>",
    unsafe_allow_html=True
)

@st.cache_data(show_spinner=False)
def cached_generate_itinerary(destination, preferences, duration, budget):
    return generate_itinerary(destination, preferences, duration, budget)

with st.sidebar:
    st.header("✈ Trip Configuration")

    destination = st.text_input("Destination (City / Country)")

    preferences = st.multiselect(
        "Trip Preferences",
        ["Popular", "Nature", "Foodie", "Luxury", "Shopping", "Historical", "Adventure", "Family"]
    )

    duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30)

    budget = st.selectbox(
        "Budget Level",
        ["Low-Range", "Mid-Range", "Luxury"]
    )

    st.markdown("---")
    generate = st.button("🚀 Generate Itinerary")

if generate:
    if not destination:
        st.error("Please enter a destination.")
        st.stop()

    with st.spinner("Generating your optimized travel plan..."):
        try:
            data = cached_generate_itinerary(
                destination,
                tuple(preferences),
                duration,
                budget
            )

            data["preferences"] = list(preferences)
            data["total_days"] = duration
            data["budget_level"] = budget

            st.session_state["itinerary_data"] = data

        except Exception as e:
            st.error("Something went wrong while generating the itinerary.")
            st.write("Error:", e)

if "itinerary_data" in st.session_state:

    data = st.session_state["itinerary_data"]

    st.divider()

    render_header(data)
    render_route_map(data)
    render_hotels(data)
    render_itinerary(data)
    render_tips(data)

    st.divider()

    pdf_buffer = generate_pdf(data)

    st.download_button(
        label="📄 Download Itinerary as PDF",
        data=pdf_buffer,
        file_name=f"{data['city_selected']}_Travel_Itinerary.pdf",
        mime="application/pdf"
    )
