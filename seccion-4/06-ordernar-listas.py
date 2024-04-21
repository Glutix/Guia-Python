"""
    ? En muchos contextos, es útil ordenar los elementos de una lista para tener un mejor control
    ? o presentación de los datos. A continuación, se muestra cómo ordenar listas en Python tanto
    ? de manera destructiva (modificando la lista original) como no destructiva (creando una nueva lista ordenada).
"""

# Listas iniciales
numeros = [4, 6, 5, 1, 3, 2]
nombres = ["ABCD", "abcd", "boom", "clash", "zoom"]

# Ordenar listas de forma ascendente y mostrar los resultados
numeros.sort()
nombres.sort()
print("Números ordenados de forma ascendente:", numeros)
print("Nombres ordenados de forma ascendente:", nombres)
print("")

# Ordenar listas de forma descendente y mostrar los resultados
numeros.sort(reverse=True)
nombres.sort(reverse=True)
print("Números ordenados de forma descendente:", numeros)
print("Nombres ordenados de forma descendente:", nombres)
print("")

"""
    ? Si prefieres ordenar una lista sin modificar la original, puedes usar la función 'sorted()'.
    ? Esta función devuelve una nueva lista ordenada, dejando intacta la lista original.
"""

# Crear nuevas listas ordenadas con sorted
nueva_lista_asc = sorted(nombres)  # Orden ascendente
nueva_lista_desc = sorted(nombres, reverse=True)  # Orden descendente

print("Lista original no modificada:", nombres)
print("")
print("Nueva lista ordenada en forma ascendente con 'sorted':", nueva_lista_asc)
print("Nueva lista ordenada en forma descendente con 'sorted':", nueva_lista_desc)
