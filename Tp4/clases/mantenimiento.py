
class Mantenimiento:
    def __init__(self, id, hora_llegada, estado, maquinas_restantes):
        self.id = id
        self.hora_llegada = hora_llegada
        self.estado = estado
        self.maquinas_restantes = maquinas_restantes

    def __str__(self):
        return f"Mantenimiento {self.id} - {self.estado} - {self.hora_llegada} - {self.maquinas_restantes}"


