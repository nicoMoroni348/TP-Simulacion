from cola import Cola
from simulacion import Simulacion
import time


class VectorEstado:
    def __init__(self):
        self.reloj = 0.0
        self.simulaciones = []
        self.prox_id = 1
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


    
    def comenzar_simulacion(self, hora_j, iteraciones_i, tiempo_simulacion):
        # Se deben guardar las simulaciones (filas) solamente a partir de la hora j y hasta i iteraciones.
        # La ultima tambien 
        
        self.tiempo_simulacion = tiempo_simulacion
        tiempo_actual = 0

        # while self.reloj <= x or self.iteracion <= n:
        i = 0
        while tiempo_actual < 100.0:
            if i == 0:
                nueva_simulacion = self.agregar_fila_simulacion(None)

            else:
                simulacion_anterior = nueva_simulacion
                nueva_simulacion = self.agregar_fila_simulacion(simulacion_anterior)


            
            tiempo_actual = nueva_simulacion.reloj

            if nueva_simulacion.evento.tipo in ("fin_mantenimiento", "llegada_mantenimiento"):
                print(nueva_simulacion.reloj, nueva_simulacion.evento.tipo)
            # time.sleep(0.2)


            i += 1





ve = VectorEstado()
ve.comenzar_simulacion(4, 2, 5)