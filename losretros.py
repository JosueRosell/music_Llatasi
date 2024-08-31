import sys
from time import sleep
import time
from termcolor import colored

def print_lyrics():
 
    lines = [
        ("My sweetheart", "red", 0.06),
        ("Where are you?", "blue", 0.06),
        ("I need someone", "green", 0.05),
        ("To spend time with", "yellow", 0.09),
        ("to give", "cyan", 0.06),
        ("And share", "magenta", 0.06),
        ("All my love", "white", 0.09),
    ]
    
    delays = [1.2, 1.5, 1.4, 1.5, 0.7, 0.4, 3]

    for i, (line, color, char_delay) in enumerate(lines):
        for char in line:
            print(colored(char, color), end='', flush=True)
            sleep(char_delay)
        print('') 
        time.sleep(delays[i])

print_lyrics()
