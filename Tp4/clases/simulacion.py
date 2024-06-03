import random
import math


from evento import Evento
from cola import Cola

class Simulacion:
    use_sine = False
    def __init__(self, id):
        self.id = id
        self.evento: Evento = None
        self.proximos_eventos = []


        self.alumno_se_fue_y_no_espero = False



        # Alumnos
        self.rnd_llegada_alumno = None
        self.tiempo_hasta_proxima_llegada = None
        self.nueva_llegada_alumno = None

        


        # Mantenimiento
        self.rnd_1_llegada_mantenimiento = None
        self.rnd_2_llegada_mantenimiento = None
        self.tiempo_hasta_proxima_llegada_mantenimiento = None
        self.nueva_llegada_mantenimiento = None


        # Fin inscripcion
        self.rnd_fin_inscripcion = None
        self.tiempo_hasta_proximo_fin_inscripcion = None
        self.nuevo_fin_inscripcion = None




        # METRICAS

        self.simulacion_anterior: Simulacion = None
        # Contador alumnos que llegan	
        # Contador alumnos que regresan más tarde	
        # Porcentaje alumnos que se van	
        # Contador alumnos atendidos	
        # Acumulador tiempos de espera	
        # Promedio tiempos de espera
        self.contador_alumnos_llegan = 0
        self.contador_alumnos_se_van_y_regresan_mas_tarde = 0
        self.porcentaje_alumnos_se_van = 0.0
        self.contador_alumnos_atendidos = 0
        self.acumulador_tiempos_espera = 0.0
        self.promedio_tiempos_espera = 0.0


    def agregar_proximo_evento(self, proximo_evento: Evento):
        self.proximos_eventos.append(proximo_evento)
        self.proximos_eventos.sort(key=lambda x: x.hora_ocurrencia)




    def generar_proxima_llegada_alumno(self, media=2):
        # -2*LN(1-E11)
        # Exponencial ()
        # media = 2 min

        self.rnd_llegada_alumno = random.random()
        self.tiempo_hasta_proxima_llegada = -media * self.rnd_llegada_alumno
        self.nueva_llegada_alumno = self.tiempo_hasta_proxima_llegada + self.evento.hora_ocurrencia


        # Agregar el evento a la lista de proximos eventos
        proximo_evento_llegada_alumno = Evento(self.nueva_llegada_alumno, "llegada_alumno")
        self.agregar_proximo_evento(proximo_evento_llegada_alumno)




    def generar_proxima_llegada_mantenimiento(self):
        # (SQRT(-2*LN(1-H11))*COS(2*PI()*I11))*3+60
        # Normal(media; de)
        # media = 60 minutos
        # de = 3 minutos
        media = 60
        de = 3

        self.rnd_1_llegada_mantenimiento = random.random()
        self.rnd_2_llegada_mantenimiento = random.random()
        if Simulacion.use_sine:
            self.tiempo_hasta_proxima_llegada_mantenimiento = (math.sqrt(-2 * math.log(1 - self.rnd_1_llegada_mantenimiento)) * math.cos(2 * math.pi * self.rnd_2_llegada_mantenimiento)) * de + media
            Simulacion.use_sine = False
            print("cosine used")
        else:
            self.tiempo_hasta_proxima_llegada_mantenimiento = (math.sqrt(-2 * math.log(1 - self.rnd_1_llegada_mantenimiento)) * math.sin(2 * math.pi * self.rnd_2_llegada_mantenimiento)) * de + media
            Simulacion.use_sine = True
            print("sine used")
        self.nueva_llegada_mantenimiento = self.tiempo_hasta_proxima_llegada_mantenimiento + self.evento.hora_ocurrencia


        # Agregar el evento a la lista de proximos eventos
        proximo_evento_llegada_mantenimiento = Evento(self.nueva_llegada_mantenimiento, "llegada_mantenimiento")
        self.agregar_proximo_evento(proximo_evento_llegada_mantenimiento)


    def generar_proximo_fin_inscripcion(self):
        # Inscripcion
        # Uniforme(A,B)
        # A = 5 minutos
        # B = 8 minutos
        a = 5
        b = 8
        self.rnd_fin_inscripcion = random.random()
        self.tiempo_hasta_proximo_fin_inscripcion = a + (b-a) * self.rnd_fin_inscripcion
        self.nuevo_fin_inscripcion = self.tiempo_hasta_proximo_fin_inscripcion + self.evento.hora_ocurrencia


        # Agregar el evento a la lista de proximos eventos
        proximo_evento_fin_inscripcion = Evento(self.nuevo_fin_inscripcion, "fin_inscripcion")
        self.agregar_proximo_evento(proximo_evento_fin_inscripcion)



    def generar_proximo_fin_mantenimiento(self):
        # Mantenimiento
        # Uniforme(A,B)
        # A = 3 minutos
        # B = 10 minutos
        a = 3
        b = 10
        self.rnd_fin_mantenimiento = random.random()
        self.tiempo_hasta_proximo_fin_mantenimiento = a + (b-a) * self.rnd_fin_mantenimiento
        self.nuevo_fin_mantenimiento = self.tiempo_hasta_proximo_fin_mantenimiento + self.evento.hora_ocurrencia

        # Agregar el evento a la lista de proximos eventos
        proximo_evento_fin_mantenimiento = Evento(self.nuevo_fin_mantenimiento, "fin_mantenimiento")
        self.agregar_proximo_evento(proximo_evento_fin_mantenimiento)
        

    
    def set_evento(self, evento):
        self.evento = evento

    def get_proximos_eventos(self):
        return self.proximos_eventos
    

    def actualizar_metricas(self, cola):
        pass

    def actualizar_contador_alumnos_llegados(self):
        # Contador alumnos que llegan
        if self.evento == "llegada_alumno":
            self.contador_alumnos_llegan = self.simulacion_anterior.contador_alumnos_llegan + 1
        else:
            self.contador_alumnos_llegan = self.simulacion_anterior.contador_alumnos_llegan
    
    def actualizar_contador_alumnos_atendidos(self):
        if self.evento == "fin_inscripcion":
            self.contador_alumnos_atendidos = self.simulacion_anterior.contador_alumnos_atendidos + 1
        else:
            self.contador_alumnos_atendidos = self.simulacion_anterior.contador_alumnos_atendidos

    
    def actualizar_contador_alumnos_se_van_regresan_mas_tarde(self, cola):
        if cola >= 5:
            self.contador_alumnos_se_van_y_regresan_mas_tarde = self.simulacion_anterior.contador_alumnos_se_van_y_regresan_mas_tarde + 1
        else:
            self.contador_alumnos_se_van_y_regresan_mas_tarde = self.simulacion_anterior.contador_alumnos_se_van_y_regresan_mas_tarde


    def manejar_retirada_alumno(self, cola):
        if cola >= 5:
            self.alumno_se_fue_y_no_espero = True
            proximo_evento_fin_regreso_alumno = Evento(self.evento.hora_ocurrencia + 30, "fin_regreso_alumno")
            self.agregar_proximo_evento(proximo_evento_fin_regreso_alumno)





    def realizar_simulacion(self, cola):
        # Este metodo haria la simulacion a partir del evento que tiene como atributo

        
        pass
        


        



