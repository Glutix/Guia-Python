# String normales
bienvenido = "Bievenidos al"
nombre_curso = "Curso de Python"

# String largos (con saltos de linea)
descripcion = """
Este curso contempla todos los detalles
que necesitas aprender para dominar Python
"""

print(f"{bienvenido} {nombre_curso}.")
print(f"Descripcion del curso: {descripcion}")

# metodos basicos de strings
# longitud de una cadena
longitud = len(descripcion)
print("Cantidad de caracteres:", longitud)

# acceder a un caracter de un string
caracter = nombre_curso[0]
print("Caracter seleccionado: ", caracter)

# recortar cadenas (substring) -> indice : final
# desde 0 hasta el 8
print(nombre_curso[0:8])
print(nombre_curso[:8])

# desde el 9 hasta el final de la cadena
print(nombre_curso[9:])

# valores por defecto inicio 0, final len(string-1)
print(nombre_curso[:])
