import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# Carga de API Key priorizando Secrets de Streamlit
API_KEY = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

def embeddings():
    if not API_KEY:
        raise ValueError("No se encontró GOOGLE_API_KEY en Secrets de Streamlit ni en las variables de entorno.")
    
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=API_KEY
    )

def llm():
    if not API_KEY:
        raise ValueError("No se encontró GOOGLE_API_KEY en Secrets de Streamlit ni en las variables de entorno.")
        
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=API_KEY
    )