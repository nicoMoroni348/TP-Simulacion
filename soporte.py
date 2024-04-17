import pandas as pd
import random
import os


def generacion_numeros_uniformes(n):
    numeros_uniformes_0_1 = []
    for _ in range(n):
        r = round(random.random(), 4)


        # Con el redondeo un 0.99995... se redondea a 1.0
        # Este codigo evita que random.random() devuelva un 1.0 al redondear
        if r == 1.0:
            r = 0.9999 # Redondeo "manual"
        numeros_uniformes_0_1.append(r)
    
    return numeros_uniformes_0_1


""" PRINTEO DE DATOS """

def mostrar_datos_lista(datos, separador=" | "):

    if len(datos) < 20:
        for i, d in enumerate(datos):
            if i % 5 == 0:
                print()
            print(d, end=separador)
        print()
    else:
        for i, d in enumerate(datos[:10]):
            print(d, end=separador)
        print(". . .")
        for i, d in enumerate(datos[-10:]):
            print(d, end=separador)
        print()


""" FUNCIONES PARA EL MENÚ """

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
    # Devuelve el primer par de indices a agrupar, segun el criterio
    index_beg = -1
    # Si index_beg es -1 significa que no encontro todavia el indice de inicio a agrupar
    index_end = -1
    for i, element in (enumerate(freq_esperadas_list)):
        if element < criteria and index_beg == -1:
            print("IF MENOR")
            index_beg = i

        # Si al agrupar indices consiguientes no llega a 5, no entra a este elif
        elif element < criteria and index_beg != -1 and element + sum(freq_esperadas_list[index_beg:i]) >= criteria:
            index_end = i
            print("ELIF")
            return (index_beg, index_end)

        if element >= criteria and index_beg != -1:
            index_end = i
            print("IF MAYOR")
            return (index_beg, index_end)
        
        print(i, element)
        input()
            

    # Este if esta por si no se puede agrupar para el siguiente intervalo, que agrupe con el anterior
    if index_beg != -1 and index_end == -1:
        return (index_beg-1, len(freq_esperadas_list)-1)




def get_new_list_and_indexes_changes(l):
    indexes_changed = []
    indexes = (0, 0)
    new_list = l[:]
    while indexes is not None:
        indexes = find_first_index_to_join(new_list)
        if indexes is not None:
            # print(f"CUR STATE: {new_list}  --  JOINING {indexes}")

            # agrega el agrupamiento a realizar en la lista 
            indexes_changed.append(indexes)
            new_list = join_elements_in_list(new_list, *indexes)
            # time.sleep(1)

    return new_list, indexes_changed


""" VALIDACIONES """

def validar_muestra():
    while True:
        try:
            
            n = int(input("Ingrese el valor de la muestra (hasta 1.000.000 y mayor que 30): "))
            if n > 30 and n <= 1000000:
                break
            else:
                print("La muestra debe estar entre 30 y 1000000, por favor ingrese un valor válido.")

        except ValueError:
            print("Por favor ingrese un número entero válido.")

    return n


def validar_intervalo_a_b():
    while True:
        try:
            a = float(input("Ingrese el valor inferior del intervalo (A): "))
            b = float(input("Ingrese el valor superior del intervalo (B): "))
            
            if a == 0 and b == 1:
                print("El valor de a y b no puede ser 0 y 1 respectivamente. Por favor ingrese nuevamente los valores.")
            else:
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
