import random
import heapq

def generar_plan_entrenamiento(material_disponible, dias_entrenamiento, nivel_experiencia):
    """
    Genera un plan de entrenamiento según el material disponible, días de entrenamiento y nivel de experiencia.
    """
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

    # Calentamiento, estiramientos y descansos
    calentamiento = ["5 minutos de cardio ligero", "Movilidad articular"]
    estiramientos = ["Estiramiento dinámico para piernas", "Estiramiento dinámico para brazos"]
    descanso_por_zona = {
        "piernas": 3,
        "pecho": 2,
        "espalda": 2,
        "brazos": 1,
        "abdominales": 1
    }

    # Series recomendadas según nivel de experiencia y días seleccionados
    series_por_nivel = {
        1: {1: 15, 2: 8, 3: 8},
        2: {1: 20, 2: 14, 3: 15, 4: 12, 5: 10},
        3: {1: 30, 2: 20, 3: 25, 4: 20, 5:16, 6:15}
    }

    # Máximo de días según nivel
    max_dias_por_nivel = {
        1: 3,
        2: 5,
        3: 6
    }

    # Validación de nivel y días
    if nivel_experiencia not in max_dias_por_nivel or dias_entrenamiento > max_dias_por_nivel[nivel_experiencia]:
        return "Error: combinación de nivel y días no permitida."

    # Cálculo de series totales y distribución uniforme entre grupos
    total_series = series_por_nivel[nivel_experiencia][dias_entrenamiento]
    grupos_musculares = ["piernas", "pecho", "espalda", "brazos", "abdominales"]
    series_por_grupo = total_series // len(grupos_musculares)
    series_sobrantes = total_series % len(grupos_musculares)

    plan_entrenamiento = {}
    usados = set()

    # Generación del plan: se distribuye un ejercicio por grupo al día y se asignan las series calculadas
    for dia in range(1, dias_entrenamiento + 1):
        plan_dia = []
        for i, grupo in enumerate(grupos_musculares):
            ejercicios_disponibles = [e for e in ejercicios[material_disponible][grupo] if e not in usados]
            # Si se quedan sin ejercicios nuevos, se vuelve a permitir su uso (usados.clear())
            if not ejercicios_disponibles:
                usados.clear()
                ejercicios_disponibles = ejercicios[material_disponible][grupo]
            ejercicio = random.choice(ejercicios_disponibles)
            series = series_por_grupo + (1 if i < series_sobrantes else 0)
            plan_dia.append((ejercicio, grupo, series))
            usados.add(ejercicio)
        plan_entrenamiento[f"Día {dia}"] = plan_dia

    return {
        "calentamiento": calentamiento,
        "plan": plan_entrenamiento,
        "estiramientos": estiramientos,
        "descanso": descanso_por_zona
    }

def calcular_tiempo_dia(ejercicios_dia, descanso_por_zona, tiempo_por_serie=2):
    """
    Calcula el tiempo total de un día de entrenamiento.

    Tiempo total = (Total de series * tiempo_por_serie) + sumatorio de (descanso_por_zona[grupo] * series_de_grupo)

    Así, cada grupo añade descanso en función del número de series que tenga asignadas.
    """
    total_series = sum(ser for _, _, ser in ejercicios_dia)
    tiempo_series = total_series * tiempo_por_serie
    series_por_grupo = {}
    for _, grupo, ser in ejercicios_dia:
        series_por_grupo[grupo] = series_por_grupo.get(grupo, 0) + ser

    # Descanso total sumando (descanso del grupo * número de series del grupo)
    tiempo_descanso = sum(descanso_por_zona[grupo] * series_por_grupo[grupo] for grupo in series_por_grupo)
    return tiempo_series + tiempo_descanso

def calcular_tiempo(plan, descanso_por_zona, tiempo_por_serie=2):
    """
    Calcula el tiempo máximo de entre todos los días del plan.
    Esto permite asegurar que el límite de tiempo (si existe) se cumpla en el día más largo.
    """
    tiempos = [calcular_tiempo_dia(ejercicios, descanso_por_zona, tiempo_por_serie) for ejercicios in plan.values()]
    return max(tiempos) if tiempos else 0

def obtener_entrada_numerica(prompt, opciones_validas=None):
    """
    Solicita una entrada numérica al usuario y valida que esté dentro de las opciones permitidas (si se da una lista).
    """
    while True:
        try:
            entrada = int(input(prompt))
            if opciones_validas and entrada not in opciones_validas:
                raise ValueError("Opción no válida.")
            return entrada
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intenta de nuevo.")

