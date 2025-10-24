inventory = {
    'Chocolate': 10,
    'Gomitas': 5,
    'Paleta': 8,
    'Chicle': 2,
    'Mexicano': 8,
    'Galleta': 12
}

option = 0
cart = []
total = 0

print("\nBienvenido a la tienda de dulces, DevCandy!")

print("\n********Tabla********\nProducto:precio\n*********************")
for index, (candy, price) in enumerate(inventory.items()):
    print(f"{index + 1}. {candy.capitalize()}: {price} pesos")

while len(cart) < 6:
    option = int(input("\n¿Quieres comprar un producto, escoge tu eleción del 1 al 6 (7 o más para salir): "))
    
    if (option >= 7):
        print(f"\nTotal a pagar es: {total} pesos.\nGracias por tu compra.")
        break
    
    list_inventory = list(inventory.items())
    candy, price = list_inventory[ option - 1 ]
    total += price
    cart.append( candy )
    print(f"Agregaste {candy} al carrito.")
else:
    print(f"\nTotal a pagar es: {total} pesos.\nGracias por tu compra.")