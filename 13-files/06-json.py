import os
import json

path = os.path.dirname(os.path.abspath(__file__))

user = {
    'name': 'Diego Rojas',
    'age': 32,
    'isActive': True
}

with open(f"{ path }/fileFolder/datos.json", mode='w') as my_file:
    json.dump(user, my_file, indent=2)
    
with open(f"{ path }/fileFolder/datos.json", mode='r') as my_file:
    read = json.load(my_file)
    print(read)