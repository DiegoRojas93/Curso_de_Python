class Person:
    def __init__(self, name):
        self.name = name
        self._energy = 100
        
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
        
person1 = Person('Diego')

print(person1.name)
print(person1._energy)
print(person1._waste_energy(20))
