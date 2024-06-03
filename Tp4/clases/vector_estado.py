from cola import Cola
from simulacion import Simulacion

class VectorEstado:
    def __init__(self):
        self.reloj = 0.0
        self.simulaciones = []
        self.proximos_eventos: Cola = None
        self.cola: Cola = None
        
        # ...
        # Variables estadisticas van aca
    
    def agregar_fila_simulacion(self):

        # Esto deberia inicializar la simulacion segun los eventos que estan proximos (el proximo)
        # Luego deberia ejecutar efectivamente la simulacion de esa fila, y por ultimo agregarlo a su vector de simulaciones
        nueva_fila_simulacion = Simulacion(len(self.simulaciones) + 1)
        nueva_fila_simulacion.evento = self.proximos_eventos.proximo_en_cola()

        # Ejecutar la simulacion
        nueva_fila_simulacion.realizar_simulacion(self.cola)

        proximos_eventos = nueva_fila_simulacion.get_proximos_eventos()
        if proximos_eventos:
            [ self.cola.agregar_en_orden_de_ocurrencia_a_cola(p_e) for p_e in proximos_eventos ]




        self.simulaciones.append()


