"""
    ! Las expresiones lambda en Python son una forma de crear funciones anónimas, es decir, 
    ! funciones sin nombre. Se utilizan comúnmente cuando se necesita una función simple 
    ! por un corto período de tiempo y no se desea definirla formalmente con la palabra clave `def`. 
    ! Las lambdas son útiles, especialmente en contextos donde se requieren funciones como argumentos.

    ? Si bien podríamos utilizar una expresión lambda para construir una función sencilla, 
    ? como por ejemplo:

    * suma = lambda x, y: x + y
    * print(suma(2, 2))

    ? Esto se considera una mala práctica según PEP 8 cuando se puede usar una función con nombre.

    ? Las expresiones lambda son más útiles en otros tipos de contexto,
    ? como por ejemplo para argumentos de funciones que esperan una función. 
    ? Aquí te muestro cómo utilizar una expresión lambda para ordenar una lista de usuarios por nombre:
"""

# Lista inicial de usuarios, donde cada usuario es representado por una lista que contiene un ID y un nombre.
usuarios = [[3, "Ale"], [2, "Jose"], [4, "Pedro"], [1, "Carlos"]]

# Ordenar por ID de forma ascendente
usuarios.sort()
print("Usuarios ordenados por ID:", usuarios)
print("")


# Utilizar una función definida para ordenar los usuarios por nombre de forma alfabética:
def ordenar_por_nombre(elemento):
    return elemento[1]


usuarios.sort(key=ordenar_por_nombre)
print("Usuarios ordenados por nombre con función definida:", usuarios)
print("")

# Utilizar una expresión lambda para lograr lo mismo de manera más concisa:
usuarios.sort(key=lambda elemento: elemento[1])
print("Usuarios ordenados por nombre con expresión lambda:", usuarios)
