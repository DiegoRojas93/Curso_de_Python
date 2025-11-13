class Person:
    species = 'Humano'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def change_species(cls, new_specie):
        cls.species = new_specie
        print("\nEspecie cambiada.\n")
        
    @staticmethod
    def is_older( age ):
        return age >= 18
    
print("====Class method===")
        
person1 = Person('Maria', 65)
person2 = Person('Diego', 32)
print(person1.species)
print(person2.species)
Person.change_species('Humanoide')
print(person1.species)
print(person2.species)

print("====Static method===")

print(Person.is_older(18))
print(Person.is_older(17))
print(person1.is_older(person1.age))