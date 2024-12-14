# Documento Técnico del Proyecto

Este documento describe el proyecto, los algoritmos empleados, la justificación de su elección, así como un análisis de eficiencia del enfoque.

## Descripción del Proyecto

El proyecto consiste en un generador de planes de entrenamiento personalizado. El usuario proporciona:

- El material disponible (cuerpo libre, bandas o pesas).
- Su nivel de experiencia (principiante, intermedio o avanzado).
- El número de días de entrenamiento por semana.
- Un límite de tiempo diario deseado (30, 60, 90, 120 minutos o sin límite).

Con estos datos, el programa crea un plan con ejercicios distribuidos en distintos grupos musculares (piernas, pecho, espalda, brazos, abdominales). Además, se calcula el tiempo total requerido por día, teniendo en cuenta el tiempo por serie (2 minutos/serie) y los descansos proporcionales al número de series por grupo.

Si el tiempo estimado supera el límite establecido, se ajusta el número de series para cumplir con dicho límite. Finalmente, se garantiza que todos los días del plan tengan la misma distribución de series por grupo muscular, logrando uniformidad.

## Algoritmos Empleados

1. **Asignación Inicial de Ejercicios y Series**:  
   Se selecciona un ejercicio por grupo y por día de forma aleatoria. Se calculan las series totales según el nivel y los días, repartiéndolas equitativamente entre los grupos.  
   Dado que el número de días (máximo 6) y el de grupos (5) es fijo y reducido, la complejidad es despreciable a nivel práctico.

2. **Cálculo de Tiempo por Día**:  
   Para cada día, el tiempo se calcula como:  
   `(Total_series * 2 minutos) + Σ(descanso_por_grupo * series_grupo)`.  
   Este cálculo es constante dado el número fijo de grupos (5).

3. **Optimización de Series con Cola de Prioridad (Heap)**:  
   Cuando el tiempo máximo diario excede el límite, se optimiza el número de series usando una cola de prioridad:
   - Se determina un "patrón" diario a partir del primer día, extrayendo el número de series por grupo.
   - Cada grupo se inserta en un min-heap con la siguiente información: `(prioridad, contador_desempate, grupo, series)`.
   - Las prioridades se asignan así:
     - Baja prioridad: abdominales, brazos.
     - Alta prioridad: piernas, pecho, espalda.
   
   El `contador_desempate` se incrementa cada vez que se reduce y reinserta un grupo con la misma prioridad, garantizando que, entre grupos de igual prioridad, la reducción de series se reparta de manera más equitativa. Así, no siempre se reduce primero el mismo grupo si existen varios con la misma prioridad.

   El proceso es iterativo:  
   - Mientras se exceda el límite de tiempo, se extrae el grupo con menor prioridad (y según su contador de desempate), se reduce una serie si es posible y se reinserta.
   - Una vez logrado el ajuste, se aplica el patrón final a todos los días, manteniendo la uniformidad.

4. **Uniformidad de Días**:  
   Una vez determinado el patrón optimizado, este se replica en todos los días, asegurando que la configuración de series por grupo sea idéntica en cada jornada.

## Justificación de la Elección de Algoritmos

- **Selección de Ejercicios y Series**:  
  Se utiliza un enfoque simple y aleatorio para elegir los ejercicios, dado el tamaño reducido del problema. La distribución de series es uniforme, lo que hace innecesario un algoritmo más complejo.

- **Uso del Heap para Prioridades y Reparto Equitativo**:  
  El heap proporciona una forma ordenada de determinar qué series reducir primero. Al asignar prioridades numéricas y un contador de desempate, aseguramos que la reducción se distribuya de forma justa entre grupos de igual prioridad, sin favorecer sistemáticamente a uno sobre otro.

- **Reducción Iterativa**:  
  La reducción progresiva, serie por serie, permite controlar el tiempo final de modo fino y flexible. Esta estrategia resulta clara y fácil de mantener. Además, la iteración y el heap, aplicados a un problema con muy pocos grupos y días, no implican un costo computacional significativo.

## Análisis de Eficiencia

- **Tamaño del Problema**:  
  Con hasta 6 días y 5 grupos, el problema es muy pequeño. Esto implica que, incluso con múltiples iteraciones, el tiempo de ejecución es extremadamente bajo.

- **Complejidad Teórica**:  
  - Generar el plan: O(días * grupos) = O(1) en la práctica (días ≤ 6, grupos = 5).
  - Calcular el tiempo diario: O(grupos) = O(1).
  - Optimización con heap: O(k * log(g)) donde g = 5 y k es el número de reducciones. Dado que g es constante (5), se considera O(k). Además, k está acotado por el número total de series disponibles.

- **Conclusión sobre Eficiencia**:  
  El programa es sumamente eficiente. Debido a la escala reducida del problema, las operaciones se ejecutan en fracciones de segundo. El heap y el contador de desempate no añaden una complejidad significativa, manteniendo la eficiencia del sistema.

## Conclusión

El proyecto implementa una lógica clara y eficiente para generar, calcular y optimizar planes de entrenamiento. El uso de una cola de prioridad con un contador de desempate garantiza una distribución justa de las reducciones entre grupos de igual prioridad. Esta solución es simple, rápida y fácil de entender, cumpliendo así con los objetivos planteados.