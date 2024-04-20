"""
    ! Una excepción es un error que ocurre durante la ejecución de un programa. Es decir, 
    ! el programa se detiene abruptamente debido a un problema inesperado. 
    ! Esto puede ser contraproducente, ya que en muchos casos necesitamos que el programa 
    ! continúe ejecutándose a pesar de que ocurra un error. No queremos que toda nuestra 
    ! aplicación falle simplemente por una línea de código que genere un problema. 
    ! Por esta razón, existen métodos para evitar o controlar este tipo de situaciones. 
    
    * A continuación, exploraremos algunos ejemplos de cómo manejar excepciones en Python.
"""

# ? Este código intenta dividir dos números y muestra un resultado:
a = 2
b = 0

# ? Intentamos realizar la división:
try:
    div = a / b
    print(div)
except ZeroDivisionError:  # ? Este bloque se ejecuta si ocurre una división por cero
    print("Error: La división por cero no está permitida.")

# ? Este mensaje se imprime siempre, independientemente de si ocurre un error o no.
print("Fin del programa.")

# ? Análisis del comportamiento:
# ? Al ejecutar este código sin el bloque try-except, se produce un error "ZeroDivisionError: division by zero",
# ? ya que dividir cualquier número por cero no es una operación válida en matemáticas.
# ? Esto interrumpe la ejecución del programa y el mensaje "Fin del programa" no se muestra.

# ? Sin embargo, con el bloque try-except incluido:
# ? 1. Si se produce una división por cero, el error es capturado y manejado por el bloque except.
# ? 2. Se muestra un mensaje de error personalizado.
# ? 3. El programa continúa su ejecución normalmente después del bloque except.
# ? 4. Se imprime "Fin del programa", indicando que el programa ha manejado el error adecuadamente y ha continuado su ejecución.
