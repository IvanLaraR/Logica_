# Ejemplos de entrada y salida
ejemplos = [
    {"entrada": "llueve", "salida": "usar paraguas"},
    {"entrada": "hace sol", "salida": "usar gafas de sol"},
    {"entrada": "hace frío", "salida": "usar abrigo"},
    {"entrada": "hace calor", "salida": "usar ropa ligera"}
]

# Función para aprender reglas a partir de ejemplos
def aprender_reglas(ejemplos):
    """Función que aprende reglas simples a partir de ejemplos."""
    reglas_aprendidas = {}
    for ejemplo in ejemplos:
        entrada = ejemplo["entrada"]
        salida = ejemplo["salida"]
        reglas_aprendidas[entrada] = salida
    return reglas_aprendidas

# Llamada a la función de aprendizaje
reglas_aprendidas = aprender_reglas(ejemplos)

# Imprimir las reglas aprendidas
print("Reglas aprendidas:")
for entrada, salida in reglas_aprendidas.items():
    print(f"Si {entrada}, entonces {salida}")
