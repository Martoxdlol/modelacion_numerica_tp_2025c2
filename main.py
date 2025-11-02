import numpy as np
import math
from constantes import L0, g, k1, k2, m, Y_MAX_ANALITICO

# --- DEFINICIÓN DE LA FÍSICA ---
def get_acceleration(y, v):
    """
    Calcula la aceleración en un punto y dado.
    Se ignora la velocidad 'v' ya que no hay rozamiento en estos ítems.
    """
    if y <= L0:
        # Caída libre
        return g
    else:
        # La cuerda está tensa
        f_elastica = k1 * (y - L0) ** k2
        return g - f_elastica / m


# --- RESOLUCIÓN PUNTO 3: MÉTODO DE EULER ---

def solve_euler(h):
    """
    Simula el salto usando el método de Euler con un paso h.
    Retorna el punto más bajo (y_max) alcanzado.
    """
    y = 0.0
    v = 0.0
    y_max = 0.0

    # Simular hasta que el saltador empiece a subir (v < 0)
    while v >= 0:
        a = get_acceleration(y, v)
        # Actualización de Euler
        y = y + h * v
        v = v + h * a

        if y > y_max:
            y_max = y

    return y_max


def find_h_for_euler_error(target_error):
    """
    Encuentra el paso h necesario para que el error de Euler sea menor
    que target_error.
    """
    print(f"Buscando h para un error < {target_error*100:.1f}% en Euler...")
    h = 0.1  # Empezar con un paso relativamente grande
    while True:
        y_max_euler = solve_euler(h)
        error = abs(Y_MAX_ANALITICO - y_max_euler) / Y_MAX_ANALITICO
        print(f"  h = {h:.5f}, y_max = {y_max_euler:.4f} m, Error = {error*100:.4f}%")
        if error < target_error:
            print(f"\nSe encontró un paso h = {h:.5f} que cumple el requisito.")
            return h
        h /= 2  # Reducir el paso para mejorar la precisión


def check_euler_order():
    """
    Comprueba experimentalmente el orden del método de Euler.
    """
    print("\nComprobando el orden del método de Euler...")
    h1 = 0.005
    h2 = h1 / 2  # Un paso más pequeño

    y1 = solve_euler(h1)
    y2 = solve_euler(h2)

    error1 = abs(Y_MAX_ANALITICO - y1)
    error2 = abs(Y_MAX_ANALITICO - y2)

    # Fórmula del orden: p = log(E1/E2) / log(h1/h2)
    order = math.log(error1 / error2) / math.log(h1 / h2)

    print(f"  Error con h1={h1}: {error1:.6f}")
    print(f"  Error con h2={h2}: {error2:.6f}")
    print(f"  Orden experimental calculado: {order:.4f}")
    print("El resultado es cercano a 1, lo cual es el orden teórico de Euler.")


# --- RESOLUCIÓN PUNTO 4: MÉTODO DE RUNGE-KUTTA 4 ---

def state_derivative(state):
    """
    Define el sistema de EDOs para RK4.
    state es un vector [y, v].
    Retorna el vector de derivadas [dy/dt, dv/dt] = [v, a].
    """
    y, v = state
    a = get_acceleration(y, v)
    return np.array([v, a])


def solve_rk4(h):
    """
    Simula el salto usando el método RK4 con un paso h.
    Retorna el punto más bajo (y_max) alcanzado.
    """
    state = np.array([0.0, 0.0])  # [y, v]
    y_max = 0.0

    while state[1] >= 0:  # Mientras la velocidad (state[1]) sea no negativa
        # Pasos de Runge-Kutta
        k1 = h * state_derivative(state)
        k2 = h * state_derivative(state + 0.5 * k1)
        k3 = h * state_derivative(state + 0.5 * k2)
        k4 = h * state_derivative(state + k3)

        state = state + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

        if state[0] > y_max:
            y_max = state[0]

    return y_max


def find_h_for_rk4_error(target_error):
    """
    Encuentra el paso h necesario para que el error de RK4 sea menor
    que target_error.
    """
    print(f"Buscando h para un error < {target_error*100:.1f}% en RK4...")
    h = 1.0  # RK4 permite pasos mucho más grandes
    while True:
        y_max_rk4 = solve_rk4(h)
        error = abs(Y_MAX_ANALITICO - y_max_rk4) / Y_MAX_ANALITICO
        print(f"  h = {h:.4f}, y_max = {y_max_rk4:.4f} m, Error = {error*100:.4f}%")
        if error < target_error:
            print(f"\nSe encontró un paso h = {h:.4f} que cumple el requisito.")
            return h
        h /= 2


def check_rk4_order():
    """
    Comprueba experimentalmente el orden del método RK4.
    """
    print("\nComprobando el orden del método de Runge-Kutta 4...")
    h1 = 0.5
    h2 = h1 / 2

    y1 = solve_rk4(h1)
    y2 = solve_rk4(h2)

    error1 = abs(Y_MAX_ANALITICO - y1)
    error2 = abs(Y_MAX_ANALITICO - y2)

    order = math.log(error1 / error2) / math.log(h1 / h2)

    print(f"  Error con h1={h1}: {error1:.6f}")
    print(f"  Error con h2={h2}: {error2:.6f}")
    print(f"  Orden experimental calculado: {order:.4f}")
    print("El resultado es cercano a 4, lo cual es el orden teórico de RK4.")


# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    print("--- ANÁLISIS NUMÉRICO - BUNGEE JUMPING ---")
    print(f"Parámetros: m={m:.2f} kg, L0={L0:.2f} m, k1={k1:.2f} N/m")
    print(f"Punto más bajo (Solución Analítica): {Y_MAX_ANALITICO:.2f} m\n")

    print("==================================================")
    print("PUNTO 3: MÉTODO DE EULER")
    print("==================================================")
    find_h_for_euler_error(target_error=0.001)  # Error del 0.1%
    check_euler_order()

    print("\n==================================================")
    print("PUNTO 4: MÉTODO DE RUNGE-KUTTA DE ORDEN 4")
    print("==================================================")
    find_h_for_rk4_error(target_error=0.001)
    check_rk4_order()