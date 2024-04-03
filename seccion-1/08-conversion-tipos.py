"""
    ! En este programa veremos como podemos hacer una conversion de tipos de datos
    ! tambien conocido como "casting". 
    ? Tambien se puede apreciar apreciar como es normalmente el orden de ejecucion de un programa.
    ? Es decir, ejecuta la instrucciones de arriba hacia abajo
"""

# original
x = "1"
y = "2.3"

print("---- Conversion de string a FLOAT ----")
# conversion de tipo (casting)
x = float(x)
y = float(y)
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
x = int(x[0])
y = int(y[0])
print(x, "-", type(x))
print(y, "-", type(y))
print("")
