"""
El ámbito o alcance (SCOPE) de una variable se refiere a la parte del código 
donde esa variable es accesible y puede ser utilizada.


En Python, existen dos tipos principales de ámbitos de variables: global y local.

- Una variable global se define fuera de cualquier función y puede ser accedida desde cualquier parte del código.
- Una variable local se define dentro de una función y solo es accesible dentro de esa función.

Veamos un ejemplo:
"""

# Variable global
nombre = "Mario"


def saludo():
    # Variable local
    nombre = "Juan"
    print(f"Hola, {nombre}")


def saludo1():
    # Variable local
    nombre = "Carlos"
    print(f"Hola, {nombre}")


# Llamamos a las funciones que imprimen los saludos
saludo()  # Imprime: "Hola, Juan"
saludo1()  # Imprime: "Hola, Carlos"

# Imprimimos la variable global fuera de las funciones
print(nombre)  # Imprime: "Mario"
