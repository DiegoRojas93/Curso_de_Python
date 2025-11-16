class Person():
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Instancia persona '{ self.name }' fue creada."             # Por defecto cuando se llama la instancia en  un print, __str__ se ejecut: <__main__.Person object at 0x7f42239ff8f0>
    
    def __len__(self):
        return len(self.name)
        # return f"El nombre {self.name} tiene {len(self.name)} caracteres."
        
person = Person('Diego')

print(person)
print(len(person))