"""
    ? Recordemos que tanto los strings como las listas son tipos de datos iterables en Python.
    ? Esto significa que podemos acceder a sus elementos uno por uno, modificarlos (en el caso de las listas),
    ? y realizar operaciones como el slicing (subdivisión).
"""

# Ejemplo con una lista de nombres:
nombres = ["Juan", "Pedro", "Mariano", "Lucas"]

# Mostramos la lista completa:
print("Lista original de nombres:", nombres)

# Accediendo a elementos individuales:
print("Primer nombre:", nombres[0])  # 'Juan'
print("Segundo nombre:", nombres[1])  # 'Pedro'

# Aquí reemplazamos el valor "Juan" por "Alejandro"
nombres[0] = "Alejandro"
print("Lista modificada:", nombres)

# Usando slicing para obtener una sublista:
print("Primeros dos nombres:", nombres[0:2])  # ['Alejandro', 'Pedro']

# Obteniendo la longitud de la lista:
print("Número de nombres en la lista:", len(nombres))

# Accediendo al último elemento usando índices negativos:
print("Último elemento de la lista:", nombres[-1])  # Muestra 'Lucas'

# Accediendo al antepenúltimo elemento también con índices negativos:
print("Antepenúltimo elemento de la lista:", nombres[-2])  # Muestra 'Mariano'

# Este ejemplo muestra cómo operar con listas de manera similar a cómo se operaría con strings en términos de acceso y modificación de elementos.
# Sin embargo, a diferencia de los strings, las listas son mutables, lo que significa que podemos cambiar sus elementos sin necesidad de crear una nueva lista.
