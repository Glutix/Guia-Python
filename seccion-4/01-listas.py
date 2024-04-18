"""
    Las listas(vector o array) son una estructura de datos que permiten almacenar múltiples valores de manera secuencial y contigua
    Esto significa que puedes guardar diferentes tipos de datos, como números, cadenas de texto, u otros objetos, 
    dentro de una lista y acceder a ellos de manera ordenada utilizando índices. 
    
    ? Por ejemplo:
    
        nombres = ["Juan", "Carlos", "Mario"]
   
    ?   se almacenan los valores de "Juan", "Carlos", "Mario" en secuencia, 
    ?   lo que nos permite acceder a ellos posteriormente mediante sus respectivos índices.

    ? Veamos un ejemplo:
"""

numeros = [1, 2, 3]
nombres = ["Juan", "Carlos", "Mario"]
boleans = [True, False, True]

# podemos concatenar 2 listas
alfanumerico = numeros + nombres

# acceder por indice
print(alfanumerico[0])
print(alfanumerico[1])
print(alfanumerico[2])
print(alfanumerico[3])
print(alfanumerico[4])
print(alfanumerico[5])

# Tambien se puede calcular la longitud de las lista ya que es un iterable
longitud = len(nombres)
print(longitud)
