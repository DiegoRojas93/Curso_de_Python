class Animal:
    def __init__(self, name):
        self.name = name
        
    def sleep(self):
        print(f"{ self.name } está durmindo.")

class Dog(Animal):
    def dog_sound(self):
        print(f"{self.name} dice: Guauu!")

class Cat(Animal):
    def cat_sound(self):
        print(f"{self.name} dice: Miauu!")

firulais = Dog("Firulais")
firulais.sleep()
firulais.dog_sound()

michi = Cat("Michi")
michi.sleep()
michi.cat_sound()