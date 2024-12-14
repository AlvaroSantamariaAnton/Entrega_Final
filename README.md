# Generador de Planes de Entrenamiento

Este programa genera un plan de entrenamiento personalizado según el material disponible, el nivel de experiencia y el número de días de entrenamiento. Además, permite establecer un límite de tiempo diario y ajusta el número de series por grupo muscular para cumplir con dicho límite.

## Características

- **Selección de material:** El usuario puede elegir entre `cuerpo libre`, `bandas` o `pesas`.
- **Nivel de experiencia:**  
  - Principiante (máximo 3 días/semana)  
  - Intermedio (máximo 5 días/semana)  
  - Avanzado (máximo 6 días/semana)
- **Días de entrenamiento:** El usuario indica cuántos días desea entrenar por semana, respetando el máximo según su nivel.
- **Generación del plan:**  
  - Se asigna un ejercicio por grupo muscular (piernas, pecho, espalda, brazos, abdominales) para cada día.
  - Se calculan las series totales según el nivel y los días, distribuyéndolas equitativamente entre los grupos.
- **Cálculo del tiempo:**  
  - Cada serie tarda 2 minutos.
  - El descanso se calcula multiplicando el descanso base por el número de series de cada grupo.
- **Límite de tiempo:**  
  - Opciones: 30, 60, 90, 120 minutos o sin límite.
  - Si el tiempo total excede el límite, se reducen las series, primero de los grupos de menor prioridad (abdominales, brazos) y luego de los de mayor prioridad (piernas, pecho, espalda).
  - Para evitar que siempre se reduzcan las series del mismo grupo de igual prioridad, se utiliza un contador de desempate, asegurando un reparto más equitativo de las reducciones.
  - Finalmente, se garantiza que todos los días tengan la misma distribución de series por grupo, logrando uniformidad.

## Lógica de Prioridad

La optimización de las series se basa en una cola de prioridad (heap):

- **Baja prioridad:** Abdominales, Brazos (se reducen primero).
- **Alta prioridad:** Piernas, Pecho, Espalda (se mantienen mejor).

La cola de prioridad asegura que primero se reduzcan las series de grupos con menor prioridad. Además, se emplea un contador de desempate para repartir las reducciones equitativamente entre grupos con la misma prioridad, evitando que uno solo se vea afectado repetidamente.

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