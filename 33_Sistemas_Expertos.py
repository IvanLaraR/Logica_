# Definición de la clase Actividad
class ActividadDeportiva:
    def __init__(self, nombre, intensidad, habilidades_requeridas):
        self.nombre = nombre  # Nombre de la actividad deportiva
        self.intensidad = intensidad  # Nivel de intensidad de la actividad
        self.habilidades_requeridas = habilidades_requeridas  # Habilidades requeridas para la actividad

# Definición de la clase Usuario
class Persona:
    def __init__(self, nombre, nivel_condicion_fisica, habilidades):
        self.nombre = nombre  # Nombre de la persona
        self.nivel_condicion_fisica = nivel_condicion_fisica  # Nivel de condición física de la persona
        self.habilidades = habilidades  # Habilidades deportivas de la persona

# Función para recomendar actividades deportivas
def recomendar_actividades(usuario, actividades):
    actividades_recomendadas = []
    for actividad in actividades:
        # Verificar si el nivel de condición física del usuario es adecuado para la actividad
        if usuario.nivel_condicion_fisica >= actividad.intensidad:
            # Verificar si el usuario tiene las habilidades requeridas para la actividad
            if all(habilidad in usuario.habilidades for habilidad in actividad.habilidades_requeridas):
                actividades_recomendadas.append(actividad.nombre)
    return actividades_recomendadas

# Crear algunas actividades deportivas
futbol = ActividadDeportiva("Fútbol", 5, ["Correr", "Patear"])
natacion = ActividadDeportiva("Natación", 3, ["Nadar", "Respiración"])
tenis = ActividadDeportiva("Tenis", 4, ["Correr", "Raquetear"])

# Crear un usuario
persona = Persona("Juan", 3, ["Nadar", "Patear"])

# Lista de actividades disponibles
actividades_disponibles = [futbol, natacion, tenis]

# Recomendar actividades al usuario
actividades_recomendadas = recomendar_actividades(persona, actividades_disponibles)

# Mostrar actividades recomendadas
if actividades_recomendadas:
    print(f"¡Hola {persona.nombre}! Te recomiendo las siguientes actividades deportivas:")
    for actividad in actividades_recomendadas:
        print(f"- {actividad}")
else:
    print("Lo siento, no hay actividades disponibles que se ajusten a tus preferencias y nivel de condición física.")
