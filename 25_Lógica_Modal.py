# Base de conocimientos de preferencias de invitados a la fiesta
preferencias_invitados = {
    'ivan': {'música_pop', 'baile'},
    'Juan': {'música_rock', 'karaoke'},
    'María': {'música_electrónica', 'juegos_de_mesa'}
}

# Función para evaluar si un invitado tiene una preferencia modal específica
def invitado_tiene_preferencia(invitado, preferencia_modal):
    """Evalúa si un invitado tiene una preferencia modal específica."""
    if invitado in preferencias_invitados:
        return preferencia_modal in preferencias_invitados[invitado]
    else:
        return False

# Función para encontrar invitados con una preferencia modal específica
def encontrar_invitados_con_preferencia(preferencia_modal):
    """Encuentra invitados con una preferencia modal específica."""
    invitados_con_preferencia = []
    for invitado, preferencias in preferencias_invitados.items():
        if preferencia_modal in preferencias:
            invitados_con_preferencia.append(invitado)
    return invitados_con_preferencia

# Ejemplo de uso
preferencia_modal_evaluar = 'música_pop'
print(f"¿Ivan tiene preferencia por la música {preferencia_modal_evaluar}?", invitado_tiene_preferencia('Ana', preferencia_modal_evaluar))
print(f"Invitados con preferencia por la música {preferencia_modal_evaluar}: {encontrar_invitados_con_preferencia(preferencia_modal_evaluar)}")
