"""
 ? Partiendo de la base que en matematicas se necesitan de 2 (DOS) 
 ? numeros para poder realizar operaciones basica y con el fin de
 ? afianzar los conocimientos ya vistos.
 ? Crearemos una calculadora basica con fines educativo.

 TODO: En esta App NO contemplara los siguientes casos excepsionales. 
 ! ❌ Divison por 0
 ! ❌ Validacion de errores
 ! ❌ Manejo de errores


 TODO: Mejoras (opcional pero recomendadas UwU)
 ✅ Implementar las operaciones de potenciacion y raices.
 ✅ Mejorar los mensajes de salida(output) del usuario.
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
