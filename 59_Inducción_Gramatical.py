# Definir una lista de frases de ejemplo
frases_ejemplo = [
    "los perros ladran",
    "los gatos maullan",
    "los pájaros cantan",
    "los peces nadan"
]

# Función para extraer reglas gramaticales a partir de las frases de ejemplo
def induccion_gramatical(frases):
    reglas_gramaticales = {}

    # Recorrer cada frase
    for frase in frases:
        # Dividir la frase en palabras
        palabras = frase.split()

        # Tomar la primera palabra como el sujeto
        sujeto = palabras[0]

        # Tomar las palabras restantes como el predicado
        predicado = " ".join(palabras[1:])

        # Agregar la regla gramatical al diccionario
        if sujeto in reglas_gramaticales:
            reglas_gramaticales[sujeto].append(predicado)
        else:
            reglas_gramaticales[sujeto] = [predicado]

    return reglas_gramaticales

# Ejemplo de uso
reglas = induccion_gramatical(frases_ejemplo)

# Imprimir las reglas gramaticales resultantes
print("Reglas Gramaticales:")
for sujeto, predicados in reglas.items():
    for predicado in predicados:
        print("{} -> {}".format(sujeto, predicado))
