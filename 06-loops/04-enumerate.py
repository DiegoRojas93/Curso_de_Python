for index, char in enumerate('Devtalles'):
    print(char, index)
    
for i, number in enumerate(list(range(100))):
    result = f'{number} 🚩' if number == 32 else number
    print(f'Hola, soy el numero: {result} del indice {i}')