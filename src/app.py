
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
from src.agents.agents import AgenteDocumental 
st.set_page_config(
    page_title="Academia Evolution", 
    page_icon="data/assets/icon_flor_lotus_iconpage.png", 
    layout="centered",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
        /* Fuentes Modernas */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Variables de color globales de Streamlit para forzar un tema claro y suave */
        :root, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stBottom"] {
            --background-color: #f9fafb !important;
            --secondary-background-color: #f3f4f6 !important;
            --text-color: #111827 !important;
            --primary-color: #3b82f6 !important;
        }

        /* Fondo Principal de la App (Suave off-white para evitar fatiga visual) */
        .stApp {
            background-color: #f9fafb !important;
            color: #111827 !important;
        }
        
        /* Cabecera superior transparente */
        [data-testid="stHeader"] {
            background-color: rgba(249, 250, 251, 0) !important;
            color: #111827 !important;
        }
        
        /* Contenedor del Contenido Principal (Ancho de lectura perfecto) */
        .block-container {
            max-width: 760px !important;
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
            background-color: #f9fafb !important;
        }
        
        /* Barra Lateral (Sidebar) limpia y minimalista */
        [data-testid="stSidebar"] {
            background-color: #f3f4f6 !important;
            border-right: 1px solid #e5e7eb !important;
        }

        /* Ocultar menús y pies de página por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Estilo de los Títulos */
        h1, h2, h3, h4, h5, h6 {
            color: #111827 !important;
            font-weight: 800 !important;
        }

        /* Título Principal */
        .gradient-header {
            color: #111827 !important;
            font-size: 2.4rem !important;
            margin-top: 0px !important;
            margin-bottom: 4px !important;
            font-weight: 800 !important;
            letter-spacing: -0.025em !important;
        }
        
        /* Subtítulo */
        .subtitle {
            color: #4b5563 !important;
            font-size: 1.05rem !important;
            margin-bottom: 2rem !important;
            font-weight: 400 !important;
        }
        
        div[data-testid="stChatMessage"] {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 14px !important;
            padding: 1.25rem 1.5rem !important;
            margin-bottom: 0.9rem !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01), 0 2px 4px -1px rgba(0, 0, 0, 0.01) !important;
            transition: all 0.2s ease !important;
        }
        
        
        div[data-testid="stChatMessage"] p, 
        div[data-testid="stChatMessage"] li, 
        div[data-testid="stChatMessage"] span, 
        div[data-testid="stChatMessage"] strong,
        div[data-testid="stChatMessage"] div {
            color: #1f2937 !important;
            font-size: 0.975rem !important;
            line-height: 1.6 !important;
        }
        
        /* Asegurar color de textos legibles en sidebar */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] li, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] strong,
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #1f2937 !important;
        }
        
        /* Burbuja del Usuario: Fondo Blanco Limpio */
        div[data-testid="stChatMessage"]:has(img[src*="user"]) {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
        }
        
        /* Burbuja del Asistente: Tono Gris-Azul sumamente suave */
        div[data-testid="stChatMessage"]:has(img[src*="lotus"]),
        div[data-testid="stChatMessage"]:has(img[src*="onlyborders"]),
        div[data-testid="stChatMessage"]:has(img[src*="bot"]) {
            background-color: #f1f5f9 !important;
            border: 1px solid #e2e8f0 !important;
        }

        /* Avatares Circulares con Fondo Blanco */
        div[data-testid="stChatMessageAvatar"] {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 50% !important;
            padding: 3px !important;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04) !important;
        }
        
        div[data-testid="stChatMessageAvatar"] img {
            border-radius: 50% !important;
            object-fit: contain !important;
        }

        /* --- ESTILIZACIÓN DEL RECUADRO DE ENTRADA (CON RELLENO BLANCO Y SOMBRA) --- */
        
        /* Recuadro de entrada en estado normal con sombra flotante premium y moderna */
        div[data-testid="stChatInput"] {
            border: 1px solid #cbd5e1 !important;
            border-radius: 16px !important;
            background-color: #ffffff !important;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 16px -6px rgba(0, 0, 0, 0.03) !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            padding: 4px 6px !important;
        }
        
        /* Forzar que la caja de texto y todos sus divs internos tengan fondo puramente blanco (soluciona relleno oscuro) */
        div[data-testid="stChatInput"],
        div[data-testid="stChatInput"] div,
        div[data-testid="stChatInput"] textarea {
            background-color: #ffffff !important;
            color: #111827 !important;
        }
        
        div[data-testid="stChatInput"] textarea {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
            font-size: 0.95rem !important;
            padding-top: 10px !important;
            padding-bottom: 10px !important;
        }
        
        /* Estado Activo / Enfocado: Aura Azul brillante y Sombra amplificada */
        div[data-testid="stChatInput"]:focus-within {
            border-color: #3b82f6 !important;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15), 0 12px 28px -5px rgba(59, 130, 246, 0.12) !important;
        }

        /* Botón de enviar */
        div[data-testid="stChatInput"] button {
            background-color: #3b82f6 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 6px !important;
            transition: all 0.2s ease !important;
        }

        div[data-testid="stChatInput"] button:hover {
            background-color: #2563eb !important;
            transform: scale(1.05) !important;
        }

        /* Integración del contenedor inferior flotante de Streamlit */
        div[data-testid="stBottom"] {
            background-color: #f9fafb !important;
            border-top: none !important;
        }
        div[data-testid="stBottom"] > div {
            background-color: transparent !important;
        }

        /* --- ESTILOS DE LA BARRA LATERAL (SIDEBAR) --- */

        /* Alinear verticalmente las columnas en el sidebar de forma simple */
        [data-testid="stSidebar"] [data-testid="column"] {
            display: flex !important;
            align-items: center !important;
            margin-bottom: 8px !important;
        }

        /* Estilo de los encabezados de sección en el sidebar */
        [data-testid="stSidebar"] h3 {
            font-size: 1.05rem !important;
            font-weight: 700 !important;
            margin: 0 !important;
            color: #111827 !important;
        }

        /* Enlaces del sidebar */
        [data-testid="stSidebar"] a {
            color: #2563eb !important;
            text-decoration: none !important;
            font-weight: 600 !important;
        }
        
        [data-testid="stSidebar"] a:hover {
            color: #1d4ed8 !important;
            text-decoration: underline !important;
        }

        /* Botón de Limpieza del Chat */
        .stButton>button {
            background-color: #f3f4f6 !important;
            color: #374151 !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            width: 100% !important;
            padding: 8px 12px !important;
            transition: all 0.2s ease-in-out !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
        }
        
        .stButton>button:hover {
            background-color: #fee2e2 !important; /* Alerta en rojo suave al pasar el cursor */
            color: #dc2626 !important;
            border-color: #fca5a5 !important;
            box-shadow: 0 4px 12px rgba(220, 38, 38, 0.08) !important;
            transform: translateY(-1px) !important;
        }

        .footer-note {
            color: #9ca3af !important;
            font-size: 0.75rem !important;
            text-align: center !important;
            margin-top: 1.5rem !important;
            margin-bottom: 1rem !important;
            font-weight: 400 !important;
        }

        /* Scrollbars elegantes */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
