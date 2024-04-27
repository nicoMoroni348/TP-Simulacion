import math


def distribucion_normal(numeros_uniformes_0_1, media, desviacion):

    e = math.e

    numeros_distribucion_normal = []
    if len(numeros_uniformes_0_1) % 2 != 0: # Si el array de aleatorios es impar
        numeros_uniformes_0_1 = numeros_uniformes_0_1[:-1] # Descarta el último elemento

    for i in range(len(numeros_uniformes_0_1)//2):

        rnd_1 = numeros_uniformes_0_1[i]
        rnd_2 = numeros_uniformes_0_1[-i - 1] # Último de la lista
    
        x_1 = math.sqrt(-2 * math.log(1-rnd_1, e)) * math.cos(2 * math.pi * rnd_2) * desviacion + media
        x_2 = math.sqrt(-2 * math.log(1-rnd_1, e)) * math.sin(2 * math.pi * rnd_2) * desviacion + media
    
        x_1 = round(x_1, 4)
        x_2 = round(x_2, 4)

        numeros_distribucion_normal.append(x_1)
        numeros_distribucion_normal.append(x_2)

    with open("datos_normal.csv", "wt") as f:
        for e in numeros_distribucion_normal:
            f.write(str(e)+"\n")

        
    return numeros_distribucion_normal
