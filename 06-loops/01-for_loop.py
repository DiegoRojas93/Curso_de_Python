for item in 'Phyton':
    print(item)
    
fruits = [ 'Manzana', 'Platano', 'Sandia' ]

for fruit in fruits:
    print(fruit)
    
for i, fruta in enumerate(fruits):
    print(f"El índice es {i} y la fruta es {fruta}")
    
for i, _ in enumerate(fruits):  # Se usa cuando no se necesita el item del iterable
    print(f"El índice es {i}")
    
numbers = [1,2,3,4,5]
sum = 0

for number in numbers:
    print(number)
    sum += number
    
print(sum)