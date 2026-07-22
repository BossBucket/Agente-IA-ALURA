import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# Obtener la API Key desde Streamlit Secrets o las variables de entorno locales
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

def embeddings():
    if not GOOGLE_API_KEY:
        raise ValueError("No se encontró la GOOGLE_API_KEY. Configúrala en los Secrets de Streamlit o en un archivo .env.")
        
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=GOOGLE_API_KEY
    )

def llm():
    if not GOOGLE_API_KEY:
        raise ValueError("No se encontró la GOOGLE_API_KEY. Configúrala en los Secrets de Streamlit o en un archivo .env.")
        
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY
    )