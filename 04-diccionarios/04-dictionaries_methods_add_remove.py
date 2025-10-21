user = {
    'name': 'Diego Rojas',
    'age': 32,
    'greet': 'Hola mundo!',
    'numbers' : [1, 2, 3]
}

user_copy = user.copy()

print(user_copy)

user_copy.pop('name') # Elimina el elemento del diccionario segun la key que se asigne

print(user_copy)

user_copy.popitem() # Elimina el ultimo elemento del diccionario

print(user_copy)

user_copy.update({'Skills': ['JavaScript', 'Java']}) # Perminte ya sea crear o actualizar una clave o valor del diccionario

print(user_copy)

user_copy['Hobbies'] = user_copy.get('Hobbies', [])    # Si el valor no existe, devuelvame un a lista vacia (Sirve como un ternario)
user_copy['Hobbies'].append("Ir a la iglesia")
print(user_copy)