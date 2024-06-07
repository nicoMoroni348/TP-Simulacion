import random
import math


from evento import Evento
from cola import Cola
from equipo import Equipo
from alumno import Alumno
from inscripcion import Inscripcion

class Simulacion:
    use_sine = False
    def __init__(self, id, simulacion_anterior):
        self.id = id


        if simulacion_anterior is None:
            self.evento = Evento(0.0, "inicializacion")
        
        self.evento: Evento = None
        # proximos eventos que se generan en esta fila
        self.proximos_eventos: Cola = None

        self.alumnos_existentes = []
        self.inscripciones_en_curso = []
        self.equipos = []

        self.reloj = self.evento.hora_ocurrencia


        self.alumno_se_fue_y_no_espero = False

        self.simulacion_anterior: Simulacion = simulacion_anterior





        # Llegadas Alumnos
        self.rnd_llegada_alumno = None
        self.tiempo_hasta_proxima_llegada = None
        self.nueva_llegada_alumno = None

        

        # Llegadas Mantenimiento
        self.rnd_1_llegada_mantenimiento = None
        self.rnd_2_llegada_mantenimiento = None
        self.tiempo_hasta_proxima_llegada_mantenimiento = None
        self.nueva_llegada_mantenimiento = None


        # Fin inscripcion
        self.rnd_fin_inscripcion = None
        self.tiempo_hasta_proximo_fin_inscripcion = None
        self.nuevo_fin_inscripcion = None


        # Fin Mantenimiento
        self.rnd_fin_mantenimiento = None
        self.tiempo_hasta_proximo_fin_mantenimiento = None
        self.nuevo_fin_mantenimiento = None




        # METRICAS


        # Contador alumnos que llegan	
        # Contador alumnos que regresan más tarde	
        # Porcentaje alumnos que se van	
        # Contador alumnos atendidos	
        # Acumulador tiempos de espera	
        # Promedio tiempos de espera

        self.contador_alumnos_llegan = None
        self.contador_alumnos_se_van_y_regresan_mas_tarde = None
        self.porcentaje_alumnos_se_van = None
        self.contador_alumnos_atendidos = None
        self.acumulador_tiempos_espera = None
        self.promedio_tiempos_espera = None



    def agregar_proximo_evento(self, proximo_evento: Evento):
        self.proximos_eventos.append(proximo_evento)
        self.proximos_eventos.sort(key=lambda x: x.hora_ocurrencia)

    def agregar_inscripcion_en_curso(self, inscripcion):
        self.inscripciones_en_curso.append(inscripcion)




    def generar_proxima_llegada_alumno(self, media=2):
        # -2*LN(1-E11)
        # Exponencial ()
        # media = 2 min

        self.rnd_llegada_alumno = random.random()
        self.tiempo_hasta_proxima_llegada = -media * self.rnd_llegada_alumno
        self.nueva_llegada_alumno = self.tiempo_hasta_proxima_llegada + self.reloj


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
            # print("cosine used")
        else:
            self.tiempo_hasta_proxima_llegada_mantenimiento = (math.sqrt(-2 * math.log(1 - self.rnd_1_llegada_mantenimiento)) * math.sin(2 * math.pi * self.rnd_2_llegada_mantenimiento)) * de + media
            Simulacion.use_sine = True
            # print("sine used")
        self.nueva_llegada_mantenimiento = self.tiempo_hasta_proxima_llegada_mantenimiento + self.reloj


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
        self.nuevo_fin_inscripcion = self.tiempo_hasta_proximo_fin_inscripcion + self.reloj


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


    def generar_evento_regreso_alumno(self):
        proximo_evento_fin_regreso_alumno = Evento(self.evento.hora_ocurrencia + 30, "fin_regreso_alumno")
        self.agregar_proximo_evento(proximo_evento_fin_regreso_alumno)
        


    def manejar_retirada_alumno(self, cola: Cola):
        if cola.get_longitud_cola() >= 5:
            self.alumno_se_fue_y_no_espero = True
            proximo_evento_fin_regreso_alumno = Evento(self.evento.hora_ocurrencia + 30, "fin_regreso_alumno")
            self.agregar_proximo_evento(proximo_evento_fin_regreso_alumno)




    
    def actualizar_evento(self, evento):
        # Actualiza el evento de la fila actual segun el atributo proximos eventos de la fila anterior
        self.evento = self.simulacion_anterior.proximos_eventos.proximo_en_cola()

    




    def inicializar_metricas(self):
        self.contador_alumnos_llegan = 0
        self.contador_alumnos_se_van_y_regresan_mas_tarde = 0
        self.porcentaje_alumnos_se_van = 0.0
        self.contador_alumnos_atendidos = 0
        self.acumulador_tiempos_espera = 0.0
        self.promedio_tiempos_espera = 0.0



    def actualizar_metricas(self, cola):
        pass





    def actualizar_contador_alumnos_llegados(self):
        # Contador alumnos que llegan
        if self.evento.tipo == "llegada_alumno":
            self.contador_alumnos_llegan = self.simulacion_anterior.contador_alumnos_llegan + 1
        else:
            self.contador_alumnos_llegan = self.simulacion_anterior.contador_alumnos_llegan
    
    def actualizar_contador_alumnos_atendidos(self):
        if self.evento == "fin_inscripcion":
            self.contador_alumnos_atendidos = self.simulacion_anterior.contador_alumnos_atendidos + 1
        else:
            self.contador_alumnos_atendidos = self.simulacion_anterior.contador_alumnos_atendidos

    
    def actualizar_contador_alumnos_se_van_regresan_mas_tarde(self, cola: Cola):
        if cola.get_longitud_cola() >= 5:
            self.contador_alumnos_se_van_y_regresan_mas_tarde = self.simulacion_anterior.contador_alumnos_se_van_y_regresan_mas_tarde + 1
        else:
            self.contador_alumnos_se_van_y_regresan_mas_tarde = self.simulacion_anterior.contador_alumnos_se_van_y_regresan_mas_tarde





    
    def actualizar_alumnos_existentes(self):
        # Si no cambia nada
        self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes



    def crear_nuevo_alumno(self):
        nuevo_alumno = Alumno(len(self.alumnos_existentes) + 1)
        nuevo_alumno.set_hora_llegada = self.reloj

        hay_equipo_libre = False

        # Recorre todos los equipos libres
        for equipo in self.equipos:

            equipo: Equipo = equipo

            # Si hay un equipo libre
            if equipo.esta_libre():
                # Entra directo a ser atendido

                # Cambiar el estado del nuevo alumno
                nuevo_alumno.set_estado("siendo_atendido")
                nuevo_alumno.set_hora_atencion = self.reloj

                # Cambiar el estado del equipo ocupado por el alumno
                equipo.set_estado("ocupado_inscripcion")

                # Crear un objeto de inscripcion para llevar el registro de que alumno esta en que equipo
                inscripcion = Inscripcion(Inscripcion.proximo_id())
                # Setear los atributos corrrespondientes
                inscripcion.set_alumno(nuevo_alumno)
                inscripcion.set_equipo(equipo)

                # Se genera el proximo evento de fin de inscripcion
                self.generar_proximo_fin_inscripcion()
                equipo.set_hora_fin_uso(self.nuevo_fin_inscripcion)

                # Setearle a la inscripcion la hora del fin de la inscripcion (no se bien para que)
                inscripcion.set_hora_fin(self.nuevo_fin_inscripcion)

                hay_equipo_libre = True

        
        if not hay_equipo_libre:    
            # Si hay +5 alumnos en la cola  -> Se va y regresa en 30 mins         
            if self.cola_alumnos.get_longitud_cola() >= 5:
                # El alumno se va y regresa en 30 minutos 
                
                # EL alumno de esta iteracion se fue y no espero
                self.alumno_se_fue_y_no_espero = True
                # Actualizamos estado
                nuevo_alumno.set_estado("esperando_desocupacion")
                # Creamos evento y agregamos a la lista
                self.generar_evento_regreso_alumno()
                
                # ACA HABRIA QUE VER si se debe guardar el objeto del alumno o no (me parece que no, pero no se, pasa que alto viaje si si)
            

            # Si no hay equipos libres -> Se mete en la cola
            else:

                # Si hay menos de 5 personas esperando en la cola

                # seteamos el estado a esperando_atencion
                nuevo_alumno.set_estado("esperando_atencion")
                # La hora de atencion se debe setear cuando se atienda efectivamente a ese alumno

                # Agregamos el alumno a la cola
                self.cola_alumnos.agregar_a_cola(nuevo_alumno)
                
        
        
        
        # Faltan los siguientes Casos de creacion de alumno
       
        # Si ....




                










    def realizar_simulacion(self):
        # Este metodo haria la simulacion a partir del evento que tiene como atributo


        



        if self.evento.tipo == "inicializacion":
            
            # Primera proxima llegada
            self.generar_proxima_llegada_alumno()
            # Primera proxima llegada de mantenimiento
            self.generar_proxima_llegada_mantenimiento()


            # Creamos los equipos
            self.equipos = Equipo.crear_equipos()
            # Creamos la cola de alumnos
            self.cola_alumnos = Cola()

            # Inicializamos las metricas
            self.inicializar_metricas()

            



        elif self.evento.tipo == "llegada_alumno":
            self.generar_proxima_llegada_alumno()

            # Hay que ver que pasa con este metodo
            self.crear_nuevo_alumno()


            # Revisar mas metricas
            self.actualizar_contador_alumnos_llegados() 
            self.manejar_retirada_alumno()


        elif self.evento.tipo == "llegada_mantenimiento":
            pass

        
        elif self.evento.tipo == "fin_inscripcion":
            pass



        elif self.evento.tipo == "fin_regreso_alumno":
            pass


        elif self.evento.tipo == "fin_mantenimiento":
            pass













        # Actualizacion de metricas y no se que mas