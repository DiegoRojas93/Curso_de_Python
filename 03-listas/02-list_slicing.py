shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetas',
    'Pantalones',
]

new_shopping_cart = shopping_cart[0:2]

new_shopping_cart[1] = 'Zapatos'

print( new_shopping_cart )
print( shopping_cart )

copy_shopping_cart = shopping_cart[:]
copy_shopping_cart[2] = 'Medias'

print(copy_shopping_cart)
print( shopping_cart )