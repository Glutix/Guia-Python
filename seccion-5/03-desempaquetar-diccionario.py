"""
    ! El operador **, conocido en Python como el operador de desempaquetado de diccionarios, 
    ! se utiliza para desempaquetar los elementos de un diccionario dentro de otro diccionario. 
    ! Este operador facilita la fusión de dos o más diccionarios en uno solo, combinando todos 
    ! sus pares clave-valor en un nuevo diccionario. Cada diccionario que se desempaqueta con ** 
    ! contribuye con sus elementos al diccionario resultante.
"""

# Definimos dos diccionarios distintos
punto1 = {"a": 1, "b": 2}
punto2 = {"c": 3, "d": 4}

# Utilizamos el operador ** para desempaquetar ambos diccionarios en uno nuevo
users = {**punto1, **punto2}
print(users)
