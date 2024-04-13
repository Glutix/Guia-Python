"""
    ? Características a añadir:
        ? - ✅ Permitir al usuario elegir la operación a realizar.
        ? - ✅ No permitir la división por 0.
        ? - ✅ No permitir calcular raíces de números negativos.
        ? - ✅ No terminar la ejecución del programa hasta que el usuario lo decida.

    💡PISTA: Podemos usar un bucle que controle esta condición para mejorar 
    la experiencia del usuario.

    TODO: En esta aplicación NO se contemplarán los siguientes casos excepcionales:
        ! - ❌ Validación de errores.
        ! - ❌ Manejo de errores.
"""

import math

print("-------> Calculadora Intermedia <-------")

while True:
    print(
        """
    A continuación, ingresa una operación a realizar:

    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Potenciación
    6) Raíz Cuadrada
    7) Salir
    """
    )

    opcion = input("> ")

    if opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 + num2
        print(f"La suma entre {num1} y {num2} es igual a {total}")
    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 - num2
        print(f"La resta entre {num1} y {num2} es igual a {total}")
    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 * num2
        print(f"La multiplicación entre {num1} y {num2} es igual a {total}")
    elif opcion == "4":
        num1 = float(input("Ingresa el dividendo: "))
        num2 = float(input("Ingresa el divisor: "))
        if num2 == 0:
            print("La división por 0 no está definida")
        else:
            total = num1 / num2
            print(f"La división entre {num1} y {num2} es igual a {total}")
    elif opcion == "5":
        num1 = float(input("Ingresa la base: "))
        num2 = float(input("Ingresa el exponente: "))
        total = math.pow(num1, num2)
        print(f"La potencia de {num1} elevado a {num2} es igual a {total}")
    elif opcion == "6":
        num1 = float(input("Ingresa el radicando: "))
        if num1 < 0:
            print("No existe raíz de un número negativo")
        else:
            total = math.sqrt(num1)
            print(f"La raíz cuadrada de {num1} es igual a {total}")
    elif opcion.lower() == "salir" or opcion == "7":
        print("¡Hasta la próxima!")
        break
    else:
        print("¡Opción ingresada inválida!")
