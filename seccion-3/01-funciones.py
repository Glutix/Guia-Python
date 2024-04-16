"""
    Una función es un conjunto de instrucciones que realiza una tarea específica. 
    Cuando definimos una función, podemos establecer parámetros de entrada, que son variables 
    que la función espera recibir para llevar a cabo su tarea. Estos parámetros actúan 
    como marcadores de posición que permiten a quienes llaman a la función pasar valores 
    o argumentos específicos cuando la invocan. Además, una función puede o no devolver 
    un valor como resultado de su ejecución.

    ? Los parámetros son variables definidas en la declaración de la función que actúan 
    ? como marcadores de posición para los valores que la función espera recibir cuando es llamada.
    
    ? Los argumentos son los valores reales que se pasan a una función cuando es llamada. 
    ? Estos argumentos corresponden a los parámetros definidos en la declaración de la función.
    
    ? Devolver un valor significa que la función produce un resultado que puede ser utilizado 
    ? en otras partes del código.

    Por ejemplo, consideremos la función 'print()', la cual utilizamos comúnmente para mostrar 
    información en la consola. Cuando llamamos a la función 'print()', debemos incluir 
    paréntesis () y, dentro de estos paréntesis, proporcionar los argumentos que queremos 
    imprimir por consola.

    Ahora, veamos cómo crear nuestra propia funcion:
"""


def saludar(nombre):
    # cuerpo de la función
    print(f"Hola {nombre}, Bienvenidos a la guia de Python.")


"""
Aquí, hemos definido una función llamada saludar() utilizando la palabra reservada def.
Entre paréntesis, declaramos un parámetro llamado 'nombre', que actúa como marcador de posición 
para el texto que queremos imprimir. Dentro del cuerpo de la función, indicamos que esta función 
imprimirá un mensaje. Sin embargo, esto solo define la función 
para utilizarla, necesitamos llamarla o invocarla.
"""


saludar("Juan")
saludar("Pedro")
saludar("Carlos")

"""
Al llamar a nuestra función saludar() y proporcionar un nombre.
estamos pasando el nombre como argumento al parámetro nombre. 
Como resultado, la función imprime "Hola {nombre}, Bienvenidos a la guia de Python."

! Ejecuta y Probalo !
"""
