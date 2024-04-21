# Inicializamos una lista con nombres
nombres = ["Jose", "Juan", "Carlos", "Mariano"]
print("Lista original:\n", nombres)
print("")

# Agregar un elemento al inicio de la lista usando el método insert()
# El primer parámetro es el índice donde se insertará el elemento (0 para el inicio)
# El segundo parámetro es el elemento a insertar
nombres.insert(0, "Sebastian")
print("Después de insertar 'Sebastian' al inicio:\n", nombres)
print("")

# Agregar un elemento al final de la lista usando el método append()
# Este método añade el elemento al final de la lista
nombres.append("Julian")
print("Después de agregar 'Julian' al final:\n", nombres)
print("")

# Eliminar el último elemento de la lista usando el método pop()
# pop() sin argumentos elimina y devuelve el último elemento de la lista
nombres.pop()
print("Después de eliminar el último elemento:\n", nombres)
print("")

# Eliminar la primera ocurrencia de un elemento específico usando el método remove()
# Si el elemento no existe en la lista, Python arrojará un ValueError
nombres.remove("Juan")
print("Después de eliminar 'Juan':\n", nombres)
print("")

# Eliminar un elemento por su índice usando la palabra clave del
# En este ejemplo, eliminamos el primer elemento de la lista
del nombres[0]
print("Después de eliminar el primer elemento por índice:\n", nombres)
print("")

# Limpiar todos los elementos de la lista usando el método clear()
# Esto deja la lista vacía
nombres.clear()
print("Después de limpiar todos los elementos: ", nombres)

# Este ejemplo demuestra cómo modificar una lista añadiendo y eliminando elementos.
# Usamos métodos como insert(), append(), pop(), remove(), y clear() para manipular los elementos de la lista de manera efectiva.
