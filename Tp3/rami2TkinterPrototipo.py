import random
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

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

def simulacion_montecarlo(n_visitas, probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion, distribucion_suscripciones_sra, distribucion_suscripciones_sr, random_values=None):
    total_utilidad = 0
    total_ventas = 0
    historial = []

    for visita in range(n_visitas):
        utilidad_visita = 0
        rnd_puerta, rnd_persona, rnd_venta_sra, rnd_venta_sr = random_values[visita] if random_values else [random.random(), random.random(), random.random(), random.random()]

        if rnd_puerta < probabilidad_puerta_abierta:
            if rnd_persona < 0.8:  # Si es una señora
                if rnd_venta_sra < probabilidad_venta_a_sra:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3], distribucion_suscripciones_sra)
                    utilidad_visita = suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
            else:  # Si es un señor
                if rnd_venta_sr < probabilidad_venta_a_sr:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3, 4], distribucion_suscripciones_sr)
                    utilidad_visita = suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
        total_utilidad += utilidad_visita
        historial.append((visita, utilidad_visita, total_utilidad))

    return total_utilidad, total_ventas, historial

def run_simulation():
    n_visitas = int(n_visitas_entry.get())
    probabilidad_puerta_abierta = float(probabilidad_puerta_abierta_entry.get())
    probabilidad_venta_a_sra = float(probabilidad_venta_a_sra_entry.get())
    probabilidad_venta_a_sr = float(probabilidad_venta_a_sr_entry.get())
    utilidad_por_suscripcion = float(utilidad_por_suscripcion_entry.get())
    distribucion_suscripciones_sra = list(map(float, distribucion_suscripciones_sra_entry.get().split()))
    distribucion_suscripciones_sr = list(map(float, distribucion_suscripciones_sr_entry.get().split()))

    random_values = []
    for _ in range(n_visitas):
        random_values.append([random.random(), random.random(), random.random(), random.random()])

    with open('random_values.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(random_values)

    total_utilidad, total_ventas, historial = simulacion_montecarlo(n_visitas, probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion, distribucion_suscripciones_sra, distribucion_suscripciones_sr, random_values)
    messagebox.showinfo("Resultados", f"Después de {n_visitas} visitas, el vendedor vendió {total_ventas} suscripciones y ganó ${total_utilidad}.")

    for visita, utilidad_visita, total_utilidad in historial:
        print(f"Visita {visita}: Utilidad de la visita = ${utilidad_visita}, Utilidad total hasta ahora = ${total_utilidad}")

def change_parameter():
    parameter = simpledialog.askstring("Cambiar parámetro", "Ingrese el nombre del parámetro que desea cambiar:")
    value = simpledialog.askstring("Cambiar parámetro", f"Ingrese el nuevo valor para {parameter}:")
    if parameter == "n_visitas":
        n_visitas_entry.delete(0, tk.END)
        n_visitas_entry.insert(0, value)
    elif parameter == "probabilidad_puerta_abierta":
        probabilidad_puerta_abierta_entry.delete(0, tk.END)
        probabilidad_puerta_abierta_entry.insert(0, value)
    elif parameter == "probabilidad_venta_a_sra":
        probabilidad_venta_a_sra_entry.delete(0, tk.END)
        probabilidad_venta_a_sra_entry.insert(0, value)
    elif parameter == "probabilidad_venta_a_sr":
        probabilidad_venta_a_sr_entry.delete(0, tk.END)
        probabilidad_venta_a_sr_entry.insert(0, value)
    elif parameter == "utilidad_por_suscripcion":
        utilidad_por_suscripcion_entry.delete(0, tk.END)
        utilidad_por_suscripcion_entry.insert(0, value)
    elif parameter == "distribucion_suscripciones_sra":
        distribucion_suscripciones_sra_entry.delete(0, tk.END)
        distribucion_suscripciones_sra_entry.insert(0, value)
    elif parameter == "distribucion_suscripciones_sr":
        distribucion_suscripciones_sr_entry.delete(0, tk.END)
        distribucion_suscripciones_sr_entry.insert(0, value)
    else:
        messagebox.showerror("Error", "Parámetro no válido.")

root = tk.Tk()

n_visitas_label = tk.Label(root, text="Número de visitas a simular")
n_visitas_entry = tk.Entry(root)
probabilidad_puerta_abierta_label = tk.Label(root, text="Probabilidad de que la puerta se abra")
probabilidad_puerta_abierta_entry = tk.Entry(root)
probabilidad_venta_a_sra_label = tk.Label(root, text="Probabilidad de venta a una señora")
probabilidad_venta_a_sra_entry = tk.Entry(root)
probabilidad_venta_a_sr_label = tk.Label(root, text="Probabilidad de venta a un señor")
probabilidad_venta_a_sr_entry = tk.Entry(root)
utilidad_por_suscripcion_label = tk.Label(root, text="Utilidad por suscripción")
utilidad_por_suscripcion_entry = tk.Entry(root)
distribucion_suscripciones_sra_label = tk.Label(root, text="Distribución de suscripciones para señoras (separadas por espacios)")
distribucion_suscripciones_sra_entry = tk.Entry(root)
distribucion_suscripciones_sr_label = tk.Label(root, text="Distribución de suscripciones para señores (separadas por espacios)")
distribucion_suscripciones_sr_entry = tk.Entry(root)
run_button = tk.Button(root, text="Ejecutar simulación", command=run_simulation)
change_parameter_button = tk.Button(root, text="Cambiar parámetro", command=change_parameter)

n_visitas_label.pack()
n_visitas_entry.pack()
probabilidad_puerta_abierta_label.pack()
probabilidad_puerta_abierta_entry.pack()
probabilidad_venta_a_sra_label.pack()
probabilidad_venta_a_sra_entry.pack()
probabilidad_venta_a_sr_label.pack()
probabilidad_venta_a_sr_entry.pack()
utilidad_por_suscripcion_label.pack()
utilidad_por_suscripcion_entry.pack()
distribucion_suscripciones_sra_label.pack()
distribucion_suscripciones_sra_entry.pack()
distribucion_suscripciones_sr_label.pack()
distribucion_suscripciones_sr_entry.pack()
run_button.pack()
change_parameter_button.pack()

root.mainloop()
