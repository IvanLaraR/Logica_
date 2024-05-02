# Definición de las funciones para simular la lógica modal, temporal y difusa

def es_posible(condicion):
    """Función que simula la lógica modal, indicando si una condición es posible."""
    return condicion

def es_futuro(tiempo):
    """Función que simula la lógica temporal, indicando si un tiempo es futuro."""
    return tiempo > 0

def es_verdadero_difuso(valor, umbral):
    """Función que simula la lógica difusa, indicando si un valor es verdadero difuso según un umbral."""
    return valor >= umbral

# Ejemplos de aplicación de las funciones

# Lógica modal
print("Lógica Modal:")
print("Es posible que llueva:", es_posible(True))  # Puede ser verdadero o falso

# Lógica temporal
print("\nLógica Temporal:")
print("El tiempo 5 es futuro:", es_futuro(5))  # Verdadero si el tiempo es positivo

# Lógica difusa
print("\nLógica Difusa:")
umbral_difuso = 0.5
print("El valor 0.7 es verdadero difuso con un umbral de 0.5:", es_verdadero_difuso(0.7, umbral_difuso))  # Verdadero si el valor es mayor o igual al umbral
