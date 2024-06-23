from .printeable import Printeable


class PersonaMantenimiento(Printeable):
    atributos_permitidos = ["estado", "maquinas_restantes"]
    def __init__(self, id):
        self.id = id
        self.hora_llegada = None
        self.estado = "desocupado"
        self.maquinas_restantes: list = [1, 2, 3, 4, 5, 6]

    def __str__(self):
        return f"Persona Mantenimiento {self.id} - {self.estado} - {self.hora_llegada} - {self.maquinas_restantes}"
    
    def set_hora_llegada(self, hora_llegada):
        self.hora_llegada = hora_llegada

    def set_estado(self, estado):
        self.estado = estado

    def quitar_equipo_mantenido(self, numero_equipo):
        self.maquinas_restantes.remove(numero_equipo)

    def resetear_equipos_a_mantener(self):
        self.maquinas_restantes: list = [1, 2, 3, 4, 5, 6]


