import requests
import os
from dotenv import load_dotenv

# ---------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------
load_dotenv()

# Get API key from .env file
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ---------------------------------
# AI SUMMARIZATION FUNCTION
# ---------------------------------
def summarize_text(user_text):

    # API endpoint
    url = "https://openrouter.ai/api/v1/chat/completions"

    # Headers
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    # Prompt + model configuration
    payload = {
        "model": "openrouter/owl-alpha",

        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant that summarizes text "
                    "into short, concise bullet points."
                    "You summarize into beginner friendly summaries."
                    "Aslo you divide the text into sections fro clarity"
                )
            },
            {
                "role": "user",
                "content": f"Summarize the following text:\n\n{user_text}"
            }
        ],

        "temperature": 0.3
    }

    # Send POST request to OpenRouter
    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    # Convert response into JSON format
    data = response.json()

    # Extract only the AI-generated summary
    summary = data["choices"][0]["message"]["content"]

    return summary


