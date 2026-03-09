# Day 25 – 17 Feb 2026
## 💬 Place-Specific Chat Assistant

## 🎯 Objective
To allow users to ask contextual questions about individual places in the itinerary.

## 🔹 Work Done
- Implemented place-specific chat service using Gemini.
- Created a chat renderer for each itinerary activity.
- Implemented session-based chat memory per place.
- Enforced strict rules:
  - answers must relate only to the selected place
  - maximum three sentences
  - plain text responses.

## ✅ Outcome
Users can now interactively ask questions about specific locations inside their itinerary.

## 🧠 Learnings
Context restriction is essential when building reliable AI assistants.

## 🔹 Code & Implementation
- Chat service:  
[chat_service.py](../code/day-25-chat-system/chat_service.py)

- Chat UI renderer:  
[chat_renderer.py](../code/day-25-chat-system/chat_renderer.py)
