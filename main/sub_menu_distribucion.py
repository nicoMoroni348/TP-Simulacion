import os
import sys
import random
from representaciones import generacion_histograma, generacion_tablas 
sys.path.append(os.getcwd())
from distribuciones import distribucion_exponencial, distribucion_normal, distribucion_uniforme
# from chi_cuadrado import chi_square_calc

"""

Aca se tiene que pedir los parametros (n, media, desviacion, etc)
Generar la distribucion
Y despues solicitar si se quiere generar historgrama, tabla de freq, o hacer la prueba de chi cuadrado.

"""


def menu_uniforme(n):
    numeros_uniformes_0_1 = []
    for i in range(n):
        numeros_uniformes_0_1.append(random.random())

    while True:
        print("\n-- Opciones Uniforme(A,B) --")
        print("1 - Mostrar histograma")
        print("2 - Mostrar tabla de frecuencias")
        print("3 - Realizar prueba de chi cuadrado")
        print("0 - Volver al menú principal")
        
        try:
            opc_uniforme = int(input("\nIngrese su opción: "))
            
            if opc_uniforme not in [0, 1, 2]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_uniforme == 1:

                intervalos = int(input("Ingrese el número de intervalos para el histograma: "))
                # Llamar a la función para mostrar el histograma
                pass

            elif opc_uniforme == 2:
                pass
                
            elif opc_uniforme == 3:
                a_min = float(input("Ingrese el valor mínimo del intervalo: "))
                a_max = float(input("Ingrese el valor máximo del intervalo: "))
                # Llamar a la función para realizar la prueba de chi cuadrado
                pass
                
            elif opc_uniforme == 0:  
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")




def menu_normal():
    while True:
        print("\n-- Opciones Distribución Normal --")
        print("1 - Mostrar histograma")
        print("2 - Realizar prueba de chi cuadrado")
        print("0 - Volver al menú principal")
        
        try:
            opc_normal = int(input("\nIngrese su opción: "))
            
            if opc_normal not in [0, 1, 2]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_normal == 1:
                intervalos = int(input("Ingrese el número de intervalos para el histograma: "))
                # Llamar a la función para mostrar el histograma
                pass
                
            elif opc_normal == 2:
                # Llamar a la función para realizar la prueba de chi cuadrado
                pass
                
            elif opc_normal == 0:
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")


def menu_exponencial():
    n = int(input("Ingrese el valor de la muestra: "))
    numeros_uniformes_0_1 = []
    for i in range(n):
        numeros_uniformes_0_1.append(random.random())
    media = float(input("Ingrese el valor de la media: "))
    desviacion = float(input("Ingrese el valor de la desviación: "))
    numeros_exp = distribucion_exponencial.distribucion_exponencial(numeros_uniformes_0_1, media)
    intervalos = int(input("Ingrese el número de intervalos para el histograma: "))
    while True:
        print("\n-- Opciones Distribución Exponencial --")
        print("1 - Mostrar histograma")
        print("2 - Realizar prueba de chi cuadrado")
        print("0 - Volver al menú principal")
        
        try:
            opc_exponencial = int(input("\nIngrese su opción: "))
            
            if opc_exponencial not in [0, 1, 2]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_exponencial == 1:
                # Llamar a la función para mostrar el histograma
                generacion_histograma.full_histogram(numeros_exp, intervalos)
                pass

            elif opc_exponencial == 2:
                # Llamar a la función para realizar la prueba de chi cuadrado
                t = generacion_tablas.generate_frequency_table(numeros_exp, intervalos)
                print(t)
                # chi_square_calc(t, media, desviacion, distribution_type="Exponencial")
                pass
                
            elif opc_exponencial == 0:
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")