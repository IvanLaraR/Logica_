# Texto de entrada
texto = "El gato está sobre la mesa y el perro está debajo de la silla."

# Función para procesar el texto y extraer información relevante
def procesar_texto(texto):
    """Función que analiza el texto y extrae información relevante."""
    palabras = texto.split()  # Dividir el texto en palabras
    ubicaciones = []  # Lista para almacenar las ubicaciones de los objetos
    for i in range(len(palabras) - 1):
        if palabras[i] == "sobre":
            ubicaciones.append((palabras[i-1], "encima de", palabras[i+1]))
        elif palabras[i] == "debajo":
            ubicaciones.append((palabras[i-1], "debajo de", palabras[i+1]))
    return ubicaciones

# Llamada a la función de procesamiento de texto
ubicaciones = procesar_texto(texto)

# Imprimir la información relevante extraída del texto
print("Información relevante extraída del texto:")
for ubicacion in ubicaciones:
    print(f"{ubicacion[0]} está {ubicacion[1]} {ubicacion[2]}")
