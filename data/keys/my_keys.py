import os
from dotenv import load_dotenv

load_dotenv(r".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")