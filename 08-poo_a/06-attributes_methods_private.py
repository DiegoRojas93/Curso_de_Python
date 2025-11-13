class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = "1234" # name mangling: _NOMBRECLASE__atributo -> _Person.name

    def __show_age(self):
        return f"{self.name} tiene {self.age} años."

person1 = Person('Diego', 32)

print(person1.name)
print(person1._Person__password)
print(person1._Person__show_age())
