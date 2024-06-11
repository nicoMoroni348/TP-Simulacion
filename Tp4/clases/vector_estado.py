from cola import Cola
from simulacion import Simulacion
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
    
    def agregar_fila_simulacion(self, simulacion_anterior=None):

        # Esto deberia inicializar la simulacion segun los eventos que estan proximos (el proximo)
        # Luego deberia ejecutar efectivamente la simulacion de esa fila, y por ultimo agregarlo a su vector de simulaciones
        
        nueva_fila_simulacion = Simulacion(self.prox_id, simulacion_anterior)
        self.prox_id += 1
        # nueva_fila_simulacion.evento = self.proximos_eventos.proximo_en_cola()

        # Ejecutar la simulacion
        nueva_fila_simulacion.realizar_simulacion()



        return nueva_fila_simulacion


    
    def comenzar_simulacion(self, hora_j, iteraciones_i, x_tiempo_simulacion):
        # Se deben guardar las simulaciones (filas) solamente a partir de la hora j y hasta i iteraciones.
        # La ultima tambien 
        
        self.tiempo_simulacion = x_tiempo_simulacion
        N_simulaciones = 100000
        tiempo_actual = 0

        # while self.reloj <= x or self.iteracion <= n:
        iteraciones_totales = 0
        primera_iteracion_guardar = 0

        entro = False
        while tiempo_actual < x_tiempo_simulacion and iteraciones_totales <= N_simulaciones:
            if iteraciones_totales == 0:
                # para que el primero sea un incializar
                nueva_simulacion = self.agregar_fila_simulacion(None)

            

            if tiempo_actual >= hora_j and iteraciones_totales <= primera_iteracion_guardar + iteraciones_i:


                if not entro:
                    primera_iteracion_guardar = iteraciones_totales
                    entro = True


                simulacion_anterior = nueva_simulacion
                nueva_simulacion = self.agregar_fila_simulacion(simulacion_anterior)

                
            tiempo_actual = nueva_simulacion.reloj

            iteraciones_totales += 1

        # print(nueva_simulacion.reloj, nueva_simulacion.evento.tipo, nueva_simulacion.porcentaje_alumnos_se_van, nueva_simulacion.promedio_tiempos_espera)
        # print(nueva_simulacion.obtener_vector_fila())

        self.ultima_simulacion = nueva_simulacion

    

    def crear_vector_estado_tabla(self):
        # Crear el vector de estado en formato de tabla
        vector_estado_tabla = []

        for fila in self.simulaciones:
            fila: Simulacion = fila

            vector_fila = fila.obtener_vector_fila()
            cero = vector_fila[0]
            uno = vector_fila[1]
            vector_fila[0] = uno
            vector_fila[1] = cero

            vector_estado_tabla.append(vector_fila)

        

        # Aca de la ultima
        ultima_fila_tabla = self.ultima_simulacion.obtener_vector_fila() 
        cero = ultima_fila_tabla[0]
        uno = ultima_fila_tabla[1]
        ultima_fila_tabla[0] = uno
        ultima_fila_tabla[1] = cero
    

        return vector_estado_tabla, ultima_fila_tabla

        








ve = VectorEstado()
ve.comenzar_simulacion(100.0, 100, 10000)

tabla = ve.crear_vector_estado_tabla()

print(tabla[0])

# print(ve.ultima_simulacion)