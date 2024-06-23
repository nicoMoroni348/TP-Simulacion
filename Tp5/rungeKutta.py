import numpy as np
from scipy.integrate import solve_ivp

# Función para calcular el nivel de paciencia P en función del tiempo de traslado
def calculate_patience(t):
    def dp_dt(t, P):  # Derivada parcial
        return 0.4 * P + 5
    
    result = solve_ivp(dp_dt, [0, t], [0], t_eval=[t])
    return result.y[0][-1]

# Función para determinar si un alumno se queda o se va, retorna True or False
def decide_to_stay_or_leave(N, t):
    P = calculate_patience(t)
    N_actual = np.random.randint(1, 7)  # Número actual de alumnos en la cola (aleatorio entre 1 y 6)
    return N_actual <= np.floor(P)

# Función para calcular el porcentaje de alumnos que se van para regresar más tarde
def calculate_percentage_of_students(N, num_simulations=10000):
    num_left = sum(decide_to_stay_or_leave(N, np.random.uniform(0, 1)) for _ in range(num_simulations))
    return (num_left / num_simulations) * 100

# Función para calcular el tiempo promedio de espera de los alumnos
def calculate_average_waiting_time():
    # Implementa aquí la lógica para calcular el tiempo promedio de espera
    # (tiempo de inscripción + tiempo de mantenimiento)
    # ...
    return average_waiting_time

# Ejemplo de uso:
N_max = 3  # Número máximo de alumnos en la cola
percentage_left = calculate_percentage_of_students(N_max)
print(f"Porcentaje de alumnos que se van: {percentage_left:.2f}%")
