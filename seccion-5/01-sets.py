"""
    ! Sets, o conjuntos, son colecciones de elementos que son tanto únicos como no ordenados.
"""

# Creación de un set con elementos repetidos; los duplicados se eliminarán automáticamente
numeros = {1, 1, 2, 2, 3, 3, 4, 4}
print("Set sin duplicados:", numeros)
print()

# Creación de un set a partir de una lista
lista = [9, 8, 7, 6]
conjunto = set(lista)
print("Set creado a partir de una lista:", conjunto)
print()

# Ejemplos de operaciones básicas que se pueden realizar con sets

# Agregar un elemento
conjunto = {"a", "b", "c"}
conjunto.add("d")
print("Set después de agregar 'd':", conjunto)
print()

# Eliminar un elemento
conjunto.remove("c")
print("Set después de eliminar 'c':", conjunto)
print()

# Unión de dos sets (elementos que aparecen en cualquiera de los dos sets)
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
union_conjunto = conjunto1 | conjunto2
print("Unión de dos sets:", union_conjunto)
print()

# Intersección de dos sets (elementos comunes a ambos sets)
interseccion_conjunto = conjunto1 & conjunto2
print("Intersección de dos sets:", interseccion_conjunto)
print()

# Diferencia de sets (elementos en el primer set que no están en el segundo set)
diferencia_conjunto = conjunto1 - conjunto2
print("Diferencia de sets:", diferencia_conjunto)
print()

# Diferencia simétrica de sets (elementos en cualquiera de los sets pero no en ambos)
diferencia_simetrica_conjunto = conjunto1 ^ conjunto2
print("Diferencia simétrica de sets:", diferencia_simetrica_conjunto)
print()

# Desventajas de los sets
# Como los sets no están ordenados, no se puede acceder a sus elementos mediante índices
# Ejemplo de verificación de la existencia de un elemento en un set
nombres = {"Ale", "Seba", "Mario", "Carlos"}
if "Mario" in nombres:
    print("Se encontró a Mario")
else:
    print("No se encontró a Mario")
