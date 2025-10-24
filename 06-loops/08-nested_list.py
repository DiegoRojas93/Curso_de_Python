nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for sublist in nested_list:
    for number in sublist:
        print(number, end=' ')  # Hace imprimer el resultado en una sola linea

print()

for sublist in nested_list:
    for number in sublist:
        print(number, end=' ')  # Hace imprimer el resultado en una sola linea
    print()                     # Hace un salto de lilnea cuando termine de leer un sublist