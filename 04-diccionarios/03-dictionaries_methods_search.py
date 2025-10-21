user = {
    'name': 'Diego Rojas',
    'age': 32,
    'greet': 'Hola mundo!',
    'numbers' : [1, 2, 3]
}

print(user.get('name'))

print(user.keys())
print(user.values())

print('name' in user)                   # Por default el nombre del diccionario ejecuta el metodo keys cuando se usa in
print('name' in user.keys())
print('Diego Rojas' in user.values())

print(user.items())                     # Trae todo el diccionario                  