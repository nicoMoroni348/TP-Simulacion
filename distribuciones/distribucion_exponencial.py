import math



def distribucion_exponencial(numeros_uniformes_0_1, media): 
    lamb = 1/media
    e = math.e

    numeros_distribucion_exponencial_negativa = []

    # Se usa 1 - rnd para que el argumento del logaritmo nunca sea 0
    for rnd in numeros_uniformes_0_1:
        x = round((-1/lamb) * math.log(1-rnd, e), 4)
        numeros_distribucion_exponencial_negativa.append(x)

    with open("datos_exponencial.csv", "wt") as f:
        for e in numeros_distribucion_exponencial_negativa:
            f.write(str(e)+"\n")
        
    return numeros_distribucion_exponencial_negativa
