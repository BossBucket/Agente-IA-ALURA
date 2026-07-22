import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GOOGLE_API_KEY = GEMINI_API_KEY
GPT_API_KEY= os.getenv("GPT_API_KEY")

