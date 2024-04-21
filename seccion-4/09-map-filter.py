"""
    ! Si bien la forma más recomendable para obtener ciertos elementos de una lista o filtrar 
    ! elementos es utilizar la comprensión de listas, en ocasiones algunos desarrolladores 
    ! prefieren usar los métodos 'map' y 'filter'
    ! Estos métodos hacen lo mismo que vimos en el capítulo anterior, 
    ! pero están más orientados a la programación funcional.

    ? Veamos algunos ejemplos:
"""

# Lista inicial de usuarios, donde cada usuario es representado por una lista que contiene un ID y un nombre.
usuarios = [[3, "Ale"], [2, "Jose"], [4, "Pedro"], [1, "Carlos"]]

# Utilización de `map` para obtener los nombres de los usuarios.
# `map` aplica una función a cada elemento de la lista.
nombres_usuarios = list(map(lambda usuario: usuario[1], usuarios))
print("Nombres de los usuarios obtenidos con `map`:", nombres_usuarios)
print()

# Utilización de `filter` para filtrar los usuarios con ID mayor a 2.
# `filter` aplica una función que retorna un booleano para decidir si incluir o no el elemento en la lista resultante.
usuarios_filtrados = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print("Usuarios filtrados con ID mayor a 2 usando `filter`:", usuarios_filtrados)
print()

# Aplicación conjunta de `map` y `filter` para obtener los nombres de los usuarios con ID mayor a 2.
nombres_usuarios_filtrados = list(
    map(lambda usuario: usuario[1], filter(lambda usuario: usuario[0] > 2, usuarios))
)
print(
    "Nombres de usuarios con ID mayor a 2, obtenidos con `map` y `filter`:",
    nombres_usuarios_filtrados,
)
print()

# Alternativa con paso intermedio para el mismo objetivo.
# Primero filtramos los usuarios con ID mayor a 2 y luego mapeamos para obtener los nombres.
usuarios_filtrados_intermedio = list(filter(lambda usuario: usuario[0] > 2, usuarios))
nombres_de_usuarios_filtrados_intermedio = list(
    map(lambda usuario: usuario[1], usuarios_filtrados_intermedio)
)
print(
    "Nombres de usuarios filtrados con ID mayor a 2 (método con paso intermedio):",
    nombres_de_usuarios_filtrados_intermedio,
)
