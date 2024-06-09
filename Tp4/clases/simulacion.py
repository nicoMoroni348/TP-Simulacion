import random
import math


from evento import Evento
from cola import Cola
from equipo import Equipo
from alumno import Alumno
from inscripcion import Inscripcion
from persona_mantenimiento import PersonaMantenimiento
from proceso_mantenimiento import ProcesoMantenimiento

class Simulacion:
    use_sine = False
    def __init__(self, id, simulacion_anterior):
        self.id = id


        
        if simulacion_anterior is None:
            self.evento = Evento(0.0, "inicializacion")
            self.inicializar_atributos_simulacion()
            return
        


        self.simulacion_anterior: Simulacion = simulacion_anterior
        # proximos eventos que se generan en esta fila
        self.proximos_eventos: list = self.simulacion_anterior.proximos_eventos
        

        self.evento: Evento = self.tomar_evento_a_ocurrir()


        self.reloj = self.evento.hora_ocurrencia



        

                

        
        
        self.cola_alumnos: Cola = self.simulacion_anterior.cola_alumnos
        self.cola_mantenimiento: Cola = self.simulacion_anterior.cola_mantenimiento

        self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes
        self.alumnos_pendientes_regresar = self.simulacion_anterior.alumnos_pendientes_regresar
        self.inscripciones_en_curso = self.simulacion_anterior.inscripciones_en_curso
        self.equipos = self.simulacion_anterior.equipos
        self.persona_mantenimiento: PersonaMantenimiento = self.simulacion_anterior.persona_mantenimiento





        self.alumno_se_fue_y_no_espero = False

        





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

        self.contador_alumnos_llegan = self.simulacion_anterior.contador_alumnos_llegan
        self.contador_alumnos_se_van_y_regresan_mas_tarde = self.simulacion_anterior.contador_alumnos_se_van_y_regresan_mas_tarde
        self.porcentaje_alumnos_se_van = self.simulacion_anterior.porcentaje_alumnos_se_van
        self.contador_alumnos_atendidos = self.simulacion_anterior.contador_alumnos_atendidos
        self.acumulador_tiempos_espera = self.simulacion_anterior.acumulador_tiempos_espera
        self.promedio_tiempos_espera = self.simulacion_anterior.promedio_tiempos_espera



    def inicializar_atributos_simulacion(self):
        # Inicializamos Los atributos que se "arrastran" por fila

        self.reloj = 0.0



        self.proximos_eventos = []

        self.alumnos_existentes = []
        self.alumnos_pendientes_regresar = []
        self.inscripciones_en_curso = []


        # Creamos los equipos
        self.equipos = Equipo.crear_equipos()

        # Creamos la persona de mantenimiento
        self.persona_mantenimiento = PersonaMantenimiento(1)


        # Creamos la cola de alumnos
        self.cola_alumnos = Cola()
        
        self.cola_mantenimiento = Cola()



    def agregar_proximo_evento(self, proximo_evento: Evento):
        self.proximos_eventos.append(proximo_evento)
        self.proximos_eventos.sort(key=lambda x: x.hora_ocurrencia)



    def tomar_evento_a_ocurrir(self):
        return self.proximos_eventos.pop(0)




    def agregar_inscripcion_en_curso(self, inscripcion):
        self.inscripciones_en_curso.append(inscripcion)
        self.inscripciones_en_curso.sort(key=lambda x: x.hora_fin)




    def generar_proxima_llegada_alumno(self, media=2):
        # -2*LN(1-E11)
        # Exponencial ()
        # media = 2 min

        self.rnd_llegada_alumno = random.random()
        self.tiempo_hasta_proxima_llegada = -media * math.log(1-self.rnd_llegada_alumno, math.e)
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
        else:
            self.tiempo_hasta_proxima_llegada_mantenimiento = (math.sqrt(-2 * math.log(1 - self.rnd_1_llegada_mantenimiento)) * math.sin(2 * math.pi * self.rnd_2_llegada_mantenimiento)) * de + media
            Simulacion.use_sine = True
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
        self.nuevo_fin_mantenimiento = self.tiempo_hasta_proximo_fin_mantenimiento + self.reloj

        # Agregar el evento a la lista de proximos eventos
        proximo_evento_fin_mantenimiento = Evento(self.nuevo_fin_mantenimiento, "fin_mantenimiento")
        self.agregar_proximo_evento(proximo_evento_fin_mantenimiento)


    def generar_evento_regreso_alumno(self):
        proximo_evento_fin_regreso_alumno = Evento(self.reloj + 30, "fin_regreso_alumno")
        self.agregar_proximo_evento(proximo_evento_fin_regreso_alumno)

    def agregar_alumno_pendiente_regresar(self, alumno: Alumno):
        alumno.set_hora_regreso(self.reloj + 30)
        self.alumnos_pendientes_regresar.append(alumno)

    
    def siguiente_alumno_pendiente_regresar(self):
        return self.alumnos_pendientes_regresar.pop(0)


    
    def actualizar_evento(self):
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



    
    def agregar_alumno_existente(self, alumno):
        # self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes + [alumno]
        self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes[:]
        self.alumnos_existentes.append(alumno)




    def crear_nuevo_alumno(self, es_nuevo=True):

        # Si es un alumno que recién entra a la simulación y no es un alumno que regresó:
        if es_nuevo:
            # Si el alumno recién entra a la simulación, crea el objeto
            nuevo_alumno = Alumno(len(self.alumnos_existentes) + 1)

        else:
            # Si es un alumno que regreso de la espera de desocupacion
            nuevo_alumno = self.siguiente_alumno_pendiente_regresar()
        
        nuevo_alumno.set_hora_llegada(self.reloj)

        hay_equipo_libre = False

        # Recorre todos los equipos libres
        for equipo in self.equipos:

            equipo: Equipo = equipo

            # Si hay un equipo libre
            if equipo.esta_libre():
                # Entra directo a ser atendido

                # Cambiar el estado del nuevo alumno
                # nuevo_alumno.set_estado("siendo_atendido")
                nuevo_alumno.set_hora_atencion(self.reloj)

                nuevo_alumno.set_estado("siendo_atendido")

                # Cambiar el estado del equipo ocupado por el alumno
                equipo.set_estado("ocupado_inscripcion")

                # Se genera el proximo evento de fin de inscripcion
                self.generar_proximo_fin_inscripcion()

                # Crear un objeto de inscripcion para llevar el registro de que alumno esta en que equipo
                inscripcion = Inscripcion(Inscripcion.get_proximo_id())
                # Setear los atributos corrrespondientes
                inscripcion.set_alumno(nuevo_alumno)
                inscripcion.set_equipo(equipo)

                
                equipo.set_hora_fin_uso(self.nuevo_fin_inscripcion)

                # Setearle a la inscripcion la hora del fin de la inscripcion (no se bien para que)
                inscripcion.set_hora_fin(self.nuevo_fin_inscripcion)

                
                self.agregar_inscripcion_en_curso(inscripcion)
                
                hay_equipo_libre = True



                break




        
        if not hay_equipo_libre:
            # Si hay +5 alumnos en la cola  -> Se va y regresa en 30 mins         
            if self.cola_alumnos.get_longitud_cola() >= 5:
                # El alumno se va y regresa en 30 minutos 
                
                # EL alumno de esta iteracion se fue y no espero
                self.alumno_se_fue_y_no_espero = True

                # Actualizamos estado
                nuevo_alumno.set_estado("esperando_desocupacion")
                # Seteamos la hora de regreso del alumno

                # Creamos evento y agregamos a la lista
                self.generar_evento_regreso_alumno()

                self.agregar_alumno_pendiente_regresar(nuevo_alumno)
                
                
            

            # Si no hay equipos libres -> Se mete en la cola
            else:

                # Si hay menos de 5 personas esperando en la cola

                # seteamos el estado a esperando_atencion
                nuevo_alumno.set_estado("esperando_atencion")
                # La hora de atencion se debe setear cuando se atienda efectivamente a ese alumno

                # Agregamos el alumno a la cola
                self.cola_alumnos.agregar_a_cola(nuevo_alumno)
                
        


        # Agregar alumno a la lista de alumnos
        self.agregar_alumno_existente(nuevo_alumno)

    

    def manejar_proceso_mantenimiento(self):
        # Este metodo se ejecuta en cada llegada de mantenimiento
        # y cada vez que se desocupa un equipo siempre y cuando la cola de mantenimiento no este vacia
        # Y cada vez que termine de mantener un equipo (si quedan equipos pendientes)

        # self.persona_mantenimiento.set_hora_llegada(self.reloj)

        # Si terminó el mantenimiento a TODAS las máquinas
        # print(self.persona_mantenimiento.maquinas_restantes)
        if not self.persona_mantenimiento.maquinas_restantes: 
            # Resetea los equipos restantes en [1, 2, 3, 4, 5, 6]
            self.persona_mantenimiento.resetear_equipos_a_mantener()
            
            # Genera la próxima llegada de la persona de mantenimiento
            self.generar_proxima_llegada_mantenimiento()
        
        hay_equipo_libre = False

        # Recorre todos los equipos libres que FALTAN POR MANTENER
        for equipo in self.equipos:

            equipo: Equipo = equipo

            # Si hay un equipo libre
            if equipo.esta_libre() and equipo.id in self.persona_mantenimiento.maquinas_restantes: 

                hay_equipo_libre = True

                # Generar evento fin de mantenimiento
                self.generar_proximo_fin_mantenimiento()

                # actualizar estado equipo
                equipo.set_estado("ocupado_mantenimiento")
                
                # Actualizar estado de persona de mantenimiento
                self.persona_mantenimiento.set_estado('en_mantenimiento')

                # Como inicia un proceso de mantenimiento, quita el equipo de su lista de equipos pendientes a mantener
                self.persona_mantenimiento.quitar_equipo_mantenido(equipo.id)
                
                # Crear objeto de proceso de mantenimiento
                proceso_mantenimiento = ProcesoMantenimiento(ProcesoMantenimiento.get_proximo_id())
                proceso_mantenimiento.set_equipo(equipo)
                proceso_mantenimiento.set_persona_mantenimiento(self.persona_mantenimiento)
                proceso_mantenimiento.set_hora_fin(self.nuevo_fin_mantenimiento)

                break
                

        
        if not hay_equipo_libre:
            # Agregamos el personal de mantenimiento a la cola prioritaria
            self.cola_mantenimiento.agregar_a_cola(self.persona_mantenimiento)

            # Actualizamos su estado a Esperando Atencion
            self.persona_mantenimiento.set_estado('esperando_atencion')

            
    def actualizar_estados_equipo_alumno_segun_fin_inscripcion(self, inscripcion_finalizada):
        for eq in self.equipos:
            eq: Equipo = eq
            if eq.id == inscripcion_finalizada.equipo.id:
                eq.set_estado("libre")
                eq.set_hora_fin_uso(self.reloj)
        
        for al in self.alumnos_existentes:
            al: Alumno = al
            if al.id == inscripcion_finalizada.alumno.id:
                al.set_estado("destruccion")
                al.set_hora_atencion(self.reloj)


    def actualizar_estado_alumno_segun_inicio_inscripcion(self, alumno: Alumno):
        for al in self.alumnos_existentes:
            al: Alumno = al
            if al.id == alumno.id:
                al.set_estado("siendo_atendido")
                al.set_hora_atencion(self.reloj)



    def ingresar_alumno_a_equipo(self, alumno):
        for equipo in self.equipos:
            equipo: Equipo = equipo

            if equipo.esta_libre():
                # ACtualizar estado del alumno en la lista de alumnos existentes
                self.actualizar_estado_alumno_segun_inicio_inscripcion(alumno)

                # Actualizar estado del equipo en la lista de equipos 
                equipo.set_estado("ocupado_inscripcion")
                
                # Generar evento fin de inscripcion y setear hora_fin al equipo
                self.generar_proximo_fin_inscripcion()
                equipo.set_hora_fin_uso(self.nuevo_fin_inscripcion)

                # Crear objeto de inscripcion
                inscripcion = Inscripcion(Inscripcion.get_proximo_id())
                # Setear los atributos corrrespondientes
                inscripcion.set_alumno(alumno)
                inscripcion.set_equipo(equipo)
                # Setear hora_fin de inscripcion 
                inscripcion.set_hora_fin(self.nuevo_fin_inscripcion)
                # Agregamos la inscripcion en las inscripciones en curso
                self.agregar_inscripcion_en_curso(inscripcion)




    def comenzar_nueva_inscripcion(self):

        objeto_atendido = None 

        if self.cola_mantenimiento.get_longitud_cola() != 0:
            objeto_atendido = self.cola_mantenimiento.proximo_en_cola()
            self.manejar_proceso_mantenimiento()
            
            
            

        else:
            if self.cola_alumnos.get_longitud_cola() != 0:
                objeto_atendido = self.cola_alumnos.proximo_en_cola()
                self.ingresar_alumno_a_equipo(objeto_atendido)

        




    def finalizar_inscripcion(self):
        inscripcion_finalizada = self.inscripciones_en_curso.pop(0)

        # Ver si falta agregar algo mas a este metodo
        self.actualizar_estados_equipo_alumno_segun_fin_inscripcion(inscripcion_finalizada)


        # Tomar nuevo alumno de la cola
        self.comenzar_nueva_inscripcion()




                










    def realizar_simulacion(self):
        # Este metodo haria la simulacion a partir del evento que tiene como atributo


        



        if self.evento.tipo == "inicializacion":
            
            # Iniciamos los atributos de la simulacion
            self.inicializar_atributos_simulacion()

            # Inicializamos las metricas
            self.inicializar_metricas()
            

            
            # Primera proxima llegada
            self.generar_proxima_llegada_alumno()
            # Primera proxima llegada de mantenimiento
            self.generar_proxima_llegada_mantenimiento() 


            
            

            

            

            



        elif self.evento.tipo == "llegada_alumno":
            self.generar_proxima_llegada_alumno()

            # Hay que ver que pasa con este metodo
            self.crear_nuevo_alumno()


            # Revisar mas metricas (DESPUES)
            self.actualizar_contador_alumnos_llegados() 
            


        elif self.evento.tipo == "llegada_mantenimiento":
            self.manejar_proceso_mantenimiento()


            # Ver que mas falta aca

        
        elif self.evento.tipo == "fin_inscripcion":
            # Se desocupa un equipo -> si la cola de mantenimiento tiene 1 directametne lo asigna a este equipo
            # No olvidarse de priorizar la cola de la persona de mantenimiento            
            self.finalizar_inscripcion()


            # self.actualizar_metricas()



        elif self.evento.tipo == "fin_regreso_alumno":
            self.crear_nuevo_alumno(es_nuevo=False)



        elif self.evento.tipo == "fin_mantenimiento":
            self.manejar_proceso_mantenimiento()














        # Actualizacion de metricas y no se que mas