""" #ECUACION DE CALOR

import numpy as np
import matplotlib.pyplot as plt

def solve_heat_equation(u0, dx, dt, timesteps, r, boundary_conditions):
    # Inicialización de la matriz
    nx = len(u0)
    u = np.zeros((timesteps, nx))

    # Condición inicial
    u[0, :] = u0

    for t in range(1, timesteps):
        for i in range(1, nx-1):
            u[t, i] = (1 - 2*r) * u[t-1, i] + r * (u[t-1, i+1] - 2*u[t-1, i] + u[t-1, i-1])

        # Aplicar condiciones de contorno
        u[t, 0], u[t, -1] = boundary_conditions(t*dt)

    return u

def initial_condition(x):
    return np.sin(np.pi * x)

def boundary_conditions(t):
    return 0, 0  # Condiciones de contorno en los extremos

# Parámetros
L = 1.0         # Longitud del dominio
T = 0.1         # Tiempo total de simulación
nx = 100        # Número de puntos en el dominio espacial
nt = 100        # Número de pasos de tiempo
dx = L / (nx-1)  # Tamaño del paso espacial
dt = T / nt      # Tamaño del paso temporal
r = 0.01         # Número de Courant (debe ser menor o igual a 0.5 para estabilidad)

# Condiciones iniciales y de contorno
x = np.linspace(0, L, nx)
u0 = initial_condition(x)

# Resolver la ecuación de calor
u = solve_heat_equation(u0, dx, dt, nt, r, boundary_conditions)

# Visualización de los resultados
plt.imshow(u, aspect='auto', extent=[0, L, 0, T], cmap='hot', origin='lower', interpolation='none')
plt.colorbar(label='Temperatura')
plt.title('Evolución de la Temperatura en la Barra')
plt.xlabel('Posición')
plt.ylabel('Tiempo')
plt.show()  """


#ECUACION DE ONDA

import numpy as np
import matplotlib.pyplot as plt

def solve_wave_equation(nx, nt, L, T, c, u_initial, u_previous, boundary_conditions):
    # Parámetros
    dx = L / (nx - 1)
    dt = T / nt
    r = c * dt / dx  # Número de Courant

    # Inicialización de la malla
    u = np.zeros((nx, nt + 1))
    u[:, 0] = u_initial
    u[:, 1] = u_previous

    # Aplicar condiciones de contorno iniciales
    u[0, :] = boundary_conditions[0]
    u[-1, :] = boundary_conditions[1]

    # Resolver la ecuación de onda
    for j in range(1, nt):
        for i in range(1, nx - 1):
            u[i, j + 1] = 2 * (1 - r**2) * u[i, j] + r**2 * (u[i + 1, j] + u[i - 1, j]) - u[i, j - 1]

        # Aplicar condiciones de contorno en cada paso de tiempo
        u[0, j + 1] = boundary_conditions[0]
        u[-1, j + 1] = boundary_conditions[1]

    return u

# Parámetros del problema
nx = 50  # Número de puntos en el espacio
nt = 100  # Número de pasos en el tiempo
L = 1.0  # Longitud del dominio
T = 0.1  # Tiempo total
c = 1.0  # Velocidad de la onda

# Condiciones iniciales y de contorno
u_initial = np.sin(np.pi * np.linspace(0, 1, nx))  # Función sinusoidal como condición inicial
u_previous = u_initial - c * T * np.sin(np.pi * np.linspace(0, 1, nx))  # Condiciones iniciales para la derivada en el tiempo
boundary_conditions = (0.0, 0.0)  # Condiciones de contorno en los extremos

# Resolver la ecuación de onda
solution = solve_wave_equation(nx, nt, L, T, c, u_initial, u_previous, boundary_conditions)

# Visualizar la solución
x = np.linspace(0, L, nx)
t = np.linspace(0, T, nt + 1)

X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, solution.T, cmap='viridis')
ax.set_xlabel('Espacio')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Amplitud')
ax.set_title('Solución de la Ecuación de Onda')

plt.show()