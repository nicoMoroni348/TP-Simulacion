from .cola import Cola
from .simulacion import Simulacion
import time





class VectorEstado:
    def __init__(self):
        self.reloj = 0.0
        self.simulaciones = []
        self.prox_id = 1
        self.ultima_simulacion = None
        # self.proximos_eventos: Cola = None
        # self.cola: Cola = None
        
        # ...
        # Variables estadisticas van aca
    
    def crear_fila_simulacion(self, simulacion_anterior, media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion):

        # Esto deberia inicializar la simulacion segun los eventos que estan proximos (el proximo)
        # Luego deberia ejecutar efectivamente la simulacion de esa fila, y por ultimo agregarlo a su vector de simulaciones
        
        
        nueva_fila_simulacion = Simulacion(self.prox_id, simulacion_anterior,
                                           media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion,
                                           )
        self.prox_id += 1
        # nueva_fila_simulacion.evento = self.proximos_eventos.proximo_en_cola()

        # Ejecutar la simulacion
        nueva_fila_simulacion.realizar_simulacion()




        return nueva_fila_simulacion
    

    def agregar_fila_simulacion(self, simulacion: Simulacion):
        self.simulaciones.append(simulacion)


    
    def comenzar_simulacion(self, hora_j, iteraciones_i, x_tiempo_simulacion, media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion): 
                             
        # Se deben guardar las simulaciones (filas) solamente a partir de la hora j y hasta i iteraciones.
        # La ultima tambien 
        
        self.tiempo_simulacion = x_tiempo_simulacion
        N_simulaciones = 100000
        tiempo_actual = 0

        # while self.reloj <= x or self.iteracion <= n:
        iteraciones_totales = 0
        primera_iteracion_guardar = 0

        nueva_simulacion = None

        contador = 100


        entro = False
        while tiempo_actual < x_tiempo_simulacion and iteraciones_totales < N_simulaciones:
            # print(iteraciones_totales)

            
            simulacion_anterior = nueva_simulacion

            if nueva_simulacion is None:
                
                # para que el primero sea un incializar
                nueva_simulacion = self.crear_fila_simulacion(None, media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion)
                # self.agregar_fila_simulacion(nueva_simulacion)

            else:

                nueva_simulacion = self.crear_fila_simulacion(simulacion_anterior, media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion)




            if tiempo_actual >= contador:
                print(tiempo_actual, iteraciones_totales)
                contador += 1000
            

            if tiempo_actual >= hora_j:


                if not entro:
                    # print(f"Primera fila guardada en iteracion {iteraciones_totales} Tiempo {tiempo_actual}")

                    primera_iteracion_guardar = iteraciones_totales
                    entro = True
                
                if iteraciones_totales <= primera_iteracion_guardar + iteraciones_i - 1:



      
                    self.agregar_fila_simulacion(nueva_simulacion)
                    # print(f"Fila guardada en iteracion {iteraciones_totales} Tiempo {tiempo_actual}")


                
            tiempo_actual = nueva_simulacion.reloj

            iteraciones_totales += 1





        self.ultima_simulacion = nueva_simulacion

        print(f"Iteraciones Totales realizadas: {iteraciones_totales}")
    
    

    def crear_vector_estado_tabla(self):
        # Crear el vector de estado en formato de tabla
        vector_estado_tabla = []

        for i, fila in enumerate(self.simulaciones):

            fila: Simulacion = fila
            


            # if 0 < fila.id <= 15:
            #     print(f"id: {fila.id} Long cola {fila.cola_alumnos.get_longitud_cola()}")

            vector_fila = fila.obtener_vector_fila_new()
        

            # cero = vector_fila[0]
            # uno = vector_fila[1]
            # vector_fila[0] = uno
            # vector_fila[1] = cero

            vector_estado_tabla.append(vector_fila)

        

        # Aca de la ultima
        ultima_fila_tabla = self.ultima_simulacion.obtener_vector_fila_new() 
        # cero = ultima_fila_tabla[0]
        # uno = ultima_fila_tabla[1]
        # ultima_fila_tabla[0] = uno
        # ultima_fila_tabla[1] = cero
        for el in vector_estado_tabla[:7]:
            print(el[:3])
    

        return vector_estado_tabla, ultima_fila_tabla

        




