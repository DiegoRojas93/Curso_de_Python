import os

path = os.path.dirname(os.path.abspath(__file__))

# Relative path
with open(f"{ path }/fileFolder/relative.txt", mode='r') as my_file:
    print(my_file.readlines())