from equipo import Equipo
from persona_mantenimiento import PersonaMantenimiento

class ProcesoMantenimiento:
    proximo_id = 0
    def __init__(self, id):
        self.id = id
        self.equipo: Equipo = None
        self.persona_mantenimiento: PersonaMantenimiento = None
        self.hora_fin: float = None

    def __str__(self):
        return f"Proceso Mantenimiento {self.id} - {self.equipo} - {self.persona_mantenimiento} - {self.hora_fin}"
    

    @staticmethod
    def proximo_id():
        ProcesoMantenimiento.proximo_id += 1
        return ProcesoMantenimiento.proximo_id
    
    def set_equipo(self, equipo: Equipo):
        self.equipo = equipo

    def set_persona_mantenimiento(self, persona_mantenimiento: PersonaMantenimiento):
        self.persona_mantenimiento = persona_mantenimiento

    def set_hora_fin(self, hora_fin: float):
        self.hora_fin = hora_fin


