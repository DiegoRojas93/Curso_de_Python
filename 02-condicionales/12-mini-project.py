name = input("Nombre del candidato: ")
experience = int(input("Años de experiencia: "))
skills = input("Escribe sus habilidades seperadas por comas (ej: Python, Django, JavaScript, Java, etc): ")

evaluate_skills = "Python" in skills or "Django" in skills

result = None

if evaluate_skills:
    if experience >= 3:
        result = "Candidato optimo."
    elif experience >= 1 :
        result = "Buen candidato."
    else:
        result = "Posible candidato."
else:
    result = "No apto, se guardara el CV para futuras ofertas."
    
print(f"El candidato es {name}: {result}")