def devide_numbers():
    try: 
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador: "))
        
        result =  a / b
        
        print(result)
        
    except ValueError:
        print("Por favor, ingresa solo números.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except Exception as error:
        print(error)
        print(type(error))
        
devide_numbers()