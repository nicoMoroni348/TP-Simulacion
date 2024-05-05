import sys
import os

sys.path.append(os.getcwd())


from support import clasificar_numero_aleatorio, generar_numeros_aleatorios, generate_table, get_table



# -- PARÁMETROS --

probabilidad_puerta = [0.7, 0.3]

probabilidad_genero = [0.8, 0.2] # este es variable

probabilidad_venta_mujer = [0.15, 0.85] # este es variable

probabilidad_venta_hombre = [0.25, 0.75]

probabilidades_suscripciones_mujer = [0.6, 0.3, 0.1] # este es variable
probabilidades_suscripciones_hombre = [0.1, 0.4, 0.3, 0.2] # este es variable

utilidad_por_suscripcion = 200.0 # este es variable

n_visitas = 1000 # este es variable

# -- SIMULACION --

def visita(rnd_puerta, rnd_genero, rnd_venta, rnd_suscripciones, utilidad_por_suscripcion, 
           probabilidad_puerta, probabilidad_genero, probabilidad_venta_mujer,
           probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
           probabilidades_suscripciones_hombre):
    
    fila_visita = [rnd_puerta, None, rnd_genero, None, rnd_venta, None, rnd_suscripciones, 0, 0.0]

    # Se clasifica el numero aleatorio generado para determinar si se abre la puerta o no
    abrio_puerta = clasificar_numero_aleatorio(rnd_puerta, [True, False], probabilidad_puerta)
    fila_visita[1] = abrio_puerta

    # Si abre la puerta 
    if abrio_puerta: 

        # Se clasifica el numero aleatorio generado para determinar el genero
        genero = clasificar_numero_aleatorio(rnd_genero,
                                                ["M", "H"], probabilidad_genero)
        fila_visita[3] = genero
        
        # Se asigna por defecto la probabilidad de venta y suscripciones para un H, si es M luego se cambia
        probabilidad_venta = probabilidad_venta_hombre
        probabilidades_suscripciones = probabilidades_suscripciones_hombre
        clases_suscripciones = [1, 2, 3, 4]

        # Si Es una seniora
        if genero == "M": 
            probabilidad_venta = probabilidad_venta_mujer
            probabilidades_suscripciones = probabilidades_suscripciones_mujer
            clases_suscripciones = [1, 2, 3]
            
        # Se clasifica el numero aleatorio generado para determinar si se vende o no
        es_venta = clasificar_numero_aleatorio(rnd_venta, [True, False], probabilidad_venta)
        fila_visita[5] = es_venta

        if es_venta:

            # Se clasifica el numero aleatorio generado para determinar la cantidad de suscripciones
            suscripciones = clasificar_numero_aleatorio( rnd_suscripciones, 
                clases_suscripciones, probabilidades_suscripciones)
            
            # Calculamos la utilidad de venta, total de utilidad (acumulado) y el total de ventas 
            utilidad_venta = suscripciones * utilidad_por_suscripcion     
            
            # Actualizamos las ultimas columnas de la fila de la visita
            fila_visita[7:9] = [suscripciones, utilidad_venta]
    
    return fila_visita


def simular_visita(iteracion, fila_anterior, rnd_puerta, rnd_genero, rnd_venta, 
                   rnd_suscripciones, utilidad_por_suscripcion, probabilidad_puerta, 
                   probabilidad_genero, probabilidad_venta_mujer, probabilidad_venta_hombre, 
                   probabilidades_suscripciones_mujer, probabilidades_suscripciones_hombre):
    
    # Tomamos lo que puede quedar igual que la fila anterior
    total_utilidad_anterior = fila_anterior[-3]
    total_ventas_anterior = fila_anterior[-2]

    visita_simulada = visita(rnd_puerta, rnd_genero, rnd_venta, rnd_suscripciones, utilidad_por_suscripcion, 
           probabilidad_puerta, probabilidad_genero, probabilidad_venta_mujer,
           probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
           probabilidades_suscripciones_hombre)
    
    total_utilidad = total_utilidad_anterior + visita_simulada[8]

    # Establecemos el total de ventas actual al anterior en caso de que no se modifique
    total_ventas = total_ventas_anterior
    if visita_simulada[5]:
        total_ventas += 1

    # Calcula la probabilidad de vender en cada iteracion segun el total de ventas actual     
    # ---------------- Se calcula si o si independiente de si se vende (es exito) o no 
    probabilidad_calculada_venta = total_ventas/(iteracion+1)

    fila_visita = [iteracion+1] + visita_simulada + [total_utilidad, total_ventas, probabilidad_calculada_venta]

    return fila_visita


def simulacion_visitas(vectores_numeros_aleatorios, n_visitas, 
                      utilidad_por_suscripcion, probabilidad_puerta, 
                      probabilidad_genero, probabilidad_venta_mujer,
                      probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
                      probabilidades_suscripciones_hombre):
    
    # Inicializamos el vector estado a retornar
    vector_estado = []

    # Desenvolvemos el vector de vectores de numeros aleatorios generados para cada variable
    vector_probabilidades_puerta, vector_probabilidades_genero, \
    vector_probabilidades_venta, vector_probabilidades_suscripciones = vectores_numeros_aleatorios

    # Definimos la fila anterior para trabajar con memoria de 2 filas
    # [iteracion, rnd_puerta, puerta, rnd_genero, genero, rnd_venta, venta, rnd_suscripciones, suscripciones, utilidad_venta, total_utilidad, total_ventas, prob_venta]
    fila_anterior = [None, 0.0, None, 0.0, None, 0.0, None, 0.0, None, 0.0, 0.0, 0, 0.0]
    

    for iteracion in range(n_visitas):

        # Definir los rnd de cada iteracion
        rnd_puerta = vector_probabilidades_puerta[iteracion]
        rnd_genero = vector_probabilidades_genero[iteracion]
        rnd_venta = vector_probabilidades_venta[iteracion]
        rnd_suscripciones = vector_probabilidades_suscripciones[iteracion]

        fila_visita = simular_visita(iteracion, fila_anterior, rnd_puerta, rnd_genero, rnd_venta, 
                   rnd_suscripciones, utilidad_por_suscripcion, probabilidad_puerta, 
                   probabilidad_genero, probabilidad_venta_mujer, probabilidad_venta_hombre, 
                   probabilidades_suscripciones_mujer, probabilidades_suscripciones_hombre)
        
                # Actualizar la fila anterior
        fila_anterior = fila_visita

        # Agregar fila al vector estado
        vector_estado.append(fila_visita)

    # Retornamos 
    return vector_estado


vectores_numeros_aleatorios = generar_numeros_aleatorios(n_visitas, generar_nuevos=False)
vectores_numeros_aleatorios = generar_numeros_aleatorios(n_visitas, generar_nuevos=True)


v_e = simulacion_visitas(vectores_numeros_aleatorios, n_visitas, 
                      utilidad_por_suscripcion, probabilidad_puerta, 
                      probabilidad_genero, probabilidad_venta_mujer,
                      probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
                      probabilidades_suscripciones_hombre)


# for e in v_e:
#     print(e)

# print(len(v_e[0]))

get_table(vector_estado=v_e, i=100, j=40)


