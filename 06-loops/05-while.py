counter = 0

while counter <= 5:
    print(f'Number: {counter}')
    counter += 1
else:
    print("Terminamos\n")

response = ''

while response.lower() != 'python':
    response = input('Escribe Python para salir: ')
else:
    print('Saliste')