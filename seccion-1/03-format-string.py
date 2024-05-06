"""
    ! La interpolación en cadenas de texto es un concepto que existe en la gran mayoría de 
    ! lenguajes de programación y hace referencia al hecho de sustituir los nombres de 
    ! variables por sus valores cuando se construye un «string».

    ! Para indicar en Python que una cadena es un «f-string» basta con precederla de una f
    ! e incluir las variables o expresiones a interpolar entre llaves {...}.

    ! Supongamos que disponemos de los datos de una persona y queremos formar 
    ! una frase de bienvenida con ellos:
"""

name = "Juan Cruz"
age = 40

message = f"""
Bienvenidos {name} a tu fiesta de cumpleaños, espero que difrutes tu día. 
Feliceses {age} años !!!
"""

print(message)
