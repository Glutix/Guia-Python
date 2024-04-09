"""
    ! Es hora de mejorar nuestro proyecto "Calculadora básica" ahora que hemos aprendido 
    ! nuevos conceptos. Vamos a crear una "calculadora intermedia" para poner en práctica 
    ! lo que hemos aprendido hasta ahora.

? Características a añadir:
    ? - ✅ Permitir al usuario elegir la operación a realizar.
    ? - ✅ No permitir la división por 0.
    ? - ✅ No permitir calcular raíces de números negativos.
    ? - ✅ No terminar la ejecución del programa hasta que el usuario lo decida.

💡PISTA: Podemos usar un bucle que controle esta condición para mejorar la experiencia del usuario.

TODO: En esta aplicación NO se contemplarán los siguientes casos excepcionales:
    ! - ❌ Validación de errores.
    ! - ❌ Manejo de errores.

"""

print("-------> Calculadora Basica <-------")
x = input("Ingresar el primer numero > ")
y = input("Ingresar el segundo numero > ")

# conversion de datos (casting)
x = int(x)
y = int(y)

message = f"""
El resultado de la suma entre {x} y {y} = {x + y}
El resultado de la resta entre {x} y {y} = {x - y}
El resultado de la multiplicacion entre {x} y {y} = {x * y}
El resultado de la divsion entre {x} y {y} = {x / y}
"""

print(message)
