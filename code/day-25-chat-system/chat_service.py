from services.gemini_client import call_model


def chat_about_place(place_name: str, city: str, user_question: str):

    prompt = f"""
You are a place-specific travel assistant.

Place: {place_name}
City: {city}

User Question:
{user_question}

Rules:
1. ONLY answer questions directly related to this place.
2. Maximum 3 sentences.
3. No bullet points.
4. Plain text only.
"""

    try:
        response = call_model(prompt)
        return response.strip()
    except Exception:
        return "⚠️ Unable to fetch response."
