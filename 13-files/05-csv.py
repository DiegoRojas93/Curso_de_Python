import os
import csv

path = os.path.dirname(os.path.abspath(__file__))

with open(f"{ path }/fileFolder/datos.csv", mode='w', newline="") as my_file:
    write = csv.writer(my_file)
    write.writerow(["Nombre", "Edad"])
    write.writerow(["Jesus", 2025])
    write.writerow(["Diego", 32])
    write.writerow(["Maria", 65])
    
with open(f"{ path }/fileFolder/datos.csv", mode='r') as my_file:
    reader = csv.reader(my_file)
    for row in reader:
        print(row)