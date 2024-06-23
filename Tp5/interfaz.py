import os
import sys

import copy

import flet as ft
from validaciones import validar_parametros_simulacion, validar_demora, validar_float_positivo, validar_media_desviacion, validar_parametros_tabla

sys.path.append(os.getcwd())

from clases.vector_estado import VectorEstado
from support import generate_table

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
        res1.value = f"{porcentaje}%"
        res2.value = f"{promedio} minutos"
        page.update()


    def simular(e):
        
        # Validaciones
        parametros_validados = validar_parametros_simulacion(
            i=i_input.value,
            j=j_input.value,
            x=tiempo_input.value
        )

        demora_inscripcion_validada = validar_demora(
            demora_min=demora_inscripcion_min_input.value,
            demora_max=demora_inscripcion_max_input.value
        )

        demora_mantenimiento_validada = validar_demora(
            demora_min=demora_mantenimiento_min_input.value,
            demora_max=demora_mantenimiento_max_input.value
        )

        media_llegadas_alumnos_validada = validar_float_positivo(media_llegadas_alumnos_input.value)

        media_desviacion_regreso_mantenimiento_validadas = validar_media_desviacion(
            media=media_regreso_mantenimiento_input.value,
            desviacion=desviacion_regreso_mantenimiento_input.value
        )

        demora_traslado_validada = validar_demora(
            demora_min=demora_traslado_min_input.value,
            demora_max=demora_traslado_max_input.value
        )

        tabla_parametros_validada = validar_parametros_tabla(
             coeficiente=tabla_coef_input.value,
             termino_independiente=tabla_term_independiente_input.value
        )
        
    
        if not (parametros_validados and demora_inscripcion_validada and demora_mantenimiento_validada and media_llegadas_alumnos_validada and media_desviacion_regreso_mantenimiento_validadas and demora_traslado_validada and tabla_parametros_validada):
            page.dialog = ventana_error
            ventana_error.open = True
            page.update()
            return


        # Convertir datos validados
        i, j, x = parametros_validados
        demora_inscripcion_min, demora_inscripcion_max = demora_inscripcion_validada
        demora_mantenimiento_min, demora_mantenimiento_max = demora_mantenimiento_validada
        demora_traslado_min, demora_traslado_max = demora_traslado_validada

        media_llegadas_alumnos = media_llegadas_alumnos_validada
        media_regreso_mantenimiento, desviacion_regreso_mantenimiento = media_desviacion_regreso_mantenimiento_validadas

        tabla_coef, tabla_term_independiente = tabla_parametros_validada


        # Simular
        ve = VectorEstado()
        ve.comenzar_simulacion(hora_j=j, iteraciones_i=i, x_tiempo_simulacion=x,
                               demora_inscripcion_a=demora_inscripcion_min, demora_inscripcion_b=demora_inscripcion_max,
                               demora_mantenimiento_a=demora_mantenimiento_min, demora_mantenimiento_b=demora_mantenimiento_max,
                               media_llegada_alumnos=media_llegadas_alumnos,
                               fin_regreso_mantenimiento_media=media_regreso_mantenimiento, fin_regreso_mantenimiento_desviacion=desviacion_regreso_mantenimiento,
                               runge_a=demora_traslado_min, runge_b=demora_traslado_max,
                               coeficiente_runge_kutta=tabla_coef, termino_ind_runge_kutta=tabla_term_independiente)
        
        # print(len(ve.ultima_simulacion.equipos))

        tabla, ultima_fila, tabla_runge_kutta = ve.crear_vector_estado_tabla()

        del ve

        # Mostrar resultados
        page.add(resultado1, resultado2)

        mostrar_resultados(round(ultima_fila[24], 6), round(ultima_fila[27], 4))

        return tabla, ultima_fila, tabla_runge_kutta


    def simular_y_generar_tabla(e):
        tabla, ultima_fila, tabla_runge_kutta = simular(e)
        
        # Mostrar vector de estados
        try:
            generate_table(vector_estado=tabla, ultima_fila=ultima_fila, tabla_runge_kutta=tabla_runge_kutta , auto_open=True)
        except PermissionError:
            page.dialog = ventana_error
            ventana_error.content = ft.Text("Debe cerrar la ventana de excel para realizar nuevamente la simulación.")
            ventana_error.open = True
            page.update()
         
         
    # COMPONENTES DE LA INTERFAZ
    
    # Resultados
    res1 = ft.Text("-", color="#4581e5", size=25, weight=ft.FontWeight.BOLD)
    resultado1 = ft.Row(controls=[ft.Text("Porcentaje de alumnos que se van para regresar más tarde:", color=ft.colors.BLACK, size=25, weight=ft.FontWeight.BOLD),
                                  res1], alignment=ft.MainAxisAlignment.CENTER)
    
    res2 = ft.Text("-", color="#4581e5", size=25, weight=ft.FontWeight.BOLD)
    resultado2 = ft.Row(controls=[ft.Text("Tiempo promedio de espera de los alumnos:", color=ft.colors.BLACK, size=25, weight=ft.FontWeight.BOLD),
                                  res2], alignment=ft.MainAxisAlignment.CENTER) 


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
    demora_inscripcion_min_input = ft.TextField(value=5, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_inscripcion_max_input = ft.TextField(value=8, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_inscripcion_input = [ft.Text("Demora de Inscripción:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                ft.Text("Entre", color=ft.colors.BLACK), 
                                demora_inscripcion_min_input,
                                ft.Text("y", color=ft.colors.BLACK), 
                                demora_inscripcion_max_input,
                                ft.Text("minutos", color=ft.colors.BLACK)]

    demora_mantenimiento_min_input = ft.TextField(value=3, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_mantenimiento_max_input = ft.TextField(value=10, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_mantenimiento_input = [ft.Text("Demora de Mantenimiento:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  ft.Text("Entre", color=ft.colors.BLACK), 
                                  demora_mantenimiento_min_input,
                                  ft.Text("y", color=ft.colors.BLACK), 
                                  demora_mantenimiento_max_input,
                                  ft.Text("minutos", color=ft.colors.BLACK)]
    
    media_llegadas_alumnos_input = ft.TextField(value=2, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    llegadas_alumnos_input = [ft.Text("Tiempo entre Llegadas de Alumnos:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  ft.Text("Media =", color=ft.colors.BLACK), 
                                  media_llegadas_alumnos_input,
                                  ft.Text("minutos", color=ft.colors.BLACK)]
    
    media_regreso_mantenimiento_input = ft.TextField(value=60, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    desviacion_regreso_mantenimiento_input = ft.TextField(value=3, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    regreso_mantenimiento_input = [ft.Text("Tiempo entre Mantenimientos:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                  media_regreso_mantenimiento_input,
                                  ft.Text("±", color=ft.colors.BLACK), 
                                  desviacion_regreso_mantenimiento_input,
                                  ft.Text("minutos", color=ft.colors.BLACK)]


    # Parámetros para el Runge Kutta
    demora_traslado_min_input = ft.TextField(value=0, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_traslado_max_input = ft.TextField(value=1, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    demora_traslado_input = [ft.Text("Tiempo de traslado:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                ft.Text("Entre", color=ft.colors.BLACK), 
                                demora_traslado_min_input,
                                ft.Text("y", color=ft.colors.BLACK), 
                                demora_traslado_max_input,
                                ft.Text("horas", color=ft.colors.BLACK)]

    tabla_coef_input = ft.TextField(value=0.4, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    tabla_term_independiente_input = ft.TextField(value=5, height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)

    tabla_input = [ft.Text("Ecuación diferencial:", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                                ft.Text("Coeficiente", color=ft.colors.BLACK), 
                                tabla_coef_input,
                                ft.Text("Término independiente", color=ft.colors.BLACK), 
                                tabla_term_independiente_input,
                                ]


    
    # Input parámetros simulación
    tiempo_input = ft.TextField(height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    tiempo_simulacion_input = [ft.Text("Tiempo a simular (x):", color=ft.colors.BLACK, size=15, weight=ft.FontWeight.BOLD),
                               tiempo_input,
                               ft.Text("minutos", color=ft.colors.BLACK)]

    i_input = ft.TextField(label="i =", label_style=ft.TextStyle(color=ft.colors.GREY_500), height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    j_input = ft.TextField(label="j =", label_style=ft.TextStyle(color=ft.colors.GREY_500), height= 50, width=80, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER, text_vertical_align=ft.VerticalAlignment.CENTER)
    i_j_input = [ft.Text("Mostrar", color=ft.colors.BLACK),
                 i_input,
                 ft.Text("iteraciones a partir del minuto", color=ft.colors.BLACK),
                 j_input]

    
    # Botones
    simular_button = ft.ElevatedButton(text="Simular", on_click=simular)
    simular_con_tabla_button = ft.ElevatedButton(text="Simular y Generar tabla", on_click=simular_y_generar_tabla)

    
    # Disposición de componentes
    page.add(
        ft.Row(controls=demora_inscripcion_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=demora_mantenimiento_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=llegadas_alumnos_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=regreso_mantenimiento_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=demora_traslado_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=tabla_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=50),
        ft.Row(controls=tiempo_simulacion_input, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=i_j_input, alignment=ft.MainAxisAlignment.CENTER),
        simular_button,
        simular_con_tabla_button,
    )


# Ejecutar la aplicación
ft.app(target=main)