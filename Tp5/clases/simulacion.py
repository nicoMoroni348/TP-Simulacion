import random
import math

import gc

import copy

from .printeable import Printeable

from .evento import Evento
from .cola import Cola
from .equipo import Equipo
from .alumno import Alumno
from .inscripcion import Inscripcion
from .persona_mantenimiento import PersonaMantenimiento
from .proceso_mantenimiento import ProcesoMantenimiento


def obtener_valores_atributos(objetos):
    valores_atributos = []
    for obj in objetos:
        for atributo in obj.atributos_permitidos:
            if hasattr(obj, atributo):
                valores_atributos.append(getattr(obj, atributo))
    return valores_atributos















class Simulacion(Printeable):
    # atributos_permitidos = ["id", "reloj",
    #                         "rnd_llegada_alumno", "tiempo_hasta_proxima_llegada", "nueva_llegada_alumno",
    #                         "rnd_1_llegada_mantenimiento", "rnd_2_llegada_mantenimiento",
    #                         "tiempo_hasta_proxima_llegada_mantenimiento", "nueva_llegada_mantenimiento",
    #                         "se_queda", "hora_regreso_de_alumno",
    #                         "rnd_fin_inscripcion", "tiempo_hasta_proximo_fin_inscripcion", "nuevo_fin_inscripcion",
    #                         "rnd_fin_mantenimiento", "tiempo_hasta_proximo_fin_mantenimiento", "nuevo_fin_mantenimiento",
    #                         "contador_alumnos_llegan", "contador_alumnos_se_van_y_regresan_mas_tarde",
    #                         "porcentaje_alumnos_se_van", "contador_alumnos_atendidos",
    #                         "acumulador_tiempos_espera", "promedio_tiempos_espera"
    #                         ]         
    
    use_sine = False

    alumnos_destruidos = 0

    def __init__(self, id, simulacion_anterior, media_llegada_alumnos, demora_inscripcion_a, demora_inscripcion_b, demora_mantenimiento_a, demora_mantenimiento_b, fin_regreso_mantenimiento_media, fin_regreso_mantenimiento_desviacion):
        self.id = id

        self.media_llegada_alumnos = media_llegada_alumnos
        self.demora_inscripcion_a = demora_inscripcion_a
        self.demora_inscripcion_b = demora_inscripcion_b
        self.demora_mantenimiento_a = demora_mantenimiento_a
        self.demora_mantenimiento_b = demora_mantenimiento_b
        self.fin_regreso_mantenimiento_media = fin_regreso_mantenimiento_media
        self.fin_regreso_mantenimiento_desviacion = fin_regreso_mantenimiento_desviacion


        
        if simulacion_anterior is None:
            self.evento = Evento(0.0, "inicializacion")
            # self.inicializar_atributos_simulacion()
            return
        

        self.simulacion_anterior: Simulacion = copy.copy(simulacion_anterior)
        # proximos eventos que se generan en esta fila
        self.proximos_eventos: list = copy.copy(self.simulacion_anterior.proximos_eventos)

        # [print(e.tipo) for e in self.proximos_eventos]
        # print("next")
        # if self.id == 1000:
        #     exit()

        

        self.evento: Evento = copy.copy(self.tomar_evento_a_ocurrir())


        self.reloj = self.evento.hora_ocurrencia

        


        
        # self.cola_alumnos: Cola = copy.copy(self.simulacion_anterior.cola_alumnos)
        self.cola_alumnos: Cola = Cola()
        [self.cola_alumnos.agregar_a_cola(copy.copy(al)) for al in self.simulacion_anterior.cola_alumnos.cola]


        self.cola_mantenimiento: Cola = copy.copy(self.simulacion_anterior.cola_mantenimiento)
        self.cola_mantenimiento: Cola = Cola()
        [self.cola_mantenimiento.agregar_a_cola(copy.copy(mant)) for mant in self.simulacion_anterior.cola_mantenimiento.cola]




        
        
        # if 50 < self.id < 100:
        #    print("viejo", [(al.id, al.estado, al.hora_llegada) for al in self.simulacion_anterior.alumnos_existentes if al is not None])
        
        #self.indice_alumno_a_reemplazar = -1
        # self.alumnos_existentes = copy.copy([al for al in self.simulacion_anterior.alumnos_existentes if al.estado not in ("destruccion")])
        #self.alumnos_existentes = [ None ] * len(self.simulacion_anterior.alumnos_existentes)

        #for i, al in enumerate(self.simulacion_anterior.alumnos_existentes):
        #    if al is None or al.estado in ("destruccion", "siendo_atendido"):
          #      self.alumnos_existentes[i] = None
         #   else:
           #     self.alumnos_existentes[i] = copy.copy(al)

        # Solucion Rami
        # print("viejo", [(al.id, al.estado, al.hora_llegada) for al in self.simulacion_anterior.alumnos_existentes if al is not None])

        self.indice_alumno_a_reemplazar = -1
        self.alumnos_existentes = [ None ] * len(self.simulacion_anterior.alumnos_existentes)

        for i, al in enumerate(self.simulacion_anterior.alumnos_existentes):
            if al is None or al.estado in ("destruccion", "siendo_atendido"):
                self.alumnos_existentes[i] = None

                # Simulacion.alumnos_destruidos += 1
            else:
                self.alumnos_existentes[i] = copy.copy(al)



        # if 50 < self.id < 100:
        #     print("nuevo", [(al.id, al.estado, al.hora_llegada) for al in self.alumnos_existentes if al is not None])
        

                


        
        
            
            
                
        
        # self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes 
        self.alumnos_pendientes_regresar = copy.copy(self.simulacion_anterior.alumnos_pendientes_regresar)

        self.inscripciones_en_curso = [copy.copy(ins) for ins in self.simulacion_anterior.inscripciones_en_curso]

        self.mantenimiento_en_curso = copy.copy(self.simulacion_anterior.mantenimiento_en_curso)


        self.equipos = [copy.copy(eq) for eq in self.simulacion_anterior.equipos]
        self.persona_mantenimiento: PersonaMantenimiento = copy.copy(self.simulacion_anterior.persona_mantenimiento)



        self.se_queda = True
        self.hora_regreso_de_alumno = self.simulacion_anterior.hora_regreso_de_alumno


        # if self.evento.tipo == "fin_mantenimiento":
        #     print(self.reloj, self.cola_alumnos.get_longitud_cola(), self.persona_mantenimiento.maquinas_restantes, self.persona_mantenimiento.estado)

        # if self.evento.tipo in ("fin_inscripcion", "llegada_alumno"):
        

        


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


        # gc.collect()


        





    # Mapear fila simulación
    # def obtener_vector_fila(self):
        
    #     vector_fila = obtener_valores_atributos(
    #         [self.evento, self, self.cola_alumnos, self.cola_mantenimiento, self.persona_mantenimiento]
    #         )
        
        
    #     vector_fila += obtener_valores_atributos(self.equipos)
    #     vector_fila += obtener_valores_atributos([alum for alum in self.alumnos_existentes if alum.estado not in ("destruccion", "siendo_atendido")])


    #     return vector_fila



    # Mapear fila simulación
    def obtener_vector_fila_new(self):   


        vector_fila =  [
            self.id,
            self.evento.tipo,
            self.reloj,
            self.rnd_llegada_alumno,
            self.tiempo_hasta_proxima_llegada,
            self.nueva_llegada_alumno,
            self.rnd_1_llegada_mantenimiento,
            self.rnd_2_llegada_mantenimiento,
            self.tiempo_hasta_proxima_llegada_mantenimiento,
            self.nueva_llegada_mantenimiento,
            self.se_queda,
            self.hora_regreso_de_alumno,
            self.rnd_fin_inscripcion,
            self.tiempo_hasta_proximo_fin_inscripcion,
            self.nuevo_fin_inscripcion,
            self.rnd_fin_mantenimiento,
            self.tiempo_hasta_proximo_fin_mantenimiento,
            self.nuevo_fin_mantenimiento,
            self.contador_alumnos_llegan,
            self.contador_alumnos_se_van_y_regresan_mas_tarde,
            self.porcentaje_alumnos_se_van,
            self.contador_alumnos_atendidos,
            self.acumulador_tiempos_espera,
            self.promedio_tiempos_espera,
            self.cola_alumnos.get_longitud_cola(),
            self.cola_mantenimiento.get_longitud_cola(),
            self.persona_mantenimiento.estado,
            self.persona_mantenimiento.maquinas_restantes,
        ]

    
        for eq in self.equipos:
            eq: Equipo = eq
            vector_fila += [eq.estado, eq.hora_fin_uso]

        
        for al in self.alumnos_existentes:
            al: Alumno = al
            if al is not None:
                vector_fila += [al.id, al.estado, al.hora_llegada, None]
            else:
                vector_fila += [None] * 4

            
            # Simulacion.alumnos_destruidos += 1

