# src/utils/pdf_processor.py

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Importamos las llaves necesarias
from data.keys.my_keys import GOOGLE_API_KEY

def crear_base_vectorial():
    # 1. Cargar todos los PDFs de la carpeta data/documents
    documentos = []
    carpeta_docs = Path("data/documents")
    for archivo in carpeta_docs.glob("*.pdf"):
        print(f"Cargando: {archivo.name}")
        loader = PyPDFLoader(str(archivo))
        documentos.extend(loader.load())
    
    if not documentos:
        print("No se encontraron PDFs en data/documents.")
        return

    # 2. Partir el texto en fragmentos (chunks)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    fragmentos = text_splitter.split_documents(documentos)
    print(f"Dividido en {len(fragmentos)} fragmentos.")
    
    # 3. Configurar los embeddings de Google
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001", 
        google_api_key=GOOGLE_API_KEY
    )
    
    # 4. Crear la base de datos vectorial (Chroma) y guardarla localmente
    print("Creando base vectorial...")
    db = Chroma.from_documents(
        documents=fragmentos, 
        embedding=embeddings, 
        persist_directory="data/processed"
    )
    
    print("¡Base vectorial (Chroma) creada y guardada con éxito en data/processed!")

if __name__ == "__main__":
    crear_base_vectorial()
