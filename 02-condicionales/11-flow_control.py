age = int(input("¿Cual es tu edad: "))

if age < 0:
    print("La edad no puede ser negativa.")
elif age <= 12:
    print("Eres un infante.")
elif age <= 17:
    print("Eres un adolecente.")
elif age <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
    