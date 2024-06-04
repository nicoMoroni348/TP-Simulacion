import flet as ft

def main(page: ft.Page):
    page.title = "Simulación: Inscripción a Exámenes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_100
    page.scroll = ft.ScrollMode.ADAPTIVE


    def close_ventana_error(e):
            ventana_error.open = False
            page.update()


    def mostrar_resultados(porcentaje, promedio):
        resultado1.value = f"{resultado1.value} {porcentaje:.2f}%"
        resultado2.value = f"{resultado2.value} {promedio}"
        page.update()


    def simular(e):
        
        # Validar parámetros
        
    
        if not (True):
            page.dialog = ventana_error
            ventana_error.open = True
            page.update()
            return

        # Convertir probabilidades a distribuciones
        

        # Simular visitas
        """
        v_e, u_f = simulacion(
            
        )
        """

        # Mostrar resultados
        page.add(resultado1,
            resultado2)

        mostrar_resultados(1, 2)

        # Mostrar vector de estados
        """
        try:
            get_table(vector_estado=v_e, ultima_fila=u_f, auto_open=True)
        except PermissionError:
            page.dialog = ventana_error
            ventana_error.content = ft.Text("Debe cerrar la ventana de excel para realizar nuevamente la simulación.")
            ventana_error.open = True
            page.update()
        """

    # COMPONENTES DE LA INTERFAZ
    
    # Resultados
    resultado1 = ft.Text("Porcentaje de alumnos que se van para regresar más tarde:", color="#45818e", size=25, weight=ft.FontWeight.BOLD)
    resultado2 = ft.Text("Tiempo promedio de espera de los alumnos:", color="#45818e", size=25, weight=ft.FontWeight.BOLD)

    # Ventanas de error
    ventana_error = ft.AlertDialog(
        title = ft.Text("Error"),
        content = ft.Text("Por favor, ingrese valores válidos para los parámetros."),
        actions=[
            ft.TextButton("Ok", on_click=close_ventana_error),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Input parámetros problema
    demora_inscripcion_min_input = ft.TextField(value=5, width=80, color=ft.colors.BLACK)
    demora_inscripcion_max_input = ft.TextField(value=8, width=80, color=ft.colors.BLACK)
    demora_inscripcion_input = [ft.Text("Demora de Inscripción:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                ft.Text("Entre", color=ft.colors.BLACK), 
                                demora_inscripcion_min_input,
                                ft.Text("y", color=ft.colors.BLACK), 
                                demora_inscripcion_max_input,
                                ft.Text("minutos", color=ft.colors.BLACK)]

    demora_mantenimiento_min_input = ft.TextField(value=3, width=80, color=ft.colors.BLACK)
    demora_mantenimiento_max_input = ft.TextField(value=10, width=80, color=ft.colors.BLACK)
    demora_mantenimiento_input = [ft.Text("Demora de Mantenimiento:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  ft.Text("Entre", color=ft.colors.BLACK), 
                                  demora_mantenimiento_min_input,
                                  ft.Text("y", color=ft.colors.BLACK), 
                                  demora_mantenimiento_max_input,
                                  ft.Text("minutos", color=ft.colors.BLACK)]
    
    media_llegadas_alumnos_input = ft.TextField(value=2, width=80, color=ft.colors.BLACK)
    llegadas_alumnos_input = [ft.Text("Tiempo entre Llegadas de Alumnos:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  ft.Text("Media:", color=ft.colors.BLACK), 
                                  media_llegadas_alumnos_input]
    
    media_regreso_mantenimiento_input = ft.TextField(value=1, width=80, color=ft.colors.BLACK)
    desviacion_regreso_mantenimiento_input = ft.TextField(value=3, width=80, color=ft.colors.BLACK)
    regreso_mantenimiento_input = [ft.Text("Tiempo entre Mantenimientos:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  media_regreso_mantenimiento_input,
                                  ft.Text("hora ±", color=ft.colors.BLACK), 
                                  desviacion_regreso_mantenimiento_input,
                                  ft.Text("minutos", color=ft.colors.BLACK)]

    # Input parámetros simulación
    tiempo_input = ft.TextField(width=80, color=ft.colors.BLACK)
    unidad_de_medida_input = ft.Dropdown(
        width=80,
        options=[
            ft.dropdown.Option("Horas"),
            ft.dropdown.Option("Minutos")
        ],
        color=ft.colors.GREY_500
    )
    tiempo_simulacion_input = [ft.Text("Tiempo a simular (x):", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                            tiempo_input,
                            unidad_de_medida_input]

    i_input = ft.TextField(label="i =", label_style=ft.TextStyle(color=ft.colors.GREY_500), width=80, color=ft.colors.BLACK)
    j_input = ft.TextField(label="j =", label_style=ft.TextStyle(color=ft.colors.GREY_500), width=80, color=ft.colors.BLACK)
    i_j_input = [ft.Text("Mostrar", color=ft.colors.BLACK),
                 i_input,
                 ft.Text("iteraciones a partir de la hora", color=ft.colors.BLACK),
                 j_input]

    # Botones
    simular_button = ft.ElevatedButton(text="Simular", on_click=simular)

    # Disposición de componentes
    page.add(
        ft.Row(controls=demora_inscripcion_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=demora_mantenimiento_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=llegadas_alumnos_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=regreso_mantenimiento_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=50),
        ft.Row(controls=tiempo_simulacion_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=i_j_input, alignment=ft.MainAxisAlignment.CENTER),
        simular_button,
    )

# Ejecutar la aplicación
ft.app(target=main)