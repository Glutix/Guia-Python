animal = "  gaTito  fEliZ  "

# transforma todos los caracteres del string en mayuscula
print(animal.upper())

# transforma todos los caracteres del string en minisculas
print(animal.lower())

# transforma el primer caracter en mayusculas y lo demas lo convierte a minisculas
print(animal.capitalize())

# transforma el string en un titulo
print(animal.title())

# quitar espacios a la izq y derecha de un string
print(animal.strip())

# quitar espacios a la derecha de un string
print(animal.rstrip())

# quitar espacios a la izq de un string
print(animal.lstrip())

# encadenamiento de metodos
print(animal.strip().capitalize())

# buscar el indice de una cadena de caracteres en un string
print(animal.find("ito"))

# remplazar una cadena replace("buscar", "rempalzar")
print(animal.replace("ito", "eto"))

# buscar si una cadena de caracteres se encuentra en un string
print("ito" in animal)

# busca si una cadena de caracteres NO se encunetra en string
print("ito" not in animal)
