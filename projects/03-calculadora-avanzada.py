"""
    ! Es hora de mejorar nuestro proyecto "Calculadora intermedia" ahora que hemos 
    ! aprendido nuevos conceptos. Vamos a crear una "calculadora avanzada" para poner 
    ! en práctica lo que hemos aprendido hasta ahora.

? Características a añadir:
    ? - ✅ Permitir al usuario elegir la operación a realizar.
    ? - ✅ No permitir la división por 0.
    ? - ✅ No permitir calcular raíces de números negativos.
    ? - ✅ Manejar errores
    ? - ✅ Validar datos
    ? - ✅ Utilizar funciones para mejorar la legibilidad y organización del código
    ? - ✅ No terminar la ejecución del programa hasta que el usuario lo decida.

💡PISTA: Podemos usar un bucle que controle esta condición para mejorar 
         la experiencia del usuario.
"""

print("-------> Calculadora intermedia <-------")
x = input("Ingresar el primer numero > ")
y = input("Ingresar el segundo numero > ")

# conversion de datos (casting)
x = int(x)
y = int(y)
