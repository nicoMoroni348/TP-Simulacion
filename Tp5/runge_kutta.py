import numpy as np
import random as random
import math as math



# ARMA LA TABLA COMPLETA
def runge_kutta(intervalo_t, coeficiente, termino_independiente):
    # Condicion inicial
    h = 0.01
    t = 0
    p = 0
    tabla_runge_kutta = []
    

    # Para armar la tabla una sola vez usamos el valor máximo que puede tomar t 
    limite_superior_t = intervalo_t[1]    

    while t <= limite_superior_t+h:        
        
        fila = runge_kutta_step(t, p, h, coeficiente, termino_independiente)
        tabla_runge_kutta.append(fila)
        
        t = fila[-2]
        p = fila[-1]

    return tabla_runge_kutta



def f(t, P, coeficiente, termino_independiente):
    # Define la función f(x, y) que representa la ecuación diferencial
    return coeficiente * P + termino_independiente



def runge_kutta_step(t, P, h, coeficiente, termino_independiente):
    
    # Calcula los valores de k1, k2, k3 y k4
    # t se calcula pero no se usa en la derivada parcial
    k1 = h * f(t, P, coeficiente, termino_independiente)
    k2 = h * f(t + h / 2, P + k1 / 2, coeficiente, termino_independiente)
    k3 = h * f(t + h / 2, P + k2 / 2, coeficiente, termino_independiente)
    k4 = h * f(t + h, P + k3, coeficiente, termino_independiente)
    
    # Actualiza los valores de t y P
    t_proximo = t + h
    P_proximo = P + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    
    return t, P, k1, k2, k3, k4, t_proximo, P_proximo



# Recorre la tabla previamente y guarda las variables, calculando N
def calcular_n(tabla_runge_kutta, intervalo_t):

    p_final = None
    n = None
    
    rnd = random.random()
    t_final = (intervalo_t[0] + rnd * (intervalo_t[1] - intervalo_t[0])) # Tiempo de traslado ()

    
    
    for fila in tabla_runge_kutta: 
        print(f"t_final: {t_final}  -   t_runge: {fila[0]}")
        if fila[0] >= t_final:
            print("ENTRO")
            p_final = fila[1] # Guarda la paciencia correspondiente al tiempo objetivo
            break
    
    n = 0
    if t_final != 0:
        n = math.floor(p_final) # Truncamiento al entero inferior más próximo
    

    return rnd, t_final*60, p_final, n




if __name__ == "__main__":
    # EJECUCIÓN

    intervalo_t = (0, 1)
    coeficiente = 0.4
    termino_independiente = 5

    tabla = runge_kutta(intervalo_t, coeficiente, termino_independiente)


    for fila in tabla:
        print(fila)


    for i in range(5):
        cliente = calcular_n(tabla, intervalo_t)
        print(cliente)
