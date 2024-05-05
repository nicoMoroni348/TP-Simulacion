import tkinter as tk
from tkinter import simpledialog


# --- Variables Globales (mala practica xD)

menu_principal = menu_config_inicial = menu_actualizar_parametros = None






# exit()


# --- DEFINICION DE PARAMETROS ---

n_visitas = 0
probabilidad_puerta_abierta = 0.0
probabilidad_abre_sra = 0.0
probabilidad_venta_a_sra = 0.0
probabilidad_venta_a_sr = 0.0
utilidad_por_suscripcion = 0.0
distribucion_suscripciones_sra = [0.0, 0.0, 0.0]
distribucion_suscripciones_sr = [0.0, 0.0, 0.0, 0.0]
crear_nuevos_rnd = False


def on_closing():
    for e in (menu_actualizar_parametros, menu_principal, menu_config_inicial):
        if e is not None:
            e.destroy()


def volver_al_menu():
    if menu_actualizar_parametros is not None:
        menu_actualizar_parametros.withdraw()

    menu_config_inicial.withdraw()
        




def actualizar_parametros():
    
    # Aquí debes agregar la lógica para actualizar los valores de los parámetros en tu aplicación

    # ACA SE DEBEN Hacer las validaciones al actualizar los parametros
    menu_actualizar_parametros.withdraw()
    menu_principal.deiconify()

    # print("Probabilidad de puerta abierta:", probabilidad_puerta_abierta)
    # print("Probabilidad de venta a señora:", probabilidad_venta_a_sra)
    # print("Probabilidad de venta a señor:", probabilidad_venta_a_sr)
    # print("Utilidad por suscripción:", utilidad_por_suscripcion)
    # print("Distribución de suscripciones para señoras:", distribucion_suscripciones_sra1, distribucion_suscripciones_sra2, distribucion_suscripciones_sra3)
    # print("Distribución de suscripciones para señores:", distribucion_suscripciones_sr1, distribucion_suscripciones_sr2, distribucion_suscripciones_sr3, distribucion_suscripciones_sr4)




def pedir_n_visitas():
    n_visitas_input_value = simpledialog.askstring("Nuevo numero de simulacion", "Ingrese n:")

    # Aca Hacer la validacion de n ()


    # si es none es que se puso cancelar, No cambia nada
    if n_visitas_input_value == None:
        return



