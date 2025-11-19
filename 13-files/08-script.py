import os

path = os.path.dirname(os.path.abspath(__file__))

js_code = """console.log("Hola mundo desde JavaScript.");
    
const suma = (a, b) => a + b
    
console.log( suma )
"""

with open(f"{ path }/fileFolder/script.js", mode='w') as my_file:
    my_file.write(js_code)