import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

def pedir_n():
    n = simpledialog.askstring("Nuevo numero de simulacion", "Ingrese n:")
    print(n)

def actualizar_parametros():
    ventana_actualizar = tk.Toplevel(root)

    def actualizar_valores():
        # Aquí debes agregar la lógica para actualizar los valores de los parámetros en tu aplicación
        print("Probabilidad de puerta abierta:", probabilidad_puerta_abierta_entry.get())
        print("Probabilidad de venta a señora:", probabilidad_venta_a_sra_entry.get())
        print("Probabilidad de venta a señor:", probabilidad_venta_a_sr_entry.get())
        print("Utilidad por suscripción:", utilidad_por_suscripcion_entry.get())
        print("Distribución de suscripciones para señoras:", distribucion_suscripciones_sra_entry1.get(),
              distribucion_suscripciones_sra_entry2.get(), distribucion_suscripciones_sra_entry3.get())
        print("Distribución de suscripciones para señores:", distribucion_suscripciones_sr_entry1.get(),
              distribucion_suscripciones_sr_entry2.get(), distribucion_suscripciones_sr_entry3.get(),
              distribucion_suscripciones_sr_entry4.get())
        ventana_actualizar.destroy()

    probabilidad_puerta_abierta_label = tk.Label(ventana_actualizar, text="Probabilidad de que la puerta se abra")
    probabilidad_puerta_abierta_entry = tk.Entry(ventana_actualizar)
    probabilidad_puerta_abierta_label.grid(row=0, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_puerta_abierta_entry.grid(row=0, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sra_label = tk.Label(ventana_actualizar, text="Probabilidad de venta a una señora")
    probabilidad_venta_a_sra_entry = tk.Entry(ventana_actualizar)
    probabilidad_venta_a_sra_label.grid(row=1, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_venta_a_sra_entry.grid(row=1, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sr_label = tk.Label(ventana_actualizar, text="Probabilidad de venta a un señor")
    probabilidad_venta_a_sr_entry = tk.Entry(ventana_actualizar)
    probabilidad_venta_a_sr_label.grid(row=2, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    probabilidad_venta_a_sr_entry.grid(row=2, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    utilidad_por_suscripcion_label = tk.Label(ventana_actualizar, text="Utilidad por suscripción")
    utilidad_por_suscripcion_entry = tk.Entry(ventana_actualizar)
    utilidad_por_suscripcion_label.grid(row=3, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    utilidad_por_suscripcion_entry.grid(row=3, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    distribucion_suscripciones_sra_label = tk.Label(ventana_actualizar, text="Distribución de suscripciones para señoras")
    distribucion_suscripciones_sra_frame = tk.Frame(ventana_actualizar)
    distribucion_suscripciones_sra_label.grid(row=4, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    distribucion_suscripciones_sra_frame.grid(row=4, column=1, sticky='w', padx=(5, 10), pady=(5, 5))
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
    distribucion_suscripciones_sr_label.grid(row=5, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    distribucion_suscripciones_sr_frame.grid(row=5, column=1, sticky='w', padx=(5, 10), pady=(5, 5))
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

    actualizar_button = tk.Button(ventana_actualizar, text="Actualizar", command=actualizar_valores)
    actualizar_button.grid(row=6, column=0, columnspan=2, pady=(10, 5))

    ventana_actualizar.protocol("WM_DELETE_WINDOW", ventana_actualizar.destroy)  # Cerrar la ventana secundaria al cerrarla

def abrir_opciones():
    opciones = tk.Toplevel(root)
    opciones.title("Opciones")

    def cerrar_ventana():
        opciones.destroy()

    generar_simulacion_button = tk.Button(opciones, text="Generar simulación")
    generar_nuevos_numeros_aleatorios_button = tk.Button(opciones, text="Generar nuevos números aleatorios", command=pedir_n)
    actualizar_parametros_button = tk.Button(opciones, text="Actualizar parámetros", command=actualizar_parametros)
    generar_simulacion_button.pack()
    generar_nuevos_numeros_aleatorios_button.pack()
    actualizar_parametros_button.pack()

    listo_button = tk.Button(opciones, text="Listo", command=cerrar_ventana)
    listo_button.pack()

    opciones.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Cerrar la ventana secundaria al cerrarla

root = tk.Tk()
root.title("Simulación")

image = Image.open("ruta/a/la/imagen.jpg")  # Reemplaza "ruta/a/la/imagen.jpg" con la ruta de tu imagen
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, columnspan=2)  # Ubica la imagen en la posición deseada

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

listo_button = tk.Button(root, text="Listo", command=abrir_opciones)
cancelar_button = tk.Button(root, text="Cancelar", command=root.quit)

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
