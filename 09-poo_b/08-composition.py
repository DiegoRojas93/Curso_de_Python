class flyer():
    def fly(self):
        print("Puedo volar.")
        
    def do_something(self):
        print("Fly Fly")
        
class swimmer():
    def swim(self):
        print("Puedo nadar.")
        
    def do_something(self):
        print("Swim Swim")
        
class Duck():
    
    def __init__(self):
        self.fly = flyer()
        self.swim = swimmer()
        
        
    def quack(self):
        print("Quack")
        
    def start_fly(self):
        self.fly.fly()
        
    def start_swim(self):
        self.swim.swim()
        

donald = Duck()
donald.quack()
donald.start_fly()
donald.start_swim()
donald.do_something()

# MRO (Method Resolution Order) = Es la forma en que se ordedan las clases de mayor a  menor.

print(Duck.__mro__) # (<class '__main__.Duck'>, <class '__main__.flyer'>, <class '__main__.swimmer'>, <class 'object'>)