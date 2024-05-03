# Funciones de membresía para la temperatura
def baja_temperatura(temperatura):
    """Función de membresía para una temperatura baja."""
    if temperatura <= 18:
        return 1
    elif temperatura > 18 and temperatura < 22:
        return (22 - temperatura) / 4
    else:
        return 0

def temperatura_media(temperatura):
    """Función de membresía para una temperatura media."""
    if temperatura > 18 and temperatura <= 22:
        return (temperatura - 18) / 4
    elif temperatura > 22 and temperatura < 26:
        return (26 - temperatura) / 4
    else:
        return 0

def alta_temperatura(temperatura):
    """Función de membresía para una temperatura alta."""
    if temperatura >= 22 and temperatura <= 26:
        return (temperatura - 22) / 4
    elif temperatura > 26:
        return 1
    else:
        return 0

# Función para determinar la pertenencia a los conjuntos difusos
def determinar_pertenencia_temperatura(temperatura):
    """Determina la pertenencia a los conjuntos difusos de temperatura."""
    baja = baja_temperatura(temperatura)
    media = temperatura_media(temperatura)
    alta = alta_temperatura(temperatura)

    return baja, media, alta

# Ejemplo de uso
temperatura_actual = 24
print("Pertenencia a los conjuntos difusos (baja, media, alta):", determinar_pertenencia_temperatura(temperatura_actual))
