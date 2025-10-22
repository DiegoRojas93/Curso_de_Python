python_course = {'Ana', 'Luis', 'Maria', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_courses = python_course.intersection(java_course)
only_python = python_course.difference(java_course)
all_courses = python_course.union(java_course)

print(f"""
two_courses: {two_courses}
only_python: {only_python}
all_courses: {all_courses}
""")