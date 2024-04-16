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





