import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Ngayon lang nakadama", 0.10),
        ("Ng wagas na pagkamangha", 0.10),
        ("Hiling ko lang naman", 0.10),
        ("Naaaaaaaaaaaa", 0.12),
        ("Tayo na sanang dalawa", 0.10),
        ("Ang siyang huli at ang umpisa", 0.10),
        ("Papatunayang ang unang", 0.07),
        ("Pag-ibig ay 'di mawawala", 0.11),
     
        
    ]

    delays = [0.9, 1.0, 1.9 , 1.5, 1.5, 1.0, 1.5, 2.5 ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
