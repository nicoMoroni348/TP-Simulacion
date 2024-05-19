import sys
import os

sys.path.append(os.getcwd())

from support import clasificar_numero_aleatorio, get_table

import random 

# -- SIMULACION --

def visita(utilidad_por_suscripcion, probabilidad_genero, probabilidad_venta_mujer, 
           probabilidades_suscripciones_mujer, probabilidades_suscripciones_hombre):
    
    # Esta funcion no devuelve ninguna metrica, solo devuelve los valores simulados de la fila/visita actual
    
    probabilidad_puerta = [0.7, 0.3]
    probabilidad_venta_hombre = [0.25, 0.75]

    #             [rnd_puerta, puerta, rnd_genero, genero, rnd_venta, venta, rnd_subs, subs, utilidad]
    fila_visita = [None, None, None, None, None, None, None, 0, 0.0]

    # Se clasifica el numero aleatorio generado para determinar si se abre la puerta o no
    rnd_puerta = random.random()
    fila_visita[0] = rnd_puerta
    abrio_puerta = clasificar_numero_aleatorio(rnd_puerta, [True, False], probabilidad_puerta)
    fila_visita[1] = abrio_puerta

    # Si abre la puerta 
    if abrio_puerta: 

        # Se clasifica el numero aleatorio generado para determinar el genero
        rnd_genero = random.random()
        fila_visita[2] = rnd_genero
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
        rnd_venta = random.random()
        fila_visita[4] = rnd_venta
        es_venta = clasificar_numero_aleatorio(rnd_venta, [True, False], probabilidad_venta)
        fila_visita[5] = es_venta

        if es_venta:

            # Se clasifica el numero aleatorio generado para determinar la cantidad de suscripciones
            rnd_suscripciones = random.random()
            fila_visita[6] = rnd_suscripciones
            suscripciones = clasificar_numero_aleatorio( rnd_suscripciones, 
                clases_suscripciones, probabilidades_suscripciones)
            
            # Calculamos la utilidad de venta, total de utilidad (acumulado) y el total de ventas 
            utilidad_venta = suscripciones * utilidad_por_suscripcion     
            
            # Actualizamos las ultimas columnas de la fila de la visita
            fila_visita[7:9] = [suscripciones, utilidad_venta]
    
    return fila_visita


def simular_visita(iteracion, fila_anterior, utilidad_por_suscripcion, 
                   probabilidad_genero, probabilidad_venta_mujer,  
                   probabilidades_suscripciones_mujer, probabilidades_suscripciones_hombre):

    # En esta funcion se toma la memoria de una fila, y se van calculando las metricas segun la fila actual y la anterior

    # Tomamos lo que puede quedar igual que la fila anterior
    total_utilidad_anterior = fila_anterior[-3]
    total_ventas_anterior = fila_anterior[-2]

    visita_simulada = visita(utilidad_por_suscripcion, probabilidad_genero, 
                             probabilidad_venta_mujer, probabilidades_suscripciones_mujer, 
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


def simulacion_visitas(n_visitas, i, j, utilidad_por_suscripcion, probabilidad_genero, 
                       probabilidad_venta_mujer, probabilidades_suscripciones_mujer, 
                       probabilidades_suscripciones_hombre):
    
    # Inicializamos el vector estado a retornar
    vector_estado = []

    # Definimos la fila anterior para trabajar con memoria de 2 filas
    # [iteracion, rnd_puerta, puerta, rnd_genero, genero, rnd_venta, venta, rnd_suscripciones, suscripciones, utilidad_venta, total_utilidad, total_ventas, prob_venta]
    fila_anterior = [None, 0.0, None, 0.0, None, 0.0, None, 0.0, None, 0.0, 0.0, 0, 0.0]
    

    for iteracion in range(n_visitas):

        fila_visita = simular_visita(iteracion, fila_anterior, utilidad_por_suscripcion, 
                   probabilidad_genero, probabilidad_venta_mujer, probabilidades_suscripciones_mujer,
                   probabilidades_suscripciones_hombre)
        
        # Actualizar la fila anterior
        fila_anterior = fila_visita

        # Agregar fila al vector estado si esta en el rango seleccionado
        if j-1 <= iteracion <= j+i-2:
            vector_estado.append(fila_visita[:])
        
        # Guardar la última fila
        if iteracion == n_visitas-1:
            ultima_fila = fila_visita[:]
    
    # Retornamos 
    return vector_estado, ultima_fila


if __name__ == "__main__":

    j = 10
    i = 990

    probabilidad_genero = [0.8, 0.2] # este es variable

    probabilidad_venta_mujer = [0.15, 0.85] # este es variable

    probabilidades_suscripciones_mujer = [0.6, 0.3, 0.1] # este es variable
    probabilidades_suscripciones_hombre = [0.1, 0.4, 0.3, 0.2] # este es variable

    utilidad_por_suscripcion = 200.0 # este es variable

    n_visitas = 1000 # este es variable
    
    v_e, u_f = simulacion_visitas(n_visitas, j, i, utilidad_por_suscripcion, 
                        probabilidad_genero, probabilidad_venta_mujer, 
                        probabilidades_suscripciones_mujer, probabilidades_suscripciones_hombre)

    for e in v_e:
        print(e)

    # print(len(v_e[0]))

    get_table(vector_estado=v_e, ultima_fila=u_f)
