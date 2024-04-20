"""
    ! El desempaquetamiento de listas es una herramienta útil para asignar los elementos 
    ! de una lista a variables individuales de manera directa.
    ! Si bien podríamos acceder a los elementos de la lista uno por uno de la siguiente manera:

    * numeros = [1, 2, 3, 4, 5, 6]
    * primero = numeros[0]
    * segundo = numeros[1]
    * tercero = numeros[2]

    ? Existe una forma más sencilla y elegante de hacerlo usando el desempaquetamiento:
"""

# Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Desempaquetamos los primeros tres elementos en variables
primero, segundo, tercero = numeros

print("Primeros tres números:", primero, segundo, tercero)

# En otro caso, podemos desempaquetar algunos elementos y el resto agruparlos en una lista separada
# Esto es útil para manejar dinámicamente partes de la lista

primero, segundo, *resto_de_la_lista = numeros
print("Primero y segundo:", primero, segundo)
print("Resto de la lista:", resto_de_la_lista)

"""
    ? Este método es particularmente útil cuando se trabaja con listas de las que solo 
    ? se necesitan algunos elementos específicos, o cuando los elementos tienen roles distintos 
    ? en el código, facilitando la gestión de datos y mejorando la claridad del código.
    ? El uso del asterisco '*' para capturar los elementos restantes en una lista, 
    ? conocido como 'extended unpacking', es muy versátil 
    ? y similar a la forma en que se manejan argumentos variables en funciones con '*args'.
"""
