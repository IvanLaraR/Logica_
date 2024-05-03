# Funciones de membresía para la luminosidad
def oscuridad(luminosidad):
    """Función de membresía para la oscuridad."""
    if luminosidad <= 50:
        return 1
    elif luminosidad > 50 and luminosidad < 100:
        return (100 - luminosidad) / 50
    else:
        return 0

def luz_media(luminosidad):
    """Función de membresía para una luminosidad media."""
    if luminosidad > 50 and luminosidad <= 100:
        return (luminosidad - 50) / 50
    elif luminosidad > 100 and luminosidad < 150:
        return (150 - luminosidad) / 50
    else:
        return 0

def mucha_luz(luminosidad):
    """Función de membresía para mucha luminosidad."""
    if luminosidad >= 100 and luminosidad <= 150:
        return (luminosidad - 100) / 50
    elif luminosidad > 150:
        return 1
    else:
        return 0

# Funciones de inferencia difusa
def inferir_intensidad_iluminacion(luminosidad):
    """Infiere la intensidad de iluminación basada en la luminosidad."""
    oscuridad_val = oscuridad(luminosidad)
    luz_media_val = luz_media(luminosidad)
    mucha_luz_val = mucha_luz(luminosidad)

    # Reglas de inferencia
    intensidad_baja = min(oscuridad_val, mucha_luz_val)
    intensidad_media = luz_media_val
    intensidad_alta = min(luz_media_val, mucha_luz_val)

    return intensidad_baja, intensidad_media, intensidad_alta

# Ejemplo de uso
luminosidad_actual = 80
print("Inferencia de la intensidad de iluminación (baja, media, alta):", inferir_intensidad_iluminacion(luminosidad_actual))
