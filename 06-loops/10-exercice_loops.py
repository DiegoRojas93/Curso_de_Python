print('''

Carrito de compras
Opciones:
1. Agregar producto
2. Eliminar producto
3. Mostrar lista ordenada
4. Buscar producto
5. Contar productos del carrito
6. Vaciar carrito
7. Salir
''')

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = 0

index = None
cantidad = None

while option <= 7 and isinstance(option, (int)):
    
    option = int(input("Escoge la opción (1-7): "))
    
    if (isinstance(option, (int)) and option > 0 ):
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
            print("Saliste!!!")
            break
            
        print(f"El resultado es: {cantidad or index or shopping_cart}\n")
        