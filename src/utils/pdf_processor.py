import os
from dotenv import load_dotenv

# Importas tu llave correctamente
from data.keys.my_keys import GOOGLE_API_KEY

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def pdfs_a_vectorstore(ruta_carpeta, directorio_db="data/processed"):
    print(f"1. Buscando y cargando PDFs en la carpeta: {ruta_carpeta}...")
    loader = PyPDFDirectoryLoader(ruta_carpeta)
    documentos = loader.load()
    
    print("2. Dividiendo el texto en fragmentos (chunks)...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(documentos)

    print("3. Generando embeddings y guardando en ChromaDB...")
    
    # CORRECCIÓN 1: Le entregamos la variable que importaste arriba directamente a LangChain
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=directorio_db
    )
    
    print(f"¡Éxito! Base vectorial guardada en el directorio: {directorio_db}")
    return vectorstore

if __name__ == "__main__":
    carpeta_datos = "data/documents" 
    
    # CORRECCIÓN 2: Le pasamos explícitamente la nueva ruta donde quieres guardar la base
    db = pdfs_a_vectorstore(carpeta_datos, directorio_db="data/processed")