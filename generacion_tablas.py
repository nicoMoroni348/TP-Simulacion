import pandas as pd
import random

"""
ESA

def categorize_values(value, classes):
    for i in range(len(classes)-1):
        if classes[i] <= value <= classes[i+1]:
            return classes[i+1]
        if value < classes[i]:
            return classes[0]



classes = [2, 4, 6, 8, 10]

xs = [1, 3, 5, 5, 7, 7, 4, 2, 6, 3, 7, 10, 9, 8, 7, 5, 3, 1, 5, 6, 7]
categorized_data = [categorize_values(x, classes) for x in xs]


frequency_table_df = pd.DataFrame(categorized_data)
frequency_table_df.columns = ["Value"]
frequency_table = frequency_table_df["Value"].value_counts().sort_index(ascending=False)

print(frequency_table)

"""
import distribucion_normal

datos = [round(random.random(),4) for _ in range(1000)]

di = distribucion_normal.distribucion_normal(datos, 5.4, 5)



def categorize_data(d, classes):
    for i in range(len(classes)-1):
        if classes[i] < d <= classes[i+1]:
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

    tabla_frecuencias = pd.crosstab(index=datos_categorizados, columns=column_name)

    return tabla_frecuencias


# t = generate_frequency_table(di, 7)
# print(t)


# # df = pd.DataFrame(datos)

# # print(datos)
# minimo = min(di)
# maximo = max(di)
# rango = maximo-minimo
# k = 7
# intervalo = rango/k


# clases = [minimo]
# for i in range(k - 1):
#     clases.append(clases[i] + intervalo)

# print(clases)


# # classes = [0.2, 0.4, 0.6, 0.8, 1]

# # crosstable = pd.crosstab(index=datos, columns="count")
# categorized_table = pd.crosstab(index=[categorize_data(d, clases) for d in di], columns="count")
# # categorized_table.columns["Datos", "Frecuencia"]

# print(categorized_table)











