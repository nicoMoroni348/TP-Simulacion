import random
import numpy as np
import matplotlib.pyplot as plt

"""

A partir de un parametro: una lista de valores cualesquiera

Generar distintos histogramas a partir de una lista (en nuestro caso de valores aleatorios)

"""



# def create_histogram(data, bins=10):
#     """
#     Esta función crea un histograma a partir de una lista de datos.
#     """
#     plt.hist(data, bins=bins)

# def show_plot():
#     """
#     Esta función muestra el gráfico.
#     """
#     plt.show()

# def set_title(title):
#     """
#     Esta función establece el título del gráfico.
#     """
#     plt.title(title)

# def set_labels(xlabel, ylabel):
#     """
#     Esta función establece las etiquetas de los ejes x e y.
#     """
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)



def full_histogram(data, bins=10, title="", xlabel="", ylabel="", bin_color="lightgreen", edgecolor="black"):
    """
    Esta función crea un histograma a partir de una lista de datos, establece el título y las etiquetas de los ejes, y muestra el gráfico.
    """
    # Crear el histograma
    plt.hist(data, bins=bins, edgecolor=edgecolor, color=bin_color)

    # Establecer el título y las etiquetas de los ejes
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    positions = np.linspace(min(data), max(data), bins+1)
    plt.xticks(positions)


    # Mostrar el gráfico
    plt.show()
    


