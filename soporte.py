""" PRINTEO DE DATOS """
import pandas as pd
import random

def mostrar_datos_lista(datos, separador=" | "):

    for i, d in enumerate(datos):
        if i % 5 == 0:
            print()
        print(d, end=separador)

    # for data in datos[:10]:
    #     print(data)
    
    # print(". . .")
    # for data in datos[-10:]:
    #     print(data)




# mostrar_datos_lista([round(random.random(), 4) for i in range(1000)])


