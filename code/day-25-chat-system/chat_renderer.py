import streamlit as st
from services.chat_service import chat_about_place


def render_chat(activity, city, day_index, activity_index):

    chat_key = f"chat_{day_index}_{activity_index}"
    input_key = f"input_{day_index}_{activity_index}"
    button_key = f"send_{day_index}_{activity_index}"

    # Initialize chat history
    if chat_key not in st.session_state:
        st.session_state[chat_key] = []

    if input_key not in st.session_state:
        st.session_state[input_key] = ""

    def handle_send():
        user_message = st.session_state[input_key].strip()

        if not user_message:
            return

        # Save user message
        st.session_state[chat_key].append({
            "role": "user",
            "content": user_message
        })

        try:
            answer = chat_about_place(
                activity.get("place"),
                city,
                user_message
            )

            st.session_state[chat_key].append({
                "role": "assistant",
                "content": answer
            })

        except Exception:
            st.session_state[chat_key].append({
                "role": "assistant",
                "content": "⚠️ Could not fetch response."
            })

        # Clear input
        st.session_state[input_key] = ""

    with st.expander("💬 Ask about this place"):

        # Display history
        for message in st.session_state[chat_key]:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**AI:** {message['content']}")

        st.text_input(
            "Ask a question",
            key=input_key
        )

        st.button(
            "Send",
            key=button_key,
            on_click=handle_send
        )
