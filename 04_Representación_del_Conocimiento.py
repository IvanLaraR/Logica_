# Representación del conocimiento usando diccionarios en Python

# Conocimiento sobre personas y sus características
conocimiento_personas = {
    "Juan": {"edad": 30, "profesion": "ingeniero", "hobbies": ["leer", "tocar guitarra"]},
    "María": {"edad": 25, "profesion": "abogada", "hobbies": ["correr", "bailar"]},
    "Pedro": {"edad": 35, "profesion": "médico", "hobbies": ["cocinar", "jugar fútbol"]}
}

# Imprimir información sobre cada persona
for persona, atributos in conocimiento_personas.items():
    print(f"Información sobre {persona}:")
    print(f"Edad: {atributos['edad']} años")
    print(f"Profesión: {atributos['profesion']}")
    print("Hobbies:", ", ".join(atributos['hobbies']))
    print()
