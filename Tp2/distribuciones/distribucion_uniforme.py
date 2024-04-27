def distribucion_uniforme(numeros_uniformes_0_1, a, b):
    numeros_distribucion_uniforme = []

    for rnd in numeros_uniformes_0_1:
        x = round(  a + rnd * (b-a)  , 4)
        numeros_distribucion_uniforme.append(x)
        
    with open("datos_uniforme.csv", "wt") as f:
        for e in numeros_distribucion_uniforme:
            f.write(str(e)+"\n")

    return numeros_distribucion_uniforme

