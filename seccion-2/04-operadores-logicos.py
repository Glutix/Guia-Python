"""
    ! Los operadores lógicos son herramientas fundamentales en la programación 
    ! Aquí hay una breve explicación de cada uno de ellos:

    ! AND (Y): Retorna True si ambos operandos son True, sino False.
    Ejemplo:

    ? True and True retorna True.
    ? True and False retorna False.
    ? False and False retorna False.
    
    ! OR (O): Retorna True si al menos un operando es True, sino False. 
    Ejemplo:

    ? True or True retorna True.
    ? True or False retorna True.
    ? False or False retorna False.

    ! NOT (NO): Retorna el opuesto de su único operando.
    Ejemplo:

    ? not True retorna False.
    ? not False retorna True.

    ! Estos operadores son esenciales para comparaciones lógicas y 
    ! controlar el flujo del programa.
"""

# Ejemplo
nota1 = input("ingresa la nota del primer parcial: ")
nota2 = input("ingresa la nota del segundo parcial: ")
nota3 = input("ingresa la nota del tercer parcial: ")
trabajo_integrador = True  # Suponiendo que completó el trabajo

# casting
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

# calc.
total = nota1 + nota2 + nota3
promedio = total / 3


# Evaluación de notas y trabajo integrador
if round(promedio) >= 6 and trabajo_integrador:
    print("Felicitaciones regularizo la materia")
elif round(promedio) >= 6 and not trabajo_integrador:
    print("No has aprobado. Falta completar el trabajo integrador.")
else:
    print("Desaprobaste la materia")


""" 
! Aunque el código anterior es funcional, a veces se pueden hacer mejoras 
! para mejorar su comprensión. tanto al código como a sus mensajes de salida😉

TODO: Ejemplo de un código más comprensible:

if round(promedio) >= 6:
    if trabajo_integrador:
        print("¡Felicitaciones! Has aprobado la materia.")
    else:
        print("No has aprobado. Por favor, completa el trabajo integrador.")
else:
    print("Lamentablemente, has desaprobado la materia.")
    
"""
