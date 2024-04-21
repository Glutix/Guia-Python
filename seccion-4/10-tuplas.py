"""
    ! Las tuplas son similares a las listas en muchos aspectos, pero con una diferencia crucial
    ! --> LAS TUPLAS NO PUEDEN SER MODIFICADAS <--
    ! Es decir, las tuplas son inmutables. Esto las hace útiles para crear estructuras de datos 
    ! que no deben ser alteradas después de su creación.

    ? Veamos un ejemplo de las operaciones que se pueden realizar con ellas:
"""

# Concatenar dos tuplas
numeros1 = (1, 2, 3)
numeros2 = (4, 5, 6)
numeros_total = numeros1 + numeros2
print("Tupla concatenada:", numeros_total)
print()

# Crear una tupla a partir de una lista
lista_nombres = ["Juan", "Ale", "Jose", "Mariano"]
tupla_nombres = tuple(lista_nombres)
print("Tupla creada a partir de una lista:", tupla_nombres)
print()

# Acceder a elementos y realizar rebanadas (slicing) en tuplas
print("Acceso a un elemento individual:", tupla_nombres[1])
print()
print("Parte de una tupla:", tupla_nombres[1:])
print()

# Desempaquetar una tupla
primero, segundo, *otros = tupla_nombres
print("Desempaquetado de tupla:", primero, segundo, otros)
print()

# Iterar sobre una tupla
print("Iteración sobre una tupla:")
for nombre in tupla_nombres:
    print(nombre)
print()

# Intentar modificar una tupla arrojará un error, demostrando su inmutabilidad:
try:
    tupla_nombres[0] = "Modificado"
except TypeError as error:
    print("Error:", error)
print()

# TODO: otras operaciones no modificativas que normalmente se harían con listas, como contar e indexar, también son posibles.
print("Número de veces que 'Jose' aparece en la tupla:", tupla_nombres.count("Jose"))
print()
print("Índice de 'Jose' en la tupla:", tupla_nombres.index("Jose"))
