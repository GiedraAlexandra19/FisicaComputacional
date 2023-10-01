#EJERCICIO 1: Escriba un código donde se emplee máquina de Atwood para determinar la 
#magnitud de la aceleración de dos objetos y la tensión en la cuerda sin peso.

"""
# Datos del problema
m1 = float(input("Ingrese la masa del primer objeto (kg): "))
m2 = float(input("Ingrese la masa del segundo objeto (kg): "))
g = 9.81  # Aceleración debida a la gravedad en la Tierra (m/s^2)

# Calcular la aceleración del sistema
a = ((m2 - m1) * g) / (m1 + m2)

# Calcular la tensión en la cuerda
tension = m1 * (g + a)

print(f"Magnitud de la aceleración del sistema: {a:.2f} m/s^2")
print(f"Tensión en la cuerda sin peso: {tension:.2f} N")

"""

#EJERCICIO 2: Un móvil de masa m recorre una distancia d en un tiempo t, al inicio
#tiene una velocidad inicial vi y una velocidad final vf . Escriba un código
#que determine la fuerza que describe el móvil al momento de realizar
#el cambio de velocidad y grafique el proceso.

import matplotlib.pyplot as plt

# Datos del problema
m = float(input("Ingrese la masa del móvil (kg): "))
vi = float(input("Ingrese la velocidad inicial (m/s): "))
vf = float(input("Ingrese la velocidad final (m/s): "))
t = float(input("Ingrese el tiempo (s): "))

# Calcula la aceleración
delta_v = vf - vi
delta_t = t
a = delta_v / delta_t

# Calcula la fuerza
F = m * a

print(f"Fuerza: {F:.2f} N")

# Crea datos para el gráfico de velocidad vs. tiempo
tiempo = [0, t]
velocidad = [vi, vf]

# Grafica 
plt.figure()
plt.plot(tiempo, velocidad, marker='o', linestyle='-', color='b')
plt.title('Gráfico de Velocidad vs. Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid(True)
plt.show()