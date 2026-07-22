import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

def obtener_api_key():
    # En Streamlit Cloud lee directamente de Secrets
    if "GOOGLE_API_KEY" in st.secrets:
        return st.secrets["GOOGLE_API_KEY"]
    if "GEMINI_API_KEY" in st.secrets:
        return st.secrets["GEMINI_API_KEY"]
    raise ValueError("Falta la clave GOOGLE_API_KEY en los Secrets de Streamlit Cloud.")

def embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=obtener_api_key()
    )

def llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=obtener_api_key()
    )