import math

e = math.e

def distribucion_normal(numeros_uniformes_0_1, media, desviacion):

    numeros_distribucion_normal = []
    for i in range(len(numeros_uniformes_0_1)//2):

        if len(numeros_uniformes_0_1) % 2 == 0: # Array de aleatorios de tamaño par

            rnd_1 = numeros_uniformes_0_1[i]
            rnd_2 = numeros_uniformes_0_1[-i - 1]
            
            
            x_1 = math.sqrt(-2 * math.log(1-rnd_1, e)) * math.cos(2 * math.pi * rnd_2) * desviacion + media
            x_2 = math.sqrt(-2 * math.log(1-rnd_1, e)) * math.sin(2 * math.pi * rnd_2) * desviacion + media

            x_1 = round(x_1, 4)
            x_2 = round(x_2, 4)


            numeros_distribucion_normal.append(x_1)
            numeros_distribucion_normal.append(x_2)

        else:
            print("jodete")


    return numeros_distribucion_normal