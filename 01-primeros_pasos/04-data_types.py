# String

name = "Diego"

# Integer

age = 32

# Float (decimal)

PI = 3.14159
tempture = -4.5;

# Boolean

is_single = True

# List (arreglo o array)

lista = [1, 2, 3, 4, 5]

# Tuple (tupla, inmutable)

tupla = (1, 2, 3, 4, 5)

# Set (conjunto, no permite duplicados)

set_conjunto = {1, 2, 3, 4, 5, 3}

print(set_conjunto)

# Dictionary (diccionario, pares clave-valor)

diccionario = {
    "nombre": "Homero Simpson",
    "edad": 46,
    "is_single": False
}

print(diccionario)

print(type(name))  # <class 'str'>
print(type(diccionario))  # <class 'dict'>
print(type(set_conjunto))  # <class 'set'>
print(type(tupla))  # <class 'tuple'>
print(type(lista))  # <class 'list'>
print(type(PI))  # <class 'float'>
print(type(age))  # <class 'int'>
print(type(is_single))  # <class 'bool'>
print(name.format_map)

print(type(name))