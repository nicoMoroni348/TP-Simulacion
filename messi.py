import random
import matplotlib.pyplot as plt

import distribucion_exponencial
import distribucion_normal
import distribucion_uniforme


n = 1000

numeros_uniformes_0_1 = []

# Generar n numeros aleatorios entre 0;1
for i in range(n):
    numeros_uniformes_0_1.append(random.random())



numeros_exponencial = distribucion_exponencial.distribucion_exponencial(numeros_uniformes_0_1, 30) # Media
numeros_normal = distribucion_normal.distribucion_normal(numeros_uniformes_0_1, 30, 0.1) # Media y desv
numeros_normal = distribucion_uniforme.distribucion_uniforme(numeros_uniformes_0_1, 10, 20) # A y B


print(numeros_exponencial)

plt.hist(numeros_normal)


plt.show()

plt.hist(numeros_exponencial)


plt.show()

