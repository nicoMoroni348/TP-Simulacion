class Printeable:
    atributos_permitidos = []

    @classmethod
    def get_atributos_permitidos(cls):
        return cls.get_atributos_permitidos