import sys
import os

sys.path.append(os.getcwd())

from support import clasificar_numero_aleatorio, generar_numeros_aleatorios



# -- PARÁMETROS --

probabilidad_puerta = [0.7, 0.3]

probabilidad_genero = [0.8, 0.2] # este es variable

probabilidad_venta_mujer = [0.15, 0.85] # este es variable

probabilidad_venta_hombre = [0.25, 0.75]

probabilidades_suscripciones_mujer = [0.6, 0.3, 0.1] # este es variable
probabilidades_suscripciones_hombre = [0.1, 0.4, 0.3, 0.2] # este es variable

utilidad_por_suscripcion = 200.0 # este es variable

n_visitas = 100000 # este es variable
 

 
 
# -- SIMULACION --
 
def simulacion_visitas(vectores_numeros_aleatorios, n_visitas, 
                      utilidad_por_suscripcion, probabilidad_puerta, 
                      probabilidad_genero, probabilidad_venta_mujer,
                      probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
                      probabilidades_suscripciones_hombre):
    

    vector_estado = []


    
    vector_probabilidades_puerta, vector_probabilidades_genero, \
    vector_probabilidades_venta, vector_probabilidades_suscripciones = vectores_numeros_aleatorios



    # [iteracion, puerta, genero, venta, suscripciones, utilidad_venta, total_utilidad, total_ventas, prob_venta]
    fila_anterior = [None, None, None, None, None, 0.0, 0.0, 0, 0.0]
    

    for iteracion in range(n_visitas):

        # Definimos la fila actual (en caso de que no se venda)
        total_utilidad_anterior = fila_anterior[-3]
        total_ventas_anterior = fila_anterior[-2]
        prob_calc_ventas_anterior = fila_anterior[-1]

        total_ventas = total_ventas_anterior

        fila_visita = [iteracion+1, False, None, False, 0, 0.0, total_utilidad_anterior, total_ventas_anterior, prob_calc_ventas_anterior]

        abrio_puerta = vector_probabilidades_puerta[iteracion] < probabilidad_puerta[0]

        if abrio_puerta:
            fila_visita[1] = True

            genero = clasificar_numero_aleatorio(vector_probabilidades_genero[iteracion],
                                                   ["M", "H"], probabilidad_genero)
            
            if genero == "M": # Es una seniora
                fila_visita[2] = "M"

                es_venta = vector_probabilidades_venta[iteracion] < probabilidad_venta_mujer[0]

                if es_venta:


                    suscripciones = clasificar_numero_aleatorio(
                        vector_probabilidades_suscripciones[iteracion], 
                        [1, 2, 3], probabilidades_suscripciones_mujer)

                    utilidad_venta = suscripciones * utilidad_por_suscripcion     

                    total_utilidad = total_utilidad_anterior + utilidad_venta
                    total_ventas = total_ventas_anterior + 1
                    
                    
                    # probabilidad_calculada_venta = total_ventas/(iteracion+1)
                    
                    # Actualizamos las ultimas columnas de la fila de la visita
                    fila_visita[3:8] = [True, suscripciones, utilidad_venta, total_utilidad, total_ventas]

                    # Guardar la fila resultado de la simulacion
                    # fila_visita = [iteracion+1, abrio_puerta, genero, es_venta, suscripciones, utilidad_venta, total_utilidad, total_ventas, probabilidad_venta]

        
            else: # Si es hombre
                fila_visita[2] = "H"
                

                es_venta = vector_probabilidades_venta[iteracion] < probabilidad_venta_hombre[0]

                if es_venta:
                    fila_visita[3] = True

                    suscripciones = clasificar_numero_aleatorio(
                        vector_probabilidades_suscripciones[iteracion], 
                        [1, 2, 3, 4], probabilidades_suscripciones_hombre)

                    utilidad_venta = suscripciones * utilidad_por_suscripcion     

                    total_utilidad = total_utilidad_anterior + utilidad_venta
                    total_ventas = total_ventas_anterior + 1
                    
                    
                    # probabilidad_calculada_venta = total_ventas/(iteracion+1)


                    # Actualizamos las ultimas columnas de la fila de la visita
                    fila_visita[3:8] = [True, suscripciones, utilidad_venta, total_utilidad, total_ventas]



                    # Guardar la fila resultado de la simulacion
                    # fila_visita = [iteracion+1, abrio_puerta, genero, es_venta, suscripciones, utilidad_venta, total_utilidad, total_ventas, probabilidad_venta]

        


        # elif utilidad_venta == 0: # si no se vende, se actualiza igual la probabilidad
        #     fila_visita[-1] = total_ventas_anterior/(iteracion+1)
            
        probabilidad_calculada_venta = total_ventas/(iteracion+1)
        fila_visita[-1] = probabilidad_calculada_venta
        # Actualizamos Probabilidad
        # fila_visita[8] = probabilidad_calculada
        # fila_visita = [iteracion+1, abrio_puerta, genero, es_venta, suscripciones, utilidad_venta, total_utilidad, total_ventas, probabilidad_venta]



        # actualizar la fila anterior
        fila_anterior = fila_visita

        # Agregar fila al vector estado
        vector_estado.append(fila_visita)


    return vector_estado





vectores_numeros_aleatorios = generar_numeros_aleatorios(n_visitas, generar_nuevos=True)



v_e = simulacion_visitas(vectores_numeros_aleatorios, n_visitas, 
                      utilidad_por_suscripcion, probabilidad_puerta, 
                      probabilidad_genero, probabilidad_venta_mujer,
                      probabilidad_venta_hombre, probabilidades_suscripciones_mujer, 
                      probabilidades_suscripciones_hombre)


import pandas as pd

df = pd.DataFrame(v_e)

df.to_excel("hola.xlsx", index=False)

# i = 40
# j = 1000

# # print(v_e[i:j])
# for fila in v_e[i-1:j]:
#     print(fila)