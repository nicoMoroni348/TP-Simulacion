from flet import App, Page, Button, Input, Table, run
import random
import csv

app = App()

class MainPage(Page):
    def __init__(self):
        super().__init__()
        self.title = "Simulación de Montecarlo"
        self.n_visitas = Input("Número de visitas a simular", type="number")
        self.probabilidad_puerta_abierta = Input("Probabilidad de que la puerta se abra", type="number")
        self.probabilidad_venta_a_sra = Input("Probabilidad de venta a una señora", type="number")
        self.probabilidad_venta_a_sr = Input("Probabilidad de venta a un señor", type="number")
        self.utilidad_por_suscripcion = Input("Utilidad por suscripción", type="number")
        self.distribucion_suscripciones_sra = Input("Distribución de suscripciones para señoras (separadas por espacios)", type="text")
        self.distribucion_suscripciones_sr = Input("Distribución de suscripciones para señores (separadas por espacios)", type="text")
        self.run_button = Button("Ejecutar simulación", self.run_simulation)
        self.table = Table(["Visita", "Utilidad de la visita", "Utilidad total hasta ahora"])
        self.add(self.n_visitas, self.probabilidad_puerta_abierta, self.probabilidad_venta_a_sra, self.probabilidad_venta_a_sr, self.utilidad_por_suscripcion, self.distribucion_suscripciones_sra, self.distribucion_suscripciones_sr, self.run_button, self.table)

    def run_simulation(self):
        n_visitas = int(self.n_visitas.value)
        probabilidad_puerta_abierta = float(self.probabilidad_puerta_abierta.value)
        probabilidad_venta_a_sra = float(self.probabilidad_venta_a_sra.value)
        probabilidad_venta_a_sr = float(self.probabilidad_venta_a_sr.value)
        utilidad_por_suscripcion = float(self.utilidad_por_suscripcion.value)
        distribucion_suscripciones_sra = list(map(float, self.distribucion_suscripciones_sra.value.split()))
        distribucion_suscripciones_sr = list(map(float, self.distribucion_suscripciones_sr.value.split()))

        total_utilidad = 0
        total_ventas = 0
        historial = []

        for visita in range(n_visitas):
            utilidad_visita = 0
            if random.random() < probabilidad_puerta_abierta:
                if random.random() < 0.8:  # Si es una señora
                    if random.random() < probabilidad_venta_a_sra:
                        suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3], distribucion_suscripciones_sra)
                        utilidad_visita = suscripciones * utilidad_por_suscripcion
                        total_ventas += 1
                else:  # Si es un señor
                    if random.random() < probabilidad_venta_a_sr:
                        suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3, 4], distribucion_suscripciones_sr)
                        utilidad_visita = suscripciones * utilidad_por_suscripcion
                        total_ventas += 1
            total_utilidad += utilidad_visita
            historial.append((visita, utilidad_visita, total_utilidad))

        self.table.data = historial

app.add_page("/", MainPage())
run(app)
