import os
import json
import re
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_json(text: str):
    if not text:
        raise ValueError("Empty response from Gemini")

    cleaned = text.strip()
    cleaned = re.sub(r"```json", "", cleaned)
    cleaned = re.sub(r"```", "", cleaned)

    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON found in response")

    return json.loads(cleaned[start:end + 1])


def call_model(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text
            raise ValueError("Empty model response")
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(1.5)
