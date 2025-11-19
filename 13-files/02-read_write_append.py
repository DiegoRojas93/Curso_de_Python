import os
path = os.path.dirname(os.path.abspath(__file__))

with open(path + '/fileFolder/test.txt', mode="r") as my_file:
    print(my_file.readlines())
    
with open(path + '/fileFolder/archivo.txt', mode="w") as my_file:
    text = my_file.write('😮')
    
# with open(path + '/archivo.txt', mode="r+") as my_file:
#     print(my_file.readlines())
#     text = my_file.write('123')

with open(path + '/fileFolder/archivo.txt', mode="a") as my_file:
    text = my_file.write('123')
    print(text)