def optimizar_plan(plan, descanso_por_zona, limite_tiempo, tiempo_por_serie=2):
    """
    Optimiza el plan para cumplir con el límite de tiempo. La lógica es:
    1. Tomar el primer día como "patrón" de series por grupo.
    2. Intentar reducir series empezando por los grupos de baja prioridad (abdominales, brazos),
       manteniendo más series en grupos de alta prioridad (piernas, pecho, espalda).
    3. Una vez se obtiene un patrón de series por grupo que cumple con el límite, 
       aplicar ese patrón a todos los días, garantizando que todos los días tengan
       las mismas series por grupo.

    Prioridades:
    - Baja prioridad (se reduce primero): abdominales, brazos
    - Alta prioridad (se reduce al final): piernas, pecho, espalda
    """
    if limite_tiempo is None:
        # Sin límite, no es necesario optimizar
        return plan

    # Definir prioridades
    prioridad_baja = {"abdominales", "brazos"}  # prioridad 1
    prioridad_alta = {"piernas", "pecho", "espalda"}    # prioridad 2

    def asignar_prioridad(grupo):
        """
        Grupos de baja prioridad obtienen 1, alta prioridad obtienen 2.
        Como es un min-heap, primero se reducirán los grupos con prioridad 1.
        """
        if grupo in prioridad_baja:
            return 1
        else:
            return 2

    if not plan:
        return plan

    # Tomar el primer día como patrón
    primer_dia = list(plan.keys())[0]
    ejercicios_dia = plan[primer_dia]

    # Crear un diccionario con las series por grupo según el primer día
    patron_series = {}
    for _, grupo, ser in ejercicios_dia:
        patron_series[grupo] = ser

    def tiempo_dia_patron(patron):
        # Crea una lista ficticia del día con el patrón y calcula su tiempo
        dia_ficticio = [(None, g, s) for g, s in patron.items()]
        return calcular_tiempo_dia(dia_ficticio, descanso_por_zona, tiempo_por_serie)

    def tiempo_excede(patron):
        # Verifica si el patrón excede el límite de tiempo
        return tiempo_dia_patron(patron) > limite_tiempo

    # Si ya no excede el tiempo, no ajustamos nada.
    if not tiempo_excede(patron_series):
        return plan

    # Crear un heap para reducir las series de los grupos según prioridad
    heap = []
    for g, s in patron_series.items():
        p = asignar_prioridad(g)
        heapq.heappush(heap, (p, g, s))

    # Reducir series mientras se exceda el tiempo
    while tiempo_excede(patron_series):
        if not heap:
            # No se pueden reducir más series, no es posible cumplir el límite
            print("No es posible ajustar el plan al límite de tiempo dado.")
            break
        p, g, s = heapq.heappop(heap)
        if s > 1:
            # Reducimos en una serie
            s -= 1
            patron_series[g] = s
            if s > 1:
                # Si aún se puede reducir más adelante, lo reinsertamos al heap
                heapq.heappush(heap, (p, g, s))
        else:
            # Si ya está en 1, no lo volvemos a insertar, no se puede reducir más.
            patron_series[g] = s

        # Si ya no hay nada en el heap y sigue excediendo:
        if not heap and tiempo_excede(patron_series):
            print("No es posible ajustar el plan al límite de tiempo dado.")
            break

    # Ahora aplicamos el patrón final a todos los días, asegurando igualdad de series
    for dia, ejercicios in plan.items():
        # Ajustar las series según el patrón optimizado
        for i, (ej, gr, se) in enumerate(ejercicios):
            plan[dia][i] = (ej, gr, patron_series[gr])

    return plan

# Ejecución principal
if __name__ == "__main__":
    print("\nBienvenido al generador de planes de entrenamiento")

    # Selección de material
    print("\nSelecciona el material disponible:")
    print("1 - Cuerpo libre")
    print("2 - Bandas")
    print("3 - Pesas")
    material_input = obtener_entrada_numerica("Ingresa el número correspondiente al material: ", opciones_validas=[1, 2, 3])
    material_map = {1: "cuerpo_libre", 2: "bandas", 3: "pesas"}
    material_disponible = material_map[material_input]

    # Selección de nivel de experiencia
    print("\nSelecciona tu nivel de experiencia:")
    print("1 - Principiante (Máximo 3 días)")
    print("2 - Intermedio (Máximo 5 días)")
    print("3 - Avanzado (Máximo 6 días)")
    nivel_experiencia = obtener_entrada_numerica("Ingresa el número correspondiente a tu nivel: ", opciones_validas=[1, 2, 3])

    # Selección de días de entrenamiento
    while True:
        dias_entrenamiento = obtener_entrada_numerica("\n¿Cuántos días a la semana quieres entrenar? (1-6): ", opciones_validas=range(1, 7))
        plan = generar_plan_entrenamiento(material_disponible, dias_entrenamiento, nivel_experiencia)
        if isinstance(plan, str):
            # Error en la combinación seleccionada
            print(f"\n{plan}")
        else:
            break

    # Selección de límite de tiempo
    print("\nSelecciona el límite de tiempo para tu entrenamiento (en minutos):")
    print("1 - 30 minutos")
    print("2 - 60 minutos")
    print("3 - 90 minutos")
    print("4 - 120 minutos")
    print("5 - Sin límite")
    limite_opcion = obtener_entrada_numerica("Ingresa el número correspondiente al límite: ", opciones_validas=[1, 2, 3, 4, 5])
    limite_map = {1: 30, 2: 60, 3: 90, 4: 120, 5: None}
    limite_tiempo = limite_map[limite_opcion]

    # Optimizar el plan según el límite de tiempo
    plan_optimizado = optimizar_plan(plan["plan"], plan["descanso"], limite_tiempo, tiempo_por_serie=2)

    # Imprimir resultado
    print("\nCalentamiento:")
    for item in plan["calentamiento"]:
        print(f"- {item}")

    print("\nPlan de entrenamiento optimizado:")
    for dia, ejercicios in plan_optimizado.items():
        print(f"\n{dia}:")
        for ejercicio, grupo, series in ejercicios:
            print(f"- {ejercicio} ({grupo}): {series} series")

    print("\nEstiramientos:")
    for item in plan["estiramientos"]:
        print(f"- {item}")

    print("\nDescanso por zona:")
    for zona, minutos in plan["descanso"].items():
        print(f"- {zona}: {minutos} minutos")

    tiempo_final = calcular_tiempo(plan_optimizado, plan["descanso"], tiempo_por_serie=2)
    print(f"\nEl tiempo estimado de cualquier día del plan es: {tiempo_final} minutos")