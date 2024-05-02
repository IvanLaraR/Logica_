# Función para realizar unificación de términos
def unificar(termino1, termino2):
    """Realiza la unificación de dos términos."""
    if isinstance(termino1, str) and isinstance(termino2, str):
        if termino1 == termino2:
            return {}
        elif es_variable(termino1):
            return {termino1: termino2}
        elif es_variable(termino2):
            return {termino2: termino1}
        else:
            return None
    elif isinstance(termino1, list) and isinstance(termino2, list) and len(termino1) == len(termino2):
        unificacion = {}
        for i in range(len(termino1)):
            unificacion_parcial = unificar(termino1[i], termino2[i])
            if unificacion_parcial is None:
                return None
            unificacion.update(unificacion_parcial)
        return unificacion
    else:
        return None

# Función para verificar si un término es una variable
def es_variable(termino):
    """Verifica si un término es una variable."""
    return isinstance(termino, str) and termino.islower()

# Ejemplo de uso
contacto1 = ['nombre', 'Juan', 'telefono', '123456789']
contacto2 = ['nombre', 'Pedro', 'telefono', '987654321']

unificacion_resultado = unificar(contacto1, contacto2)

if unificacion_resultado is not None:
    print("Los contactos pueden unificarse con las siguientes asignaciones:")
    for variable, valor in unificacion_resultado.items():
        print(f"{variable} = {valor}")
else:
    print("Los contactos no pueden unificarse.")
