"""
    ! Los comparadores lógicos son muy utilizados en programación.
    ! Permiten hacer comparaciones lógicas para poder tomar decisiones 
    ! dentro del programa, ya lo veremos más adelante.
    

    ? Ejemplo
    print(1 > 2)  --> 1 es mayor que 2 = ❌Falso
    print(1 < 2)  --> 1 es menor que 2 = ✅Verdadero
    print(1 >= 2) --> 1 es mayor o igual que 2 = ❌Falso
    print(1 <= 2) --> 1 es menor o igual que 2 = ✅Verdadero
    print("2" == 2) --> 2(str) es igual que 2(int) = ❌Falso
    print("Hola" != "hola") --> "Hola" es distinto que "hola" = ✅Verdadero

    ? NOTA: Nótese que el símbolo de comparación es "=="
    ? NO CONFUNDIR CON EL SIGNO DE ASIGNACIÓN "=".

    ? En el último ejemplo "Hola" != "hola" esto es verdadero
    ? porque no son exactamente la misma cadena de caracteres.
"""

# Ejecute el siguiente código para comprobar
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print("2" == 2)
print("Hola" != "hola")


print("\nCasos especiales.\n")

print("El número 1 es igual True")
print(1 == True)


print("El número 0 es igual False")
print(0 == False)

print("El número 0.0 es igual False")
print(0.0 == False)
