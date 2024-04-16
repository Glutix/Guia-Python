"""
    Los xargs, que viene de 'eXtended ARGumentS' (argumentos extendidos), se utiliza para pasar 
    múltiples argumentos a una función. Básicamente, convierte los parámetros que recibe 
    en un iterable, es decir, en una secuencia de elementos sobre los cuales la función 
    puede iterar. Si recuerdas la función 'range()', que generaba una secuencia de números, 
    puedes pensar en xargs de manera similar, aunque más flexible, ya que puede trabajar 
    con cualquier tipo de datos. Más adelante exploraremos otros tipos de iterables.

    ? Ejemplo:

    def suma(num1, num2):
        return num1 + num2
    
    ? Esta función simple recibe dos parámetros, num1 y num2, y luego retorna su resultado.
    ? No hay ningún problema si la llamo y le paso 2 argumentos:

    suma(2, 2) -> ✅ 4

    ? Sin embargo, daría un error si intento pasarle más de dos argumentos:

    suma(2, 2, 3) -> ❌ Error
    suma(2, 2, 3, 4) -> ❌ Error

    TODO: Veamos cómo podemos solucionar esto.
"""


# xargs: con el simbolo "*" le indicamos que vamos a recibir todos los parámetros.
def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(total)


suma(1, 2, 3)  # --> 6
suma(2, 2)  # --> 4
suma(3, 3, 3, 3, 3)  # --> 15
