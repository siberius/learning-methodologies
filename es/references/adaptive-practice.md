# Práctica adaptativa y continuidad

Consulta para sesiones repetidas, planificación o selección de dificultad. Distingue cuándo repasar, qué tarea presentar y cuánta ayuda ofrecer. No requieren el mismo modelo.

| Necesidad | Implementación pequeña | Ampliación opcional y requisitos |
| --- | --- | --- |
| Una actividad | Tareas revisadas, secuencia explícita, ayuda y estado de sesión | Normalmente sin modelo persistente del estudiante |
| Recuperación tras días | Calendario explícito e historial local | FSRS para ítems estables y eventos de repaso interpretables |
| Elegir dificultad | Niveles revisados y reglas transparentes | Elo con datos adecuados, incertidumbre y calibración |
| Dependencias entre habilidades | Mapa con evidencia independiente | BKT o IRT con modelo defendible, datos y validación |
| Plan prolongado | Objetivo, tiempo disponible, fase actual y tarea siguiente | Hitos revisables, preguntas pendientes y fechas de repaso |

Explica la función antes del algoritmo. Conserva el stack existente; no instales planificador, servidor o cuentas por figurar aquí. Las reglas sencillas son válidas con límites explícitos. HLR es otro modelo entrenado para datos adecuados, no un requisito inicial.

## Condiciones para adaptar

Define ID estables de ítems y habilidades, versiones de contenido, interpretación de respuestas y condiciones de apoyo. Separa respuestas adivinadas, asistidas, reveladas e independientes. Respeta el significado de las valoraciones de la biblioteca; no conviertas respuestas asistidas en recuperación independiente. Separa moneda del juego y modelo de aprendizaje. Conserva datos mínimos y marcas temporales solo cuando la planificación las necesite.

Define el inicio sin historial y una alternativa útil cuando los datos falten, estén dañados o desactualizados. Revisa supuestos con datos representativos, incluidos idioma y accesibilidad. Permite corrección docente y acceso a ayuda. La predicción es incierta: ni un objetivo universal de 80–90 % de aciertos ni dos respuestas correctas miden la ZDP o prueban dominio. La retención deseada supone un equilibrio con la carga de trabajo, no una garantía educativa.

Si eliges un algoritmo, usa una implementación mantenida y verifica su versión. Comprueba actualizaciones, zonas horarias y cambio de día, envíos duplicados, cambios de contenido, exportación, recuperación y datos inválidos. Compara la ampliación con la base sencilla; precisión predictiva, participación y aprendizaje son resultados distintos. No infieras discapacidad o personalidad del tiempo de respuesta.

## Cierra o retoma una fase

Registra resultado, condiciones de ayuda, preguntas abiertas y siguiente paso viable. Completar una fase no equivale a demostrar dominio. Crear otra no completa automáticamente la anterior. Los resúmenes conservan enlaces necesarios a evidencias e incertidumbre, no transcripciones completas. Al volver, comprueba supuestos antiguos con una tarea proporcionada; una interrupción no borra el progreso.

## Fuentes

[Documentación Anki FSRS](https://docs.ankiweb.net/manual/deck-options), [Pelánek sobre Elo educativo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) y [Settles y Meeder sobre HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Describen modelos y contextos específicos, no la eficacia de una aplicación nueva. Verifica la documentación actual al integrar una biblioteca.
