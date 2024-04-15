import random


""" En el código que proporcionaste, para cada valor d en la lista data, se realizan las siguientes operaciones:

index = int((d - min_val) / interval): Esta línea de código calcula a qué intervalo (o bin) pertenece el valor actual d. 
Resta el valor mínimo (min_val) de d, divide el resultado por el tamaño del intervalo (interval), y luego convierte el resultado a un entero. 
Esto da como resultado el índice del intervalo al que pertenece d.
if index == bins: index -= 1: Esta línea de código maneja el caso en el que d es igual al valor máximo en data. En este caso, el cálculo anterior 
daría un índice que está fuera del rango de la lista observed_freq, por lo que se reduce el índice en 1 para asegurarse de que caiga dentro del 
rango correcto.
observed_freq[index] += 1: Esta línea de código incrementa el conteo en el intervalo correspondiente en la lista observed_freq. Esto efectivamente 
cuenta cuántos valores en data caen dentro de cada intervalo.
Estas operaciones se realizan para cada valor en data, lo que permite calcular la frecuencia observada de los valores en cada intervalo. 
Esto es un paso crucial en la realización de la prueba de Chi cuadrado.


"""
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
# Bins = intervalo de clase







def chi_square_calc(frequency_table, media=1.0, desviacion=1.0, distribution_type="Uniforme"):
    # Calcular la frecuencia observada
    freq_observadas = list(frequency_table["Frecuencias"])
    n_datos = sum(freq_observadas)
    clases = list(frequency_table["Clases"])
    intervalo = round(clases[1] - clases[0], 4)
    k_clases = len(clases)
    clases_bonitas = list(frequency_table["Intervalos"])
    freq_esperadas = [0] * k_clases
    


    if distribution_type == "Uniforme":
        funcion = lambda _: n_datos / k_clases
    elif distribution_type == "Exponencial":
        funcion = lambda xinf, xsup: (1 -  e ** (- (1/media) * xsup)) - (1 -  e ** (- (1/media) * xinf))
    elif distribution_type == "Normal":
        funcion = lambda xinf, xsup: norm.cdf(xsup, media, desviacion) - norm.cdf(xinf, media, desviacion)
    else:
        print("Distribucion no valida")
        return
    

    # Calcular por primera vez las frecuencias esperadas y fefos
    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = funcion(0)
        else:
            freq_esperadas[i] = round( (funcion(round(clases[i]-intervalo, 4), clases[i])) * n_datos, 4 )
        


    # Agrupar intervalos si hace falta
    
    if [x < 5 for x in freq_esperadas]:
        freq_esperadas, indices_a_modificar = get_new_list_and_indexes_changes(freq_esperadas)


        # Por cada par de indices a juntar, modificar todas las columnas 
        for indice_inicio, indice_final in indices_a_modificar:
            freq_observadas = join_elements_in_list(freq_observadas, indice_inicio, indice_final)
            freq_esperadas = join_elements_in_list(freq_esperadas, indice_inicio, indice_final)
            clases = join_classes_in_list(clases, indice_inicio, indice_final)
        k_clases = len(freq_observadas)







    # Calcular Fefos

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
        "fe-fo/fe": fefo_sobre_fe

    })
    
    # print(tabliti)
    

    chi_cuadrado = round(sum(fefo_sobre_fe), 4)
    # print(f"Chi cuadrao: {chi_cuadrado}")
    return chi_cuadrado, tabliti
















def chi_square_calc_freq_esperada_recalc(frequency_table, media=1.0, desviacion=1.0, distribution_type="Uniforme"):
    # Calcular la frecuencia observada
    freq_observadas = list(frequency_table["Frecuencias"])
    n_datos = sum(freq_observadas)
    clases = list(frequency_table["Clases"])
    intervalo = round(clases[1] - clases[0], 4)
    k_clases = len(clases)
    clases_bonitas = list(frequency_table["Intervalos"])
    freq_esperadas = [0] * k_clases
    


    if distribution_type == "Uniforme":
        funcion = lambda _: n_datos / k_clases
    elif distribution_type == "Exponencial":
        funcion = lambda xinf, xsup: (1 -  e ** (- (1/media) * xsup)) - (1 -  e ** (- (1/media) * xinf))
    elif distribution_type == "Normal":
        funcion = lambda xinf, xsup: norm.cdf(xsup, media, desviacion) - norm.cdf(xinf, media, desviacion)
    else:
        print("Distribucion no valida")
        return
    

    # Calcular por primera vez las frecuencias esperadas y fefos
    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = funcion(0)
        else:
            freq_esperadas[i] = (funcion(round(clases[i]-intervalo, 4), clases[i])) * n_datos
        


    # Agrupar intervalos si hace falta
    
    if [x < 5 for x in freq_esperadas]:
        freq_esperadas, indices_a_modificar = get_new_list_and_indexes_changes(freq_esperadas)


        # Por cada par de indices a juntar, modificar todas las columnas 
        for indice_inicio, indice_final in indices_a_modificar:
            freq_observadas = join_elements_in_list(freq_observadas, indice_inicio, indice_final)
            clases = join_classes_in_list(clases, indice_inicio, indice_final)
        k_clases = len(freq_observadas)



    
    # Re calcular frecuencias esperadas
    freq_esperadas = [0] * k_clases

    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = funcion(0)
        else:
            freq_esperadas[i] = (funcion(round(clases[i]-intervalo, 4), clases[i])) * n_datos









    # Calcular Fefos

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
        "fe-fo/fe": fefo_sobre_fe

    })
    
    print(tabliti)
    

    chi_cuadrado = sum(fefo_sobre_fe)
    print(f"Chi cuadrao: {chi_cuadrado}")
    return chi_cuadrado











