import matplotlib.pyplot as plt
import numpy as np

# Definimos las constantes
g = 9.81  # m/s^2
m = 1  # kg

# Definimos las funciones para calcular la energía potencial y cinética
def energia_potencial(h):
  return m * g * h

def energia_cinetica(v):
  return m * v**2 / 2

# Definimos la función para calcular la energía mecánica
def energia_mecanica(h, v):
  return energia_potencial(h) + energia_cinetica(v)

# Definimos los valores de h y v
h = np.linspace(0, 10, 100)
v = np.linspace(0, 10, 100)

# Calculamos la energía potencial, cinética y mecánica
E_p = energia_potencial(h)
E_c = energia_cinetica(v)
E_m = energia_mecanica(h, v)

""" # Impresión de resultados
print("Energía potencial:", E_p)
print("Energía cinética:", E_c)
print("Energía mecánica:", E_m)   """

# Creamos el gráfico
plt.plot(h, E_p, label="Energía potencial")
plt.plot(h, E_c, label="Energía cinética")
plt.plot(h, E_m, label="Energía mecánica")
plt.xlabel("Tiempo (s)")
plt.ylabel("Energía (J)")
plt.legend()
plt.show()  