def devide_numbers():
    try: 
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador: "))
        
        result =  a / b
        
    except ValueError:
        print("Por favor, ingresa solo números.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except Exception as error:
        print(error)
        print(type(error))
    else:
        print(result)           # Se ejecuta cuando no hay excepciones
    finally:
        print("Gracias por usar nuestra calculadora.")

devide_numbers()