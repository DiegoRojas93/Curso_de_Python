print('''

Carrito de compras
Opciones:
1. Agregar producto
2. Eliminar producto
3. Mostrar lista ordenada
4. Buscar producto
5. Contar productos del carrito
6. Vaciar carrito
''')

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = int(input("Escoge la opción (1-6): "))

index = None
cantidad = None

if option == 1:
    item = input("Agrega un producto a la lista: ")
    shopping_cart.append( item )
elif option == 2:
    item = input("Elimina un producto a la lista: ")
    shopping_cart.remove( item )
elif option == 3:
    shopping_cart.sort()
elif option == 4:
    item = input("Busca el producto en la lista: ")
    index = shopping_cart.index( item )
elif option == 5:
    cantidad = len(shopping_cart)
    pass
elif option == 6:
    shopping_cart.clear()
    pass
else:
    print("Opcion no válida")

print(f"El resultado es: {cantidad or index or shopping_cart}")