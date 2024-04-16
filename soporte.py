import pandas as pd
import random
import os
import time


def generacion_numeros_uniformes(n):
    numeros_uniformes_0_1 = []
    for i in range(n):
        numeros_uniformes_0_1.append(random.random())
    
    return numeros_uniformes_0_1


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




def join_elements_in_list(li, index_beg, index_end):

    l = li[:index_beg] + [sum(li[index_beg:index_end+1])] + li[index_end+1:] 
    return l



def join_classes_in_list(li, index_beg, index_end):

    l = li[:index_beg] + [max(li[index_beg:index_end+1])] + li[index_end+1:] 
    return l





def find_first_index_to_join(freq_esperadas_list, criteria=5.0):
    index_beg = -1
    index_end = -1
    for i, element in (enumerate(freq_esperadas_list)):
        if element < criteria and index_beg == -1:
            index_beg = i

        elif element < criteria and index_beg != -1 and element + sum(freq_esperadas_list[index_beg:i]) >= criteria:
            index_end = i
            return (index_beg, index_end)

        if element >= criteria and index_beg != -1:
            index_end = i
            return (index_beg, index_end)
            

    
    if index_beg != -1 and index_end == -1:
        return (index_beg-1, index_beg)
    



def get_new_list_and_indexes_changes(l):
    indexes_changed = []
    indexes = (0, 0)
    new_list = l[:]
    while indexes is not None:
        indexes = find_first_index_to_join(new_list)
        if indexes is not None:
            # print(f"CUR STATE: {new_list}  --  JOINING {indexes}")

            indexes_changed.append(indexes)
            new_list = join_elements_in_list(new_list, *indexes)
            # time.sleep(1)

    return new_list, indexes_changed


# EJEMPLO DE EXPONENCIAL

# l = [37.97, 20.29, 10.84, 5.79, 3.097, 1.66]


# messi = [93.99, 112.78, 131.58, 150.38, 169.18, 187.98]


# print(l)
# l, indexes = get_new_list_and_indexes_changes(l)

# print(l)
# print(indexes)

# for ib, ie in indexes:
#     messi = join_classes_in_list(messi, ib, ie)

# print(messi)





def validar_muestra():
    while True:
        try:
            n = int(input("Ingrese el valor de la muestra (hasta 1000000 y mayor que 0): "))
            if n > 0 and n <= 1000000:
                break
            else:
                print("La muestra debe estar entre 1 y 1000000, por favor ingrese un valor válido.")

        except ValueError:
            print("Por favor ingrese un número entero válido.")

    return n


def validar_intervalo_a_b():
    while True:
        try:
            a = float(input("Ingrese el valor inferior del intervalo (A): "))
            b = float(input("Ingrese el valor superior del intervalo (B): "))
            if a < b:
                return a, b
            else:
                print("El valor de 'A' debe ser menor que el valor de 'B'. Por favor ingrese nuevamente los valores.")
        except ValueError:
            print("Por favor ingrese valores numéricos válidos.")


def seleccionar_intervalos_histograma():
    while True:
        try:
            intervalos = int(input("Seleccione el número de intervalos (10, 15, 20, 25): "))
            if intervalos in [10, 15, 20, 25]:
                return intervalos
            else:
                print("Por favor seleccione un número de intervalos válido.")
        except ValueError:
            print("Por favor ingrese un número entero.")


def validar_media():
    while True:
        try:
            media = float(input("Ingrese el valor de la media: "))
            if media > 0:
                return media
            else:
                print("La media debe ser un número positivo. Inténtelo de nuevo.")
        except ValueError:
            print("Ingrese un valor numérico para la media.")


def validar_desviacion_estandar(media):
    while True:
        try:
            desviacion = float(input("Ingrese el valor de la desviación estándar: "))
            if desviacion > 0 and desviacion < media:
                return desviacion
            else:
                print("La desviación estándar debe ser un número positivo y menor que la media. Inténtelo de nuevo.")
        except ValueError:
            print("Ingrese un valor numérico para la desviación estándar.")

