"""
    ¿Sabías que en matemáticas se necesitan al menos dos números para realizar 
    operaciones básicas? 
    
    Con el objetivo de afianzar los conocimientos adquiridos hasta ahora, 
    vamos a crear una calculadora básica con fines educativos.

    ? Mejoras (opcional pero recomendadas):
        ? - ✅ Implementar las operaciones de potenciación y raíces.
        ? - ✅ Mejorar los mensajes de salida (output) para mejorar la experiencia del usuario.
    
    TODO: En esta aplicación NO se contemplarán los siguientes casos excepcionales:
        ! - ❌ División por 0
        ! - ❌ Calcular raíces de números negativos.
        ! - ❌ Validación de datos
        ! - ❌ Manejo de errores
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
