"""
    ! Las estructuras de control permiten modificar el flujo 
    ! de ejecución de las instrucciones de un programa.

    ? A menudo en programación nos encontramos con problemas donde
    ? en base a una condición ejecutamos un algoritmo u otro.
    
    ! Ejemplo
    ? Se estrenó en el cine una película solo para personas mayores
    ? de 18 años, eso significa que debemos hacer un "control"
    ? y no permitir el acceso de los menores de edad.
    ? Pero este cine también contempla el caso en el que si la persona
    ? es mayor a 50 años se le hace un descuento del 30%
    ? a continuación se mostrará una posible solución.

    TODO: ¡El programa tiene un error 😒! ¡Solucionalo!
    PISTA: Los condicionales parecen no estar correctamente.
"""

print("¡Bienvenido al cine!!!")
edad = input("Ingresa tu edad > ")
edad = int(edad)

if edad >= 18:
    # entrará en este bloque del programa si la condición es verdadera
    # aquí podríamos ejecutar el código que queramos.
    print("Disfruta de la película")
elif edad >= 50:
    print("Disfruta de la película")
    print("Tienes un descuento del 30%")
else:
    # Si la condición es falsa
    # aquí podríamos ejecutar el código que queramos.
    print("No puedes ver la película")


""" 
#! SOLUCIÓN

if edad >= 50:
    print("Disfruta de la película")
    print("Tienes un descuento del 30%")
elif edad >= 18:
    print("Disfruta de la película")
else:
    print("No puedes ver la película") 

#? Como podrás notar, el orden en cómo se colocan los condicionales 
#? sí importa. Dado que en el código con ERROR nunca iba a entrar a la
#? sentencia "elif" porque el primer "if" lo impedía.
"""
