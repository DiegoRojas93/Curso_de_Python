"""
! La introspección de objetos en Python es la capacidad que tiene el lenguaje para examinar un objeto en tiempo de ejecución y obtener información sobre:

* Su tipo

* Sus atributos

* Sus métodos

* Su módulo de origen

* Su herencia

* Su estructura interna
"""

x = [1, 2, 3]

print(type( x ))                    # Devuelve el tipo exacto del objeto
print(dir( x ))                     # Lista los atributos y métodos del objeto, incluyendo los heredados.
print(hasattr( x, '__len__' ))      # Te devuelve un booleano para saber si tiene el atributo o metodo
print(hasattr( x, '__reduce__' ))
print(getattr( x, 'append' ))       # Te devuelve el valor de un atributo o metodo (Objetp, atributo, "Mesaje personalizado si no existe el atributo")
print(getattr( x, '__hola__', "No existe" ))
print(callable( x.append ))         # Te devuelve un booleano para saber si el método se puede usar
print(id( x ))                      # Te devuelve la dirección (identidad) en memoria del objeto en Hexadecimal: 140147735317312
print(help( x ))                    # Te muestra la documentación de dicho objeto

class Persona:
    def __init__(self):
        self.nombre = "Ana"
        self.edad = 30
        
persona = Persona()

print(persona.__dict__)            # Muestra los atributos definidos por el usuario dentro de la instancia. {'nombre': 'Ana', 'edad': 30}