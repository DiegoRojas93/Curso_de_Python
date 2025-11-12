import string, random;

def password_generator(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    num = 0
    password = ""
    
    while num < length:
        char = random.choice(chars)
        
        password += char
        
        num += 1
    else: print(f"Tu contraseña segura es: {password}")

length = int(input("¿Cuantos caracteres quieres tu contraseña?: "))

password_generator(length)