# Inicializamos vector_fila con un tamaño suficiente para contener todos los datos de los alumnos
        # vector_fila = [None] * len(self.alumnos_existentes) * 4

        # for i, al in enumerate(self.alumnos_existentes):
        #     al: Alumno = al
        #     if al is not None:
        #         # Actualizamos los datos del alumno en las posiciones correspondientes de vector_fila
        #         vector_fila[i*4:i*4+4] = [al.id, al.estado, al.hora_llegada, None]
        #     else:
        #         # Si el alumno no existe, llenamos las posiciones correspondientes con None
        #         vector_fila[i*4:i*4+4] = [None] * 4

        #     Simulacion.alumnos_destruidos += 1




        return vector_fila

    



        






    def inicializar_atributos_simulacion(self):
        # Inicializamos Los atributos que se "arrastran" por fila

        self.reloj = 0.0



        self.proximos_eventos = []

        self.alumnos_existentes = []
        self.alumnos_pendientes_regresar = []
        self.inscripciones_en_curso = []

        self.mantenimiento_en_curso = None

        self.hora_regreso_de_alumno = None
        self.se_queda = None


        # Creamos los equipos
        # self.equipos = copy.copy(Equipo.crear_equipos())
        self.equipos = [copy.copy(Equipo(i, "libre", None)) for i in range(1, 7)]
        # print(len(self.equipos), self.id, self.evento.tipo)


        # Creamos la persona de mantenimiento
        self.persona_mantenimiento = PersonaMantenimiento(1)


        # Creamos la cola de alumnos
        self.cola_alumnos = Cola()

        
        self.cola_mantenimiento = Cola()


        



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






























    def agregar_proximo_evento(self, proximo_evento: Evento):
        self.proximos_eventos.append(proximo_evento)

        self.proximos_eventos.sort(key=lambda x: x.hora_ocurrencia)

        



    def tomar_evento_a_ocurrir(self):

        return self.proximos_eventos.pop(0)



    def agregar_inscripcion_en_curso(self, inscripcion):
        self.inscripciones_en_curso.append(inscripcion)
        self.inscripciones_en_curso.sort(key=lambda x: x.hora_fin)




    def generar_proxima_llegada_alumno(self):
        # -2*LN(1-E11)
        # Exponencial ()
        # media = 2 min
        media = self.media_llegada_alumnos

        self.rnd_llegada_alumno = random.random()
        self.tiempo_hasta_proxima_llegada = -media * math.log(1-self.rnd_llegada_alumno, math.e)
        self.nueva_llegada_alumno = self.tiempo_hasta_proxima_llegada + self.reloj


        # Agregar el evento a la lista de proximos eventos
        proximo_evento_llegada_alumno = Evento(self.nueva_llegada_alumno, "llegada_alumno")
        self.agregar_proximo_evento(proximo_evento_llegada_alumno)




    def generar_proxima_llegada_mantenimiento(self):
        # (SQRT(-2*LN(1-H11))*COS(2*PI()*I11))*3+60
        # Normal(media; de)
        media = self.fin_regreso_mantenimiento_media
        de = self.fin_regreso_mantenimiento_desviacion

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
        a = self.demora_inscripcion_a
        b = self.demora_inscripcion_b

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
        
        a = self.demora_mantenimiento_a
        b = self.demora_mantenimiento_b
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
        self.contador_alumnos_llegan += 1
    
    def actualizar_contador_alumnos_atendidos(self):
        self.contador_alumnos_atendidos += 1
    
    def actualizar_contador_alumnos_se_van_regresan_mas_tarde(self):

        self.contador_alumnos_se_van_y_regresan_mas_tarde += 1
        self.porcentaje_alumnos_se_van = (self.contador_alumnos_se_van_y_regresan_mas_tarde / self.contador_alumnos_llegan) * 100

    

    def actualizar_tiempo_de_espera(self, alumno_atendido: Alumno):
        self.acumulador_tiempos_espera += alumno_atendido.hora_atencion - alumno_atendido.hora_llegada
        self.promedio_tiempos_espera = self.acumulador_tiempos_espera / self.contador_alumnos_atendidos

    
    def agregar_alumno_existente(self, alumno):
        # self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes + [alumno]
        # self.alumnos_existentes = self.simulacion_anterior.alumnos_existentes[:]
        if None in self.alumnos_existentes:
            indice = self.alumnos_existentes.index(None)
            self.alumnos_existentes[indice] = alumno
        else:
            self.alumnos_existentes += [alumno]




    def crear_nuevo_alumno(self, es_nuevo=True):

        # Si es un alumno que recién entra a la simulación y no es un alumno que regresó:
        if es_nuevo:
            # Si el alumno recién entra a la simulación, crea el objeto
            nuevo_alumno = Alumno(Alumno.get_proximo_id())

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
            # 
            
            # RUNGE KUTTA PAPAAAA ;)
            if self.cola_alumnos.get_longitud_cola() >= calcular_n():
                # El alumno se va y regresa en 30 minutos 
                self.actualizar_contador_alumnos_se_van_regresan_mas_tarde()
                
                # EL alumno de esta iteracion se fue y no espero
                self.se_queda = False

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
        # print(self.alumnos_existentes[-1].estado)

    

    def iniciar_proceso_mantenimiento(self):
        # Este metodo se ejecuta en cada llegada de mantenimiento


    
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

                self.mantenimiento_en_curso = proceso_mantenimiento

                break

        if not hay_equipo_libre:
            # Agregamos el personal de mantenimiento a la cola prioritaria
            self.cola_mantenimiento.agregar_a_cola(self.persona_mantenimiento)

            # Actualizamos su estado a Esperando Atencion
            self.persona_mantenimiento.set_estado('esperando_atencion')




    def actualizar_estados_equipo_mant_segun_proceso_mant(self, proceso_mant_terminado: ProcesoMantenimiento):

        for eq in self.equipos:
            eq: Equipo = eq
            if eq.id == proceso_mant_terminado.equipo.id:

                eq.set_estado("libre")
                proceso_mant_terminado.equipo.set_estado("libre")
        
        self.persona_mantenimiento.set_estado("esperando_atencion")
        proceso_mant_terminado.persona_mantenimiento.set_estado("esperando_atencion")

    


    def finalizar_proceso_mantenimiento(self):
        # Este metodo se ejecuta cada vez que se desocupa un equipo siempre y cuando la cola de mantenimiento no este vacia
        # Y cada vez que termine de mantener un equipo (si quedan equipos pendientes)


        # DONDE termino de Mantener
        proceso_mantenimiento_terminado = self.mantenimiento_en_curso


        self.actualizar_estados_equipo_mant_segun_proceso_mant(proceso_mantenimiento_terminado)


        # Verificar si inicia un mantenimiento o ya termino
        

        # Si terminó el mantenimiento a TODAS las máquinas
        if not self.persona_mantenimiento.maquinas_restantes: 
            # Resetea los equipos restantes en [1, 2, 3, 4, 5, 6]
            self.persona_mantenimiento.resetear_equipos_a_mantener()
            self.persona_mantenimiento.set_estado("desocupado")
            
            # Genera la próxima llegada de la persona de mantenimiento
            self.generar_proxima_llegada_mantenimiento()

            

            return


        self.iniciar_proceso_mantenimiento()
        self.comenzar_nuevo_uso_equipo()


        # if self.cola_alumnos.get_longitud_cola() != 0:
            
            





            
    def actualizar_estados_equipo_alumno_segun_fin_inscripcion(self, inscripcion_finalizada: Inscripcion):
        for eq in self.equipos:
            eq: Equipo = eq
            if eq.id == inscripcion_finalizada.equipo.id:
                # Si hay alguien en la cola, se tiene que quedar en ocupado (ver si cambiar esto)
                eq.set_estado("libre") 
                # eq.set_hora_fin_uso(self.reloj) # Este atributo refiere a cuando se va a Terminar de usar, no cuando se termino de usar
        
        for al in self.alumnos_existentes:
            al: Alumno = al
            if al is not None and al.id == inscripcion_finalizada.alumno.id:
                al.set_estado("destruccion")

                


                
                # al.set_hora_atencion(self.reloj) # Este tendria que haber sido hora de fin inscripcion

                

                

    def actualizar_estado_alumno_segun_inicio_inscripcion(self, alumno: Alumno):
        for al in self.alumnos_existentes:
            al: Alumno = al
            if al is not None and al.id == alumno.id:
                al.set_estado("siendo_atendido")
                al.set_hora_atencion(self.reloj)



    def ingresar_alumno_a_equipo(self, alumno: Alumno):
        for equipo in self.equipos:
            equipo: Equipo = equipo

            if equipo.esta_libre():
                # ACtualizar estado del alumno en la lista de alumnos existentes
                self.actualizar_estado_alumno_segun_inicio_inscripcion(alumno)

                alumno.set_hora_atencion(self.reloj)

                # Actualizamos el tiempo de espera del alumno
                self.actualizar_tiempo_de_espera(alumno)


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


                

                


                break



    def hay_equipos_libres(self):
        for e in self.equipos:
            e: Equipo = e
            if e.estado == "libre":
                return True
        return False

    def hay_equipos_libres_ya_mantenidos(self):
        for e in self.equipos:
            e: Equipo = e
            if e.estado == "libre" and e.id not in self.persona_mantenimiento.maquinas_restantes:
                return True
        return False


    def comenzar_nuevo_uso_equipo(self):

        objeto_atendido = None 

        if self.cola_mantenimiento.get_longitud_cola() != 0 and not self.hay_equipos_libres_ya_mantenidos(): # y que si hay un equipo libre y no está en la lista de equipos restantes del mantenimiento 
            objeto_atendido = self.cola_mantenimiento.proximo_en_cola()

            self.iniciar_proceso_mantenimiento()
        
        else:    # si la cola prioritaria está vacía
            if self.cola_alumnos.get_longitud_cola() != 0:

                objeto_atendido = self.cola_alumnos.proximo_en_cola()
                
                self.ingresar_alumno_a_equipo(objeto_atendido)

                
        # Si no hay nadie en la cola ni de mantenimiento ni de alumnos, no hace nada, queda en libre el estado del equipo

        # Ver si aca seteamos el estado del equipo en libre

        




    def finalizar_inscripcion(self):
        inscripcion_finalizada = self.inscripciones_en_curso.pop(0) 

        # Ver si falta agregar algo mas a este metodo
        self.actualizar_estados_equipo_alumno_segun_fin_inscripcion(inscripcion_finalizada)

        # Actualizar contador de alumnos atendidos
        self.actualizar_contador_alumnos_atendidos()


        # Tomar nuevo alumno de la cola
        self.comenzar_nuevo_uso_equipo()




                










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

            self.actualizar_contador_alumnos_llegados() 
            


        elif self.evento.tipo == "llegada_mantenimiento":
            self.iniciar_proceso_mantenimiento()


            # Ver que mas falta aca

        
        elif self.evento.tipo == "fin_inscripcion":
            # Se desocupa un equipo -> si la cola de mantenimiento tiene 1 directametne lo asigna a este equipo
            # No olvidarse de priorizar la cola de la persona de mantenimiento            
            self.finalizar_inscripcion()

            
            



        elif self.evento.tipo == "fin_regreso_alumno":
            self.crear_nuevo_alumno(es_nuevo=False)



        elif self.evento.tipo == "fin_mantenimiento":
            self.finalizar_proceso_mantenimiento()

        






        # print(f"Al final de sim: {self.cola_alumnos.get_longitud_cola()}")




        # if 5 < self.id < 100:

            # print(self.id, self.evento.tipo, self.reloj, self.rnd_llegada_alumno, self.rnd_fin_inscripcion, self.rnd_1_llegada_mantenimiento, self.rnd_fin_mantenimiento, 
            #     self.cola_alumnos.get_longitud_cola(), self.cola_mantenimiento.get_longitud_cola(), 
            #     [e.estado for e in self.equipos], self.persona_mantenimiento.maquinas_restantes)
            # for al in self.alumnos_existentes:
            #     if al is not None:
            #         print(f"({al.estado, al.hora_llegada})", end="-")
            #     else:
            #         print(None, end="-")
            # print()
            # print([(al.id, al.estado, al.hora_llegada) for al in self.alumnos_existentes if al is not None])




        # Actualizacion de metricas y no se que mas