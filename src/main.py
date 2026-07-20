# -LISTO API:usar una nueva cuanta gemini para la api 
# -LISTO DOC: bajar los docs en pdf al proyecto
# -MAIN: ver que debe ir en el main
# -VECTOR BASE: procesar los pddf en la base vectorial
# -GITHUB LISTO: subir mi primer commit "gemini-3.5-flash",
# src/main.py

from dotenv import load_dotenv

load_dotenv()

from src.agents.agents import AgenteDocumental

def iniciar_app():
    print("Iniciando sistema...")
    
    mi_asistente = AgenteDocumental()
    
    print("\n" + "="*50)
    print("¡Listo! Escribe tu pregunta (o 'salir').")
    print("="*50)
    
    while True:
        pregunta = input("\nTú: ")
        
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            print("Saliendo ¡Hasta luego!")
            break
            
        try:
            respuesta = mi_asistente.consultar(pregunta)
            print(f"\nAgente: {respuesta}")
        except Exception as e:
            # Si el internet falla o Google se desconecta, atrapamos el error aquí
            print(f"\n[ERROR TÉCNICO OCULTO]: {e}")
            print("\nAgente: tuve un pequeño problema de conexión con el servidor. ¿Podrías repetir tu respuesta?")

if __name__ == "__main__":
    iniciar_app()