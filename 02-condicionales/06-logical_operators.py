# Evaluar condiciones

# and (Todas las condiciones debe ser verdaderas)

# print( True and True )
# print( True and False )
# print( False and True )
# print( False and False )

# or (Almenos una de las condiciones debe ser verdader)

# print( True or True )
# print( True or False )
# print( False or True )
# print( False or False )

# not (negar)

# print( not True )
# print( not False )


# and

age = 32
licensed = True

if age >= 18 and licensed:
    print("Puedes conducir.")
    
is_student = False
membership = True

if is_student or membership:
    print("Obtienes un descuento especial.")
    
is_admin = False

if not is_admin:
    print("Acceso denegado.")