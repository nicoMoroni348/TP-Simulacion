import random
import math
import matplotlib.pyplot as plt


e = math.e

n = 1000

numeros_uniformes_0_1 = []



# Generar n numeros aleatorios entre 0;1
for i in range(n):
    numeros_uniformes_0_1.append(random.random())


# -- DISTRIBUCIÓN UNIFORME --

# a = float(input("Ingrese el límite inferior de la distribución uniforme: "))
# b = float(input("Ingrese el límite superior de la distribución uniforme: "))

# x = a + rnd * (b-a) 

# numeros_distribucion_uniforme = []

#if a >= b:
#    print("El límite inferior a debe ser menor que el límite superior b.")
#else:
#   for rnd in numeros:
#       x = a + rnd * (b-a)
#       numeros_distribucion_uniforme.append(x)
    

# -- DISTRIBUCIÓN EXPONENCIAL --

# media = 4.0
# lamb = 1/media

# numeros_distribucion_exponencial_negativa = []

# for rnd in numeros_uniformes_0_1:
#     x = (-1/lamb) * math.log(1-rnd, e)
#     numeros_distribucion_exponencial_negativa.append(x)
    

#(-1/lambd) * ln(1-rnd)




# -- DISTRIBUCIÓN NORMAL --
#=(RAIZ(-2*LN(C6))*COS(2*PI()*D6))*Desv+Media


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













