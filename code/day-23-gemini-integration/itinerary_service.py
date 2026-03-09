from services.gemini_client import call_model, extract_json


def generate_itinerary(destination, preferences, duration, budget):

    preference_string = ", ".join(preferences)

    prompt = f"""
You are an expert AI Travel Planner.

Generate a detailed {duration}-day travel itinerary.

Destination: {destination}
Preferences: {preference_string}
Budget Level: {budget}

Return ONLY valid JSON in EXACT structure:

{{
  "city_selected": "{destination}",
  "nearest_airport": {{
      "airport_name": "",
      "airport_code": "",
      "latitude": "",
      "longitude": ""
  }},
  "total_days": {duration},
  "budget_level": "{budget}",
  "preferences": {preferences},
  "total_estimated_cost": "",
  "recommended_hotels": [
    {{
      "name": "",
      "category": "",
      "price_range": "",
      "latitude": "",
      "longitude": ""
    }}
  ],
  "itinerary": [
    {{
      "day": 1,
      "activities": [
        {{
          "time": "",
          "place": "",
          "category": "",
          "latitude": "",
          "longitude": "",
          "description": "",
          "estimated_cost": ""
        }}
      ]
    }}
  ],
  "travel_tips": []
}}

Return ONLY JSON.
"""

    response = call_model(prompt)
    return extract_json(response)
