import math
import os


def sumar():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 + num2
        print(f"La suma entre {num1} y {num2} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


def restar():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 - num2
        print(f"La resta entre {num1} y {num2} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


def multiplicar():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        total = num1 * num2
        print(f"La multiplicación entre {num1} y {num2} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


def dividir():
    try:
        num1 = float(input("Ingresa el dividendo: "))
        num2 = float(input("Ingresa el divisor: "))
        if num2 == 0:
            print("La división por 0 no está definida")
        else:
            total = num1 / num2
            print(f"La división entre {num1} y {num2} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


def potenciacion():
    try:
        num1 = float(input("Ingresa la base: "))
        num2 = float(input("Ingresa el exponente: "))
        total = math.pow(num1, num2)
        print(f"La potencia de {num1} elevado a {num2} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


def raiz_cuadrada():
    try:
        num1 = float(input("Ingresa el radicando: "))
        if num1 < 0:
            print("No existe raíz de un número negativo")
        else:
            total = math.sqrt(num1)
            print(f"La raíz cuadrada de {num1} es igual a {total}")
    except ValueError:
        print("Por favor, ingresa números válidos.")


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
    7) Escriba "salir" o presione 7 para salir
    """
    )

    opcion = input("> ")

    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        multiplicar()
    elif opcion == "4":
        dividir()
    elif opcion == "5":
        potenciacion()
    elif opcion == "6":
        raiz_cuadrada()
    elif opcion.lower() == "salir" or opcion == "7":
        os.system("cls")
        print(
            """
                    ,______    __     __     _____       .___
                    |  _  |    \ \   / /    | ____|      |  |
                    | |_) /     \ \_/ /     | |__        |  |
                    |  _ \       \   /      |  __|       |__|
                    | |_) |       | |       | |___      ._____
                    |____/        |_|       |_____|     |____|
        """
        )
        print("\n\t\t\t\t¡Hasta la próxima!\n\n")
        break
    else:
        print("¡Opción ingresada inválida!")
