class Cola:
    def __init__(self):
        self.cola = []
    
    def agregar_a_cola(self, elemento):
        self.cola.append(elemento)

    def proximo_en_cola(self):
        if self.cola:
            return self.cola.pop(0)
    
    def get_longitud_cola(self):
        return len(self.cola)
    
    def agregar_en_orden_de_ocurrencia_a_cola(self, elemento):
        self.cola.append(elemento)
        self.cola.sort(key=lambda x: x.hora_ocurrencia)