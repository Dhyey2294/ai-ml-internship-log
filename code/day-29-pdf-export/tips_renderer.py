import streamlit as st

def render_tips(data):
    st.markdown("## ✈️ Travel Tips")
    for tip in data.get("travel_tips", []):
        st.markdown(f"- {tip}")
