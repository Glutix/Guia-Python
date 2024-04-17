"""
Como mencionamos anteriormente, una función puede o no devolver un valor.

En algunos casos sería útil que una función devuelva un valor.

¿De qué dependerá esto?

Esto dependerá de cómo esté definida la función y su finalidad.
Por ejemplo:

def saludar():
    print("Hola mundo")

Esta función no devuelve nada, solo imprime el mensaje "Hola mundo" por consola.
Pero en cambio, podríamos necesitar otro tipo de función que sí devuelva algo.

Veamos un ejemplo...
"""

nombre = input("Ingresa tu nombre: ")
fecha_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = 2024


def obtener_edad(fecha_nacimiento):
    edad = anio_actual - fecha_nacimiento
    return edad


def saludo(nombre, fecha_nacimiento):
    edad = obtener_edad(fecha_nacimiento)
    print(f"Hola {nombre}, tu edad es {edad}")


saludo(nombre, fecha_nacimiento)
