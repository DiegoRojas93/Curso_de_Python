'''
Iterables:  Iterables, Listas, Diccionarios, Set, Tuplas
Iterator: Un objeto que recuerda su posición
'''

numbers = [1,2,3,4,5]

numbersIter = iter( numbers )

print(numbersIter)      # <list_iterator object at 0x7ce6df903610>

for number in numbers:
    print(next(numbersIter))
    
user = {
    'name': "Diego Rojas",
    'age': 32,
    "can_swim": False
}

for key, value in user.items():
    print(key, value)