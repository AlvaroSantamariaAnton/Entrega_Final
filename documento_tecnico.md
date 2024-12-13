# Documento Técnico del Proyecto

Este documento describe el proyecto, los algoritmos empleados, la justificación de su elección y un breve análisis de eficiencia.

## Descripción del Proyecto

El proyecto consiste en un generador de planes de entrenamiento personalizado. El usuario proporciona:

- El material disponible (cuerpo libre, bandas o pesas).
- Su nivel de experiencia (principiante, intermedio o avanzado).
- El número de días de entrenamiento por semana.
- Un límite de tiempo diario deseado (30, 60, 90, 120 minutos o sin límite).

Con estos datos, el programa crea un plan con ejercicios distribuidos en distintos grupos musculares (piernas, pecho, espalda, brazos, abdominales). Además, se calcula el tiempo total requerido por día, teniendo en cuenta el tiempo por serie y los descansos proporcionales al número de series por grupo.

Si el tiempo estimado supera el límite establecido, se ajusta el número de series con el objetivo de cumplir dicho límite. Finalmente, se garantiza que todos los días del plan tengan la misma distribución de series por grupo muscular, logrando uniformidad.

## Algoritmos Empleados

1. **Asignación Inicial de Ejercicios y Series**:  
   Se parte de un conjunto predeterminado de ejercicios por material y grupo muscular.  
   - Se elige un ejercicio por grupo para cada día, evitando repeticiones hasta agotar las opciones.  
   - Se calculan las series totales en función del nivel y los días de entrenamiento, repartiéndolas equitativamente entre los grupos.

   Este proceso es principalmente aleatorio (selección con `random.choice`) y la complejidad es O(días * número_de_grupos), que es muy bajo, dado que el número de días (máximo 6) y el número de grupos (5) son constantes.

2. **Cálculo de Tiempo por Día**:  
   Para cada día se suma el tiempo de las series y el descanso. Las operaciones son simples sumas y multiplicaciones, con complejidad O(n) en función del número total de ejercicios diarios (constante, ya que siempre hay 5 grupos por día).

3. **Optimización de Series con Cola de Prioridad (Heap)**:  
   Cuando se excede el límite de tiempo, se utiliza una cola de prioridad (`heapq` en Python) para determinar qué series reducir primero.  
   
   **Lógica del algoritmo**:
   - Primero se determina un "patrón" de series por grupo usando el primer día del plan.
   - Se insertan los grupos musculares en un min-heap donde la prioridad más baja se asigna a los grupos de baja prioridad (abdominales, brazos). Estos serán reducidos primero.
   - Mientras el tiempo exceda el límite y existan grupos con series por encima de 1, se extrae del heap el grupo con prioridad más baja, se reduce en una serie, y si sigue siendo reducible, se reinsertan.
   - Este proceso se repite hasta cumplir el límite de tiempo o agotar las posibilidades.

   La complejidad de esta optimización depende del número de grupos (5) y de las series totales. Sin embargo, dado el número fijo y reducido de grupos, el número de operaciones en el heap es insignificante a nivel de escalabilidad. Insertar y extraer en el heap es O(log n), donde n es el número de grupos, que en este caso es constante y muy bajo. Por lo tanto, la optimización es muy eficiente.

4. **Uniformidad de Días**:  
   Una vez se obtiene una distribución optimizada de series por grupo para el patrón, se aplica la misma a todos los días. Esto es una simple reasignación de valores, con complejidad O(días * grupos), nuevamente muy reducida.

## Justificación de la Elección de Algoritmos

- **Selección de Ejercicios y Series**: Se utiliza un enfoque simple y aleatorio porque el problema no demanda un algoritmo complejo. La tarea principal es distribuir ejercicios y series uniformemente, algo trivial dado el tamaño reducido del problema.

- **Heap para Prioridades**:  
  Se emplea una cola de prioridad porque ofrece una forma directa y eficiente de siempre extraer primero el grupo con menor prioridad (y por ende, el que se reducirá en series antes que los demás).  
  Otra estructura (como listas ordenadas) podría funcionar, pero resultaría menos eficiente o menos limpia conceptualmente. El heap permite priorizar reducciones sin necesidad de reordenamientos costosos ni de implementar estructuras más complejas.

- **Reducción Iterativa**:  
  La reducción de series se hace de forma iterativa y paso a paso, recalculando el tiempo tras cada reducción. Aunque se podría concebir un cálculo más directo (por ejemplo, calcular de un solo golpe cuántas series se deben quitar de los grupos de baja prioridad), la implementación escalonada es más flexible, fácil de mantener y comprender, y da margen a futuras extensiones (por ejemplo, distintos criterios de prioridad).

## Análisis de Eficiencia

- **Tamaño del Problema**:  
  El problema trabaja con:
  - Un máximo de 6 días.
  - 5 grupos musculares.
  - Un conjunto finito de ejercicios (no más de unos pocos por grupo).

  Este es un problema de muy pequeña escala. Por ello, la eficiencia computacional no es una preocupación real: todas las operaciones se ejecutarán en una fracción de segundo incluso en un hardware modesto.

- **Complejidad Teórica**:  
  - Generar el plan: O(días * grupos) = O(1), ya que días ≤ 6 y grupos = 5.
  - Calcular el tiempo: O(días * grupos) = O(1).
  - Optimización con heap: O(k * log(g)), donde k es el número de reducciones y g el número de grupos (5). Dado que g es constante, esta operación es O(k). El valor de k está limitado por el total de series asignadas, también acotado por la lógica interna del programa.

- **Conclusión Sobre Eficiencia**:  
  El programa es sumamente eficiente. Debido a la naturaleza acotada del problema (pocos días, pocos grupos), el rendimiento es muy alto y no se necesitan algoritmos más complejos. La elección de un heap para la prioridad es conceptualmente clara y eficiente a nivel de implementación, aunque prácticamente cualquier aproximación funcionaría con el pequeño tamaño del problema.

## Conclusión

El proyecto implementa una lógica clara para generar planes de entrenamiento, calcular su tiempo y optimizarlos. La utilización de una cola de prioridad para gestionar las reducciones de series proporciona una manera limpia y estructurada de abordar el problema de priorización. El resultado es un programa simple, rápido y fácil de entender que cumple con los objetivos planteados.