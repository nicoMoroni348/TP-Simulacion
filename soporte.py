
import pandas as pd
import random
import os


""" PRINTEO DE DATOS """
def mostrar_datos_lista(datos, separador=" | "):

    for i, d in enumerate(datos):
        if i % 5 == 0:
            print()
        print(d, end=separador)
    
    print()

    # for data in datos[:10]:
    #     print(data)
    
    # print(". . .")
    # for data in datos[-10:]:
    #     print(data)




if os.name == 'nt':  
    import msvcrt
else: 
    import tty
    import sys
    import termios

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_enter():
    if os.name == 'nt':
        msvcrt.getch()
    else:
        sys.stdin.read(1)