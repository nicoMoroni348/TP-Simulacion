import tkinter as tk
from tkinter import simpledialog


root = tk.Tk()




def pedir_n():
    n = simpledialog.askstring("Nuevo numero de simulacion", "Ingrese n:")
    print(n)



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
run_simulation_button = tk.Button(root, text="Ejecutar simulación")
update_parameters_button = tk.Button(root, text="Actualizar parámetros")
create_new_random_distribution_button = tk.Button(root, text="Generar nuevos numeros aleatorios", command=pedir_n)

widgets = [
    # n_visitas_label,
    
    # n_visitas_entry,
    probabilidad_puerta_abierta_label,
    probabilidad_puerta_abierta_entry,
    probabilidad_venta_a_sra_label,
    probabilidad_venta_a_sra_entry,
    probabilidad_venta_a_sr_label,
    probabilidad_venta_a_sr_entry,
    utilidad_por_suscripcion_label,
    utilidad_por_suscripcion_entry,
    distribucion_suscripciones_sra_label,
    distribucion_suscripciones_sra_entry,
    distribucion_suscripciones_sr_label,
    distribucion_suscripciones_sr_entry,
    run_simulation_button,
    create_new_random_distribution_button,
    update_parameters_button,
    
]

[w.pack() for w in widgets]


root.mainloop()