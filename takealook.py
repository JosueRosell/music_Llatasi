import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("We even got a secret handshake", 0.09, False),
        ("And she loves the music", 0.06, False),
        ("that my band makes", 0.06, False),
        ("I know I'm young, but if I had to choose", 0.06, True),

        ("her or the Sun", 0.1, False),
        ("I'd be one nocturnal son of a gun", 0.1, True),
        ("Take a look at my girlfriend", 0.08, True),
        ("She's the only one I got", 0.08, False),
        ("(ba, ba, da, da)", 0.08, True),
        ("Not much of a girlfriend", 0.08, False),
        ("I never seem to get a lot", 0.08, True),
        ("(ba, ba, da, da, ba, ba, da, da)", 0.08, False)

    ]

    delays = [0.6, 0.4, 0.4, 0.4, 0.5, 0.4, 0.4, 2.0, 
              0.8, 0.6, 0.8, 0.6, 0.9, 0.6, 0.8, 0.6, 4]

    for i, (line, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[91m", end='')  

        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        if is_colored:
            print("\033[0m", end='')  

        time.sleep(delays[i])
        print('')

print_lyrics()
