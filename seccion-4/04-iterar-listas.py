"""
    ! Es común necesitar recorrer una lista para mostrar cada uno de sus elementos o realizar 
    ! algún tipo de operación con ellos. La iteración sobre listas es una de las operaciones 
    ! más fundamentales en programación Python.

    ? Veamos un ejemplo práctico:
"""

# Definimos una lista de números
numeros = [1, 2, 3, 4, 5]

# Iterar sobre la lista para mostrar cada número
print("Mostrando cada número de la lista:")
for numero in numeros:
    print(numero)

# Supongamos que queremos realizar una operación con cada elemento, como por ejemplo, duplicar su valor
print("Duplicando los valores de cada número en la lista:")
for numero in numeros:
    duplicado = numero * 2
    print(duplicado)

"""
Este ejemplo muestra dos formas básicas de iterar sobre los elementos de una lista:
1. Mostrando cada elemento: simplemente recorremos la lista con un bucle 'for' y usamos 'print' para mostrar cada elemento.
2. Realizando una operación: en este caso, duplicamos cada elemento de la lista y mostramos el resultado.

Iterar sobre una lista es una técnica esencial que permite manipular y aprovechar sus datos de manera efectiva.
"""
