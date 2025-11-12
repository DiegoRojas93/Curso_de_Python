global_variable = "Soy global."

def outher_function ():
    enclosing_variable = "Soy enclousing."
    
    def inner_function():
        local_variable = "Soy local."

        print(global_variable)
        print(enclosing_variable)
        print(local_variable)
        
    inner_function()
    
outher_function()