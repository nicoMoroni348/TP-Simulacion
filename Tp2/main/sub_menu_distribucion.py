import os
import sys
from representaciones import generacion_histograma, generacion_tablas 
from distribuciones import distribucion_exponencial, distribucion_normal, distribucion_uniforme
from chi_cuadrado import prueba_chi_cuadrado
from soporte import generacion_numeros_uniformes, validar_muestra, validar_intervalo_a_b, mostrar_datos_lista, seleccionar_intervalos_histograma, validar_media
sys.path.append(os.getcwd())

"""

Aca se tiene que pedir los parametros (n, media, desviacion, etc)
Generar la distribucion
Y despues solicitar si se quiere generar historgrama, tabla de freq, o hacer la prueba de chi cuadrado.

"""


def menu_uniforme():
    n = validar_muestra()
    a, b = validar_intervalo_a_b()
    numeros_random = generacion_numeros_uniformes(n)
    numeros_uniformes = distribucion_uniforme.distribucion_uniforme(numeros_random, a, b)
    intervalos = seleccionar_intervalos_histograma()
    t = generacion_tablas.generate_frequency_table(numeros_uniformes, intervalos)
    
    while True:

        print("\n-- Opciones Uniforme(A,B) --")
        print("1 - Mostrar serie de números generada")
        print("2 - Mostrar histograma")
        print("3 - Mostrar tabla de frecuencias")
        print("4 - Calcular chi cuadrado")
        print("5 - Ingresar nuevo numeros de intervalos")
        print("0 - Volver al menú principal")

        try:
            opc_uniforme = int(input("\nIngrese su opción: "))

            if opc_uniforme not in [0, 1, 2, 3, 4, 5]:  
                print("\nIngrese un valor dentro de las opciones...")

            elif opc_uniforme == 1:
                print("Serie de números generada:")
                mostrar_datos_lista(numeros_uniformes)

            elif opc_uniforme == 2:
                generacion_histograma.full_histogram(numeros_uniformes, intervalos)

            elif opc_uniforme == 3:
                print("\n Tabla de frecuencias:")
                print(t)
                input("\nPresione enter para continuar...")

            elif opc_uniforme == 4:
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(numeros_uniformes, t, distribution_type="Uniforme")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                input("\nPresione enter para continuar...")

            elif opc_uniforme == 5:
                    intervalos = seleccionar_intervalos_histograma()
                    t = generacion_tablas.generate_frequency_table(numeros_uniformes, intervalos)

            elif opc_uniforme == 0:
                return  
            
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")





def menu_normal():
    n = validar_muestra()

    numeros_random = generacion_numeros_uniformes(n)

    media = float(input("Ingrese el valor de la media: "))
    desviacion = float(input("Ingrese el valor de la desviación: "))

    numeros_nomrales = distribucion_normal.distribucion_normal(numeros_random, media, desviacion)

    intervalos = seleccionar_intervalos_histograma()

    t = generacion_tablas.generate_frequency_table(numeros_nomrales, intervalos)

    while True:
        print("\n-- Opciones Distribución Normal --")
        print("1 - Mostrar serie de números generada")
        print("2 - Mostrar histograma")
        print("3 - Mostrar tabla de frecuencias")
        print("4 - Calcular chi cuadrado")
        print("5 - Ingresar nuevo numeros de intervalos")
        print("0 - Volver al menú principal")
        
        try:
            opc_normal = int(input("\nIngrese su opción: "))
            
            if opc_normal not in [0, 1, 2, 3, 4, 5]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_normal == 1:
                print("Serie de números generada:")
                mostrar_datos_lista(numeros_nomrales)
            
            elif opc_normal == 2:
                generacion_histograma.full_histogram(numeros_nomrales, intervalos)

            elif opc_normal == 3:
                print("\n Tabla de frecuencias:")
                print(t)
                input("\nPresione enter para continuar...")
                
            elif opc_normal == 4:
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(numeros_nomrales, t, distribution_type="Normal")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                
                input("\nPresione enter para continuar...")
            
            elif opc_normal == 5:
                intervalos = seleccionar_intervalos_histograma()

                t = generacion_tablas.generate_frequency_table(numeros_nomrales, intervalos)
                
            elif opc_normal == 0:
                break
        
        except ValueError:
            print(opc_normal)
            print("Opción no válida. Por favor ingrese un número entero.")


def menu_exponencial():
    n = validar_muestra()

    numeros_random = generacion_numeros_uniformes(n)

    media = validar_media()

    numeros_exp = distribucion_exponencial.distribucion_exponencial(numeros_random, media)

    intervalos = seleccionar_intervalos_histograma()

    t = generacion_tablas.generate_frequency_table(numeros_exp, intervalos)    
    while True:
        print("\n-- Opciones Distribución Exponencial --")
        print("1 - Mostrar serie de números generada")
        print("2 - Mostrar histograma")
        print("3 - Mostrar tabla de frecuencias")
        print("4 - Calcular chi cuadrado")
        print("5 - Ingresar nuevo numeros de intervalos")
        print("0 - Volver al menú principal")
        
        try:
            opc_exponencial = int(input("\nIngrese su opción: "))
            
            if opc_exponencial not in [0, 1, 2, 3, 4, 5]:
                print("\nIngrese un valor dentro de las opciones...")
            
            elif opc_exponencial == 1:
                print("Serie de números generada:")
                mostrar_datos_lista(numeros_exp)

            elif opc_exponencial == 2:
                generacion_histograma.full_histogram(numeros_exp, intervalos)

            elif opc_exponencial == 3:
                print("\n Tabla de frecuencias:")
                print(t)
                input("\nPresione enter para continuar...")

            elif opc_exponencial == 4:
                chi_cuadrado, tabliti = prueba_chi_cuadrado.chi_square_calc(numeros_exp, t, distribution_type="Exponencial")
                print("Tabla de chi cuadrado: \n", tabliti)
                print("Chi cuadrado: ", chi_cuadrado)
                input("\nPresione enter para continuar...")

            elif opc_exponencial == 5:
                intervalos = seleccionar_intervalos_histograma()
                t = generacion_tablas.generate_frequency_table(numeros_exp, intervalos)  


                
            elif opc_exponencial == 0:
                break
        
        except ValueError:
            print("Opción no válida. Por favor ingrese un número entero.")