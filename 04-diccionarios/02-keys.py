user = {
    "name": "Diego",
    "age": 32,
    "email": "micorreo@gmail.com",
    (4.60971, -74.08175) : "Coordenadas de Bógota"
}

print(f"user: {user}")

user["name"] = "Diego Rojas"
user["country"] = "Bogotá"

print(f"user: {user}")

print(user[4.60971, -74.08175])