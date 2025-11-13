class Person:
    species = 'Humano'
    
    def __init__(self, name, age):
        # Atrubutos de instancia
        self.name = name
        self.age = age
        
    def work(self):
        return f'{self.name} esta trabajando muy duro.'
    
    def eat(self, food):
        return 'SuperPower' if food.lower() == "tacos" else '+Energia'

person1 = Person('Jesus', 2025)

print(person1.name)
print(person1.species)
print(person1.work())
print(person1.eat('Tacos'))
print(person1.eat('Tamal'))