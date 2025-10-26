import random
import time
import os

# --- Configuración del Juego ---
ANCHO_PISTA = 50        # Ancho de la pista en caracteres
NUM_CORREDORES = 4      # Número de asteriscos
VELOCIDAD = 0.1         # Tiempo en segundos entre cada "frame" (más bajo = más rápido)

# --- Función para limpiar la pantalla ---
def limpiar_pantalla():
    """Limpia la terminal (compatible con Windows, Mac y Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Función para obtener la elección del usuario ---
def obtener_eleccion():
    """Muestra el menú y pide al usuario que elija un corredor."""
    while True:
        limpiar_pantalla()
        print("🏁 BIENVENIDO A LA CARRERA DE ASTERISCOS 🏁")
        print("============================================")
        print("Elige tu corredor:")
        for i in range(NUM_CORREDORES):
            print(f"  [{i+1}] Corredor *")
        print("============================================")
        
        try:
            eleccion = input(f"¿Por cuál asterisco apuestas? (1-{NUM_CORREDORES}): ")
            eleccion = int(eleccion)
            
            if 1 <= eleccion <= NUM_CORREDORES:
                # Restamos 1 para que coincida con el índice de la lista (0, 1, 2, 3)
                return eleccion - 1
            else:
                print(f"Error: Debes elegir un número entre 1 y {NUM_CORREDORES}.")
                time.sleep(2)
        except ValueError:
            print("Error: Introduce solo un número.")
            time.sleep(2)

# --- Función para dibujar la pista ---
def dibujar_pista(posiciones, eleccion_usuario):
    """Dibuja el estado actual de la carrera."""
    limpiar_pantalla()
    print("🏁 ¡LA CARRERA HA COMENZADO! 🏁")
    print(" " * (ANCHO_PISTA + 5) + "META")
    
    # Dibuja la línea de meta
    print("INICIO" + ("=" * (ANCHO_PISTA - 2)) + "||")

    for i in range(NUM_CORREDORES):
        # Calcula cuántos espacios en blanco poner
        espacios = " " * posiciones[i]
        
        # Prepara la línea del corredor
        linea_corredor = f"  [{i+1}] {espacios}*"
        
        # Añade un indicador si es la apuesta del usuario
        if i == eleccion_usuario:
            linea_corredor += "  <-- (Tu apuesta)"
            
        print(linea_corredor)

    # Dibuja la línea de meta inferior
    print("INICIO" + ("=" * (ANCHO_PISTA - 2)) + "||")

# --- Función principal del juego ---
def jugar():
    eleccion_usuario = obtener_eleccion()
    
    # Inicializa las posiciones de todos los corredores en 03
    posiciones = [0] * NUM_CORREDORES
    
    ganador = None
    
    while ganador is None:
        # 1. Dibuja el estado actual
        dibujar_pista(posiciones, eleccion_usuario)
        
        # 2. Mueve a cada corredor
        for i in range(NUM_CORREDORES):
            # Avance aleatorio: puede ser 0, 1 o 2 pasos
            avance = random.randint(0, 2)
            posiciones[i] += avance
            
            # 3. Comprueba si hay un ganador
            # Gana si su posición es mayor o igual al ancho de la pista
            if posiciones[i] >= ANCHO_PISTA:
                ganador = i  # Guardamos el índice (0, 1, 2, o 3)
                break # Salimos del bucle 'for'
        
        if ganador is not None:
            break # Salimos del bucle 'while'
            
        # 4. Pausa para dar efecto de animación
        time.sleep(VELOCIDAD)

    # --- Mostrar resultado final ---
    dibujar_pista(posiciones, eleccion_usuario) # Dibuja la última jugada
    print("\n" + "🏆" * 20)
    # Sumamos 1 al índice para mostrar el número de corredor (1-4)
    print(f"¡EL GANADOR ES EL CORREDOR {ganador + 1}! 🏆")
    print("🏆" * 20)

    if ganador == eleccion_usuario:
        print(f"\n¡FELICIDADES! ¡Elegiste al ganador!")
    else:
        print(f"\n¡Mala suerte! Tu corredor ({eleccion_usuario + 1}) no ganó esta vez.")

# --- Iniciar el juego ---
if __name__ == "__main__":
    jugar()