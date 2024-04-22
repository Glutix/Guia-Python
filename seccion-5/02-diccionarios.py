"""
    ! Los diccionarios en Python son estructuras de datos que almacenan pares de valores en forma de clave-valor.
    ! Son muy utilizados debido a su eficiencia para buscar y manipular datos si conoces la clave.
"""

# Crear un diccionario
diccionario = {"x": 25, "y": 33}
print("Diccionario inicial:", diccionario)
print()

# Acceder a los valores de los diccionarios usando claves
print("Valor de 'x':", diccionario["x"])
print("Valor de 'y':", diccionario["y"])
print()

# Agregar nuevos pares clave-valor al diccionario
diccionario["z"] = 45
print("Diccionario después de agregar 'z':", diccionario)
print()

# Verificar si una clave se encuentra dentro de un diccionario
clave_buscar = "pepe"
if clave_buscar in diccionario:
    print(f"Encontré '{clave_buscar}' en el diccionario.")
else:
    print(f"No se encuentra '{clave_buscar}' en el diccionario.")
print()

# Obtener un valor con un valor por defecto si la clave no existe
valor_por_defecto = diccionario.get("pepe", "Valor por defecto")
print("Valor obtenido con get:", valor_por_defecto)
print()

# Borrar un elemento del diccionario por su clave
del diccionario["z"]
print("Diccionario después de borrar 'z':", diccionario)
print()

# Iterar sobre un diccionario, imprimiendo claves y valores
print("Iteración sobre el diccionario:")
for llave, valor in diccionario.items():
    print(f"Clave: {llave}, Valor: {valor}")
print()

# Otras operaciones útiles con diccionarios:
# Actualizar un diccionario con otro
otro_diccionario = {"a": 1, "b": 2}
diccionario.update(otro_diccionario)
print("Diccionario después de actualizar:", diccionario)
print()

# Limpiar todos los elementos de un diccionario
diccionario.clear()
print("Diccionario después de limpiar:", diccionario)
