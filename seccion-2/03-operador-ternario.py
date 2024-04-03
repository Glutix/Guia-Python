"""
    ! El operador ternario es una forma corta de escribir condicionales
    ? A continuacion haremos un programa que simplemente verifique e
    ? imprima por consola si una persona es mayor o menor de edad.

    ? Forma larga:
    edad = input("Ingresa tu edad > ")
    edad = int(edad)

    if edad >= 18:
        mensaje = "Es mayor de edad"
    else:
        mensaje = "Es menor de edad"

    print(mensaje)
"""

# Forma corta utilizando operador ternario
edad = input("Ingresa tu edad > ")
edad = int(edad)

# valor1 si se cumple la (condicion) si no se cumple entonces valor2
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
