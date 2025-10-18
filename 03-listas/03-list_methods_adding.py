numbers_list = [ 1, 2, 3, 4, 5 ]

numbers_list.append(100)

print(numbers_list)

numbers_list.insert(1, 200) # Inserta el elemento en una posición y hace correr una posición hacia la derecha los demás elementos

print(numbers_list)

numbers_list.extend( [200, 300, 500] )

print(numbers_list)