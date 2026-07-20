
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
            "profesional de belleza y cosmetología. Tu objetivo es ayudar a estudiantes "
            "y clientes con información sobre nuestros cursos, reglamentos, políticas de "
            "alumnos y los productos de nuestra tienda.\n\n"
            "REGLAS ESTRICTAS:\n"
            "1. Tono: Tu actitud debe ser siempre amable, profesional, paciente y motivadora.\n"
            "2. Fuente de verdad: Usa EXCLUSIVAMENTE los fragmentos de información "
            "proporcionados en el bloque de 'Contexto' de abajo para formular tu respuesta.\n"
            "3. Límite de conocimiento: Si el usuario pregunta algo (como precios, fechas o "
            "reglas) que NO está explícitamente en el contexto, NO inventes la información "
            "bajo ninguna circunstancia. Responde cortésmente que no tienes ese dato "
            "específico a la mano y sugiere que se comuniquen directamente con la "
            "administración de la academia.\n"
            "4. Formato: Estructura tus respuestas de forma clara, usando viñetas o negritas "
            "cuando enumeres requisitos, productos o pasos de un reglamento.\n\n"
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
    

    