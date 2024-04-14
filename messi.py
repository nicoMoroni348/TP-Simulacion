import random
import matplotlib.pyplot as plt
import distribucion_exponencial
import distribucion_normal
import distribucion_uniforme
import generacion_histograma
import generacion_tablas
from soporte import mostrar_datos_lista


n = 10 ** 4

numeros_uniformes_0_1 = []

# Generar n numeros aleatorios entre 0;1
for i in range(n):
    numeros_uniformes_0_1.append(random.random())



numeros_exponencial = distribucion_exponencial.distribucion_exponencial(numeros_uniformes_0_1, 30) # Media
numeros_normal = distribucion_normal.distribucion_normal(numeros_uniformes_0_1, 30, 0.1) # Media y desv
numeros_uniforme = distribucion_uniforme.distribucion_uniforme(numeros_uniformes_0_1, 10, 20) # A y B


# print(numeros_exponencial)


t = generacion_tablas.generate_frequency_table(numeros_normal, 10)
# mostrar_datos_lista(numeros_exponencial)
print(t["Frecuencias"].sum())
print(t)
generacion_histograma.full_histogram(numeros_normal, 10)