""", unsafe_allow_html=True)

# --- 4. BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Logo superior
    st.image("data/assets/evolution_academy_logo.png", use_container_width=True)
    st.markdown("---")
    
    # Sección: Oferta Académica
    st.markdown("### Oferta Académica")
    col1, col2 = st.columns([1, 4])
    with col1: st.image("data/assets/icon_virrete.png", width=28)
    with col2: st.markdown("Cosmetología")
    
    col3, col4 = st.columns([1, 4])
    with col3: st.image("data/assets/icon_maquillaje.png", width=28)
    with col4: st.markdown("Maquillaje")
    
    col5, col6 = st.columns([1, 4])
    with col5: st.image("data/assets/icon_pencil.png", width=28)
    with col6: st.markdown("Microblading")
    
    st.markdown("---")
    
    # Sección: Contacto
    st.markdown("### Contacto")
    colw1, colw2 = st.columns([1, 4])
    with colw1: st.image("data/assets/icon_whatsapp.png", width=24)
    with colw2: st.markdown("[WhatsApp](https://wa.me/521234567890)")
    
    st.markdown("---")
    
    # Control para limpiar chat
    if st.button("Limpiar Chat"):
        st.session_state.mensajes_ui = []
        if "mi_asistente" in st.session_state:
            st.session_state.mi_asistente.historial = []
        st.rerun()

st.markdown("<h1 class='gradient-header'>Asistente Evolution</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>IA experta en reglamentos y cursos de belleza</p>", unsafe_allow_html=True)

if "mi_asistente" not in st.session_state:
    st.session_state.mi_asistente = AgenteDocumental()
    
if "mensajes_ui" not in st.session_state:
    st.session_state.mensajes_ui = []
for mensaje in st.session_state.mensajes_ui:
    avatar_img = "data/assets/icon_user.png" if mensaje["role"] == "user" else "data/assets/icon_flor_lotus_onlyborders.png"
    with st.chat_message(mensaje["role"], avatar=avatar_img):
        st.markdown(mensaje["content"])

pregunta = st.chat_input("¿En qué puedo ayudarte hoy?")

if pregunta:
    with st.chat_message("user", avatar="data/assets/icon_user.png"):
        st.markdown(pregunta)
    st.session_state.mensajes_ui.append({"role": "user", "content": pregunta})
    
    with st.chat_message("assistant", avatar="data/assets/icon_flor_lotus_onlyborders.png"):
        with st.spinner("Consultando con la academia..."):
            respuesta = st.session_state.mi_asistente.consultar(pregunta)
            st.markdown(respuesta)
            
    st.session_state.mensajes_ui.append({"role": "assistant", "content": respuesta})

st.markdown('<p class="footer-note">Academia Evolution · Las respuestas generadas por la IA son de carácter informativo y normativo.</p>', unsafe_allow_html=True)