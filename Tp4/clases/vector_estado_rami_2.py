class VectorEstado:
    def __init__(self):
        self.estados = []  # Lista para almacenar los estados

    def agregar_estado(self, reloj, evento, proximos_eventos, equipos, alumnos, variables_auxiliares):
        """
        Agrega un nuevo estado al vector de estado.

        Args:
            reloj (float): Hora simulada.
            evento (str): Tipo de evento ocurrido.
            proximos_eventos (list): Lista de próximos eventos a ejecutarse.
            equipos (list): Lista de estados de los equipos.
            alumnos (list): Lista de estados de los alumnos.
            variables_auxiliares (dict): Diccionario con variables auxiliares.
        """
        estado = {
            "reloj": reloj,
            "evento": evento,
            "proximos_eventos": proximos_eventos,
            "equipos": equipos,
            "alumnos": alumnos,
            "variables_auxiliares": variables_auxiliares
        }
        self.estados.append(estado)

    def mostrar_ultimo_estado(self):
        """
        Muestra el último estado agregado al vector de estado.
        """
        if self.estados:
            ultimo_estado = self.estados[-1]
            print("Último estado:")
            print(f"Hora simulada: {ultimo_estado['reloj']}")
            print(f"Evento ocurrido: {ultimo_estado['evento']}")
            print(f"Próximos eventos: {ultimo_estado['proximos_eventos']}")
            print(f"Equipos: {ultimo_estado['equipos']}")
            print(f"Alumnos: {ultimo_estado['alumnos']}")
            print(f"Variables auxiliares: {ultimo_estado['variables_auxiliares']}")
        else:
            print("El vector de estado está vacío.")
