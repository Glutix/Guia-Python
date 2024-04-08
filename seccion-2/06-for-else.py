"""
    ! Continuando con el ejemplo anterior, supongamos que deseamos buscar un número
    ! dentro de un rango de números del 0 al 9 y, si lo encontramos, 
    ! informar al usuario que se encontró.
    ! En caso contrario, informar que no se encontró.
"""

buscar = int(input("Ingresar un número entero: "))

for numero in range(10):
    print("Cantidad de veces iteradas: ", numero)
    if numero == buscar:
        print("Se encontró el número: ", buscar)
        break  # break sirve para romper la ejecución del bucle
else:
    print("No se encontró el número ", buscar)
