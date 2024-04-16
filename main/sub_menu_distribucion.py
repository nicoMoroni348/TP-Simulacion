import os
import sys
from representaciones import generacion_histograma, generacion_tablas 
from distribuciones import distribucion_exponencial, distribucion_normal, distribucion_uniforme
from chi_cuadrado import prueba_chi_cuadrado
from soporte import generacion_numeros_uniformes
sys.path.append(os.getcwd())

"""

Aca se tiene que pedir los parametros (n, media, desviacion, etc)
Generar la distribucion
Y despues solicitar si se quiere generar historgrama, tabla de freq, o hacer la prueba de chi cuadrado.

"""


def menu_uniforme():
    n = int(input("Ingrese el valor de la muestra: "))
    a = float(input("Ingrese el valor inferior del intervalo: "))
    b = float(input("Ingrese el valor superior del intervalo: ")) 
    numeros_random = generacion_numeros_uniformes(n)
    numeros_uniformes = distribucion_uniforme.distribucion_uniforme(numeros_random, a, b)
    intervalos = int(input("Ingrese el número de intervalos para el histograma: "))

    while True:
        print("\n-- Opciones Uniforme(A,B) --")
        print("1 - Mostrar histograma")
        print("2 - Realizar prueba de chi cuadrado")
        print("0 - Volver al menú principal")
        
        try:
            opc_uniforme = int(input("\nIngrese su opción: "))
            
            if opc_uniforme not in [0, 1, 2]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_uniforme == 1:
                generacion_histograma.full_histogram(numeros_uniformes, intervalos)
                # Llamar a la función para mostrar el histograma

            elif opc_uniforme == 2:
                t = generacion_tablas.generate_frequency_table(numeros_uniformes, intervalos)
                # print(t)
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(t, distribution_type="Uniforme")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                input("\nPresione enter para continuar...")


            elif opc_uniforme == 0:  
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")


def menu_normal():
    n = int(input("Ingrese el valor de la muestra: "))
    numeros_random = generacion_numeros_uniformes(n)
    media = float(input("Ingrese el valor de la media: "))
    desviacion = float(input("Ingrese el valor de la desviación: "))
    numeros_nomrales = distribucion_normal.distribucion_normal(numeros_random, media, desviacion)
    intervalos = int(input("Ingrese el número de intervalos para el histograma: "))
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
                # Llamar a la función para mostrar el histograma
                generacion_histograma.full_histogram(numeros_nomrales, intervalos)
                
            elif opc_normal == 2:
                t = generacion_tablas.generate_frequency_table(numeros_nomrales, intervalos)
                # print(t)
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(t, media, desviacion, distribution_type="Normal")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                
                input("\nPresione enter para continuar...")
                
            elif opc_normal == 0:
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")


def menu_exponencial():
    n = int(input("Ingrese el valor de la muestra: "))
    numeros_random = generacion_numeros_uniformes(n)
    media = float(input("Ingrese el valor de la media: "))
    desviacion = float(input("Ingrese el valor de la desviación: "))
    numeros_exp = distribucion_exponencial.distribucion_exponencial(numeros_random, media)
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

            elif opc_exponencial == 2:
                # Llamar a la función para realizar la prueba de chi cuadrado
                t = generacion_tablas.generate_frequency_table(numeros_exp, intervalos)
                # print(t)
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(t, media, desviacion, distribution_type="Exponencial")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                input("\nPresione enter para continuar...")

                
            elif opc_exponencial == 0:
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")