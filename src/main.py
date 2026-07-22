# -LISTO API:usar una nueva cuanta gemini para la api 
# -LISTO DOC: bajar los docs en pdf al proyecto
# -MAIN: ver que debe ir en el main
# -VECTOR BASE: procesar los pddf en la base vectorial
# -GITHUB LISTO: subir mi primer commit "gemini-3.5-flash",
# src/main.py
import time
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
            error_str = str(e)
            
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print("\n[SISTEMA]: Límite de la API gratuita alcanzado (Error 429).")
                print("Agente: Uf, estamos yendo muy rápido. Dame 30 segundos para tomar aire y reiniciar la conexión...")
                time.sleep(30)
                
                print("Agente: ¡Listo! ¿Me puedes repetir tu última pregunta?")
            elif "503" in error_str or "UNAVAILABLE" in error_str or "429" in error_str:
                str.warning("⚠️ **Servidores ocupados:** Google está experimentando un alto tráfico en este momento. Por favor, espera 15 segundos y reenvía tu mensaje.")
            
            else:
                print(f"\n[ERROR TÉCNICO]: {e}")
                print("Agente: Uy, tuve un pequeño problema de red con el servidor.")

if __name__ == "__main__":
    iniciar_app()