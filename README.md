# Generador de Planes de Entrenamiento

Este programa genera un plan de entrenamiento personalizado basado en el material disponible, el nivel de experiencia y el número de días de entrenamiento que el usuario desea. Además, permite establecer un límite de tiempo (en minutos) para el entrenamiento diario y ajusta el número de series por grupo muscular para cumplir con ese límite.

## Características

- **Selección de material:** El usuario puede elegir entre entrenamiento de `cuerpo libre`, con `bandas` o con `pesas`.
- **Nivel de experiencia:**  
  - Principiante (máximo 3 días/semana)  
  - Intermedio (máximo 5 días/semana)  
  - Avanzado (máximo 6 días/semana)
- **Días de entrenamiento:** El usuario indica cuántos días a la semana desea entrenar, respetando las restricciones según el nivel.
- **Generación del plan:**  
  - Se asignan ejercicios a cada grupo muscular (piernas, pecho, espalda, brazos y abdominales) según el material elegido.
  - Se calculan las series totales según el nivel y los días, distribuyéndolas equitativamente entre los grupos.
- **Cálculo de tiempo:**  
  - Cada serie toma un tiempo fijo (2 minutos).
  - Cada grupo muscular añade descanso proporcional a la cantidad de series asignadas (descanso_por_grupo * número_de_series).
- **Límite de tiempo:**  
  - El usuario puede elegir un límite (30, 60, 90, 120 minutos o sin límite).
  - Si el tiempo del día más largo excede el límite, el programa reduce las series prioritizando mantener más series en grupos musculares de mayor importancia (piernas, pecho, espalda) y reduciendo primero abdominales y brazos.
  - Finalmente, se asegura que todos los días tengan la misma distribución de series por grupo, logrando uniformidad.

## Lógica de Prioridad

La optimización se realiza en base a prioridades:

- **Baja prioridad (se reduce primero):** Abdominales, Brazos.
- **Alta prioridad (se reduce al final):** Piernas, Pecho, Espalda.

Se utiliza una cola de prioridad (heap) para ir reduciendo series de los grupos menos prioritarios antes de ajustar los más prioritarios.

## Ejecución

1. Asegúrate de tener Python 3.x instalado.
2. Ejecuta el script desde la terminal:
   ```bash
   python planificador_rutinas.py
   ```

## Ejemplo de Salida

```
Bienvenido al generador de planes de entrenamiento

Selecciona el material disponible:
1 - Cuerpo libre
2 - Bandas
3 - Pesas
Ingresa el número correspondiente al material: 3

Selecciona tu nivel de experiencia:
1 - Principiante (Máximo 3 días)
2 - Intermedio (Máximo 5 días)
3 - Avanzado (Máximo 6 días)
Ingresa el número correspondiente a tu nivel: 1

¿Cuántos días a la semana quieres entrenar? (1-6): 1

Selecciona el límite de tiempo para tu entrenamiento (en minutos):
1 - 30 minutos
2 - 60 minutos
3 - 90 minutos
4 - 120 minutos
5 - Sin límite
Ingresa el número correspondiente al límite: 5

Calentamiento:
- 5 minutos de cardio ligero
- Movilidad articular

Plan de entrenamiento optimizado:

Día 1:
- Peso muerto (piernas): 3 series
- Press con mancuernas (pecho): 3 series
- Remo con mancuerna (espalda): 3 series
- Extensión de tríceps (brazos): 3 series
- Plancha con mancuerna (abdominales): 3 series

Estiramientos:
- Estiramiento dinámico para piernas
- Estiramiento dinámico para brazos

Descanso por zona:
- piernas: 3 minutos
- pecho: 2 minutos
- espalda: 2 minutos
- brazos: 1 minutos
- abdominales: 1 minutos

El tiempo estimado de cualquier día del plan es: 57 minutos
```