# Base de conocimientos de tareas y reglas de dependencia
base_conocimientos_tareas = {
    'lavar_platos': ['secar_platos'],
    'secar_platos': ['guardar_platos'],
    'guardar_platos': [],
    'cocinar': ['lavar_platos', 'guardar_utensilios'],
    'guardar_utensilios': [],
    'limpiar_cocina': ['guardar_utensilios']
}

# Función para el encadenamiento hacia adelante
def encadenamiento_hacia_adelante(tareas_pendientes, reglas):
    """Realiza el encadenamiento hacia adelante para planificar las tareas."""
    tareas_realizadas = []
    while tareas_pendientes:
        tarea_actual = tareas_pendientes.pop(0)
        if tarea_actual in reglas:
            tareas_pendientes.extend(reglas[tarea_actual])
        tareas_realizadas.append(tarea_actual)
    return tareas_realizadas

# Función para el encadenamiento hacia atrás
def encadenamiento_hacia_atras(tarea_final, reglas):
    """Realiza el encadenamiento hacia atrás para planificar las tareas."""
    tareas_pendientes = [tarea_final]
    tareas_realizadas = []
    while tareas_pendientes:
        tarea_actual = tareas_pendientes.pop()
        if tarea_actual in reglas:
            tareas_pendientes.extend(reglas[tarea_actual])
        tareas_realizadas.append(tarea_actual)
    return tareas_realizadas

# Ejemplo de uso del encadenamiento hacia adelante
tareas_por_hacer = ['cocinar']
tareas_realizadas_adelante = encadenamiento_hacia_adelante(tareas_por_hacer, base_conocimientos_tareas)
print("Tareas realizadas mediante encadenamiento hacia adelante:")
print(tareas_realizadas_adelante)

# Ejemplo de uso del encadenamiento hacia atrás
tarea_objetivo = 'lavar_platos'
tareas_realizadas_atras = encadenamiento_hacia_atras(tarea_objetivo, base_conocimientos_tareas)
print("\nTareas realizadas mediante encadenamiento hacia atrás:")
print(tareas_realizadas_atras)
