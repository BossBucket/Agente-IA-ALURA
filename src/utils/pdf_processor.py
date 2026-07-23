import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from src.models.my_models import embeddings

PERSIST_DIR = "data/processed"
DOCS_DIR = "data/documents"

def crear_base_vectorial():
    # 1. Cargar todos los PDFs de la carpeta data/documents
    documentos = []
    carpeta_docs = Path(DOCS_DIR)
    
    if not carpeta_docs.exists():
        print(f"La carpeta {DOCS_DIR} no existe.")
        return None

    for archivo in carpeta_docs.glob("*.pdf"):
        print(f"Cargando: {archivo.name}")
        loader = PyPDFLoader(str(archivo))
        documentos.extend(loader.load())
    
    if not documentos:
        print("No se encontraron PDFs en data/documents.")
        return None

    # 2. Partir el texto en fragmentos (chunks)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    fragmentos = text_splitter.split_documents(documentos)
    print(f"Dividido en {len(fragmentos)} fragmentos.")
    
    # 3. Crear la base de datos vectorial con los embeddings de FastEmbed
    print("Creando base vectorial...")
    db = Chroma.from_documents(
        documents=fragmentos, 
        embedding=embeddings(), 
        persist_directory=PERSIST_DIR
    )
    print("¡Base vectorial creada y guardada con éxito!")
    return db

def obtener_o_crear_vectorstore():
    # Si la carpeta procesada no existe o está vacía, la crea automáticamente
    if not os.path.exists(PERSIST_DIR) or not os.listdir(PERSIST_DIR):
        print("No se encontró base vectorial. Procesando PDFs...")
        return crear_base_vectorial()
    else:
        # Si ya existe, simplemente la carga
        return Chroma(
            persist_directory=PERSIST_DIR, 
            embedding_function=embeddings()
        )

if __name__ == "__main__":
    crear_base_vectorial()