def chi_square_calc_sin_agrupar(frequency_table, media=1.0, desviacion=1.0, distribution_type="Uniforme"):
    # Calcular la frecuencia observada
    freq_observadas = list(frequency_table["Frecuencias"])
    n_datos = sum(freq_observadas)
    clases = list(frequency_table["Clases"])
    intervalo = round(clases[1] - clases[0], 4)
    k_clases = len(clases)
    clases_bonitas = list(frequency_table["Intervalos"])
    freq_esperadas = [0] * k_clases
    fefo_cuadrado = [0] * k_clases
    fefo_sobre_fe = [0] * k_clases
    


    if distribution_type == "Uniforme":
        funcion = lambda _: n_datos / k_clases
    elif distribution_type == "Exponencial":
        funcion = lambda xinf, xsup: (1 -  e ** (- (1/media) * xsup)) - (1 -  e ** (- (1/media) * xinf))
    elif distribution_type == "Normal":
        funcion = lambda xinf, xsup: norm.cdf(xsup, media, desviacion) - norm.cdf(xinf, media, desviacion)
    else:
        print("Distribucion no valida")
        return
    

    # Calcular por primera vez las frecuencias esperadas y fefos
    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = funcion(0)
        else:
            freq_esperadas[i] = round((funcion(round(clases[i]-intervalo, 4), clases[i])) * n_datos, 4)
        fefo_cuadrado[i] = round((freq_esperadas[i] - freq_observadas[i]) ** 2, 4)
        fefo_sobre_fe[i] = round(fefo_cuadrado[i] / freq_esperadas[i], 4)
        
        


        

        
    


    # Crear tabla

    tabliti = pd.DataFrame({
        "Clases": clases,
        "Fo": freq_observadas,
        "Fe": freq_esperadas,
        "fe-fo^2": fefo_cuadrado,
        "fe-fo/fe": fefo_sobre_fe

    })
    
    # print(tabliti)
    

    chi_cuadrado = round(sum(fefo_sobre_fe), 4)
    # print(f"Chi cuadrao: {chi_cuadrado}")
    return chi_cuadrado, tabliti






def test_normal(un, media, desv, k=10):

    datos = distribucion_normal.distribucion_normal(un, media, desv)
    tab = generacion_tablas.generate_frequency_table(datos, k)
    chi_square_calc(tab, distribution_type="Normal", media=media, desviacion=desv)
    chi_square_calc_sin_agrupar(tab, distribution_type="Normal", media=media, desviacion=desv)

def test_expo(un, media, k=10):
    datos = distribucion_exponencial.distribucion_exponencial(un, media)
    tab = generacion_tablas.generate_frequency_table(datos, k)
    print("\n\nTABLA CON DATOS AGRUPADOS\n")
    print(chi_square_calc(tab, distribution_type="Exponencial", media=media)[1] )
    print("\n\nTABLA DATOS NO AGRUPADOS\n\n")
    print(chi_square_calc_sin_agrupar(tab, distribution_type="Exponencial", media=media)[1] )





# unifo = [round(random.uniform(0, 1), 4) for _ in range(1000)]

# test_expo(unifo, 30)

# unifo = [round(random.uniform(0, 1), 4) for _ in range(100)]

# datos = distribucion_exponencial.distribucion_exponencial(unifo, 5)

# with open("datostp2.csv", "w") as f:
#     for d in datos:
#         f.write(str(d)+"\n")


with open("datostp2.csv", "rt") as f:
    datos = [round(float(d),4) for d in f.readlines()]

ft = generacion_tablas.generate_frequency_table(datos, 10)
c, t = chi_square_calc(frequency_table=ft, media=5, distribution_type="Exponencial")
c2, t2 = chi_square_calc_sin_agrupar(frequency_table=ft, media=5, distribution_type="Exponencial")
print(c)
print(t)


# datos = distribucion_exponencial.distribucion_exponencial(unifo, 30)

# print(datos)












'''
from scipy.stats import norm

# Define los parámetros para la distribución normal
mu = 0.5113
sigma = 0.93093370591303

# Define los límites
a = -2.359227
b = -2.035683

# Calcula la función de densidad de probabilidad acumulada (CDF) para los límites
cdf_a = norm.cdf(a, mu, sigma)
cdf_b = norm.cdf(b, mu, sigma)

# Imprime los resultados
print(f"La función de densidad de probabilidad acumulada en {a} es {cdf_a}")
print(f"La función de densidad de probabilidad acumulada en {b} es {cdf_b}")





    

datos = [random.uniform(0, 1) for _ in range(1000)]
# print(datos)
tab = generacion_tablas.generate_frequency_table(datos, 10)
chi_square_test(tab)
    


def goated():
    # Calcular la frecuencia esperada
    # fe
    expected_freq = [len(data) / bins] * bins

    # Realizar la prueba de Chi-cuadrado
    # SUM (fe-fo)^2
    chi_square_stat = 0
    for observed, expected in zip(observed_freq, expected_freq):
        chi_square_stat += ((observed - expected) ** 2) / expected

    print(f"Chi-square statistic: {chi_square_stat}")

# # Generar algunos datos aleatorios
# data = [random.uniform(0, 1) for _ in range(1000)]

# freq = generacion_tablas.generate_frequency_table(data, 10)

# # Realizar la prueba de Chi-cuadrado
# chi_square_test(freq)



'''