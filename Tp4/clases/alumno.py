

class Alumno:
    alumnos = []
    def __init__(self, id, estado, hora_llegada, hora_atencion):
        self.id = id
        self.estado = estado
        self.hora_llegada = hora_llegada
        self.hora_atencion = hora_atencion
    
    def __str__(self):
        return f"Alumno {self.id} - {self.estado} - {self.hora_llegada} - {self.hora_atencion}"




