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

import generacion_tablas
import math
from scipy.stats import norm
import pandas as pd

e = math.e
# Bins = intervalo de clase



def chi_square_calc(frequency_table, media=0.0, desviacion=0.0, distribution_type="Uniforme"):
    # Calcular la frecuencia observada
    
    freq_observadas = (frequency_table["Frecuencias"])
    clases = list(frequency_table["Clases"])
    intervalo = round(clases[1] - clases[0], 4)
    k_clases = len(clases)
    clases_bonitas = list(frequency_table["Intervalos"])
    freq_esperadas = [0] * k_clases
    fefo_cuadrado = [0] * k_clases
    fefo_sobre_fe = [0] * k_clases


    if distribution_type == "Uniforme":
        funcion = lambda _: sum(freq_observadas) / k_clases
    elif distribution_type == "Exponencial":
        funcion = lambda xinf, xsup: (1 -  e ** (- (1/media) * xsup)) - (1 -  e ** (- (1/media) * xinf))
    elif distribution_type == "Normal":
        funcion = lambda xinf, xsup: norm.cdf(xsup, media, desviacion) - norm.cdf(xinf, media, desviacion)
    else:
        print("Distribucion no valida")
        return
    

    for i in range(k_clases):
        if distribution_type == "Uniforme":
            freq_esperadas[i] = funcion(0)
        else:
            freq_esperadas[i] = funcion(round(clases[i]-intervalo, 4), clases[i])
        fefo_cuadrado[i] = round((freq_esperadas[i] - freq_observadas[i]) ** 2, 4)
        fefo_sobre_fe[i] = round(fefo_cuadrado[i] / freq_esperadas[i], 4)
    

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

datos = [round(random.uniform(0, 1), 4) for _ in range(1000)]
# print(datos)
tab = generacion_tablas.generate_frequency_table(datos, 10)
chi_square_calc(tab)


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