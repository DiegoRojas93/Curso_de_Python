class Person:
    def __init__(self, name, age):
        if (age > 40):
            self.name = name
            self.age = age
        
person1 = Person("Jesus", 2025)

print(person1)
print(person1.name)
print(person1.age)