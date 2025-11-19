import os

path = os.path.dirname(os.path.abspath(__file__))

try:
    with open(f"{ path }/fileFolder/sinPermisos.txt", mode='r') as my_file:
        print(my_file.readlines())
except FileNotFoundError:
    print("El archivo no existe.")
except PermissionError:
    print("No tiene permisos para abrir este archivo.")
except Exception as e:
    print(f"Ocurrio un error: {e}")