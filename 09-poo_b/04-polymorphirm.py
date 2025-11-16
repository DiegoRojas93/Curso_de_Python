class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("Guau Guau!")

class Cat(Animal):
    def make_sound(self):
        print("Miau Miau!")


def make_noise( animal ):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("Esto no es un animal.")
        
make_noise(Dog())
make_noise(Cat())
make_noise("Hola mundo!")