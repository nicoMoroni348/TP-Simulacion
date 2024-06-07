class VectorEstado:
    def __init__(self):
        self.reloj = 0.0
        self.simulaciones = []
        self.proximos_eventos = []
        # Otras variables estadísticas van aquí

    def agregar_evento(self, evento):
        """
        Agrega un evento al vector de estado.

        Args:
            evento (str): Tipo de evento ocurrido.
        """
        self.proximos_eventos.append(evento)

    def agregar_simulacion(self, estado_actual):
        """
        Agrega un estado completo de simulación al vector de estado.

        Args:
            estado_actual (dict): Diccionario con información sobre el estado actual.
                Ejemplo:
                {
                    "reloj": 10.0,
                    "eventos": ["Llegada", "Mantenimiento"],
                    "equipos": [...],
                    "alumnos": [...],
                    "variables_auxiliares": {...}
                }
        """
        self.simulaciones.append(estado_actual)

    def mostrar_ultimo_estado(self):
        """
        Muestra el último estado agregado al vector de estado.
        """
        if self.simulaciones:
            ultimo_estado = self.simulaciones[-1]
            print("Último estado:")
            print(f"Hora simulada: {ultimo_estado['reloj']}")
            print(f"Eventos ocurridos: {ultimo_estado['eventos']}")
            print(f"Equipos: {ultimo_estado['equipos']}")
            print(f"Alumnos: {ultimo_estado['alumnos']}")
            print(f"Variables auxiliares: {ultimo_estado['variables_auxiliares']}")
        else:
            print("El vector de estado está vacío.")

# Ejemplo de uso
if __name__ == "__main__":
    vector_estado = VectorEstado()
    # Agregar eventos y simulaciones (reemplaza con datos específicos)
    vector_estado.agregar_evento("Llegada")
    vector_estado.agregar_simulacion({
        "reloj": 10.0,
        "eventos": ["Llegada", "Mantenimiento"],
        "equipos": [...],
        "alumnos": [...],
        "variables_auxiliares": {...}
    })
    # ...
    vector_estado.mostrar_ultimo_estado()
