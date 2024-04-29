
import random
import csv

def acumular_probabilidades(probabilidades):
    acumulados = [probabilidades[0]]
    for i in range(1, len(probabilidades)):
        acumulados.append(probabilidades[i] + acumulados[i-1])
    return acumulados

def clasificar_numero_aleatorio(rnd, clases, probabilidad_x_clase):
    vector_probabilidades_acumuladas = acumular_probabilidades(probabilidad_x_clase)
    for i, prob in enumerate(vector_probabilidades_acumuladas):
        if rnd < prob:
            return clases[i]

def simulacion_montecarlo(n_visitas, probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion, distribucion_suscripciones_sra, distribucion_suscripciones_sr, random_values=None):
    total_utilidad = 0
    total_ventas = 0
    historial = []

    for visita in range(n_visitas):
        utilidad_visita = 0
        rnd_puerta, rnd_persona, rnd_venta_sra, rnd_venta_sr = random_values[visita] if random_values else [random.random(), random.random(), random.random(), random.random()]

        if rnd_puerta < probabilidad_puerta_abierta:
            if rnd_persona < 0.8:  # Si es una señora
                if rnd_venta_sra < probabilidad_venta_a_sra:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3], distribucion_suscripciones_sra)
                    utilidad_visita = suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
            else:  # Si es un señor
                if rnd_venta_sr < probabilidad_venta_a_sr:
                    suscripciones = clasificar_numero_aleatorio(random.random(), [1, 2, 3, 4], distribucion_suscripciones_sr)
                    utilidad_visita = suscripciones * utilidad_por_suscripcion
                    total_ventas += 1
        total_utilidad += utilidad_visita
        historial.append((visita, utilidad_visita, total_utilidad))

    return total_utilidad, total_ventas, historial

def mostrar_iteraciones(historial, j, i):
    for visita, utilidad_visita, total_utilidad in historial[j:j+i]:
        print(f"Visita {visita}: Utilidad de la visita = ${utilidad_visita}, Utilidad total hasta ahora = ${total_utilidad}")

def main():
    semilla = int(input("Ingrese una semilla para el generador de números aleatorios: "))
    random.seed(semilla)

    n_visitas = int(input("Ingrese el número de visitas a simular: "))
    probabilidad_puerta_abierta = float(input("Ingrese la probabilidad de que la puerta se abra: "))
    probabilidad_venta_a_sra = float(input("Ingrese la probabilidad de venta a una señora: "))
    probabilidad_venta_a_sr = float(input("Ingrese la probabilidad de venta a un señor: "))
    utilidad_por_suscripcion = float(input("Ingrese la utilidad por suscripción: "))
    distribucion_suscripciones_sra = list(map(float, input("Ingrese la distribución de suscripciones para señoras (separadas por espacios): ").split()))
    distribucion_suscripciones_sr = list(map(float, input("Ingrese la distribución de suscripciones para señores (separadas por espacios): ").split()))

    random_values = []
    for _ in range(n_visitas):
        random_values.append([random.random(), random.random(), random.random(), random.random()])

    with open('random_values.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(random_values)

    total_utilidad, total_ventas, historial = simulacion_montecarlo(n_visitas, probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion, distribucion_suscripciones_sra, distribucion_suscripciones_sr, random_values)
    print(f"Después de {n_visitas} visitas, el vendedor vendió {total_ventas} suscripciones y ganó ${total_utilidad}.")

    j = int(input("Ingrese la iteración inicial j: "))
    i = int(input("Ingrese el número de iteraciones a mostrar i: "))
    mostrar_iteraciones(historial, j, i)

    while True:
        print("\n¿Desea cambiar algún parámetro?")
        print("1. Número de visitas")
        print("2. Probabilidad de que la puerta se abra")
        print("3. Probabilidad de venta a una señora")
        print("4. Probabilidad de venta a un señor")
        print("5. Utilidad por suscripción")
        print("6. Distribución de suscripciones para señoras")
        print("7. Distribución de suscripciones para señores")
        print("8. Salir")
        opcion = int(input("Ingrese el número de la opción que desea cambiar: "))

        if opcion == 1:
            n_visitas = int(input("Ingrese el nuevo número de visitas a simular: "))
        elif opcion == 2:
            probabilidad_puerta_abierta = float(input("Ingrese la nueva probabilidad de que la puerta se abra: "))
        elif opcion == 3:
            probabilidad_venta_a_sra = float(input("Ingrese la nueva probabilidad de venta a una señora: "))
        elif opcion == 4:
            probabilidad_venta_a_sr = float(input("Ingrese la nueva probabilidad de venta a un señor: "))
        elif opcion == 5:
            utilidad_por_suscripcion = float(input("Ingrese la nueva utilidad por suscripción: "))
        elif opcion == 6:
            distribucion_suscripciones_sra = list(map(float, input("Ingrese la nueva distribución de suscripciones para señoras (separadas por espacios): ").split()))
        elif opcion == 7:
            distribucion_suscripciones_sr = list(map(float, input("Ingrese la nueva distribución de suscripciones para señores (separadas por espacios): ").split()))
        elif opcion == 8:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        print("\n¿Desea usar los mismos datos aleatorios o generar nuevos?")
        print("1. Usar los mismos datos aleatorios")
        print("2. Generar nuevos datos aleatorios")
        opcion = int(input("Ingrese el número de la opción que desea elegir: "))

        if opcion == 1:
            with open('random_values.csv', 'r') as file:
                reader = csv.reader(file)
                random_values = list(map(float, row) for row in reader)
        elif opcion == 2:
            random_values = []
            for _ in range(n_visitas):
                random_values.append([random.random(), random.random(), random.random(), random.random()])
            with open('random_values.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(random_values)
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        total_utilidad, total_ventas, historial = simulacion_montecarlo(n_visitas, probabilidad_puerta_abierta, probabilidad_venta_a_sra, probabilidad_venta_a_sr, utilidad_por_suscripcion, distribucion_suscripciones_sra, distribucion_suscripciones_sr, random_values)
        print(f"\nDespués de {n_visitas} visitas, el vendedor vendió {total_ventas} suscripciones y ganó ${total_utilidad}.")

        j = int(input("\nIngrese la iteración inicial j: "))
        i = int(input("Ingrese el número de iteraciones a mostrar i: "))
        mostrar_iteraciones(historial, j, i)

if __name__ == "__main__":
    main()


"""
probabilidad_puerta_abierta = 0.7
probabilidad_venta_a_sra = 0.15



def acumular_probabilidades(probabilidades):
    acumulados = [probabilidades[0]]
    for i in range(1, len(probabilidades)):
        acumulados.append(probabilidades[i] + acumulados[i-1])

    return acumulados


def clasificar_numero_aleatorio(rnd, clases, probabilidad_x_clase):
    vector_probabilidades_acumuladas = acumular_probabilidades(probabilidad_x_clase)
    
    for i, prob in enumerate(vector_probabilidades_acumuladas):
        if rnd < prob:
            return clases[i]
        

clases = ["amigo1", "amigo2", "amigo3"]
prb = [0.5, 0.3, 0.2]

print(clasificar_numero_aleatorio(0.79999, clases, prb))
"""