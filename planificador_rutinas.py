import random

"Genera un plan de entrenamiento personalizado basado en material, nivel y días"
def generar_plan_entrenamiento(material_disponible, dias_entrenamiento, nivel_experiencia):
    "Diccionario de ejercicios organizados por material y grupos musculares"
    ejercicios = {
        "cuerpo_libre": {
            "piernas": ["Sentadillas", "Zancadas", "Puente de glúteos", "Sentadilla búlgara", "Step-ups", "Sentadillas isométricas"],
            "abdominales": ["Planchas", "Crunch abdominal", "Elevaciones de piernas", "Twist ruso", "Bicicleta abdominal", "Plancha lateral"],
            "pecho": ["Flexiones", "Flexiones inclinadas", "Flexiones diamante", "Flexiones declinadas"],
            "espalda": ["Superman", "Remo invertido", "Extensiones de espalda", "Pull-ups"],
            "brazos": ["Fondos de tríceps", "Curls con peso corporal", "Flexiones cerradas", "Plancha con levantamiento de brazo"]
        },
        "bandas": {
            "piernas": ["Sentadillas asistidas", "Zancadas con bandas", "Kickbacks", "Monster Walks", "Abducción de cadera"],
            "abdominales": ["Planchas con bandas", "Crunch con resistencia", "Twist ruso con bandas", "Elevaciones de piernas con bandas"],
            "pecho": ["Press de pecho con bandas", "Aperturas con bandas", "Flexiones asistidas con bandas"],
            "espalda": ["Remo con bandas", "Pull apart con bandas", "Face Pull con bandas"],
            "brazos": ["Curl de bíceps con bandas", "Extensión de tríceps con bandas", "Tríceps kickback con bandas"]
        },
        "pesas": {
            "piernas": ["Sentadillas con barra", "Peso muerto", "Prensa de piernas", "Zancadas con mancuernas", "Hip Thrust"],
            "abdominales": ["Crunch con peso", "Planchas con disco", "Russian Twist con peso", "Plancha con mancuerna"],
            "pecho": ["Press de banca", "Press inclinado", "Press con mancuernas", "Aperturas con mancuernas"],
            "espalda": ["Remo con barra", "Dominadas lastradas", "Pullover", "Remo con mancuerna"],
            "brazos": ["Curl de bíceps", "Extensión de tríceps", "Curl martillo", "Press cerrado"]
        }
    }

    "Calentamiento y estiramientos comunes para cualquier nivel"
    calentamiento = ["5 minutos de cardio ligero", "Movilidad articular"]
    estiramientos = ["Estiramiento dinámico para piernas", "Estiramiento dinámico para brazos"]

    "Tiempos de descanso recomendados por grupo muscular (en minutos)"
    descanso_por_zona = {
        "piernas": 5,
        "pecho": 3,
        "espalda": 3,
        "brazos": 2,
        "abdominales": 2
    }

    "Series recomendadas según el nivel de experiencia y días de entrenamiento"
    series_por_nivel = {
        1: {1: 15, 2: 8, 3: 8},
        2: {1: 20, 2: 14, 3: 15, 4: 12, 5: 10},
        3: {1: 30, 2: 20, 3: 25, 4: 20, 5: 16, 6: 15}
    }

    "Días máximos de entrenamiento según el nivel de experiencia"
    max_dias_por_nivel = {
        1: 3,
        2: 5,
        3: 6
    }

    "Validación del nivel de experiencia y días de entrenamiento seleccionados"
    if nivel_experiencia not in max_dias_por_nivel or dias_entrenamiento > max_dias_por_nivel[nivel_experiencia]:
        return "Error: combinación de nivel y días no permitida."

    "Cálculo de series totales y distribución entre grupos musculares"
    total_series = series_por_nivel[nivel_experiencia][dias_entrenamiento]
    grupos_musculares = ["piernas", "pecho", "espalda", "brazos", "abdominales"]
    series_por_grupo = total_series // len(grupos_musculares)
    series_sobrantes = total_series % len(grupos_musculares)

    "Inicialización del plan de entrenamiento y ejercicios utilizados"
    plan_entrenamiento = {}
    usados = set()  # Mantiene un registro de ejercicios ya asignados

    "Generación del plan diario"
    for dia in range(1, dias_entrenamiento + 1):
        plan_dia = []
        for i, grupo in enumerate(grupos_musculares):
            "Filtra ejercicios no usados del grupo actual"
            ejercicios_disponibles = [e for e in ejercicios[material_disponible][grupo] if e not in usados]
            if not ejercicios_disponibles:
                usados.clear()  # Reinicia si no hay más ejercicios disponibles
                ejercicios_disponibles = ejercicios[material_disponible][grupo]
            ejercicio = random.choice(ejercicios_disponibles)   # Selecciona un ejercicio aleatorio
            "Calcula las series asignadas al grupo muscular actual"
            series = series_por_grupo + (1 if i < series_sobrantes else 0)  # Distribuye las series sobrantes
            plan_dia.append((ejercicio, grupo, series))
            usados.add(ejercicio)
        plan_entrenamiento[f"Día {dia}"] = plan_dia

    "Retorna el plan completo con calentamiento y estiramientos"
    return {
        "calentamiento": calentamiento,
        "plan": plan_entrenamiento,
        "estiramientos": estiramientos,
        "descanso": descanso_por_zona
    }

def obtener_entrada_numerica(prompt, opciones_validas=None):
    "Función para validar y obtener una entrada numérica del usuario"
    while True:
        try:
            entrada = int(input(prompt))
            if opciones_validas and entrada not in opciones_validas:
                raise ValueError("Opción no válida.")
            return entrada
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    "Inicio del programa interactivo"
    print("\nBienvenido al generador de planes de entrenamiento")

    "Selección de material disponible"
    print("\nSelecciona el material disponible:")
    print("1 - Cuerpo libre")
    print("2 - Bandas")
    print("3 - Pesas")
    material_input = obtener_entrada_numerica("Ingresa el número correspondiente al material: ", opciones_validas=[1, 2, 3])
    material_map = {1: "cuerpo_libre", 2: "bandas", 3: "pesas"}
    material_disponible = material_map[material_input]

    "Selección del nivel de experiencia"
    print("\nSelecciona tu nivel de experiencia:")
    print("1 - Principiante (Máximo 3 días)")
    print("2 - Intermedio (Máximo 5 días)")
    print("3 - Avanzado (Máximo 6 días)")
    nivel_experiencia = obtener_entrada_numerica("Ingresa el número correspondiente a tu nivel: ", opciones_validas=[1, 2, 3])

    "Selección del número de días de entrenamiento"
    while True:
        dias_entrenamiento = obtener_entrada_numerica("\n¿Cuántos días a la semana quieres entrenar? (1-6): ", opciones_validas=range(1, 7))

        plan = generar_plan_entrenamiento(material_disponible, dias_entrenamiento, nivel_experiencia)

        if isinstance(plan, str):
            print(f"\n{plan}")
        else:
            break

    "Impresión del plan generado"
    print("\nCalentamiento:")
    for item in plan["calentamiento"]:
        print(f"- {item}")

    print("\nPlan de entrenamiento:")
    for dia, ejercicios in plan["plan"].items():
        print(f"\n{dia}:")
        for ejercicio, grupo, series in ejercicios:
            print(f"- {ejercicio} ({grupo}): {series} series")

    print("\nEstiramientos:")
    for item in plan["estiramientos"]:
        print(f"- {item}")

    print("\nDescanso por zona:")
    for zona, minutos in plan["descanso"].items():
        print(f"- {zona}: {minutos} minutos")
