"""
    ! En este programa veremos como podemos hacer una conversion de tipos de datos
    ! tambien conocido como "casting". 
    ? Tambien se puede apreciar como es normalmente el orden de ejecucion de un programa.
    ? Es decir, ejecuta la instrucciones de arriba hacia abajo
"""

# original
x = "1"
y = "2.3"

print("---- Conversion de string a FLOAT ----")
# conversion de tipo (casting)
x = float(x)  # 1.0
y = float(y)  # 2.3
print(x, "-", type(x))
print(y, "-", type(y))
print("")


print("---- Conversion de float a STRING ----")
# conversion de tipo (casting)
x = str(x)
y = str(y)

print(x, "-", type(x))
print(y, "-", type(y))
print("")


print("---- Conversion de string a INTEGER ----")
# conversion de tipo (casting)
x = round(float(x))
y = round(float(y))
x = int(x)
y = int(y)
print(x, "-", type(x))
print(y, "-", type(y))
print("")
