from datetime import datetime
import os

path = os.path.dirname(os.path.abspath(__file__))
message = "Error en la bases de datos."
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(f"{ path }/fileFolder/logs.txt", mode='a') as my_file:
    my_file.write(f"[{ date }]: {message}\n")