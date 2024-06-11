from printeable import Printeable

class Evento(Printeable):
    atributos_permitidos = ["tipo"]
    def __init__(self, hora_ocurrencia, tipo):
        self.hora_ocurrencia = hora_ocurrencia
        self.tipo = tipo


