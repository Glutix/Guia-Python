"""
    ! Además de los bucles tradicionales, como el 'for', también existe el bucle 'while' 
    ! para recorrer iterables. En esta ocasión, nos enfocaremos en el bucle 'while' 
    ! para explorar la iteración a través de un string y así consolidar 
    ! nuestros conocimientos hasta el momento.
"""

# Supongamos que tenemos esta cadena de caracteres
string = "Este curso está enfocado a las personas que quieren dar sus primeros pasos en Python"

# Queremos verificar si dentro de ella se encuentra la palabra "Python"
buscar = "Python"

# Inicializamos variables
indice = 0
encontrado = False

# Utilizamos un bucle while para recorrer el string
while indice < len(string):
    # Extraemos un subString del string principal para comparar con la palabra buscada
    subString = string[indice : indice + len(buscar)]

    # Si el subString coincide con la palabra buscada, marcamos como encontrado y salimos del bucle
    if subString == buscar:
        encontrado = True
        break

    # Incrementamos el índice para avanzar en el string
    indice += 1

# Mostramos el resultado
if encontrado:
    print("La palabra 'Python' se encuentra en el texto.")
else:
    print("La palabra 'Python' no se encuentra en el texto.")


"""
    ? Este código utiliza un bucle while para iterar a través del texto y extraer subcadenas 
    ? para compararlas con la palabra buscada. Si encuentra una coincidencia, 
    ? establece la bandera encontrado en True y sale del bucle. 
    ? Finalmente, muestra un mensaje indicando si se encontró o no la palabra.


    ! ¿Qué es una bandera?
    
    Las variables “bandera” nos sirven para indicar y almacenar 
    que algún evento o condición se cumplió. 
    Aquí solemos usar variables de tipo boolean .
"""
