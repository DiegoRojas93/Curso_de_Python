nested_dict = {
    'user1': { 'name': "Diego Rojas", 'age': 32, 'city': 'Bogotá' },
    'user2': { 'name': "David", 'age': 28, 'city': 'Medellín' },
    'user3': { 'name': "Luis", 'age': 20, 'city': 'cali' }
}

for key, value in nested_dict.items():
    print(f'{key}: ')
    for subkey, subvalue in value.items():
        print(f'    {subkey}: {subvalue}')