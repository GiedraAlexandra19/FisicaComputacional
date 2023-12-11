import math

def calcular_centro_de_masa(subparticulas):
    total_masa = sum(subparticula['masa'] for subparticula in subparticulas)
    centro_masa_x = sum(subparticula['masa'] * subparticula['posicion'][0] for subparticula in subparticulas) / total_masa
    centro_masa_y = sum(subparticula['masa'] * subparticula['posicion'][1] for subparticula in subparticulas) / total_masa
    return centro_masa_x, centro_masa_y

def calcular_velocidad(subparticulas):
    velocidad_x = sum(subparticula['masa'] * subparticula['velocidad'][0] for subparticula in subparticulas) / sum(subparticula['masa'] for subparticula in subparticulas)
    velocidad_y = sum(subparticula['masa'] * subparticula['velocidad'][1] for subparticula in subparticulas) / sum(subparticula['masa'] for subparticula in subparticulas)
    return velocidad_x, velocidad_y

def calcular_aceleracion(subparticulas):
    aceleracion_x = sum(subparticula['masa'] * subparticula['aceleracion'][0] for subparticula in subparticulas) / sum(subparticula['masa'] for subparticula in subparticulas)
    aceleracion_y = sum(subparticula['masa'] * subparticula['aceleracion'][1] for subparticula in subparticulas) / sum(subparticula['masa'] for subparticula in subparticulas)
    return aceleracion_x, aceleracion_y

def calcular_momento(subparticulas):
    momento_x = sum(subparticula['masa'] * subparticula['velocidad'][0] for subparticula in subparticulas)
    momento_y = sum(subparticula['masa'] * subparticula['velocidad'][1] for subparticula in subparticulas)
    return momento_x, momento_y

def calcular_fuerza(subparticulas):
    fuerza_x = sum(subparticula['masa'] * subparticula['aceleracion'][0] for subparticula in subparticulas)
    fuerza_y = sum(subparticula['masa'] * subparticula['aceleracion'][1] for subparticula in subparticulas)
    return fuerza_x, fuerza_y

def main():
    subparticulas = []
    num_subparticulas = int(input("Ingrese el número de subpartículas: "))

    for i in range(num_subparticulas):
        masa = float(input(f"Ingrese la masa de la subpartícula {i + 1}: "))
        posicion_x = float(input(f"Ingrese la posición X de la subpartícula {i + 1}: "))
        posicion_y = float(input(f"Ingrese la posición Y de la subpartícula {i + 1}: "))
        velocidad_x = float(input(f"Ingrese la velocidad X de la subpartícula {i + 1}: "))
        velocidad_y = float(input(f"Ingrese la velocidad Y de la subpartícula {i + 1}: "))
        aceleracion_x = float(input(f"Ingrese la aceleración X de la subpartícula {i + 1}: "))
        aceleracion_y = float(input(f"Ingrese la aceleración Y de la subpartícula {i + 1}: "))

        subparticulas.append({
            'masa': masa,
            'posicion': (posicion_x, posicion_y),
            'velocidad': (velocidad_x, velocidad_y),
            'aceleracion': (aceleracion_x, aceleracion_y),
        })

    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular posición del centro de masa.")
        print("2. Calcular velocidad del centro de masa.")
        print("3. Calcular aceleración del centro de masa.")
        print("4. Calcular momento total.")
        print("5. Calcular fuerza total.")
        print("0. Salir.")

        opcion = int(input("Opción: "))

        if opcion == 1:
            centro_masa = calcular_centro_de_masa(subparticulas)
            print(f"\nCentro de Masa: ({centro_masa[0]}, {centro_masa[1]})")

        elif opcion == 2:
            velocidad_centro_masa = calcular_velocidad(subparticulas)
            print(f"\nVelocidad del Centro de Masa: ({velocidad_centro_masa[0]}, {velocidad_centro_masa[1]})")

        elif opcion == 3:
            aceleracion_centro_masa = calcular_aceleracion(subparticulas)
            print(f"\nAceleración del Centro de Masa: ({aceleracion_centro_masa[0]}, {aceleracion_centro_masa[1]})")

        elif opcion == 4:
            momento_total = calcular_momento(subparticulas)
            print(f"\nMomento Total: ({momento_total[0]}, {momento_total[1]})")

        elif opcion == 5:
            fuerza_total = calcular_fuerza(subparticulas)
            print(f"\nFuerza Total: ({fuerza_total[0]}, {fuerza_total[1]})")

        elif opcion == 0:
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()