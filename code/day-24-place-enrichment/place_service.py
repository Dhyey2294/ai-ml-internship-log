from services.gemini_client import call_model, extract_json


def enrich_place_details(place_name: str, city: str):

    prompt = f"""
Provide structured JSON for:

Place Name: {place_name}
City: {city}

Return ONLY:

{{
  "place": "",
  "category": "",
  "latitude": "",
  "longitude": "",
  "description": "",
  "estimated_cost": ""
}}

Return ONLY JSON.
"""

    response = call_model(prompt)
    return extract_json(response)
