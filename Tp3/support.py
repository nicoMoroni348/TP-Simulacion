import random


def acumular_probabilidades(probabilidades):
    acumulados = [probabilidades[0]]
    for i in range(1, len(probabilidades)):
        acumulados.append(probabilidades[i] + acumulados[i-1])
    return acumulados


def clasificar_numero_aleatorio(rnd, clases, probabilidad_x_clase):
    vector_probabilidades_acumuladas = acumular_probabilidades(probabilidad_x_clase)
    for i, prob in enumerate(vector_probabilidades_acumuladas):
        if rnd < prob:
            return clases[i]
        


def generar_numeros_aleatorios(n=1, generar_nuevos=True):
    tipo_generacion = ('puerta', 'género', 'venta', 'suscripciones')
    
    if generar_nuevos:
        v_puerta = [random.random() for _ in range(n)]
        v_genero = [random.random() for _ in range(n)]
        v_venta = [random.random() for _ in range(n)]
        v_suscripciones = [random.random() for _ in range(n)]

        vectores_aleatorios = [v_puerta, v_genero, v_venta, v_suscripciones]
        
        for i in range(len(vectores_aleatorios)):
            with open(f"csvs/numeros_aleatorios_{tipo_generacion[i]}.csv", "wt") as f:
                vec_to_join = [str(valor) for valor in vectores_aleatorios[i]]
                f.write( "\n".join(vec_to_join) )
    
    else:
        
        vectores_aleatorios = []
        for i in range(4):
            with open(f"numeros_aleatorios_{tipo_generacion[i]}.csv", "rt") as f:
                vec = [float(linea.strip()) for linea in f.readlines()]
                vectores_aleatorios.append(vec)
        
    return vectores_aleatorios

