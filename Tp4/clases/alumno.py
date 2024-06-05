

class Alumno:
    alumnos = []
    def __init__(self, id):
        self.id = id
        self.estado = None
        self.hora_llegada = None
        self.hora_atencion = None
    
    def __str__(self):
        return f"Alumno {self.id} - {self.estado} - {self.hora_llegada} - {self.hora_atencion}"

    def estado_actual(self, hora_actual):
        if self.hora_atencion is None:
            return "Esperando atención"
        elif hora_actual < self.hora_atencion:
            return "Esperando atención"
        else:
            return "Siendo atendido"