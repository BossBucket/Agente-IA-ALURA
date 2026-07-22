
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


# st.markdown("""
#     <style>
#         /* ... (CSS content) ... */
#     </style>
# """, unsafe_allow_html=True)

# --- 4. BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Logo superior
    st.image("data/assets/evolution_academy_logo.png", use_container_width=True)
    st.markdown("---")
    
    # Sección: Oferta Académica
    st.markdown("### Oferta Académica")
    st.markdown("• **Cosmetología**")
    st.markdown("• **Maquillaje**")
    st.markdown("• **Microblading**")
    
    st.markdown("---")
    
    # Sección: Contacto
    st.markdown("### Contacto")
    st.markdown("[WhatsApp Directo](https://wa.me/521234567890)")
    
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