# OR

print('''
---------OR---------''')

True or print("Hola 1")
False or print("Hola 2")
print("Hola 3") or print("Hola 4")
False or False or print("Hola 5")

# AND

print('''
---------AND---------''')

True and print("Hola 1")
False and print("Hola 2")
print("Hola 3") and print("Hola 4")
False and False and print("Hola 5")


print('''
---------Ejemplo practico---------''')

name = None

print( name and name.upper() )