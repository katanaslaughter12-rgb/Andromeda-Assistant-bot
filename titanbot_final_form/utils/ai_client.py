
import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def ask_ai(messages):
    try:
        return client.models.generate_content(model="gemini-2.0-flash", contents=messages[-1]["content"]).text
    except Exception as e:
        return str(e)
