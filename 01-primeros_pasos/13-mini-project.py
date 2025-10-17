name = input("¿Cual es tu nombre? ")
age = input("¿Cual es tu edad? ")
email = input("¿Cual es tu email? ")
password = input("¿Cual es tu contraseña? ")

future_age = int(age) + ( 2050 - 2025 )
password_hidden = '*' * len( password )

result = f"""
Nombre: {name}
Email: {email}
Tendras {future_age} años en el 2050
Contraseña: {password_hidden}
"""

print("----------Results----------")
print(result)