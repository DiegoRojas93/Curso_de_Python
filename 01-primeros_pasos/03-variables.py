"""
    Recomendaciones del PEP 8 (Python Enhancement Proposal)
    y es la propuesta número 8, creada por Guido van Rossum (el creador de Python) para Python:

    snake_case: Se utiliza para nombres de variables y funciones.
    variable privadas: Se indica con un guion bajo al inicio del nombre. Usadas en clases.
    constantes: Se indican con mayúsculas y guiones bajos.
    camelCase: Se utiliza para nombres de clases.
    Ejemplo: mi_variable, _mi_variable_privada, MI_CONSTANTE, MiClase
    Comentarios: Se utilizan para explicar el código y se pueden hacer en una sola línea o
    multilínea.
"""

name = "Diego"
last_name = "Rojas"
MI_AGE = 32
PI = 3.14159
_cedula = "12345678"  # Variable "privada_mi_variable_privada

print(f"Hola, soy { name } { last_name } y tengo { MI_AGE } años. Mi número favorito es { PI }.")