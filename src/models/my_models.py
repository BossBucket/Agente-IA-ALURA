
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import streamlit as st
from data.keys.my_keys import GOOGLE_API_KEY

GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

def embeddings():
    """Retorna el modelo de traducción de texto a vectores para la base"""
    if not GOOGLE_API_KEY:
        raise ValueError("No se encontró la GOOGLE_API_KEY en Secrets ni en las variables de entorno.")
        
    return GoogleGenerativeAIEmbeddings(
        model="gemini-3.5-flash",
        google_api_key=GOOGLE_API_KEY
    )



def llm():
    """Retorna el modelo de lenguaje."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash", 
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3 
    )