import tkinter as tk
from tkinter import simpledialog, messagebox
from simulacion_visita import simulacion_visitas
from simulacion_visita_new import simulacion_visitas as simulacion_new
from support import get_table, generar_numeros_aleatorios, validar_parametros,  \
                validar_distribuciones, probabilidad_a_distribucion, validar_i_j,\
                validar_n
from tkinter import ttk

class SimulationApp:
    def __init__(self):
        self.menu_principal = None
        self.menu_config_inicial = None
        self.menu_actualizar_parametros = None

        # Parameters Attributes
        self.n_visitas = 100
        self.crear_nuevos_rnd = True
        self.i = 1
        self.j = 1
        self.probabilidad_puerta_abierta = [0.7, 0.3]
        self.probabilidad_genero = [0.8, 0.2]
        self.probabilidad_venta_a_sra = [0.15, 0.85]
        self.probabilidad_venta_a_sr = [0.25, 0.75]
        self.distribucion_suscripciones_sra = [0.6, 0.3, 0.1]
        self.distribucion_suscripciones_sr = [0.1, 0.4, 0.3, 0.2]
        self.utilidad_por_suscripcion = 200.0


    def volver_al_menu(self):
        if self.menu_actualizar_parametros is not None:
            self.menu_actualizar_parametros.withdraw()

        self.menu_config_inicial.withdraw()

    def on_closing(self):
        for e in (self.menu_actualizar_parametros, self.menu_principal, self.menu_config_inicial):
            if e is not None:
                e.destroy()



    # Convert `comenzar_simulacion` into a method
    def comenzar_simulacion(self):

        # Validar los entries
        i_y_j = validar_i_j(self.i_entry.get(), self.j_entry.get(), n=self.n_visitas)
        
        if not i_y_j:
            self.mostrar_ventana_error()
            return
        
        self.i = i_y_j[0]
        self.j = i_y_j[1]

        # self.i = int(self.i_entry.get())
        # self.j = int(self.j_entry.get())

        # print(self.n_visitas)
        
        # Llamar a la función simular_visita
        vectores_numeros_aleatorios = generar_numeros_aleatorios(n=self.n_visitas, generar_nuevos=self.crear_nuevos_rnd)
        self.crear_nuevos_rnd = False

        # print(type(vectores_numeros_aleatorios), vectores_numeros_aleatorios)
        print(type(self.n_visitas), self.n_visitas)
        print(type(self.utilidad_por_suscripcion), self.utilidad_por_suscripcion)
        print(type(self.probabilidad_puerta_abierta), self.probabilidad_puerta_abierta)
        print(type(self.probabilidad_genero), self.probabilidad_genero)
        print(type(self.probabilidad_venta_a_sra), self.probabilidad_venta_a_sra)
        print(type(self.probabilidad_venta_a_sr), self.probabilidad_venta_a_sr)
        print(type(self.distribucion_suscripciones_sra), self.distribucion_suscripciones_sra)
        print(type(self.distribucion_suscripciones_sr), self.distribucion_suscripciones_sr)


        
        # v_e = simulacion_visitas(vectores_numeros_aleatorios, self.n_visitas, 
        #                     self.utilidad_por_suscripcion, self.probabilidad_puerta_abierta, 
        #                     self.probabilidad_genero, self.probabilidad_venta_a_sra,
        #                     self.probabilidad_venta_a_sr, self.distribucion_suscripciones_sra, 
        #                     self.distribucion_suscripciones_sr)

        v_e = simulacion_new(self.n_visitas, self.utilidad_por_suscripcion, self.probabilidad_puerta_abierta, 
                            self.probabilidad_genero, self.probabilidad_venta_a_sra,
                            self.probabilidad_venta_a_sr, self.distribucion_suscripciones_sra, 
                            self.distribucion_suscripciones_sr)
        



        # y Generar la tabla get_table
        try:
            get_table(vector_estado=v_e, i=self.i, j=self.j, auto_open=True)
        except PermissionError:
            self.mostrar_ventana_error("Debe cerrar la ventana de excel para realizar nuevamente la simulacion")
        




    def pedir_n_visitas(self):
        n_visitas_input_value = simpledialog.askstring("Nuevo número de simulación", "Ingrese n:")

        if n_visitas_input_value is None:
            return


        # VALIDAR N
        n = validar_n(n_visitas_input_value)
        if not n:
            self.mostrar_ventana_error()
            return
        

        self.n_visitas = n
        self.crear_nuevos_rnd = True

        # actualizar label del menu principal
        self.n_label.config(text=f"n actual: {str(self.n_visitas)}")

        self.mostrar_ventana_actualizacion_nuevos_rnd()


    # Convert `actualizar_parametros` into a method
    def actualizar_parametros(self):




        params = validar_parametros(
            puerta=self.probabilidad_puerta_abierta_entry.get(),
            genero=self.probabilidad_abre_sra_entry.get(),
            venta_sra=self.probabilidad_venta_a_sra_entry.get(),
            venta_sr=self.probabilidad_venta_a_sr_entry.get(),
            utilidad=self.utilidad_por_suscripcion_entry.get()
        )

        distribs = validar_distribuciones(
            dist_sra=(
                self.distribucion_suscripciones_sra_entry1,
                self.distribucion_suscripciones_sra_entry2,
                self.distribucion_suscripciones_sra_entry3
            ),
            dist_sr=(
                self.distribucion_suscripciones_sr_entry1,
                self.distribucion_suscripciones_sr_entry2,
                self.distribucion_suscripciones_sr_entry3,
                self.distribucion_suscripciones_sr_entry4
            )
        )


        if not params or not distribs:
            self.mostrar_ventana_error()
            return

            # Volver a la ventana que se estaba antes (antes de apretar el boton)

        
        self.probabilidad_puerta_abierta, self.probabilidad_genero,\
        self.probabilidad_venta_a_sra, self.probabilidad_venta_a_sr = [probabilidad_a_distribucion(p) for p in params[:-1]]
        self.utilidad_por_suscripcion = params[-1]

        self.distribucion_suscripciones_sra, self.distribucion_suscripciones_sr = distribs






        # --------------- PRE VALIDACION
        # self.probabilidad_puerta_abierta = probabilidad_a_distribucion(float(self.probabilidad_puerta_abierta_entry.get()))
        # self.probabilidad_genero = probabilidad_a_distribucion(float(self.probabilidad_abre_sra_entry.get()))
        # self.probabilidad_venta_a_sra = probabilidad_a_distribucion(float(self.probabilidad_venta_a_sra_entry.get()))
        # self.probabilidad_venta_a_sr = probabilidad_a_distribucion(float(self.probabilidad_venta_a_sr_entry.get()))

        # self.distribucion_suscripciones_sra = [float(self.distribucion_suscripciones_sra_entry1.get()), 
        #                                 float(self.distribucion_suscripciones_sra_entry2.get()), 
        #                                 float(self.distribucion_suscripciones_sra_entry3.get())]

        # self.distribucion_suscripciones_sr = [float(self.distribucion_suscripciones_sr_entry1.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry2.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry3.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry4.get())]

        # self.utilidad_por_suscripcion = float(self.utilidad_por_suscripcion_entry.get())










        # ACA SE DEBERIA ABRIR la ventanita que te avise que se actualizaros los parametros

        self.mostrar_ventana_actualizacion()

        self.abrir_menu_principal()




    def mostrar_ventana_actualizacion(self):
        response = messagebox.showinfo("Actualización de Parámetros", "¡Se han actualizado todos los Parámetros")
        if response:
            print("Los datos se han actualizado correctamente.")


    


    def mostrar_ventana_actualizacion_nuevos_rnd(self):
        # response = messagebox.showinfo("Actualización de Núeros Aleatorios", "¡Se han generado los nuevos números aleatorios")
        response = messagebox.showinfo("Actualización de N", "¡Se ha actualizado en numero de visitas!")
        if response:
            print("Los datos se han actualizado correctamente.")


    def mostrar_ventana_error(self, mensaje="¡Parámetros ingresados no válidos"):
        response = messagebox.showerror("Error", mensaje)
        # if response:
        #     print("Los datos se han actualizado correctamente.")




    def abrir_menu_actualizar_parametros(self):
        
        # Se cierra el menu principal
        self.menu_principal.withdraw()

        # Se define el menu actualizar parametros
        self.menu_actualizar_parametros = tk.Toplevel(self.menu_principal)
        self.menu_actualizar_parametros.configure(bg='white')
        self.menu_actualizar_parametros.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu_actualizar_parametros.resizable(False, False)
        self.menu_actualizar_parametros.iconbitmap('goat.ico')


        # ---------- Labels y Entries
        self.probabilidad_puerta_abierta_label = tk.Label(self.menu_actualizar_parametros, text="Probabilidad de que la puerta se abra", bg='white') # 0.7
        self.probabilidad_puerta_abierta_entry = tk.Entry(self.menu_actualizar_parametros, bg='#f0f0f0')
        self.probabilidad_puerta_abierta_entry.insert(0, str(self.probabilidad_puerta_abierta[0]))

        self.probabilidad_abre_sra_label = tk.Label(self.menu_actualizar_parametros, text="Probabilidad de que abra una señora", bg='white')  # 0.8
        self.probabilidad_abre_sra_entry = tk.Entry(self.menu_actualizar_parametros, bg='#f0f0f0')
        self.probabilidad_abre_sra_entry.insert(0, str(self.probabilidad_genero[0]))

        self.probabilidad_venta_a_sra_label = tk.Label(self.menu_actualizar_parametros, text="Probabilidad de venta a un señora", bg='white') # 0.15
        self.probabilidad_venta_a_sra_entry = tk.Entry(self.menu_actualizar_parametros, bg='#f0f0f0')
        self.probabilidad_venta_a_sra_entry.insert(0, str(self.probabilidad_venta_a_sra[0]))

        self.probabilidad_venta_a_sr_label = tk.Label(self.menu_actualizar_parametros, text="Probabilidad de venta a un señor", bg='white') # 0.25
        self.probabilidad_venta_a_sr_entry = tk.Entry(self.menu_actualizar_parametros, bg='#f0f0f0')
        self.probabilidad_venta_a_sr_entry.insert(0, str(self.probabilidad_venta_a_sr[0]))

        self.utilidad_por_suscripcion_label = tk.Label(self.menu_actualizar_parametros, text="Utilidad por suscripción", bg='white')
        self.utilidad_por_suscripcion_entry = tk.Entry(self.menu_actualizar_parametros, bg='#f0f0f0')
        self.utilidad_por_suscripcion_entry.insert(0, str(self.utilidad_por_suscripcion))

        self.distribucion_suscripciones_sra_label = tk.Label(self.menu_actualizar_parametros, text="Distribución de suscripciones para señoras")
        self.distribucion_suscripciones_sra_frame = tk.Frame(self.menu_actualizar_parametros)
        tk.Label(self.distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry1 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry1.insert(0, str(self.distribucion_suscripciones_sra[0]))

        tk.Label(self.distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry2 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry2.insert(0, str(self.distribucion_suscripciones_sra[1]))
        
        tk.Label(self.distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry3 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry3.insert(0, str(self.distribucion_suscripciones_sra[2]))

        self.distribucion_suscripciones_sr_label = tk.Label(self.menu_actualizar_parametros, text="Distribución de suscripciones para señores")
        self.distribucion_suscripciones_sr_frame = tk.Frame(self.menu_actualizar_parametros)
        
        tk.Label(self.distribucion_suscripciones_sr_frame, text="1").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry1 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry1.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry1.insert(0, str(self.distribucion_suscripciones_sr[0]))
        
        tk.Label(self.distribucion_suscripciones_sr_frame, text="2").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry2 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry2.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry2.insert(0, str(self.distribucion_suscripciones_sr[1]))

        tk.Label(self.distribucion_suscripciones_sr_frame, text="3").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry3 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry3.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry3.insert(0, str(self.distribucion_suscripciones_sr[2]))

        tk.Label(self.distribucion_suscripciones_sr_frame, text="4").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry4 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry4.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry4.insert(0, str(self.distribucion_suscripciones_sr[3]))

        # Botones

        # self.listo_button = tk.Button(self.menu_config_inicial, text="Confirmar",fg="white", command=self.inicializar_parametros, bg='green', activebackground='darkgreen', bd=1, relief='raised')
        # self.listo_button.bind("<Enter>", lambda e: self.listo_button.config(bg="darkgreen"))
        # self.listo_button.bind("<Leave>", lambda e: self.listo_button.config(bg="green"))

        # self.cancelar_button = tk.Button(self.menu_config_inicial, text="Cancelar",fg="white", command=self.on_closing, bg='#C62020', activebackground='darkred', bd=1, relief='raised')
        # self.cancelar_button.bind("<Enter>", lambda e: self.cancelar_button.config(bg="darkred"))
        # self.cancelar_button.bind("<Leave>", lambda e: self.cancelar_button.config(bg="#C62020"))


        self.actualizar_button = tk.Button(self.menu_actualizar_parametros, text="Actualizar", command=self.actualizar_parametros,
                                    bg='#add8e6', activebackground='#A6F775', bd=0, relief='raised', overrelief='groove', highlightbackground='black')
        self.actualizar_button.bind("<Enter>", lambda e: self.cancelar_button.config(bg="#A6F775"))
        self.actualizar_button.bind("<Leave>", lambda e: self.cancelar_button.config(bg="#add8e6"))
        

        self.volver_button = tk.Button(self.menu_actualizar_parametros, text="Regresar", command=self.abrir_menu_principal, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='raised', overrelief='groove', highlightbackground='black')
        self.volver_button.bind("<Enter>", lambda e: self.cancelar_button.config(bg="darkred"))
        self.volver_button.bind("<Leave>", lambda e: self.cancelar_button.config(bg="darkred"))



        # --- Juntamos lo widgets menos el boton para gridear mas comodo
        widgets_menu_actualizar = [
            (self.probabilidad_puerta_abierta_label, self.probabilidad_puerta_abierta_entry),
            (self.probabilidad_abre_sra_label, self.probabilidad_abre_sra_entry),
            (self.probabilidad_venta_a_sra_label, self.probabilidad_venta_a_sra_entry),
            (self.probabilidad_venta_a_sr_label, self.probabilidad_venta_a_sr_entry),
            (self.utilidad_por_suscripcion_label, self.utilidad_por_suscripcion_entry),
            (self.distribucion_suscripciones_sra_label, self.distribucion_suscripciones_sra_frame),
            (self.distribucion_suscripciones_sr_label, self.distribucion_suscripciones_sr_frame),
            (self.actualizar_button, self.volver_button)
        ]

        for i, (label, entry_frame) in enumerate(widgets_menu_actualizar):
            label.grid(row=i, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
            entry_frame.grid(row=i, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

        # FALTA asignarle una funcion que actualice los parametros
        # actualizar_button.grid(row=7, column=0, columnspan=2, pady=(10, 5))




    def inicializar_parametros(self):

        n = validar_n(self.n_visitas_entry.get())

        params = validar_parametros(
            puerta=self.probabilidad_puerta_abierta_entry.get(),
            genero=self.probabilidad_abre_sra_entry.get(),
            venta_sra=self.probabilidad_venta_a_sra_entry.get(),
            venta_sr=self.probabilidad_venta_a_sr_entry.get(),
            utilidad=self.utilidad_por_suscripcion_entry.get()
        )

        distribs = validar_distribuciones(
            dist_sra=(
                self.distribucion_suscripciones_sra_entry1,
                self.distribucion_suscripciones_sra_entry2,
                self.distribucion_suscripciones_sra_entry3
            ),
            dist_sr=(
                self.distribucion_suscripciones_sr_entry1,
                self.distribucion_suscripciones_sr_entry2,
                self.distribucion_suscripciones_sr_entry3,
                self.distribucion_suscripciones_sr_entry4
            )
        )


        if not params or not distribs or not n:
            self.mostrar_ventana_error()
            return

            # Volver a la ventana que se estaba antes (antes de apretar el boton)

        
        self.n_visitas = n
        self.probabilidad_puerta_abierta, self.probabilidad_genero,\
        self.probabilidad_venta_a_sra, self.probabilidad_venta_a_sr = [probabilidad_a_distribucion(p) for p in params[:-1]]
        self.utilidad_por_suscripcion = params[-1]
        # print("Nuevos parametros")
        print(self.probabilidad_puerta_abierta)

        self.distribucion_suscripciones_sra, self.distribucion_suscripciones_sr = distribs
            



        # ACA HAY QUE CONECTAR CON LAS VALIDACIONES (y sacar los float)


        # ---------------------- Ex Validacion
        # self.n_visitas = int(self.n_visitas_entry.get())
        # self.probabilidad_puerta_abierta = probabilidad_a_distribucion(float(self.probabilidad_puerta_abierta_entry.get()))
        # self.probabilidad_genero = probabilidad_a_distribucion(float(self.probabilidad_abre_sra_entry.get()))
        # self.probabilidad_venta_a_sra = probabilidad_a_distribucion(float(self.probabilidad_venta_a_sra_entry.get()))
        # self.probabilidad_venta_a_sr = probabilidad_a_distribucion(float(self.probabilidad_venta_a_sr_entry.get()))

        # self.distribucion_suscripciones_sra = [float(self.distribucion_suscripciones_sra_entry1.get()), 
        #                                 float(self.distribucion_suscripciones_sra_entry2.get()), 
        #                                 float(self.distribucion_suscripciones_sra_entry3.get())]

        # self.distribucion_suscripciones_sr = [float(self.distribucion_suscripciones_sr_entry1.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry2.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry3.get()), 
        #                                 float(self.distribucion_suscripciones_sr_entry4.get())]

        # self.utilidad_por_suscripcion = float(self.utilidad_por_suscripcion_entry.get())



        # PASAR AL MENU PRINCIPAL
        self.abrir_menu_principal()
        



    def abrir_menu_principal(self):
        



        # Se cierra la configuracion Inicial 
        self.volver_al_menu()
        

        # Se define el menu principal

        self.menu_principal = tk.Toplevel(self.menu_config_inicial)
        self.menu_principal.configure(bg='white')
        self.menu_principal.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu_principal.geometry("250x200")
        self.menu_principal.resizable(False, False)
        self.menu_principal.iconbitmap('goat.ico')
    

        # Actualización de i & j
        self.i_label = tk.Label(self.menu_principal, text="i (Cantidad de iteraciones)", bg='white')
        self.i_entry = tk.Entry(self.menu_principal, bg='#f0f0f0')
        self.i_entry.insert(0, str(self.i))
        self.j_label = tk.Label(self.menu_principal, text="j (Desde que iteracion)", bg='white')
        self.j_entry = tk.Entry(self.menu_principal, bg='#f0f0f0')
        self.j_entry.insert(0, str(self.j))
        
        self.i_label.grid(row=0, column=0)
        self.i_entry.grid(row=0, column=1)

        
        self.j_label.grid(row=1, column=0)
        self.j_entry.grid(row=1, column=1)

        # mostrar n

        self.n_label = tk.Label(self.menu_principal, text=f"n actual: {str(self.n_visitas)}", bg='white')
        self.n_label.grid(row= 2, pady=(10, 5), columnspan=3)

        # Menu principal

        self.generar_simulacion_button = tk.Button(self.menu_principal, text="Generar simulación", command=self.comenzar_simulacion, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
        self.generar_simulacion_button.grid(row=3, pady=(10, 5), columnspan=3)
        self.generar_simulacion_button.bind("<Enter>", lambda e: self.generar_simulacion_button.config(bg="#87ceeb"))
        self.generar_simulacion_button.bind("<Leave>", lambda e: self.generar_simulacion_button.config(bg="#add8e6"))

        self.generar_nuevos_numeros_aleatorios_button = tk.Button(self.menu_principal, text="Actualizar Cantidad de visitas", command=self.pedir_n_visitas, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
        self.generar_nuevos_numeros_aleatorios_button.grid(row= 4, pady=(10, 5), columnspan=3)
        self.generar_nuevos_numeros_aleatorios_button.bind("<Enter>", lambda e: self.generar_nuevos_numeros_aleatorios_button.config(bg="#87ceeb"))
        self.generar_nuevos_numeros_aleatorios_button.bind("<Leave>", lambda e: self.generar_nuevos_numeros_aleatorios_button.config(bg="#add8e6"))

        self.actualizar_parametros_button = tk.Button(self.menu_principal, text="Actualizar parámetros", command=self.abrir_menu_actualizar_parametros, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
        self.actualizar_parametros_button.grid(row=5, pady=(10, 5), columnspan=3)
        self.actualizar_parametros_button.bind("<Enter>", lambda e: self.actualizar_parametros_button.config(bg="#87ceeb"))
        self.actualizar_parametros_button.bind("<Leave>", lambda e: self.actualizar_parametros_button.config(bg="#add8e6"))





    def abrir_menu_config_incial(self):
        self.menu_config_inicial = tk.Tk()
        self.menu_config_inicial.configure(bg='white')
        self.menu_config_inicial.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu_config_inicial.resizable(False, False)
        self.menu_config_inicial.iconbitmap('goat.ico')


        # Widgets de la primer ventana (Configuracion Inicial)

        self.n_visitas_label = tk.Label(self.menu_config_inicial, text="Número de visitas a simular", bg='white')
        self.n_visitas_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.n_visitas_entry.insert(0, str(self.n_visitas))

        self.probabilidad_puerta_abierta_label = tk.Label(self.menu_config_inicial, text="Probabilidad de que la puerta se abra", bg='white') # 0.7
        self.probabilidad_puerta_abierta_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.probabilidad_puerta_abierta_entry.insert(0, str(self.probabilidad_puerta_abierta[0]))

        self.probabilidad_abre_sra_label = tk.Label(self.menu_config_inicial, text="Probabilidad de que abra una señora", bg='white')  # 0.8
        self.probabilidad_abre_sra_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.probabilidad_abre_sra_entry.insert(0, str(self.probabilidad_genero[0]))

        self.probabilidad_venta_a_sra_label = tk.Label(self.menu_config_inicial, text="Probabilidad de venta a un señora", bg='white') # 0.15
        self.probabilidad_venta_a_sra_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.probabilidad_venta_a_sra_entry.insert(0, str(self.probabilidad_venta_a_sra[0]))

        self.probabilidad_venta_a_sr_label = tk.Label(self.menu_config_inicial, text="Probabilidad de venta a un señor", bg='white') # 0.25
        self.probabilidad_venta_a_sr_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.probabilidad_venta_a_sr_entry.insert(0, str(self.probabilidad_venta_a_sr[0]))

        self.utilidad_por_suscripcion_label = tk.Label(self.menu_config_inicial, text="Utilidad por suscripción", bg='white')
        self.utilidad_por_suscripcion_entry = tk.Entry(self.menu_config_inicial, bg='#f0f0f0')
        self.utilidad_por_suscripcion_entry.insert(0, str(self.utilidad_por_suscripcion))

        self.distribucion_suscripciones_sra_label = tk.Label(self.menu_config_inicial, text="Distribución de suscripciones para señoras")
        self.distribucion_suscripciones_sra_frame = tk.Frame(self.menu_config_inicial)
        tk.Label(self.distribucion_suscripciones_sra_frame, text="1").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry1 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry1.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry1.insert(0, str(self.distribucion_suscripciones_sra[0]))

        tk.Label(self.distribucion_suscripciones_sra_frame, text="2").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry2 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry2.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry2.insert(0, str(self.distribucion_suscripciones_sra[1]))
        
        tk.Label(self.distribucion_suscripciones_sra_frame, text="3").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry3 = tk.Entry(self.distribucion_suscripciones_sra_frame, width=5)
        self.distribucion_suscripciones_sra_entry3.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sra_entry3.insert(0, str(self.distribucion_suscripciones_sra[2]))

        self.distribucion_suscripciones_sr_label = tk.Label(self.menu_config_inicial, text="Distribución de suscripciones para señores")
        self.distribucion_suscripciones_sr_frame = tk.Frame(self.menu_config_inicial)
        
        tk.Label(self.distribucion_suscripciones_sr_frame, text="1").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry1 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry1.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry1.insert(0, str(self.distribucion_suscripciones_sr[0]))
        
        tk.Label(self.distribucion_suscripciones_sr_frame, text="2").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry2 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry2.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry2.insert(0, str(self.distribucion_suscripciones_sr[1]))

        tk.Label(self.distribucion_suscripciones_sr_frame, text="3").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry3 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry3.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry3.insert(0, str(self.distribucion_suscripciones_sr[2]))

        tk.Label(self.distribucion_suscripciones_sr_frame, text="4").pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry4 = tk.Entry(self.distribucion_suscripciones_sr_frame, width=5)
        self.distribucion_suscripciones_sr_entry4.pack(side=tk.LEFT)
        self.distribucion_suscripciones_sr_entry4.insert(0, str(self.distribucion_suscripciones_sr[3]))






        
        self.listo_button = tk.Button(self.menu_config_inicial, text="Confirmar",fg="white", command=self.inicializar_parametros, bg='green', activebackground='darkgreen', bd=1, relief='raised')
        self.listo_button.bind("<Enter>", lambda e: self.listo_button.config(bg="darkgreen"))
        self.listo_button.bind("<Leave>", lambda e: self.listo_button.config(bg="green"))

        self.cancelar_button = tk.Button(self.menu_config_inicial, text="Cancelar",fg="white", command=self.on_closing, bg='#C62020', activebackground='darkred', bd=1, relief='raised')
        self.cancelar_button.bind("<Enter>", lambda e: self.cancelar_button.config(bg="darkred"))
        self.cancelar_button.bind("<Leave>", lambda e: self.cancelar_button.config(bg="#C62020"))



        # self.listo_button = tk.Button(self.menu_config_inicial, text="Confirmar", command=self.inicializar_parametros, 
        #                          bg='#90EE90', activebackground='#7CFC00', bd=0, relief='groove', overrelief='groove', highlightbackground='black',)
        
        # # self.listo_button = tk.Button(self.menu_config_inicial, text="Confirmar", command=self.inicializar_parametros, 
        # #                          bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')

        # self.listo_button.bind("<Enter>", lambda e: self.listo_button.config(bg="#7CFC00"))
        # self.listo_button.bind("<Leave>", lambda e: self.listo_button.config(bg="#90EE90"))

        # self.cancelar_button = tk.Button(self.menu_config_inicial, text="Cancelar", command=self.on_closing, bg='#add8e6', activebackground='#87ceeb', bd=0, relief='groove', overrelief='groove', highlightbackground='black')
        # self.cancelar_button.bind("<Enter>", lambda e: self.cancelar_button.config(bg="#87ceeb"))
        # self.cancelar_button.bind("<Leave>", lambda e: self.cancelar_button.config(bg="#add8e6"))

        widgets_config_inicial = [
            (self.n_visitas_label, self.n_visitas_entry),
            (self.probabilidad_puerta_abierta_label, self.probabilidad_puerta_abierta_entry),
            (self.probabilidad_abre_sra_label, self.probabilidad_abre_sra_entry),
            (self.probabilidad_venta_a_sra_label, self.probabilidad_venta_a_sra_entry),
            (self.probabilidad_venta_a_sr_label, self.probabilidad_venta_a_sr_entry),
            (self.utilidad_por_suscripcion_label, self.utilidad_por_suscripcion_entry),
            (self.distribucion_suscripciones_sra_label, self.distribucion_suscripciones_sra_frame),
            (self.distribucion_suscripciones_sr_label, self.distribucion_suscripciones_sr_frame),
            (self.listo_button, self.cancelar_button),
        ]

        for i, (label, entry) in enumerate(widgets_config_inicial):
            label.grid(row=i, column=0, sticky='e', padx=(10, 5), pady=(5, 5))
            entry.grid(row=i, column=1, sticky='w', padx=(5, 10), pady=(5, 5))

        self.menu_config_inicial.mainloop()
        


if __name__ == "__main__":
    app = SimulationApp()
    app.abrir_menu_config_incial()
