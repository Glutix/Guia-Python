"""
    ! Algo importante a tener en cuenta es que un bucle "for" recorre una lista de elementos, 
    ! también llamada iterable. 
    
    ? ¿Qué es un iterable? 
    Un iterable es una secuencia de elementos que se puede recorrer mediante índices. 
    Hasta ahora, hemos conocido dos tipos de iterables: el generado por la función range(numero)
    y los "string". A medida que avancemos, exploraremos otros tipos de iterables.



    ? Continuando con el ejemplo anterior, supongamos que deseamos buscar un número
    ? dentro de una lista de números del 0 al 9 y, si lo encontramos, 
    ? informar al usuario que se encontró.
    ? En caso contrario, informar que no se encontró.
    ? Veámonos en un ejemplo
"""

buscar = int(input("Ingresar un número entero: "))

for numero in range(10):
    print("Cantidad de veces iteradas: ", numero)
    if numero == buscar:
        print("Se encontró el número: ", buscar)
        break  # break sirve para romper la ejecución del bucle
else:
    print("No se encontró el número ", buscar)
