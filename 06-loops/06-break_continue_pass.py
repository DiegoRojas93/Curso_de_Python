# pass: salta la linea

for number in list(range(10)):
    pass

# break: rompe el ciclo

for number in list( range(10) ):
    if number == 5:break
    print( number )
    
# continue: ignora el ciclo actual y continue con el siguiente

for number in list( range(10) ):
    if number == 5:
        print('🚩')
        continue
    print( number )