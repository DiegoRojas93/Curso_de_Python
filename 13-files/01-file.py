import os
path = os.path.dirname(os.path.abspath(__file__))

my_file = open(path + '/fileFolder/test.txt')

# print(my_file.read())

# Seek = Resetea el puntero (la posicion del string) para volverlo a leer archivo.
# my_file.seek(0)
# print(my_file.read())

# Readline: lee linea por linea

print(my_file.readline())
print(my_file.readline())

# Readlines: devuelve en formato de lista las demas lineas

print(my_file.readlines())