# global: permite modificar una variable si esta en el ambito global

global_variable = "Soy una variable global."

def change_global():
    global global_variable
    
    global_variable = "Soy una variable local."
    
    print(global_variable)
    
change_global()