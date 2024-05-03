# Base de conocimientos de habilidades de empleados
base_conocimientos_habilidades = {
    'Ana': {'programacion', 'diseño', 'gestion_proyectos'},
    'Juan': {'programacion', 'testing', 'gestion_proyectos'},
    'María': {'diseño', 'gestion_proyectos', 'comunicacion'}
}

# Función para evaluar si un empleado tiene cierta habilidad
def empleado_tiene_habilidad(empleado, habilidad):
    """Evalúa si un empleado tiene cierta habilidad."""
    if empleado in base_conocimientos_habilidades:
        return habilidad in base_conocimientos_habilidades[empleado]
    else:
        return False

# Función para encontrar empleados con una habilidad específica
def encontrar_empleados_con_habilidad(habilidad):
    """Encuentra empleados con una habilidad específica."""
    empleados_con_habilidad = []
    for empleado, habilidades in base_conocimientos_habilidades.items():
        if habilidad in habilidades:
            empleados_con_habilidad.append(empleado)
    return empleados_con_habilidad

# Ejemplo de uso
habilidad_evaluar = 'programacion'
print(f"¿Ana tiene la habilidad de {habilidad_evaluar}?", empleado_tiene_habilidad('Ana', habilidad_evaluar))
print(f"Empleados con la habilidad de {habilidad_evaluar}: {encontrar_empleados_con_habilidad(habilidad_evaluar)}")
