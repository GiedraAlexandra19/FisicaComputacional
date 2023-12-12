from sympy import symbols, Eq, solve

# Definir símbolos
F, m, a = symbols('F m a')

# Ecuación de la tercera Ley de Newton: F = m * a
ecuacion_tercera_ley = Eq(F, m * a)

# Resolver la ecuación para 'a' (aceleración)
aceleracion = solve(ecuacion_tercera_ley, a)[0]

# Imprimir el resultado
print(f"La aceleración (a) es: {aceleracion}")

def calcular_fuerza(masa, aceleracion):
    fuerza = masa * aceleracion
    return fuerza

# Solicitar la entrada del usuario para la masa y la aceleración
masa = float(input("Ingrese la masa (kg): "))
aceleracion = float(input("Ingrese la aceleración (m/s^2): "))

# Calcular la fuerza utilizando la tercera Ley de Newton
fuerza_resultante = calcular_fuerza(masa, aceleracion)

# Mostrar el resultado
print(f"La fuerza resultante es: {fuerza_resultante} Newtons.")