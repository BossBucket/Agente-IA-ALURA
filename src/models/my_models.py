
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from data.keys.my_keys import GOOGLE_API_KEY

def embeddings():
    """Retorna el modelo de traducción de texto a vectores para la base"""
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

def llm():
    """Retorna el modelo de lenguaje."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash", 
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3 
    )