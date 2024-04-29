import random

# Probabilidades y utilidades
probabilidad_puerta_abierta = 0.7
probabilidad_venta_a_sra = 0.15
probabilidad_venta_a_sr = 0.25
utilidad_por_suscripcion = 200

# Distribución de frecuencias relativas
distribucion_suscripciones_sra = [0.60, 0.30, 0.10]
distribucion_suscripciones_sr = [0.10, 0.40, 0.30, 0.20]


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
        


# def generar_numero_aleatorio(generar_nuevo=True):
#     if generar_nuevo:
#         r = random.random()
#         with open("numeros_aleatorios.csv", "r+t") as f:
#             f


def generar_numeros_aleatorios(n=1, generar_nuevos=True):
    tipo_generacion = ('puerta', 'género', 'venta', 'suscripciones')
    
    if generar_nuevos:
        v_puerta = [random.random() for _ in range(n)]
        v_genero = [random.random() for _ in range(n)]
        v_venta = [random.random() for _ in range(n)]
        v_suscripciones = [random.random() for _ in range(n)]

        vectores_aleatorios = [v_puerta, v_genero, v_venta, v_suscripciones]
        
        for i in range(len(vectores_aleatorios)):
            with open(f"numeros_aleatorios_{tipo_generacion[i]}.csv", "wt") as f:
                vec_to_join = [str(valor) for valor in vectores_aleatorios[i]]
                f.write( "\n".join(vec_to_join) )
    
    else:
        
        vectores_aleatorios = []
        for i in range(4):
            with open(f"numeros_aleatorios_{tipo_generacion[i]}.csv", "rt") as f:
                vec = [float(linea.strip()) for linea in f.readlines()]
                vectores_aleatorios.append(vec)
        
    return vectores_aleatorios






def simulacion_visita(n_visitas, generar_nuevos=True):

    

    total_utilidad = 0
    total_ventas = 0

    vector_probabilidades_puerta, vector_probabilidades_genero, \
    vector_probabilidades_venta, vector_probabilidades_suscripciones = generar_numeros_aleatorios(n_visitas, generar_nuevos)
    if not generar_nuevos:
        n_visitas = len(vector_probabilidades_puerta)

    vector_estado = []


    for visita in range(n_visitas):
        if random.random() < probabilidad_puerta_abierta:
            if random.random() < 0.8:  # Si es una señora
                if random.random() < probabilidad_venta_a_sra:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3], distribucion_suscripciones_sra)
                    total_utilidad += suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
                    fila = ["Señora", suscripciones, total_utilidad]
                    vector_estado.append(fila)
            else:  # Si es un señor
                if random.random() < probabilidad_venta_a_sr:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3, 4], distribucion_suscripciones_sr)
                    total_utilidad += suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
                    fila = ["Señor", suscripciones, total_utilidad]

    return total_utilidad, total_ventas

def main():
    n_visitas = int(input("Ingrese el número de visitas a simular: "))
    total_utilidad, total_ventas = simulacion_visita(n_visitas)
    print(f"Después de {n_visitas} visitas, el vendedor vendió {total_ventas} suscripciones y ganó ${total_utilidad}.")
    print(f"La probabilidad de que venda es de: {total_ventas/n_visitas}")

if __name__ == "__main__":
    main()
