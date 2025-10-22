# Methods

my_set = { 1,2,3 }

print(my_set)

my_set.add(4)
my_set.add(5)
my_set.add(6)
my_set.add(9)

print(my_set)

my_set.remove(6)    # Remueve el elemento, pero si no existe arroja error.

print(my_set)

my_set.discard(9)   # Remueve el elemento pero no arroja error si el elemento no existe.
my_set.discard(9)

print(my_set)