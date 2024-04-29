import sys
import os

sys.path.append(os.getcwd())

import tkinter as tk
from tkinter import simpledialog
import simulacion_visita as sv

def pedir_n():
    n = simpledialog.askstring("Nuevo numero de simulacion", "Ingrese n:")
    print(n)

def actualizar_parametros():
    ventana_actualizar = tk.Toplevel(root)
    ventana_actualizar.configure(bg='white')

    probabilidad_puerta_abierta_label = tk.Label(ventana_actualizar, text="Probabilidad de que la puerta se abra")
    probabilidad_puerta_abierta_entry = tk.Entry(ventana_actualizar)
    probabilidad_puerta_abierta_label.grid(row=0, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_puerta_abierta_entry.grid(row=0, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_abre_sra_label = tk.Label(ventana_actualizar, text="Probabilidad de que abra la puerta una señora")
    probabilidad_abre_sra_entry = tk.Entry(ventana_actualizar)
    probabilidad_abre_sra_label.grid(row=1, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_abre_sra_entry.grid(row=1, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sra_label = tk.Label(ventana_actualizar, text="Probabilidad de venta a una señora")
    probabilidad_venta_a_sra_entry = tk.Entry(ventana_actualizar)
    probabilidad_venta_a_sra_label.grid(row=2, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_venta_a_sra_entry.grid(row=2, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sr_label = tk.Label(ventana_actualizar, text="Probabilidad de venta a un señor")
    probabilidad_venta_a_sr_entry = tk.Entry(ventana_actualizar)
    probabilidad_venta_a_sr_label.grid(row=3, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_venta_a_sr_entry.grid(row=3, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    utilidad_por_suscripcion_label = tk.Label(ventana_actualizar, text="Utilidad por suscripción")
    utilidad_por_suscripcion_entry = tk.Entry(ventana_actualizar)
    utilidad_por_suscripcion_label.grid(row=4, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    utilidad_por_suscripcion_entry.grid(row=4, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    distribucion_suscripciones_sra_label = tk.Label(ventana_actualizar, text="Distribución de suscripciones para señoras")
    distribucion_suscripciones_sra_frame = tk.Frame(ventana_actualizar)
    distribucion_suscripciones_sra_label.grid(row=5, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    distribucion_suscripciones_sra_frame.grid(row=5, column=1, sticky='w', padx=(5, 10), pady=(5, 5))
    tk.Label(distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry1 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry2 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry3 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)

    distribucion_suscripciones_sr_label = tk.Label(ventana_actualizar, text="Distribución de suscripciones para señores")
    distribucion_suscripciones_sr_frame = tk.Frame(ventana_actualizar)
    distribucion_suscripciones_sr_label.grid(row=6, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    distribucion_suscripciones_sr_frame.grid(row=6, column=1, sticky='w', padx=(5, 10), pady=(5, 5))
    tk.Label(distribucion_suscripciones_sr_frame, text="1").pack(side=tk.LEFT)
    distribucion_suscripciones_sr_entry1 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
    distribucion_suscripciones_sr_entry1.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sr_frame, text="2").pack(side=tk.LEFT)
    distribucion_suscripciones_sr_entry2 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
    distribucion_suscripciones_sr_entry2.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sr_frame, text="3").pack(side=tk.LEFT)
    distribucion_suscripciones_sr_entry3 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
    distribucion_suscripciones_sr_entry3.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sr_frame, text="4").pack(side=tk.LEFT)
    distribucion_suscripciones_sr_entry4 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
    distribucion_suscripciones_sr_entry4.pack(side=tk.LEFT)


    actualizar_button = tk.Button(ventana_actualizar, text="Actualizar", command=lambda: actualizar_valores(
        probabilidad_puerta_abierta_entry.get(),
        probabilidad_venta_a_sra_entry.get(),
        probabilidad_venta_a_sr_entry.get(),
        utilidad_por_suscripcion_entry.get(),
        distribucion_suscripciones_sra_entry1.get(),
        distribucion_suscripciones_sra_entry2.get(),
        distribucion_suscripciones_sra_entry3.get(),
        distribucion_suscripciones_sr_entry1.get(),
        distribucion_suscripciones_sr_entry2.get(),
        distribucion_suscripciones_sr_entry3.get(),
        distribucion_suscripciones_sr_entry4.get()
    ), bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    actualizar_button.grid(row=6, column=0, columnspan=2, pady=(10, 5))
    actualizar_button.bind("<Enter>", lambda e: actualizar_button.config(bg="#87ceeb"))
    actualizar_button.bind("<Leave>", lambda e: actualizar_button.config(bg="#add8e6"))
def actualizar_valores(probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion,
                        distribucion_suscripciones_sra1, distribucion_suscripciones_sra2, distribucion_suscripciones_sra3,
                        distribucion_suscripciones_sr1, distribucion_suscripciones_sr2, distribucion_suscripciones_sr3, distribucion_suscripciones_sr4):
    
    # Aquí debes agregar la lógica para actualizar los valores de los parámetros en tu aplicación

    # ACA SE DEBEN Hacer las validaciones al actualizar los parametros


    print("Probabilidad de puerta abierta:", probabilidad_puerta_abierta)
    print("Probabilidad de venta a señora:", probabilidad_venta_a_sra)
    print("Probabilidad de venta a señor:", probabilidad_venta_a_sr)
    print("Utilidad por suscripción:", utilidad_por_suscripcion)
    print("Distribución de suscripciones para señoras:", distribucion_suscripciones_sra1, distribucion_suscripciones_sra2, distribucion_suscripciones_sra3)
    print("Distribución de suscripciones para señores:", distribucion_suscripciones_sr1, distribucion_suscripciones_sr2, distribucion_suscripciones_sr3, distribucion_suscripciones_sr4)

def abrir_opciones():
    opciones = tk.Toplevel(root)
    opciones.configure(bg='white')
    generar_simulacion_button = tk.Button(opciones, text="Generar simulación", command=generar_simulacion, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    generar_simulacion_button.pack(pady=(10, 5))
    generar_simulacion_button.bind("<Enter>", lambda e: generar_simulacion_button.config(bg="#87ceeb"))
    generar_simulacion_button.bind("<Leave>", lambda e: generar_simulacion_button.config(bg="#add8e6"))

    generar_nuevos_numeros_aleatorios_button = tk.Button(opciones, text="Generar nuevos números aleatorios", command=pedir_n, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    generar_nuevos_numeros_aleatorios_button.pack(pady=(10, 5))
    generar_nuevos_numeros_aleatorios_button.bind("<Enter>", lambda e: generar_nuevos_numeros_aleatorios_button.config(bg="#87ceeb"))
    generar_nuevos_numeros_aleatorios_button.bind("<Leave>", lambda e: generar_nuevos_numeros_aleatorios_button.config(bg="#add8e6"))

    actualizar_parametros_button = tk.Button(opciones, text="Actualizar parámetros", command=actualizar_parametros, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    actualizar_parametros_button.pack(pady=(10, 5))
    actualizar_parametros_button.bind("<Enter>", lambda e: actualizar_parametros_button.config(bg="#87ceeb"))
    actualizar_parametros_button.bind("<Leave>", lambda e: actualizar_parametros_button.config(bg="#add8e6"))

root = tk.Tk()
root.configure(bg='white')

n_visitas_label = tk.Label(root, text="Número de visitas a simular", bg='white')
n_visitas_entry = tk.Entry(root, bg='#f0f0f0')

probabilidad_puerta_abierta_label = tk.Label(root, text="Probabilidad de que la puerta se abra", bg='white') # 0.7
probabilidad_puerta_abierta_entry = tk.Entry(root, bg='#f0f0f0')

probabilidad_abre_sra_label = tk.Label(root, text="Probabilidad de que abra una señora", bg='white')  # 0.8
probabilidad_abre_sra_entry = tk.Entry(root, bg='#f0f0f0')

probabilidad_venta_a_sra_label = tk.Label(root, text="Probabilidad de venta a un señora", bg='white') # 0.15
probabilidad_venta_a_sra_entry = tk.Entry(root, bg='#f0f0f0')

probabilidad_venta_a_sr_label = tk.Label(root, text="Probabilidad de venta a un señor", bg='white') # 0.25
probabilidad_venta_a_sr_entry = tk.Entry(root, bg='#f0f0f0')


utilidad_por_suscripcion_label = tk.Label(root, text="Utilidad por suscripción", bg='white')
utilidad_por_suscripcion_entry = tk.Entry(root, bg='#f0f0f0')

distribucion_suscripciones_sra_label = tk.Label(root, text="Distribución de suscripciones para señoras")
distribucion_suscripciones_sra_frame = tk.Frame(root)
tk.Label(distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
distribucion_suscripciones_sra_entry1 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
tk.Label(distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
distribucion_suscripciones_sra_entry2 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
tk.Label(distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
distribucion_suscripciones_sra_entry3 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)

distribucion_suscripciones_sr_label = tk.Label(root, text="Distribución de suscripciones para señores")
distribucion_suscripciones_sr_frame = tk.Frame(root)
tk.Label(distribucion_suscripciones_sr_frame, text="1").pack(side=tk.LEFT)
distribucion_suscripciones_sr_entry1 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
distribucion_suscripciones_sr_entry1.pack(side=tk.LEFT)
tk.Label(distribucion_suscripciones_sr_frame, text="2").pack(side=tk.LEFT)
distribucion_suscripciones_sr_entry2 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
distribucion_suscripciones_sr_entry2.pack(side=tk.LEFT)
tk.Label(distribucion_suscripciones_sr_frame, text="3").pack(side=tk.LEFT)
distribucion_suscripciones_sr_entry3 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
distribucion_suscripciones_sr_entry3.pack(side=tk.LEFT)
tk.Label(distribucion_suscripciones_sr_frame, text="4").pack(side=tk.LEFT)
distribucion_suscripciones_sr_entry4 = tk.Entry(distribucion_suscripciones_sr_frame, width=5)
distribucion_suscripciones_sr_entry4.pack(side=tk.LEFT)


listo_button = tk.Button(root, text="Listo", command=abrir_opciones, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
listo_button.grid(row=16, column=0, columnspan=2, pady=(10, 5))
listo_button.bind("<Enter>", lambda e: listo_button.config(bg="#87ceeb"))
listo_button.bind("<Leave>", lambda e: listo_button.config(bg="#add8e6"))

cancelar_button = tk.Button(root, text="Cancelar", bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
cancelar_button.grid(row=17, column=0, columnspan=2, pady=(10, 5))
cancelar_button.bind("<Enter>", lambda e: cancelar_button.config(bg="#87ceeb"))
cancelar_button.bind("<Leave>", lambda e: cancelar_button.config(bg="#add8e6"))

widgets = [
    (n_visitas_label, n_visitas_entry),
    (probabilidad_puerta_abierta_label, probabilidad_puerta_abierta_entry),
    (probabilidad_venta_a_sra_label, probabilidad_venta_a_sra_entry),
    (probabilidad_venta_a_sr_label, probabilidad_venta_a_sr_entry),
    (utilidad_por_suscripcion_label, utilidad_por_suscripcion_entry),
    (distribucion_suscripciones_sra_label, distribucion_suscripciones_sra_frame),
    (distribucion_suscripciones_sr_label, distribucion_suscripciones_sr_frame),
    (listo_button, cancelar_button),
]

for i, (label, entry) in enumerate(widgets):
    label.grid(row=i, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    entry.grid(row=i, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

root.mainloop()
