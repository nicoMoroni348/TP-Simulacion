import pandas as pd
import numpy as np

def categorize_data(d, classes):
    for i in range(len(classes)-1):
        if classes[i] <= d < classes[i+1]:  # Incluir el límite inferior de la clase
            return classes[i+1]
    return classes[0]

def generate_frequency_table(data, k_classes, column_name="frecuencias"):
    # Se establecen valores para generar las clases
    minimo = min(data)
    maximo = max(data)
    rango = maximo-minimo
    intervalo = rango/k_classes

    # Se crean las clases
    clases = [minimo+intervalo]
    for i in range(k_classes-1):
        clases.append(clases[i] + intervalo)
    
    # Crear datos categorizados
    datos_categorizados = [categorize_data(d, clases) for d in data]

    # Convertir a una serie de pandas y especificar las categorías
    datos_categorizados = pd.Series(datos_categorizados, dtype=pd.CategoricalDtype(categories=clases, ordered=True))

    tabla_frecuencias = pd.crosstab(index=datos_categorizados, columns=column_name)

    return tabla_frecuencias

import random

datos = [1, 2, 5, 5, 6, 8, 8, 8, 9, 10, 1, 3]

clases = [4, 8, 12, 16]


contador = [0] * len(clases)


def get_class_index(d, classes):

    for i in range(len(classes)-1):

        if  classes[i] < d <= classes[i+1]: #     4 < d <= 8
            return i+1
        
        elif d <= classes[i]:    #  <  4
            return i
            

for d in datos:
    contador[ get_class_index(d, clases) ] += 1




# catego = [categorize_data(d, clases) for d in datos]

# datos_categorizados = pd.Series(catego, dtype=pd.CategoricalDtype(categories=clases, ordered=True))

# tabla_frecuencias = pd.crosstab(index=datos_categorizados, columns="Frecuencia")

print(datos)

print(clases)
print(contador)


'''
import pandas as pd
import numpy as np

def generate_frequency_table(data, k_classes, column_name="frecuencias"):
    # Se establecen valores para generar las clases
    minimo = min(data)
    maximo = max(data)
    rango = maximo-minimo
    intervalo = rango/k_classes

    # Se crean las clases
    clases = [minimo + i*intervalo for i in range(k_classes+1)]
    
    # Crear datos categorizados
    datos_categorizados = pd.cut(data, bins=clases, include_lowest=True, right=False)

    tabla_frecuencias = pd.crosstab(index=datos_categorizados, columns=column_name)

    return tabla_frecuencias


'''