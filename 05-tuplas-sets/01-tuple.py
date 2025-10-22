"""
* Caracteristicas

Son inmutables. Despues de creadas no se pueden eliminar o agregar más elementos
Permite datos duplicados
Son ordenados
Son indexados

* Metodos

.count()    # Cuenta la cantidad de veces que se repite un elemento
.index()    # Te indica la posición del elemento que quieres buscar
"""


my_tuple = ( 1,2,3,4, 'Hola', True, 2, 'Hi', 5, 4, 3, 2 )

print(f'my_tuple: {my_tuple}')
print(f'2 se repite: {my_tuple.count(2)} veces')
print(f'True se repite: {my_tuple.count(True)}')    # True se repite 2 veces por que tambien toma el 1
print(f'El número 2 se encuentra en la posición: { my_tuple.index(2) }')
