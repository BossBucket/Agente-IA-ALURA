
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

from src.models.my_models import embeddings, llm

class AgenteDocumental:
    def __init__(self, ruta_bd="data/processed"):
        """Constructor: Inicializa la IA, conecta la BD y ensambla la cadena."""
        self.embeddings = embeddings()
        self.llm = llm()
        
        self.db = Chroma(
            persist_directory=ruta_bd, 
            embedding_function=self.embeddings
        )
        self.retriever = self.db.as_retriever(search_kwargs={"k": 3})
        
        
        system_prompt = (
            "Eres el asistente virtual oficial de 'Academia Evolution', una academia "
            "profesional de belleza y cosmetología.\n\n"
            "REGLAS ESTRICTAS:\n"
            "1. BREVEDAD (CRÍTICO): Sé EXTREMADAMENTE conciso y directo. Tus respuestas "
            "deben tener como MÁXIMO 4 párrafos cortos. No des explicaciones que el "
            "usuario no haya pedido explícitamente.\n"
            "2. Fuente de verdad: Usa EXCLUSIVAMENTE la información del 'Contexto'.\n"
            "3. Límite de conocimiento: Si no sabes algo, di que no tienes el dato y sugiere "
            "llamar a la administración en una sola oración breve.\n"
            "4. Formato: Usa listas (viñetas) solo si necesitas enumerar más de 3 elementos.\n"
            "5. NO USES EMOJIS: Tienes terminantemente prohibido usar emojis o emoticonos en tus respuestas. Debes ser profesional y usar solo texto plano y viñetas estándar.\n\n"
            "Contexto recuperado de la base de datos:\n"
            "---------------------\n"
            "{context}\n"
            "---------------------\n"
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"), 
            ("human", "{input}"),
        ])
        
        
        self.cadena = (
            RunnablePassthrough.assign(
                context=lambda datos: self._limpiar_docs(self.retriever.invoke(datos["input"]))
            )
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        self.historial = []

    def _limpiar_docs(self, documentos):
        """Método privado para convertir los objetos de BD a texto puro."""
        return "\n\n".join(doc.page_content for doc in documentos)

    def consultar(self, pregunta):
        """Método público para interactuar con el agente."""
        
        # 1. Ejecutamos la cadena enviando la pregunta Y el historial acumulado
        respuesta = self.cadena.invoke({
            "input": pregunta,
            "chat_history": self.historial
        })
        
        # 2. Guardamos la interacción actual en nuestro arreglo para el próximo turno
        self.historial.extend([
            HumanMessage(content=pregunta),
            AIMessage(content=respuesta)
        ])
        
        return respuesta
def consultar(self, pregunta, modo_prueba=True): # <-- Activa el modo prueba por defecto
        """Método público para interactuar con el agente."""
        
        # EL MOCK: Si estamos diseñando la interfaz, no gastamos peticiones a Google
        if modo_prueba:
            import time
            time.sleep(1.5)  # Simulamos que la IA está "pensando" por 1.5 segundos
            respuesta_simulada = f"Soy un mensaje de prueba. Recibí tu pregunta: '{pregunta}'. La interfaz funciona perfectamente."
            
            # Guardamos en el historial para que la memoria gráfica también funcione
            self.historial.extend([
                HumanMessage(content=pregunta),
                AIMessage(content=respuesta_simulada)
            ])
            return respuesta_simulada
            
        # --- AQUÍ EMPIEZA EL CÓDIGO REAL ---
        respuesta = self.cadena.invoke({
            "input": pregunta,
            "chat_history": self.historial
        })
        
        self.historial.extend([
            HumanMessage(content=pregunta),
            AIMessage(content=respuesta)
        ])
        
        return respuesta