"""
    ! Las estructuras repetitivas, también conocidas como bucles o loops, son bloques de código 
    ! que se ejecutan repetidamente hasta que se cumple una condición específica o se alcanza 
    ! un objetivo predeterminado. Estas estructuras son fundamentales para automatizar tareas y 
    ! procesar datos de manera eficiente dentro de un programa.


    ! Ejemplo:

    ? Si quisiéramos imprimir por pantalla los números del 0 al 99, tendríamos que escribir:
        print(1)
        print(2)
        print(3)
        ... y asi sucesivamente hasta llegar al 100.

    ? Sería un proceso engorroso y propenso a errores. Para evitar esto, podemos utilizar 
    ? una estructura repetitiva. Veamos cómo hacerlo:
"""

# range crea una secuencia de números que comienza del 0 hasta el numero indicado
# por ejemplo range(5) seria 0, 1, 2, 3, 4
for numero in range(100):
    print(numero)
