students = {
    'Ana': [8,7,9],
    'Luis': [6,5,7],
    'Sofia': [10,9,10]
}

students["Diego Rojas"] = [10,9,8]

a, b, c = students['Luis']

average = (a + b + c) / len(students['Luis'])

x, y, z = students['Diego Rojas']


average2 = (x + y + z) / len(students['Diego Rojas'])

print(f"""
students: {students}
average: {average:.2f}
average2: {average2:.2f}
""")