import time

# Texto de la canción
letra_cancion = """Nunca hemos sido los guapos del barrio
Siempre hemos sido una cosa normal
Ni mucho ni poco, ni para comerte el coco
Oye, yo te digo, una cosa normal
Y ahora vamos a las discotecas
Si no tienes cuidado te muerden las piernas
Bebes un poco, te haces el loco
Ves a una niña disimular
Has sido tú, te crees que no te he visto
Has sido tú, chica cocodrilo"""

# Función para mostrar la letra como si estuviera escribiéndose en tiempo real
def escribir_letra(letra, velocidad=0.1):
    for char in letra:
        print(char, end='', flush=True)
        time.sleep(velocidad)  # Pausa entre cada carácter

# Llamamos a la función con la letra de la canción
escribir_letra(letra_cancion, velocidad=0.05)
