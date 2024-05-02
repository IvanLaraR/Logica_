# Definición de las tareas y su secuencia de ejecución
tareas = ["Recoger basura", "Comprar víveres", "Pagar facturas", "Hacer ejercicio", "Cocinar la cena"]

# Función para planificar la ejecución de las tareas
def planificar_tareas(tareas):
    """Función que planifica la ejecución de las tareas en orden."""
    print("Planificación de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"Paso {i}: {tarea}")
    print("¡Tareas planificadas correctamente!")

# Llamada a la función de planificación
planificar_tareas(tareas)
