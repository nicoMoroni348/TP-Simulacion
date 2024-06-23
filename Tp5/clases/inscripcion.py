from .alumno import Alumno
from .equipo import Equipo

class Inscripcion:
    proximo_id = 0
    def __init__(self, id):
        self.id = id
        self.alumno= None
        self.equipo = None
        self.hora_fin = None 
      

    @staticmethod
    def get_proximo_id():
        Inscripcion.proximo_id += 1
        return Inscripcion.proximo_id
    
    def set_alumno(self, alumno: Alumno):
        self.alumno = alumno

    def set_equipo(self, equipo: Equipo):
        self.equipo = equipo

    def set_hora_fin(self, hora_fin: float):
        self.hora_fin = hora_fin

        

