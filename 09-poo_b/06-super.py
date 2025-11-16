class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print(f"{self.name} esta haciendo un sonido.")
        
    def info(self):
        print(f"Soy {self.name} y tengo {self.age} años.")
        
class Dog(Animal):
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def sound(self):
        super().sound()
        print("Guau Guau!")
        
    def info(self):
        super().info()
        print(f"Soy de raza { self.breed }.")
        
        
class Cat(Animal):
    def sound(self):
        super().sound()
        print("Miau Miau!")
        
myDog = Dog("Firulais", 5, 'Labrador')

myDog.sound()
myDog.info()