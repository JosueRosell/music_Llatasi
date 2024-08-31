import sys
from time import sleep
import time
from termcolor import colored

def print_lyrics():
 
    lines = [
        ("Todos los días", "cyan", 0.07),
        ("salgo a caminar", "blue", 0.08),
        ("Hago mil cosas", "green", 0.07),
        ("pa' no pensar", "yellow", 0.08),
        ("Me lleno de adornos", "magenta", 0.07),
        ("Sufro de trastornos", "red", 0.07),
        ("Siempre te quiero llamar", "white", 0.07),
        ("No quiero nada,", "cyan", 0.05),
        ("nada,", "cyan", 0.1),
        ("nada", "cyan", 0.12),
        ("Y es que soy", "yellow", 0.08),
        ("tan complicada", "green", 0.08),
        ("Ay, ay, ay de mí", "red", 0.10),
        ("De este amor que se metió", "magenta", 0.08),
        ("y que se dispara", "blue", 0.08),
        ("Se contagia", "cyan", 0.08),
        ("y te reclama", "white", 0.08)
    ]
    
    delays = [1.0, 0.8, 0.8, 0.8, 0.7, 0.7, 1.5, 0.9, 
              0.5, 0.5, 0.8, 1.0, 1.2, 1.0, 1.0, 0.8, 3]

    for i, (line, color, char_delay) in enumerate(lines):
        for char in line:
            print(colored(char, color), end='', flush=True)
            sleep(char_delay)
        print('') 
        time.sleep(delays[i])

print_lyrics()
