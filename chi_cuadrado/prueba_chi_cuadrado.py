import random
import os
import sys
sys.path.append(os.getcwd())

from distribuciones import distribucion_normal
from distribuciones import distribucion_exponencial
from representaciones import generacion_tablas
import math
from scipy.stats import norm
import pandas as pd
from soporte import get_new_list_and_indexes_changes, join_elements_in_list, join_classes_in_list

e = math.e

def chi_square_calc(datos, frequency_table, distribution_type="Uniforme"):

    # Setea media y desviacion estandar en caso de utilizarla
    media = round(sum(datos) / len(datos), 4)
    # para que no quede indefinida la variable desviacion en caso de no ser una distribucion Normal
    desviacion = 1.0

    n_datos = len(datos)

    # Obtener cada columna de la tabla de frecuencia
    freq_observadas = list(frequency_table["Frecuencias"])
    clases = list(frequency_table["Clases"])

    intervalo = round(clases[1] - clases[0], 4)
    k_clases = len(clases)
    clases_bonitas = list(frequency_table["Intervalos"])


    # Inicializar vector de frecuencias esperadas en 0
    freq_esperadas = [0] * k_clases
    


    # Definicion de la funcion densidad acumulada segun la distribucion, para calcular la esperada
    if distribution_type == "Uniforme":
        funcion = lambda _: n_datos / k_clases
    elif distribution_type == "Exponencial":
        funcion = lambda xinf, xsup: (1 -  e ** (- (1/media) * xsup)) - (1 -  e ** (- (1/media) * xinf))
    elif distribution_type == "Normal":

        # Calcular la desviacion estandar
        desviacion = round(  math.sqrt(sum([(e - media) ** 2 for e in datos]) / (len(datos)-1) )     , 4)

        # Aqui utilizamos la libreria scipy stats
        funcion = lambda xinf, xsup: norm.cdf(xsup, media, desviacion) - norm.cdf(xinf, media, desviacion)
        
    # Si pasa por parametro una distribucion invalida
    else:
        print("Distribucion no valida")
        return
    

    # Calcular por primera vez las frecuencias esperadas
    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = round(funcion(0), 4)
        else:
            # Si no es uniforme, se aplica la funcion pasando por parametro 
            freq_esperadas[i] = round( (funcion(   round(clases[i]-intervalo, 4),    clases[i])) * n_datos, 4 )



    # Agrupar intervalos si hace falta
    # Verificar si en el vector freq_esperadas hay algun valor menor a 5
    if [x < 5 for x in freq_esperadas]:

        # Agrupa el vector de frecuencias esperadas, 
        # y retorna ademas los cambios que le fue haciendo al vector para poder luego aplicarlo a las demas columnas
        freq_esperadas, indices_a_modificar = get_new_list_and_indexes_changes(freq_esperadas)


        # Por cada par de indices a juntar, modificar todas las columnas MENOS LAS FRECUENCIAS ESPERADAS, porque eso se hizo 2 lineas atras
        for indice_inicio, indice_final in indices_a_modificar:
            freq_observadas = join_elements_in_list(freq_observadas, indice_inicio, indice_final)          
            clases = join_classes_in_list(clases, indice_inicio, indice_final)
        k_clases = len(freq_observadas)




    # Calcular los estadisticos individuales de prueba:
    # (fe-fo)^2/fe

    fefo_cuadrado = [0] * k_clases
    fefo_sobre_fe = [0] * k_clases
    for i in range(k_clases):
        fefo_cuadrado[i] = round((freq_esperadas[i] - freq_observadas[i]) ** 2, 4)
        fefo_sobre_fe[i] = round(fefo_cuadrado[i] / freq_esperadas[i], 4)
    


    # Crear tabla

    tabliti = pd.DataFrame({
        "Clases": clases,
        "Fo": freq_observadas,
        "Fe": freq_esperadas,
        "fe-fo^2": fefo_cuadrado,
        "(fe-fo)^2/fe": fefo_sobre_fe

    })
    
    # print(tabliti)
    

    chi_cuadrado = round(sum(fefo_sobre_fe), 4)
    # print(f"Chi cuadrao: {chi_cuadrado}")
    return chi_cuadrado, tabliti






# with open("datos_normal.csv", "rt") as f:

#     datos = [float(d.strip()) for d in f.readlines()]


# t = generacion_tablas.generate_frequency_table(datos, 10)


# chi, t2 = chi_square_calc(datos, t, "Normal")
# print(chi)
# print(t2)