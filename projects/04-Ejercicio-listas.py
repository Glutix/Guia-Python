"""
Los profesores de la universidad "X" necesitan un sistema para cargar la información de sus alumnos.
El sistema debe distinguir entre los alumnos que aprobaron y los que no, considerando 3 parciales y un trabajo integrador.
El trabajo integrador puede mejorar la nota final si el estudiante obtuvo entre:
- 5 y 6 -> +0.25 puntos
- 6 y 8 -> +0.50 puntos
- 8 y 10 -> +1 punto
"""

# Listas para aprobados y desaprobados
aprobados = []
desaprobados = []

# Bucle para ingresar datos de los estudiantes
while True:
    interruptor = input('Ingresa "X" o "Salir" si deseas salir del programa: ')
    if interruptor.lower() in ["x", "salir"]:
        print("Gracias por utilizar el programa.")
        break

    nombre = input("Ingresar el nombre: ")
    apellido = input("Ingresar el apellido: ")
    dni = input("Ingresar el D.N.I: ")
    nota1 = float(input("Ingresar nota 1: "))
    nota2 = float(input("Ingresar nota 2: "))
    nota3 = float(input("Ingresar nota 3: "))
    nota_integrador = float(input("Ingresar la nota del trabajo integrador: "))

    promedio = (nota1 + nota2 + nota3) / 3

    # Aplicar ajuste por nota del trabajo integrador
    ajuste = 0
    if 5 <= nota_integrador < 6:
        ajuste = 0.25
    elif 6 <= nota_integrador < 8:
        ajuste = 0.50
    elif 8 <= nota_integrador <= 10:
        ajuste = 1

    promedio_ajustado = promedio + ajuste

    # Clasificación basada en el promedio ajustado
    estudiante_info = (
        f"{nombre} {apellido}, DNI: {dni}, Promedio: {round(promedio_ajustado, 2)}"
    )

    if promedio_ajustado >= 6:
        aprobados.append(estudiante_info + ", Aprobado")
    else:
        desaprobados.append(estudiante_info + ", Desaprobado")

# Mostrar los resultados
if aprobados:
    print("\nLista de Aprobados:")
    for estudiante in aprobados:
        print(estudiante)
else:
    print("No hubo estudiantes aprobados.")

if desaprobados:
    print("\nLista de Desaprobados:")
    for estudiante in desaprobados:
        print(estudiante)
else:
    print("No hubo estudiantes desaprobados.")
