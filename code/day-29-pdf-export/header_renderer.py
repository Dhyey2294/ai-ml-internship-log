import streamlit as st


def render_header(data):

    st.markdown(f"## 🗺️ {data.get('city_selected', '')}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Duration", f"{data.get('total_days')} Days")
    col2.metric("Budget", data.get("budget_level"))
    col3.metric("Preferences", len(data.get("preferences", [])))

    total_cost = data.get("total_estimated_cost")

    if total_cost:
        st.markdown("### 💰 Estimated Trip Cost")

        st.markdown(
            f"""
            <div style="
                font-size:20px;
                font-weight:500;
                padding:8px 0;
            ">
                {total_cost}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()
