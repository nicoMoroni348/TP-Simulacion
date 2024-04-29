import random
import pandas as pd
import xlsxwriter
import xlsxwriter.format

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
            with open(f"csvs/numeros_aleatorios_{tipo_generacion[i]}.csv", "rt") as f:
                vec = [float(linea.strip()) for linea in f.readlines()]
                vectores_aleatorios.append(vec)
        
    return vectores_aleatorios







def generate_table(vector_estado, i, j, filepath="Tabla de simulacion.xlsx", auto_open=True):

    # Creamos el writer para escribir sobre el excel
    writer = pd.ExcelWriter(filepath, engine="xlsxwriter") 

    # Creamos el dataframe de pandas para escribirlo luego en el excel
    data_frame = pd.DataFrame(vector_estado[j-1:i+j-1])
    data_frame.columns = ['Iteracion', 'Rnd_Puerta', 'Puerta', "Rnd_Genero", 'Genero',
                          "Rnd_Venta", 'Venta', "Rnd_Suscripciones", 
                          'Suscripciones', 'Utilidad_venta', 'Total_utilidad', 
                          'Total_ventas', 'Probabilidad_venta']
    
    
    data_frame.to_excel(writer, sheet_name="Vector Estado", index=False)


    # print(data_frame)




    # Tomamos la hoja creada con pandas y formateamos las columnas para que sea legible
    worksheet = writer.sheets["Vector Estado"]
    # cell_format = workbook.add_format({'num_format': '#.####'})
    # cell_format.set_  # Enable text wrapping in cells (optional)

    column_widths = {
    'Iteracion': 10,
    "Rnd_Puerta": 20,
    'Puerta': 15,
    "Rnd_Genero": 20,
    'Genero': 10,
    "Rnd_Venta": 20,
    'Venta': 12,
    "Rnd_Suscripciones": 20,
    'Suscripciones': 15,
    'Utilidad_venta': 15,
    'Total_utilidad': 15,
    'Total_ventas': 15,
    'Probabilidad_venta': 20,
    }

    

    # Loop through columns and set widths
    for col_idx, col_name in enumerate(data_frame.columns):
        worksheet.set_column(col_idx, col_idx, column_widths[col_name])
        # if pd.api.types.is_numeric_dtype(data_frame[col_name]):
        #     worksheet.set_cell_format(col_idx, col_idx, cell_format)






    

    # Se cierra el writer
    writer.close()




# generate_table([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#                 [2,22,33,44,55,66,77,88,99],
#                 [3,222,333,444,55,66,77,88,99],
#                 [4,22,42133,44,55,66,77,88,99],
#                 [5,22,33,44,55,66,77,88,99],
#                 [6,52522,33,44,55,66,77,88,99],
#                 [7,22,33,44,55,66,77,88,99444],], i=3, j=2)