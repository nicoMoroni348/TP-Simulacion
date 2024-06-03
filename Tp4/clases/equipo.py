
class Equipo:
    equipos = []
    def __init__(self, id, estado, hora_fin_uso):
        self.id = id
        self.estado = estado
        self.hora_fin_uso = hora_fin_uso
    
    def __str__(self):
        return f"Equipo {self.id} - {self.estado} - {self.hora_fin_uso}"