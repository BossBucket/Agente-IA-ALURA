import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

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

    raise ValueError("No se encontró GOOGLE_API_KEY en Secrets de Streamlit.")

def embeddings():
    # Usar la clase de langchain_community evita el bug de 'cache_folder'
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=obtener_api_key()
    )