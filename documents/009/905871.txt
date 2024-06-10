from bisect import *
try:
    while True:
        print ['light fly', 'fly', 'bantam', 'feather', 'light', 'light welter',
               'welter', 'light middle', 'middle', 'light heavy', 'heavy'][bisect_left([48, 51, 54, 57, 60, 64, 69, 75, 81, 91], float(raw_input()))]
except EOFError:
    pass