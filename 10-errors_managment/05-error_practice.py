import re

class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email
        self.message = f"El correo '{self.email}' esta mal digitado o no es un correo."
        super().__init__(self.message)

def valid_email(email):
    pettern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not( re.fullmatch(pettern, email) ): raise InvalidEmailError(email)

email = 'diegorojas431@gmail.com'
    
try:
    valid_email(email)
except InvalidEmailError as e:
    print(f"Error: {e}")
else:
    print(f"El correo '{email} es verdadero.")
finally:
    print("Gracias por confiar.")