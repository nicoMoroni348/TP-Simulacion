import random
import math
import matplotlib.pyplot as plt
import start.py 
desviacion = 0.1
media = 50

numeros_distribucion_normal = []
for i in range(len(numeros_uniformes_0_1)//2):

    if n % 2 == 0: # Array de aleatorios de tamaño par

        rnd_1 = numeros_uniformes_0_1[i]
        rnd_2 = numeros_uniformes_0_1[-i - 1]
        
        
        x_1 = math.sqrt(-2 * math.log(rnd_1, e)) * math.cos(2 * math.pi * rnd_2) * desviacion + media
        x_2 = math.sqrt(-2 * math.log(rnd_1, e)) * math.sin(2 * math.pi * rnd_2) * desviacion + media


        numeros_distribucion_normal.append(x_1)
        numeros_distribucion_normal.append(x_2)

    else:
        print("jodete")


plt.hist(numeros_distribucion_normal)

plt.show()

print(numeros_distribucion_normal)