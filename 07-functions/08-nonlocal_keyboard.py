# nonlocal: permite modificar una variable que sea externa pero no global

global_variable = "Soy una variable global."
global_variable2 = "Soy las segunda variable global."

def outer():
    enclousing_variable = "Enclousing variable."
    
    def inner():
        
        nonlocal enclousing_variable
        global global_variable
        
        global_variable = "Ahora soy una variable local."
        global_variable2 = "Ahora segunda una variable local."
        enclousing_variable = "Enclousing modificado."
        
    inner()
    
    print(global_variable)
    print(global_variable2)
    print(enclousing_variable)
    
outer()