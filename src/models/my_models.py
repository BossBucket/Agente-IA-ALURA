import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

def obtener_api_key():
    
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            return st.secrets["GOOGLE_API_KEY"].strip()
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"].strip()
    except Exception:
        pass

    
    key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if key:
        return key.strip()

    raise ValueError("No se encontró una API Key válida en Streamlit Secrets ni en variables de entorno.")

def embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="text-embedding-004", 
        google_api_key=obtener_api_key()
    )

def llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=obtener_api_key()
    )