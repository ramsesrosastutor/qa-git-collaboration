from bienvenida import bienvenida


def operaciones():
    # Solicitar datos del estudiante
    nombre = input("Ingresa tu nombre: ")
    grupo = input("Ingresa tu cohorte o grupo: ")

    # Solicitar los números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Llamar a la función de bienvenida
    bienvenida(nombre, grupo)

    # Agregar los numeros que se agregaron por el usuario
    print(f"Primer Numero: {numero1}")
    print(f"Segundo Numero: {numero2}")

    # Realizar las operaciones matemáticas
    print(f"Suma: {numero1 + numero2:g}")
    print(f"Resta: {numero1 - numero2:g}")
    print(f"Multiplicación: {numero1 * numero2:g}")

    if numero2 != 0:
        print(f"División: {numero1 / numero2:g}")
    else:
        print("División: No es posible dividir entre cero.")


if __name__ == "__main__":
    operaciones()
