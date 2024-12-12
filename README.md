# Generador de Planes de Entrenamiento

Este programa permite generar planes de entrenamiento personalizados basados en el material disponible, el nivel de experiencia y la cantidad de días de entrenamiento deseados. Es ideal para usuarios que buscan estructurar su rutina de ejercicios de manera eficiente o buscan una base sobre la que crear su propio plan.

## Funcionalidades Principales

1. **Selección de Material**: El programa ofrece planes específicos para tres tipos de equipamiento:
   - **Cuerpo libre** (sin equipamiento).
   - **Bandas de resistencia**.
   - **Pesas** (mancuernas y barras).

2. **Personalización por Nivel de Experiencia**:
   - Principiante (máximo 3 días por semana).
   - Intermedio (máximo 5 días por semana).
   - Avanzado (máximo 6 días por semana).

3. **Generación Automática del Plan**:
   - El programa distribuye ejercicios entre los grupos musculares principales (piernas, abdominales, pecho, espalda y brazos).
   - Ajusta el número de series según el nivel y los días seleccionados.
   - Incluye calentamiento, estiramientos y tiempos de descanso sugeridos por zona muscular.

## Requisitos

- Python 3.x instalado.
- Biblioteca estándar de Python (no se requieren dependencias externas).

## Uso

1. Clona o descarga este repositorio.
2. Ejecuta el script `plan_entrenamiento.py`:
   ```bash
   python plan_entrenamiento.py
   ```
3. Sigue las instrucciones interactivas en la consola:
   - Selecciona el tipo de material disponible.
   - Indica tu nivel de experiencia.
   - Especifica la cantidad de días que deseas entrenar por semana.
4. Revisa el plan de entrenamiento generado, que incluirá:
   - Calentamiento recomendado.
   - Plan detallado para cada día.
   - Estiramientos sugeridos.
   - Tiempos de descanso por grupo muscular.

## Estructura del Proyecto

- **`plan_entrenamiento.py`**: Contiene el código principal del programa.
- **`README.md`**: Documentación del proyecto.

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

Calentamiento:
- 5 minutos de cardio ligero
- Movilidad articular

Plan de entrenamiento:

Día 1:
- Sentadillas con barra (piernas): 3 series
- Aperturas con mancuernas (pecho): 3 series
- Dominadas lastradas (espalda): 3 series
- Curl de bíceps (brazos): 3 series
- Crunch con peso (abdominales): 3 series

Estiramientos:
- Estiramiento dinámico para piernas
- Estiramiento dinámico para brazos

Descanso por zona:
- piernas: 5 minutos
- pecho: 3 minutos
- espalda: 3 minutos
- brazos: 2 minutos
- abdominales: 2 minutos
```

## Personalización

Si deseas modificar los ejercicios o las configuraciones predeterminadas, edita el diccionario `ejercicios` o las variables relacionadas en el archivo `plan_entrenamiento.py`.