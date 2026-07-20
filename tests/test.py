try:
    from langchain_openai import OpenAIEmbeddings
    print("¡Éxito! La librería está instalada y se pudo importar.")
except ImportError as e:
    print(f"Error al importar: {e}")