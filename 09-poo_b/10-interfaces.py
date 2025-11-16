from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print('Zzzz...')
        
class Dog(Animal):
    def sound(self):
        print("Guau Guau!")

class Cat(Animal):
    def sound(self):
        print("Miau Miau!")

firulauis = Dog()
michi = Cat()

firulauis.sound()
michi.sound()