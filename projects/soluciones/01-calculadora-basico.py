import math

print("-------> Calculadora Básica <-------")
x = float(input("Ingresa el primer número > "))
y = float(input("Ingresa el segundo número > "))

suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
potencia = math.pow(x, y)
raiz_x = math.sqrt(x)
raiz_y = math.sqrt(y)

message = f"""
El resultado de la suma entre {x} y {y} = {suma}
El resultado de la resta entre {x} y {y} = {resta}
El resultado de la multiplicación entre {x} y {y} = {multiplicacion}
El resultado de la división entre {x} y {y} = {division}
El resultado de la potencia de base {x} y exponente {y} es igual a {potencia}
El resultado de la raíz cuadrada de {x} es igual a {raiz_x} y la raíz cuadrada de {y} es igual a {raiz_y}
"""
print(message)
