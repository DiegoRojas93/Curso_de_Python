"""
    *args: Permite pasar N cantidad de datos como parametros
    
    Nota: Los datos son almacenados una tupla
"""

def sum_operation(*args):
    print(args)
    print(sum(args))
    
sum_operation(1,2,3,4,5,6,7,8,9)

print("================")
"""
    **kwargs: permite pasar N cantidad de datos tipo variable:valor
    
    Nota: Los datos son almacenados un diccionario
"""

def sum_operation2(**kwargs):
    acum = 0
    
    for value in kwargs.values():
        acum += value
        
    print(kwargs)
    print(acum)
    
sum_operation2(num1=1, num2=2, num3=3)



print("================")



def sum_operation3(*args, **kwargs):
    acum = 0
    
    for value in kwargs.values():
        acum += value
        
    print(args)
    print(kwargs)
    print(sum(args) + acum)
    
sum_operation3(1,2,3,4,5,6,7,8,9, num1=1, num2=2, num3=3)