
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


# Call Gemini model
def ask_gemini(model, user_input):

    response = client.models.generate_content(
        model=model,
        contents=user_input
    )

    return response.text

