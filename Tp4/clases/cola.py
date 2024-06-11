from printeable import Printeable

class Cola(Printeable):
    atributos_permitidos = ["longitud_cola"]
    def __init__(self):
        self.cola = []
        self.longitud_cola = 0
    
    def agregar_a_cola(self, elemento):
        self.cola.append(elemento)
        self.longitud_cola = len(self.cola)

    def proximo_en_cola(self):
        if self.cola:
            self.longitud_cola -= 1
            return self.cola.pop(0)
    
    def get_longitud_cola(self):
        
        return self.longitud_cola
    
    def agregar_en_orden_de_ocurrencia_a_cola(self, elemento):
        self.cola.append(elemento)
        self.cola.sort(key=lambda x: x.hora_ocurrencia)
        self.longitud_cola = len(self.cola)