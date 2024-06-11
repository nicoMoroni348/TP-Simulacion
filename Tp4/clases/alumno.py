
from printeable import Printeable
class Alumno(Printeable):
    atributos_permitidos = ["id", "estado", "hora_llegada"]
    alumnos = []
    def __init__(self, id):
        self.id = id
        self.estado = None
        self.hora_llegada = None
        self.hora_atencion = None

        self.hora_regreso = None
    
    def __str__(self):
        return f"Alumno {self.id} - {self.estado} - {self.hora_llegada} - {self.hora_atencion}"

    def estado_actual(self, hora_actual):
        if self.hora_atencion is None:
            return "Esperando atención"
        elif hora_actual < self.hora_atencion:
            return "Esperando atención"
        else:
            return "Siendo atendido"
        

    def set_estado(self, estado):
        self.estado = estado

    def set_hora_atencion(self, hora_atencion):
        self.hora_atencion = hora_atencion

    def set_hora_llegada(self, hora_llegada):
        self.hora_llegada = hora_llegada

    def set_hora_regreso(self, hora_regreso):
        self.hora_regreso = hora_regreso
        