def abrir_menu_actualizar_parametros():

    # Se cierra el menu principal
    menu_principal.withdraw()

    # Se define el menu actualizar parametros
    global menu_actualizar_parametros
    menu_actualizar_parametros = tk.Toplevel(menu_config_inicial)
    menu_actualizar_parametros.configure(bg='white')
    menu_actualizar_parametros.protocol("WM_DELETE_WINDOW", on_closing)
    menu_actualizar_parametros.resizable(False, False)


    # ---------- Labels y Entries
    probabilidad_puerta_abierta_label = tk.Label(menu_actualizar_parametros, text="Probabilidad de que la puerta se abra")
    probabilidad_puerta_abierta_entry = tk.Entry(menu_actualizar_parametros)
    # probabilidad_puerta_abierta_label.grid(row=0, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # probabilidad_puerta_abierta_entry.grid(row=0, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_abre_sra_label = tk.Label(menu_actualizar_parametros, text="Probabilidad de que abra la puerta una señora")
    probabilidad_abre_sra_entry = tk.Entry(menu_actualizar_parametros)
    # probabilidad_abre_sra_label.grid(row=1, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # probabilidad_abre_sra_entry.grid(row=1, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sra_label = tk.Label(menu_actualizar_parametros, text="Probabilidad de venta a una señora")
    probabilidad_venta_a_sra_entry = tk.Entry(menu_actualizar_parametros)
    # probabilidad_venta_a_sra_label.grid(row=2, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # probabilidad_venta_a_sra_entry.grid(row=2, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    probabilidad_venta_a_sr_label = tk.Label(menu_actualizar_parametros, text="Probabilidad de venta a un señor")
    probabilidad_venta_a_sr_entry = tk.Entry(menu_actualizar_parametros)
    # probabilidad_venta_a_sr_label.grid(row=3, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # probabilidad_venta_a_sr_entry.grid(row=3, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    utilidad_por_suscripcion_label = tk.Label(menu_actualizar_parametros, text="Utilidad por suscripción")
    utilidad_por_suscripcion_entry = tk.Entry(menu_actualizar_parametros)
    # utilidad_por_suscripcion_label.grid(row=4, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # utilidad_por_suscripcion_entry.grid(row=4, column=1, sticky='w', padx=(5, 10), pady=(5, 5))




    # ------------ Distribuciones de Suscrpciones

    distribucion_suscripciones_sra_label = tk.Label(menu_actualizar_parametros, text="Distribución de suscripciones para señoras")
    distribucion_suscripciones_sra_frame = tk.Frame(menu_actualizar_parametros)
    # distribucion_suscripciones_sra_label.grid(row=5, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # distribucion_suscripciones_sra_frame.grid(row=5, column=1, sticky='w', padx=(5, 10), pady=(5, 5))  
    
    
    tk.Label(distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry1 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry2 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry3 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)

    distribucion_suscripciones_sr_label = tk.Label(menu_actualizar_parametros, text="Distribución de suscripciones para señores")
    distribucion_suscripciones_sr_frame = tk.Frame(menu_actualizar_parametros)
    # distribucion_suscripciones_sr_label.grid(row=6, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
    # distribucion_suscripciones_sr_frame.grid(row=6, column=1, sticky='w', padx=(5, 10), pady=(5, 5))
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

    # Botones
    actualizar_button = tk.Button(menu_actualizar_parametros, text="Actualizar", command=actualizar_parametros, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    volver_button = tk.Button(menu_actualizar_parametros, text="Regresar", command=abrir_menu_principal, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')




    # --- Juntamos lo widgets menos el boton para gridear mas comodo
    widgets_menu_actualizar = [
        (probabilidad_puerta_abierta_label, probabilidad_puerta_abierta_entry),
        (probabilidad_abre_sra_label, probabilidad_abre_sra_entry),
        (probabilidad_venta_a_sra_label, probabilidad_venta_a_sra_entry),
        (probabilidad_venta_a_sr_label, probabilidad_venta_a_sr_entry),
        (utilidad_por_suscripcion_label, utilidad_por_suscripcion_entry),
        (distribucion_suscripciones_sra_label, distribucion_suscripciones_sra_frame),
        (distribucion_suscripciones_sr_label, distribucion_suscripciones_sr_frame),
        (actualizar_button, volver_button)
    ]

    for i, (label, entry_frame) in enumerate(widgets_menu_actualizar):
        label.grid(row=i, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
        entry_frame.grid(row=i, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    # FALTA asignarle una funcion que actualice los parametros
    # actualizar_button.grid(row=7, column=0, columnspan=2, pady=(10, 5))

    # volver_button.grid(row=7, column=0, columnspan=2, pady=(10, 5))
    # actualizar_button.bind("<Enter>", lambda e: actualizar_button.config(bg="#87ceeb"))
    # actualizar_button.bind("<Leave>", lambda e: actualizar_button.config(bg="#add8e6"))



def abrir_menu_principal():

    

    # Se validan las configuraciones iniciales aca





    # Se cierra la configuracion Inicial 
    volver_al_menu()
    

    # Se define el menu principal
    global menu_principal
    menu_principal = tk.Toplevel(menu_config_inicial)
    menu_principal.configure(bg='white')
    menu_principal.protocol("WM_DELETE_WINDOW", on_closing)
    menu_principal.geometry("300x200")
    menu_principal.resizable(False, False)

    generar_simulacion_button = tk.Button(menu_principal, text="Generar simulación", bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    generar_simulacion_button.pack(pady=(10, 5))
    generar_simulacion_button.bind("<Enter>", lambda e: generar_simulacion_button.config(bg="#87ceeb"))
    generar_simulacion_button.bind("<Leave>", lambda e: generar_simulacion_button.config(bg="#add8e6"))

    generar_nuevos_numeros_aleatorios_button = tk.Button(menu_principal, text="Generar nuevos números aleatorios", command=pedir_n_visitas, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    generar_nuevos_numeros_aleatorios_button.pack(pady=(10, 5))
    generar_nuevos_numeros_aleatorios_button.bind("<Enter>", lambda e: generar_nuevos_numeros_aleatorios_button.config(bg="#87ceeb"))
    generar_nuevos_numeros_aleatorios_button.bind("<Leave>", lambda e: generar_nuevos_numeros_aleatorios_button.config(bg="#add8e6"))

    actualizar_parametros_button = tk.Button(menu_principal, text="Actualizar parámetros", command=abrir_menu_actualizar_parametros, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    actualizar_parametros_button.pack(pady=(10, 5))
    actualizar_parametros_button.bind("<Enter>", lambda e: actualizar_parametros_button.config(bg="#87ceeb"))
    actualizar_parametros_button.bind("<Leave>", lambda e: actualizar_parametros_button.config(bg="#add8e6"))








def abrir_menu_config_incial():

    # Definicion de la primer ventana (Configuracion Inicial)
    global menu_config_inicial
    menu_config_inicial = tk.Tk()
    menu_config_inicial.configure(bg='white')
    menu_config_inicial.protocol("WM_DELETE_WINDOW", on_closing)
    menu_config_inicial.resizable(False, False)




    # Widgets de la primer ventana (Configuracion Inicial)

    n_visitas_label = tk.Label(menu_config_inicial, text="Número de visitas a simular", bg='white')
    n_visitas_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')

    probabilidad_puerta_abierta_label = tk.Label(menu_config_inicial, text="Probabilidad de que la puerta se abra", bg='white') # 0.7
    probabilidad_puerta_abierta_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')

    probabilidad_abre_sra_label = tk.Label(menu_config_inicial, text="Probabilidad de que abra una señora", bg='white')  # 0.8
    probabilidad_abre_sra_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')

    probabilidad_venta_a_sra_label = tk.Label(menu_config_inicial, text="Probabilidad de venta a un señora", bg='white') # 0.15
    probabilidad_venta_a_sra_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')

    probabilidad_venta_a_sr_label = tk.Label(menu_config_inicial, text="Probabilidad de venta a un señor", bg='white') # 0.25
    probabilidad_venta_a_sr_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')


    utilidad_por_suscripcion_label = tk.Label(menu_config_inicial, text="Utilidad por suscripción", bg='white')
    utilidad_por_suscripcion_entry = tk.Entry(menu_config_inicial, bg='#f0f0f0')

    distribucion_suscripciones_sra_label = tk.Label(menu_config_inicial, text="Distribución de suscripciones para señoras")
    distribucion_suscripciones_sra_frame = tk.Frame(menu_config_inicial)
    tk.Label(distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry1 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry2 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
    tk.Label(distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
    distribucion_suscripciones_sra_entry3 = tk.Entry(distribucion_suscripciones_sra_frame, width=5)
    distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)

    distribucion_suscripciones_sr_label = tk.Label(menu_config_inicial, text="Distribución de suscripciones para señores")
    distribucion_suscripciones_sr_frame = tk.Frame(menu_config_inicial)
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

    listo_button = tk.Button(menu_config_inicial, text="Confirmar", command=abrir_menu_principal, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    # listo_button.grid(row=16, column=0, columnspan=2, pady=(10, 5))
    listo_button.bind("<Enter>", lambda e: listo_button.config(bg="#87ceeb"))
    listo_button.bind("<Leave>", lambda e: listo_button.config(bg="#add8e6"))

    cancelar_button = tk.Button(menu_config_inicial, text="Cancelar", command=on_closing, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
    # cancelar_button.grid(row=17, column=0, columnspan=2, pady=(10, 5))
    cancelar_button.bind("<Enter>", lambda e: cancelar_button.config(bg="#87ceeb"))
    cancelar_button.bind("<Leave>", lambda e: cancelar_button.config(bg="#add8e6"))

    widgets_config_inicial = [
        (n_visitas_label, n_visitas_entry),
        (probabilidad_puerta_abierta_label, probabilidad_puerta_abierta_entry),
        (probabilidad_abre_sra_label, probabilidad_abre_sra_entry),
        (probabilidad_venta_a_sra_label, probabilidad_venta_a_sra_entry),
        (probabilidad_venta_a_sr_label, probabilidad_venta_a_sr_entry),
        (utilidad_por_suscripcion_label, utilidad_por_suscripcion_entry),
        (distribucion_suscripciones_sra_label, distribucion_suscripciones_sra_frame),
        (distribucion_suscripciones_sr_label, distribucion_suscripciones_sr_frame),
        (listo_button, cancelar_button),
    ]

    for i, (label, entry) in enumerate(widgets_config_inicial):
        label.grid(row=i, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
        entry.grid(row=i, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

    menu_config_inicial.mainloop()



abrir_menu_config_incial()