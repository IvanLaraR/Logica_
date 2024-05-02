# Definición de funciones básicas de lógica proposicional

def y_logico(verdadero, falso):
    """Función que implementa la operación lógica AND."""
    return verdadero and falso

def o_logico(verdadero, falso):
    """Función que implementa la operación lógica OR."""
    return verdadero or falso

def no_logico(verdadero):
    """Función que implementa la operación lógica NOT."""
    return not verdadero

def implica_logico(condicion, resultado):
    """Función que implementa la operación lógica IMPLICA (condicion implica resultado)."""
    return not condicion or resultado

# Variables proposicionales con nombres comunes
condicion_verdadera = True  # Esta variable está configurada como verdadera
condicion_falsa = False     # Esta variable está configurada como falsa

# Uso de las funciones lógicas para evaluar expresiones
resultado_y = y_logico(condicion_verdadera, condicion_falsa)
resultado_o = o_logico(condicion_verdadera, condicion_falsa)
resultado_no = no_logico(condicion_verdadera)
resultado_implica = implica_logico(condicion_verdadera, condicion_falsa)

# Imprimir los resultados de las operaciones lógicas
print(f"Resultado de condicion_verdadera Y condicion_falsa: {resultado_y}")
print(f"Resultado de condicion_verdadera O condicion_falsa: {resultado_o}")
print(f"Resultado de NO condicion_verdadera: {resultado_no}")
print(f"Resultado de condicion_verdadera IMPLICA condicion_falsa: {resultado_implica}")
