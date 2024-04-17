import pandas as pd
import random



def categorize_data(d, classes):
    for i in range(len(classes)-1):
        if classes[i] < d <= classes[i+1]:
            return classes[i+1]
    return classes[0]


def get_class_index(d, classes):

    for i in range(len(classes)-1):

        if  classes[i] < d <= classes[i+1]:      #     4 < d <= 8
            return i+1
        
        elif d <= classes[i]:    #  <  4
            return i


def generate_frequency_table(data, k_classes, column_name="frecuencias"):

    # Se establecen valores para generar las clases
    minimo = round(min(data),4)
    maximo = round(max(data), 4)
    rango = maximo-minimo
    intervalo = round(rango/k_classes, 4)

    # Se crean las clases
    clases = [round(minimo+intervalo, 4)]
    for i in range(k_classes-2):
        clases.append(round(clases[i] + intervalo, 4))
    clases.append(maximo)
    
    # Contar Frecuencias
    contador_frecuencias = [0] * k_classes
    

    for d in data:
        index = get_class_index(d, clases)
        if index is not None:
            contador_frecuencias[index] += 1
        else:
            print(d)
    


    clases_bonito = []
    for i,c in enumerate(clases):
        if i == 0:
            first = minimo
        else:
            first = clases[i-1]
        b = f"{first} - {round(c,4)}"
        clases_bonito.append(b)


    tabla_frecuencias = pd.DataFrame({
        "Clases": clases,
        "Intervalos": clases_bonito,
        "Frecuencias": contador_frecuencias
        })
    

    return tabla_frecuencias

