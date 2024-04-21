"""
    ! A veces necesitamos "comprimir" una lista, es decir, extraer ciertos elementos de una lista.
    ! Por ejemplo, si tenemos una lista de usuarios donde cada usuario está representado por una
    ! lista que contiene un ID y un nombre, podríamos querer obtener solo los nombres o los IDs.

    ? Veamos cómo hacer esto:
"""

# Lista inicial de usuarios, donde cada usuario es representado por una lista que contiene un ID y un nombre.
usuarios = [[3, "Ale"], [2, "Jose"], [4, "Pedro"], [1, "Carlos"]]

# Extracción de los nombres de los usuarios mediante un bucle for:
nombres_usuarios = []
for usuario in usuarios:
    # Agregamos a la nueva lista todos los nombres de los usuarios, ubicados en la posición 1 de cada sublista.
    nombres_usuarios.append(usuario[1])

print("Nombres de los usuarios:", nombres_usuarios)
print()

# Extracción de los IDs de los usuarios mediante un bucle for:
ids_usuarios = []
for usuario in usuarios:
    # Agregamos a la nueva lista todos los IDs de los usuarios, ubicados en la posición 0 de cada sublista.
    ids_usuarios.append(usuario[0])

print("IDs de los usuarios:", ids_usuarios)
print()

# Utilización de comprensión de listas para obtener los IDs y los nombres de manera más eficiente:
users_id = [usuario[0] for usuario in usuarios]
users_name = [usuario[1] for usuario in usuarios]

print("IDs de los usuarios (con comprensión de listas):", users_id)
print()
print("Nombres de los usuarios (con comprensión de listas):", users_name)
print()

# Filtrado de usuarios con ID mayor a 2 usando comprensión de listas:
usuarios_filtrados = [usuario for usuario in usuarios if usuario[0] > 2]
print("Usuarios con ID mayor a 2:", usuarios_filtrados)
print()

# Obtención de los nombres de los usuarios cuyo ID sea mayor a 2:
nombres_usuarios_filtrados = [usuario[1] for usuario in usuarios if usuario[0] > 2]
print("Nombres de usuarios con ID mayor a 2:", nombres_usuarios_filtrados)
