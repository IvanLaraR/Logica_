# Definimos algunas funciones para simular predicados y cuantificadores

def es_mayor(edad):
    """Predicado que verifica si una persona es mayor de 18 años."""
    return edad > 18

def todos_mayores(lista_edades):
    """Cuantificador universal que verifica si todos en una lista son mayores de edad."""
    for edad in lista_edades:
        if not es_mayor(edad):
            return False
    return True

def existe_mayor(lista_edades):
    """Cuantificador existencial que verifica si al menos uno en la lista es mayor de edad."""
    for edad in lista_edades:
        if es_mayor(edad):
            return True
    return False

# Lista de edades para evaluar
grupo_edades = [22, 15, 34, 18, 17]

# Evaluar las funciones de predicado y cuantificadores
print("Evaluación de predicados y cuantificadores:")
print(f"Todos son mayores de edad: {todos_mayores(grupo_edades)}")  # Debería ser False
print(f"Al menos uno es mayor de edad: {existe_mayor(grupo_edades)}")  # Debería ser True

# Aplicando el predicado a una edad específica
edad_individual = 20
print(f"La persona de {edad_individual} años es mayor de edad: {es_mayor(edad_individual)}")  # Debería ser True
