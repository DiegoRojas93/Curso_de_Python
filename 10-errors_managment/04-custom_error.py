class InvalidAgeError(Exception):
    def __init__(self, age, message = "La edad debe ser mayor o mayor  18 años."):
        self.age = age
        self.message =  message
        super().__init__(self.message)

def isMayor(name, age):
    if age < 18: raise InvalidAgeError(age)
    
    print(f"Usuario {name} se ha registrado con la edad de {age} años.")
    
try:
    isMayor('Diego', 15)
except InvalidAgeError as e:
    print(f"Error: {e}")