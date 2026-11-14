---
name: metodologias-de-aprendizaje
description: Diseña o revisa aplicaciones educativas conectando objetivos de aprendizaje, necesidades del alumnado, actividades, retroalimentación y evidencias de aprendizaje. Úsalo para nuevas herramientas educativas o cambios sustanciales en su diseño didáctico. No lo apliques a cambios estéticos ni a correcciones habituales de errores sin un problema de diseño del aprendizaje.
metadata:
  version: "1.4.0"
  language: "es"
  based_on: "learning-methodologies@1.4.0"
  license: "MIT"
  repo: "https://github.com/siberius/learning-methodologies"
  author: "Luděk Sušický"
  format: "paquete nativo con Markdown independiente generado"
---


<!-- Generado a partir de SKILL.md y references/. Edita las fuentes. -->


# Metodologías de aprendizaje

Ayuda a diseñar, implementar o revisar aplicaciones educativas cuyas actividades, apoyos y evaluación respondan a las necesidades del alumnado destinatario. Ajusta la profundidad del trabajo a la petición, sus consecuencias y la incertidumbre. Una actividad breve de aula no necesita un estudio completo de evaluación ni un nuevo documento de planificación.

## Métodos didácticos para aplicaciones creadas con IA

Utiliza los métodos para traducir objetivos educativos en acciones del estudiante, reglas de retroalimentación y evidencias en la aplicación generada. La recuperación requiere un intento antes de revelar la respuesta; el andamiaje requiere ayuda accesible y distinguir desempeño con apoyo e independiente. La IA ayuda a implementar estas decisiones; el resultado necesita revisión disciplinar y didáctica. Se aplica a aplicaciones sin conexión y al uso justificado de IA durante el aprendizaje.

Consulta la [justificación didáctica](#reference-didactic-rationale) al explicar la elección de un método o su implementación. Vincula métodos con decisiones de producto y evidencias necesarias.

## Acompaña las decisiones del creador

En cada decisión didáctica sustancial, revisa objetivo, acción del estudiante, evidencia, apoyo y restricciones. Reutiliza las elecciones anteriores. Ante una elección importante pendiente, ofrece pocas opciones pertinentes, normalmente dos o tres, con una descripción sencilla y un ejemplo en este proyecto. Recomienda una, explica su principal contrapartida y pregunta qué enfoque prefiere el creador. Lee el [diálogo de diseño](#reference-design-dialogue) al iniciar o reabrir esa elección. Esta conversación es distinta del diálogo del tutor con el estudiante.

No reabras decisiones resueltas o rechazadas sin un cambio pertinente. Respeta la delegación explícita de decisiones habituales y continúa con una justificación breve. El silencio no autoriza ampliar el alcance. Mientras esperas, avanza en partes independientes. Un cambio cosmético no activa este proceso.

Consulta según la necesidad: [métodos](#reference-methods) para actividades y apoyo; [juegos](#reference-learning-games) para motivación y mecánicas; [evaluación](#reference-assessment) para evidencias y puntuación; [interfaz cognitiva](#reference-cognitive-ux) para representaciones, multimedia y atención; [práctica adaptativa](#reference-adaptive-practice) para sesiones repetidas o dificultad. Mantén las rutas condicionales siguientes para simulaciones, estado del tutor e IA en ejecución. Lee el método pertinente antes de ofrecerlo; no cargues todas las referencias.

Convierte la elección en comportamiento observable del producto y una comprobación significativa. Distingue ofrecido, elegido, implementado y verificado. La verificación técnica no demuestra eficacia educativa.

## Ruta de trabajo

Sigue esta ruta con la profundidad necesaria: establecer el objetivo y las restricciones → elegir un método para el obstáculo de aprendizaje → conectar la actividad del estudiante con la evidencia → implementar dentro del alcance → comprobar el resultado. En una revisión, examina el diseño existente en lugar de implementarlo. Reutiliza el contexto conocido; no exijas un documento de planificación para cada paso.

Consulta los [ejemplos de decisión](#reference-decision-examples) cuando necesites aclarar la ayuda, las respuestas alternativas o una alineación curricular incierta. Ilustran decisiones; no son guiones que deban copiarse en todas las lecciones.

## Establece el contexto de aprendizaje

Utiliza la información ya presente en la petición, el proyecto y los materiales aportados. Para completar el contexto, pregunta solo por información ausente que cambie sustancialmente el diseño. Ante incertidumbres menores, declara una suposición razonable y continúa. Evita los cuestionarios fijos y las solicitudes repetidas de aprobación para decisiones ordinarias ya cubiertas por la petición.

Identifica el contexto pertinente: alumnado y conocimientos previos, materia, resultados previstos, uso en el aula o autónomo, tiempo y dispositivos disponibles, idioma, necesidades de accesibilidad y cualquier currículo aportado. Sigue un currículo cuando corresponda al entorno; no presupongas un marco nacional. Elige el tono según el contexto y las preferencias del autor. No deduzcas la atención, motivación, capacidad o pedagogía preferida a partir de etiquetas generacionales.

Incluye la actividad docente que rodea a la aplicación cuando resulte útil: preparación, trabajo individual o grupal, intervención docente, discusión y seguimiento. Una demostración dirigida por el docente puede necesitar una buena pregunta para debatir en lugar de cuentas y puntuaciones individuales.

Separa edad, papel educativo y experiencia en el tema; niño, alumno, estudiante y participante adulto no son categorías intercambiables ni niveles de capacidad. Al definir o cambiar el público, lee su perfil en el [diálogo de diseño](#reference-design-dialogue). Adapta denominación y apoyo al entorno; usa términos neutros en orientaciones generales. Creador, persona que aprende y docente o familiar acompañante pueden ser personas distintas.

## Conecta los objetivos con actividades observables

Para cada objetivo importante, relaciona la acción del estudiante, la evidencia, los criterios de logro, las condiciones de ayuda y la siguiente decisión didáctica. En tareas pequeñas, hazlo de forma concisa. En una indagación abierta, la evidencia puede referirse a la calidad de las preguntas, el uso de pruebas o la revisión de una explicación, sin una única respuesta predeterminada.

Ejemplo: el estudiante predice cómo cambia la corriente al variar la resistencia, lo comprueba con un modelo, explica las discrepancias y resuelve de forma autónoma un caso nuevo. Mover un control deslizante o completar una pantalla no demuestra por sí solo comprensión.

Elige una intervención adecuada a partir del obstáculo de aprendizaje observado. Trata la explicación de un error como hipótesis provisional, no como diagnóstico. Selecciona un conjunto reducido y coherente de métodos; no añadas funciones solo porque figuren en el catálogo. Consulta los [métodos](#reference-methods) al seleccionar o implementar un método, una secuencia de apoyo o una regla de progresión.

Para mecánicas, motivación o revisión de juegos educativos, consulta [juegos educativos y gamificación con propósito](#reference-learning-games). Incluye secuencias jugables, selección de mecánicas, límites de evidencia e implementación desde herramientas pequeñas hasta productos longitudinales. Adapta a primaria, secundaria, universidad y adultos de distintos países según conocimientos previos y contexto local.

La referencia de métodos abarca explícitamente el aprendizaje socrático, la técnica de Feynman, la zona de desarrollo próximo y el andamiaje, los ejemplos resueltos, la práctica de recuperación y espaciada, el aprendizaje a partir del error, la metacognición, la indagación, el juego de roles, el aprendizaje entre iguales y cooperativo, los proyectos, la enseñanza invertida y la gamificación opcional. Son enfoques seleccionables, no funciones obligatorias de todas las aplicaciones.

La taxonomía de Bloom describe objetivos cognitivos y tipos de conocimiento. Mantén separadas la dificultad y los prerrequisitos; no impongas seis niveles bloqueados. Para resultados prácticos, interpersonales o de otro tipo, elige evidencias adecuadas y reconoce qué no puede demostrar una tarea en pantalla.

## Elige una realización proporcionada

Distingue la IA utilizada para construir la aplicación de la IA utilizada por el alumnado en el producto terminado. Elige entre contenido estático revisado, interacciones o simulaciones deterministas e IA durante el uso según el objetivo y las condiciones de funcionamiento. Las pistas, la retroalimentación y la práctica espaciada pueden funcionar sin un servicio de IA.

Antes de añadir una función importante, considera su aportación al aprendizaje, la carga de interacción, el trabajo docente, el mantenimiento, los datos necesarios y el coste de funcionamiento. Explica las compensaciones relevantes. No añadas cuentas, analítica, paneles, un backend, servicios de pago ni flujos de datos externos solo para que el producto parezca completo. Confirma las decisiones que cambien el alcance cuando no estén ya autorizadas.

Consulta las [simulaciones](#reference-simulations) al modelar un sistema, realizar un experimento o diseñar un juego de roles. Distingue claramente las observaciones reales, los cálculos del modelo y las reconstrucciones ficticias. Nunca presentes resultados inventados por la IA como mediciones ni finjas que se ha realizado un experimento.

Consulta la [IA durante el uso](#reference-runtime-ai) solo cuando el producto terminado llame a un servicio de IA. Define la función docente, los límites de las fuentes, la supervisión humana, los flujos de datos, los límites de coste y el comportamiento ante fallos. Un prompt no sustituye la seguridad de la aplicación.

Consulta los [modos del tutor y la continuidad](#reference-tutor-state) al implementar una tutoría de varios pasos, transiciones entre práctica y evaluación o la reanudación del aprendizaje. Conserva el estado y las evidencias en la aplicación; estas funciones no necesitan IA durante el uso.

## Haz fiables la retroalimentación y las decisiones

Proporciona un siguiente paso útil después de un error. En la práctica, permite pedir ayuda y acceder a una explicación directa o una solución comentada cuando sea necesario; evita las preguntas interminables. Reduce el apoyo según el desempeño autónomo y mantén disponible la ayuda solicitada. Una evaluación puede limitar la ayuda bajo condiciones explícitas.

Distingue el éxito autónomo, el éxito con apoyo, la exposición a la respuesta y la incertidumbre. Un acierto por azar, una declaración de confianza o dos aciertos con apoyo no demuestran automáticamente dominio. No deduzcas una capacidad estable, motivación o trastorno a partir de una interacción breve.

Consulta la [evaluación](#reference-assessment) al diseñar tareas puntuadas, rúbricas, adaptación o evaluación del aprendizaje. Comprueba la corrección disciplinar, las alternativas plausibles, las unidades y tolerancias numéricas y si la tarea exige realmente el desempeño previsto. Conserva las explicaciones y los métodos alternativos válidos. Separa las recompensas del juego y la velocidad del logro, salvo que respondan a un objetivo explícito.

## Preserva el acceso y la capacidad de intervención docente

Diseña atendiendo a los criterios pertinentes de WCAG 2.2 AA y a las necesidades reales del alumnado. Comprueba el uso con teclado, el foco visible, las etiquetas y la retroalimentación comprensibles, las alternativas al uso exclusivo de color o sonido y la justificación o ajuste de los tiempos. Elige formas adecuadas de percibir la información y expresar la comprensión; no asignes estilos de aprendizaje fijos. Solicita ayuda especializada en accesibilidad cuando la implementación lo justifique.

Recoge solo los datos necesarios para la actividad e identifica quién los ve, adónde van y cómo se conservan. Cuando corresponda, comprueba los requisitos del proveedor, del centro y del ámbito local para el despliegue concreto; no inventes normas jurídicas universales. Una actividad local anónima no necesita incorporar cuentas ni seguimiento persistente.

Proporciona una forma proporcionada para que el docente o autor responsable revise el contenido, corrija los juicios e intervenga ante una adaptación inadecuada. Puede bastar un archivo de contenido editable en lugar de un sistema de gestión. Las decisiones importantes de calificación o asignación de nivel necesitan revisión humana con responsabilidad definida.

## Coordina los conocimientos especializados sin ampliar innecesariamente el proceso

Utiliza estas perspectivas según las necesidades; un solo agente puede cubrirlas en una tarea pequeña:

- Metodólogo: resultados previstos, contexto docente y decisiones didácticas.
- Especialista en didáctica de la materia: precisión del contenido, prerrequisitos, ejemplos y concepciones erróneas.
- Diseñador de evaluación: evidencias, criterios, alternativas y límites de inferencia.
- Diseñador de interacción: recorrido del estudiante, ayuda, accesibilidad y uso en el aula.
- Desarrollador: contratos de datos, cálculos, estado, persistencia y comportamiento ante fallos.
- Revisor: discrepancias entre el objetivo, el diseño y el comportamiento observado.

Lleva sus decisiones a la implementación. No califiques una elección técnica conveniente como pedagógicamente correcta sin evidencia. Resuelve los desacuerdos relevantes comprobando fuentes, mediante una comprobación específica o dejando explícita una cuestión pendiente. Usa revisión independiente cuando lo justifiquen la complejidad o las consecuencias; no formes un equipo para cada tarea. Invoca otros skills solo para trabajos pertinentes y cuando estén disponibles.

## Verifica e informa con la profundidad adecuada

En la implementación, comprueba el recorrido afectado del estudiante, los errores significativos, la ayuda y los estados de fallo pertinentes. En peticiones exclusivamente analíticas, informa de hallazgos y propuestas sin modificar el producto. Adapta las comprobaciones a la aplicación: una simulación necesita comprobaciones del modelo; la IA durante el uso requiere comprobar los fallos del servicio y el tratamiento de sus salidas; una actividad estática sencilla no necesita ninguna de estas dependencias por defecto.

Mantén separadas tres conclusiones: corrección funcional, adecuación didáctica y resultados de aprendizaje observados. Las comprobaciones técnicas por sí solas no demuestran eficacia educativa. Un pequeño piloto puede revelar problemas sin demostrar un beneficio causal. Informa de las comprobaciones realizadas y las suposiciones pendientes; no inventes observaciones del alumnado ni resultados de eficacia.

En la entrega, resume el objetivo de aprendizaje, el enfoque elegido, las suposiciones de funcionamiento importantes, las comprobaciones completadas y los límites restantes. Incluye una tabla de objetivos y evidencias solo cuando facilite utilizar el resultado. Ajusta el formato a la petición del usuario.

## Integración

Al elegir un modelo, el esfuerzo de razonamiento o la velocidad, o al adaptar el mecanismo de carga, consulta los [perfiles de modelos y entornos](#reference-model-profiles). Incluyen orientación basada en documentación para OpenAI, Claude y Gemini. Mantén un contrato educativo común e informa de las pruebas realizadas por separado de la compatibilidad prevista. No cargues este perfil para una tarea didáctica ordinaria que no lo necesite.

Adecuado para juegos educativos, cuestionarios, tutoriales, simulaciones, formación y revisiones de su diseño didáctico. El núcleo no requiere paquetes, API, un modelo de IA concreto ni datos del alumnado. Las referencias se incluyen a continuación para el uso independiente. En el paquete nativo son archivos separados que se consultan según la necesidad. La instalación, el despliegue y otros cambios externos requieren autorización para dichas acciones. Este skill no sustituye las instrucciones del proyecto ni autoriza ampliar el alcance.

Referencias de diseño: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [pautas DUA de CAST](https://udlguidelines.cast.org/). Orientan el diseño y la revisión; citarlas no certifica conformidad ni eficacia educativa.

## Reference: methods

Sección de origen: Elección de métodos de aprendizaje


Utiliza esta referencia después de definir el objetivo y la evidencia de logro. Elige la intervención útil más pequeña para el obstáculo actual del estudiante. El formato de una aplicación no determina por sí solo un método docente. No añadas todos los métodos de esta lista.

### Métodos: Fichas para una elección concreta

Usa ID estables entre traducciones y registros. Cada fila conecta descripción para el creador, necesidad, acción y evidencia. Las secciones siguientes desarrollan apoyo y límites. Para la ficha elegida, concreta implementación pequeña, ampliación opcional, comprobación de fallos y fuente pertinente; no muestres todo el catálogo por defecto. Las fuentes apoyan principios específicos, no la eficacia de la aplicación generada.

Para la ficha elegida, indica público, conocimientos previos necesarios y adaptaciones de idioma, apoyo o evaluación; no elijas el método solo por edad.

| ID y descripción | Cuándo ofrecer e implementación pequeña | Evidencia y comprobación del apoyo |
| --- | --- | --- |
| `worked-example-fading`: observar, completar y aplicar un procedimiento | Procedimiento nuevo; ejemplo revisado y tarea incompleta | Caso independiente nuevo; permitir saltar apoyo conocido y recuperarlo |
| `guided-inquiry`: predecir, cambiar una variable y explicar | Comprender un sistema; experimento delimitado | Justificar otra predicción; manipulación aleatoria no sustituye razonamiento |
| `productive-failure`: intentar enfoques y compararlos con una explicación | Conocimientos previos y tiempo para consolidar | Comparar enfoques y aplicar la idea; no abandonar al principiante |
| `retrieval-spacing`: recordar antes de revelar y volver después | Conservar conocimientos accesibles; intento, corrección y repaso | Recuperación independiente con demora; corrección inmediata no es espaciado |
| `contrast-interleaving`: distinguir casos similares y elegir estrategia | Confusión de categorías o procedimientos tras apoyo inicial | Explicar el rasgo distintivo; mezclar temas al azar no basta |
| `socratic-dialogue`: examinar razonamiento mediante una pregunta | Una respuesta razonada puede revelar incertidumbre útil | Revisar o defender con evidencia; explicación directa disponible |
| `self-explanation`: explicar con palabras propias y revisar | Detectar lagunas tras aprendizaje inicial | Exactitud y aplicación, no solo fluidez |
| `cooperative-project`: coordinar roles para producir algo significativo | Indagación compartida o tarea auténtica con tiempo | Contribución y explicación individual; éxito grupal no prueba dominio de todos |
| `role-play`: decidir desde un papel y reflexionar | Perspectivas, comunicación o juicio procedimental | Explicar decisiones y consecuencias; coincidir con el personaje no es acertar |
| `metacognitive-review`: comparar plan o confianza con evidencia | Autorregulación y próximos pasos | Cambiar una acción según desempeño; confianza no es capacidad |
| `criterion-rubric`: valorar cualidades observables mediante criterios | Respuestas abiertas, proyectos y alternativas justificadas | Ejemplos límite y revisión; no premiar acuerdo de opiniones |
| `representation-transfer`: conectar representaciones concretas y formales | Éxito ligado a objetos del juego | Aplicar en otra representación; conservar vías accesibles equivalentes |

En versiones diferenciadas identifica objetivo común y decisión que debe conservar cada una. Varía idioma, representación, ritmo y ayuda sin resolver por el estudiante esa decisión. Conserva un contexto interesante para quienes reciben apoyo. Amplía con justificación, contraejemplos o transferencia, no solo más ítems. Explicita un cambio intencional del objetivo. Los grupos dependen de evidencia revisable, no etiquetas permanentes.

Extensiones como repaso persistente o IA requieren motivo y referencias correspondientes. Conserva fuente, versión y jurisdicción de vínculos curriculares; distingue estándar oficial, componente y prerrequisito inferido. Una conexión conceptual no es automáticamente una progresión validada.


### Métodos: Elige a partir de una necesidad observada

| Obstáculo observado | Intervención posible | Comprobación antes de adoptarla |
|---|---|---|
| No se retienen conocimientos esenciales | Práctica de recuperación con repaso espaciado | ¿Puede el alumnado recordarlos de forma autónoma tras un intervalo? |
| Un principiante no sabe iniciar un procedimiento | Ejemplo resuelto, seguido de tareas parcialmente completadas y autónomas | ¿Dispone de los prerrequisitos y entiende los pasos? |
| El alumnado repite una concepción errónea específica | Casos de contraste, explicación, pregunta dirigida y práctica correctiva | ¿Distingue la tarea esa concepción de otros errores? |
| El alumnado sabe ejecutar, pero no explicar ni transferir | Autoexplicación, casos de contraste y aplicación en otro contexto | ¿Exige el éxito razonar en lugar de copiar un patrón? |
| Al alumnado le cuesta valorar su comprensión | Predicción, juicio de confianza, comprobación autónoma y reflexión | ¿Puede comparar su juicio con evidencias? |
| El objetivo incluye indagación o interacción profesional | Investigación guiada, juego de roles o simulación con reflexión final | ¿Son fiables el modelo, el escenario, las evidencias y los criterios? |

Estas observaciones son hipótesis didácticas provisionales. Una respuesta incorrecta, lenta o una petición de ayuda no diagnostica un trastorno de aprendizaje, motivación, inteligencia ni un rasgo estable. Pregunta o examina más cuando encajen varias explicaciones.

### Métodos: Bloom como perspectiva de diseño

La taxonomía revisada tiene dos dimensiones: conocimiento (factual, conceptual, procedimental y metacognitivo) y proceso cognitivo (recordar, comprender, aplicar, analizar, evaluar y crear). Úsalas para describir objetivos y examinar la cobertura de las tareas. Una tarea puede combinar procesos; su verbo no determina por sí solo la clasificación.

Separa la dificultad de las tareas, los prerrequisitos curriculares y las reglas de progresión. No desbloquees seis niveles obligatorios ni deduzcas dominio de una etiqueta de Bloom. Construye las relaciones de prerrequisito desde la disciplina. Incluye objetivos prácticos, interpersonales o afectivos cuando corresponda, con sus propias evidencias observables. Las categorías cognitivas de Bloom no abarcan todos los objetivos educativos.

### Métodos: Zona de desarrollo próximo y andamiaje

La zona de desarrollo próximo se refiere a la relación entre el desempeño autónomo y lo que resulta posible con apoyo adecuado. Usa esta perspectiva cuando un estudiante pueda completar una tarea con ayuda, pero todavía no de forma autónoma. El andamiaje ofrece indicios, ejemplos o pasos parciales temporales. No deduzcas un límite exacto de capacidad de un solo error.

Para principiantes, considera un ejemplo resuelto con el razonamiento visible, una tarea para completar y práctica autónoma. Ajusta el detalle a los conocimientos previos. Proporciona solo la información necesaria para el paso actual; la complejidad decorativa y las demandas simultáneas necesitan una finalidad de aprendizaje.

Utiliza una secuencia flexible de ayuda: aclarar el obstáculo, dar una pista específica, ofrecer un paso parcial y después una solución comentada cuando sea necesaria o se solicite. Tras el trabajo con apoyo, propone una tarea autónoma comparable. Reduce el apoyo según el desempeño autónomo demostrado. Dos aciertos o la confianza declarada no demuestran por sí solos dominio.

### Métodos: Aprendizaje socrático

Utiliza preguntas dirigidas para examinar supuestos, evidencias y razonamiento cuando el estudiante tenga suficientes conocimientos para responder. El elenchos examina la coherencia entre una afirmación y las premisas aceptadas; la finalidad en el aula no es derrotar al estudiante. Las categorías de preguntas de Paul y Elder ofrecen orientaciones sobre significado, supuestos, evidencias, perspectivas, implicaciones y la propia pregunta.

Plantea una pregunta útil cada vez y responde a la explicación real del estudiante. Permítele defender una respuesta correcta en lugar de suponer que toda respuesta inicial es errónea. Evita las preguntas interminables y retener explicaciones necesarias. Si faltan prerrequisitos, las preguntas dejan de ayudar o el estudiante pide una demostración, proporciona enseñanza directa o un ejemplo.

### Métodos: Técnica de Feynman

Invita al estudiante a explicar un tema con sus palabras a un principiante curioso, identificar una carencia concreta, volver a una fuente fiable y revisar la explicación. Puede revelar el razonamiento tras una introducción inicial o antes de aplicar lo aprendido. No finjas no comprender una explicación precisa solo para prolongar el diálogo.

Comprueba la precisión factual con fuentes y una rúbrica adecuada; incluye después una tarea de aplicación. La fluidez, la simplificación y los elogios de la IA no demuestran por sí solos comprensión profunda. El nombre de la técnica no garantiza la eficacia de su implementación.

### Métodos: Recuperación, espaciamiento y reflexión

La práctica de recuperación pide reconstruir conocimientos antes de ver la respuesta. Proporciona retroalimentación correctiva y otra oportunidad para utilizarla. El espaciamiento retoma el aprendizaje tras un intervalo significativo; devolver inmediatamente un error a la cola es práctica correctiva, no una estrategia completa de espaciamiento. Repasa también parte del material previamente acertado. Configura los intervalos según el contenido, el objetivo de retención y las sesiones disponibles; no afirmes que un calendario es óptimo para todos los casos.

### Métodos: Metacognición y aprendizaje autorregulado

Ayuda al alumnado a establecer un subobjetivo útil, planificar, supervisar su comprensión y revisar el enfoque usando evidencias. Pide predecir el éxito o explicar una elección y comparar después con el desempeño autónomo. Mantén la reflexión concreta: qué evidencia cambió su perspectiva y qué probará después. No equipares confianza con competencia ni añadas un diario obligatorio extenso a una actividad pequeña sin propósito.

### Métodos: Mapas conceptuales y relaciones

Usa un mapa conceptual cuando explicar o construir relaciones forme parte del objetivo. Permite construir un mapa pequeño, etiquetar una relación ausente o criticar una conexión propuesta; compáralo después con fuentes revisadas o una rúbrica. Un mapa pulido generado íntegramente para el estudiante es un recurso, no evidencia de su comprensión.

Etiqueta explícitamente las conexiones: prerrequisito, parte de, contrasta con, se asocia con o causa bajo condiciones declaradas. No deduzcas causalidad de la coincidencia ni conviertas a la fuerza una red de enlaces cruzados en un árbol. Acepta estructuras válidas diferentes; evalúa el significado y la justificación de las relaciones, no las coordenadas ni la similitud visual. No presupongas que la fuente cubre todas las conexiones.

En la implementación, utiliza identificadores estables de conceptos y relaciones tipadas y dirigidas cuando haga falta. Ofrece una alternativa textual o en lista y edición con teclado si se requiere manipulación; arrastrar no debe ser la única forma de responder. Una tabla breve de relaciones puede servir al objetivo sin un editor gráfico. Comprueba un mapa alternativo válido y un enlace incorrecto frente a las reglas de retroalimentación.

### Métodos: Métodos contextuales

- Indagación: apoya la pregunta, predicción, prueba, observación y explicación. Las afirmaciones sobre el mundo real necesitan datos reales adecuados o un modelo suficientemente validado; las salidas ilustrativas deben estar etiquetadas y acotadas. La narración de un modelo lingüístico no sustituye la evidencia experimental.
- Juego de roles: define el papel, los límites del escenario y los criterios de logro; realiza después una reflexión final. Identifica el diálogo histórico como reconstrucción y distingue los hechos documentados del habla inventada. La interacción ficticia también puede tener consecuencias emocionales o sociales.
- Aprendizaje entre iguales: proporciona una tarea compartida, una contribución individual identificable y criterios para una explicación útil. Incluye una forma de resolver desacuerdos y comprobar la comprensión individual.
- Enseñanza entre iguales: permite explicar y dar retroalimentación con criterios comprensibles y acceso a una explicación revisada o al docente cuando sea necesario. No conviertas a un compañero sin experiencia en autoridad final sobre la precisión disciplinar.
- Aprendizaje por proyectos: define un producto auténtico, hitos intermedios y evidencias individuales. Un resultado atractivo no demuestra por sí solo el aprendizaje previsto.
- Enseñanza invertida: conecta la preparación con la aplicación en el aula y ofrece una alternativa para quien no pudo prepararse. Es una decisión organizativa, no un beneficio automático de aprendizaje.
- Gamificación: utiliza funciones opcionales de progreso o narración cuando apoyen el objetivo. La competición pública, las recompensas y la puntuación por velocidad necesitan un motivo y una alternativa accesible.

### Métodos: Evidencia y lecturas complementarias

- [Krathwohl, 2002, A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf): dos dimensiones y una jerarquía flexible con categorías que se solapan.
- [IES, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): recomendaciones fundamentadas para el espaciamiento, la recuperación, los ejemplos resueltos y las preguntas explicativas. La solidez de la evidencia varía según la recomendación.
- [UNESCO, Guidance for Generative AI in Education and Research](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research): capacidad de decisión humana y validación de los usos educativos.

## Reference: assessment

Sección de origen: Evidencias, evaluación y retroalimentación


### Evaluación: Comienza por la decisión

Para cada objetivo importante, especifica la acción del estudiante, la evidencia recogida, los criterios de logro y la siguiente decisión didáctica. Incluye condiciones como el acceso a pistas, materiales de consulta, colaboración y límites de tiempo. Establece criterios prácticos o sociales cuando esos sean los resultados previstos, en lugar de sustituirlos por un cuestionario de recuerdo.

Ejemplo: ante un circuito desconocido, el estudiante predice el efecto de un cambio y explica por qué. La evidencia incluye la predicción y la explicación causal. Una rúbrica comprueba el principio pertinente, su aplicación y el razonamiento. Una concepción errónea da lugar a un ejemplo de contraste y otro intento autónomo.

### Evaluación: Explicita las finalidades

En modo de práctica, los estudiantes pueden solicitar explicaciones, reintentar y utilizar apoyo graduado. Registra el uso de ayuda por separado del éxito autónomo. La retroalimentación debe señalar qué es correcto, identificar la carencia pertinente y ofrecer un siguiente paso realizable, seguido de una oportunidad para revisar o aplicar lo aprendido.

En modo de evaluación, define antes del intento la ayuda permitida y la puntuación. Mantén la ayuda tutorial conforme a esas condiciones. Explica si la retroalimentación es inmediata o diferida y por qué. No transfieras silenciosamente las puntuaciones de práctica a calificaciones con consecuencias. La evaluación formativa utiliza evidencias para ajustar el aprendizaje; la sumativa informa del logro respecto a criterios definidos. Una puntuación sin una decisión posterior no constituye por sí sola evaluación formativa.

### Evaluación: Diseña tareas fiables

Comprueba la clave de respuestas, la explicación y las alternativas plausibles. En tareas de opción múltiple, prefiere distractores significativos relacionados con errores conocidos y evita pistas involuntarias. En respuestas abiertas, acepta formulaciones equivalentes, métodos alternativos válidos y suposiciones adecuadas. No conviertas una respuesta modelo en la única formulación correcta.

Utiliza una rúbrica breve con criterios observables, descripciones del desempeño y ejemplos, incluidas respuestas limítrofes y alternativas correctas. Separa dimensiones cuando resulte útil: precisión factual, razonamiento, procedimiento, comunicación o colaboración. Penaliza los aspectos formales del lenguaje solo cuando formen parte del objetivo. La velocidad y la clasificación pública necesitan una finalidad educativa explícita; los puntos de participación, insignias y certificados de finalización no demuestran dominio.

Al implementar un banco de tareas, explicita las decisiones pertinentes en su formato de datos existente. Pueden resultar útiles un identificador estable de tarea, un identificador de objetivo, el enunciado, las respuestas aceptadas o rúbrica, la explicación, las pistas, la fuente y el estado de revisión. Añade unidades y tolerancias numéricas cuando sea necesario. Mantén separados los registros de respuesta: respuesta, ayuda utilizada, intento y estado de evaluación. Es un ejemplo de contrato, no un esquema obligatorio ni un motivo para añadir seguimiento a una demostración compartida.

### Evaluación: Límites del juicio de la IA

Trata una puntuación o clasificación de errores de la IA como un juicio provisional. Valídalo con ejemplos revisados por docentes y comprobaciones disciplinares cuando estén disponibles. Si la evidencia es ambigua, solicita aclaración o márcala para revisión; no fabriques certeza ni uses una cifra de confianza sin calibrar como prueba. Permite que el alumnado cuestione la retroalimentación y que el docente corrija la valoración viendo la respuesta original y la justificación de la puntuación. Las decisiones con consecuencias requieren un proceso de revisión humana con responsabilidad definida, adecuado al contexto.

### Evaluación: Evalúa la afirmación de aprendizaje

Cuando sea viable, compara una tarea inicial con otra comparable y autónoma después de la enseñanza; comprueba posteriormente una muestra de retención tras un intervalo y de transferencia a otro contexto. Interpreta la mejora con cautela: los ítems repetidos, las pistas y las condiciones iniciales desiguales pueden cambiar las puntuaciones. Un pequeño piloto de aula puede identificar problemas, pero no demuestra por sí solo eficacia causal.

Registra finalización, uso, tiempo, disfrute, latencia y errores como indicadores de funcionamiento o experiencia. Manténlos separados de los resultados de aprendizaje. Elige el mínimo de datos necesario para la decisión didáctica y declara qué no puede demostrar la evidencia.

### Evaluación: Fuentes

- [EEF, Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback): intenciones de aprendizaje, evidencias de carencias, oportunidad de la retroalimentación y posibilidades de actuar sobre ella. Esta orientación para la retroalimentación docente no valida todas las implementaciones con IA.
- [Guía práctica del IES](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): la recuperación autónoma y el repaso diferido orientan el enfoque de evaluación propuesto.

El proceso, la rúbrica de ejemplo y las decisiones de implementación anteriores son recomendaciones de diseño. Su adecuación debe comprobarse según el alumnado, la materia, las consecuencias y la evidencia disponible.

### Evaluación: Comprueba decisiones y corrige consecuencias

En un ítem de respuesta única, resuelve el enunciado real de forma independiente e intenta defender cada opción con sus unidades, precisión y supuestos. Debe quedar una sola defendible. Para respuesta múltiple sigue la regla declarada; en tareas abiertas conserva alternativas válidas. Aplica después cada procedimiento erróneo declarado a los datos reales: debe producir el distractor previsto. Revisa opciones afectadas tras cambiar el enunciado. Fracciones equivalentes o redondeo no especificado no deben generar otra respuesta correcta.

Conecta respuesta observada, explicación posible, tarea que distinga causas y siguiente acción concreta. Una respuesta incorrecta no diagnostica la causa. En diseño centrado en evidencias (ECD), identifica competencia, evidencia observable y tarea que la provoca. Un evento del juego puede reflejar dificultad motora, exploración o azar; la telemetría no demuestra persistencia ni personalidad. Explica la recogida necesaria de datos.

Si contenido, clave o explicación del tutor son incorrectos, reconoce y corrige el error; revisa ayudas, tareas, puntuaciones y progreso dependientes. No uses el intento afectado como prueba de ignorancia. Conserva evidencia original necesaria y versión del contenido; indica incertidumbre y ofrece otra comprobación cuando proceda. Las vistas docente y estudiantil deben usar la misma versión del enunciado y opciones.

Estos procedimientos desarrollan principios de [Learning Commons para comprobar comprensión](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). No importan formatos fijos, currículo estadounidense por defecto ni restricciones de atribución.

## Reference: simulations

Sección de origen: Simulaciones y juego de roles


Consulta esta referencia cuando un producto modele un sistema, apoye un experimento o permita actuar dentro de un escenario. Selecciona solo las comprobaciones pertinentes.

### Simulaciones: Identifica qué representa la salida

Distingue estos tipos de evidencia con lenguaje comprensible para el alumnado:

- **Medición:** observaciones de un instrumento real, un conjunto de datos o un experimento registrado. Identifica la fuente y los límites pertinentes de la medición.
- **Cálculo o simulación:** resultados de un modelo matemático o basado en reglas definido. Declara los supuestos y el ámbito en que resulta útil.
- **Ficción o reconstrucción:** sucesos, diálogos, personajes o consecuencias inventados para aprender. Identifícalos como tales.

Nunca describas números generados como mediciones ni diálogos inventados como citas auténticas. Una simulación puede ilustrar una hipótesis; su salida por sí sola no demuestra el comportamiento del mundo real.

### Simulaciones: Define y comprueba el modelo

Registra el objetivo de aprendizaje, las variables de estado, las entradas, las unidades, los rangos permitidos, los supuestos, las reglas de actualización y las salidas observables. Explica las simplificaciones que afecten a la interpretación. Elige controles que muestren la relación prevista sin exigir descubrir ajustes no documentados.

Para el trabajo numérico, calcula las salidas con un motor numérico verificado o reglas explícitas. Mantén ese motor separado de los comentarios del modelo lingüístico. Este puede explicar resultados obtenidos, pero no inventar cálculos ausentes ni fingir que se realizó un experimento.

Usa comprobaciones proporcionadas: un ejemplo conocido, un caso límite, coherencia de unidades y un invariante pertinente o una tendencia esperada. En modelos estocásticos, especifica la fuente de aleatoriedad y permite una semilla reproducible cuando resulte útil. Documenta las limitaciones en lugar de sugerir validez universal.

### Simulaciones: Diseña el ciclo de aprendizaje

Pide al estudiante que prediga y explique antes de ejecutar el modelo cuando apoye el objetivo. Permítele cambiar entradas significativas, observar la salida obtenida, compararla con su predicción y revisar la explicación. Proporciona una reflexión final que distinga el comportamiento del modelo de las afirmaciones sobre el mundo y pregunte dónde podría fallar.

No atribuyas comprensión solo por alcanzar una configuración objetivo. Busca una explicación, comparación o transferencia a un caso nuevo.

### Simulaciones: Juego de roles histórico y social

Indica si un personaje es ficticio, compuesto o basado en historia documentada. Mantén distinguibles los hechos documentados y el habla reconstruida. Aporta la procedencia de las afirmaciones históricas y reconoce interpretaciones discutidas cuando corresponda. No afirmes tener acceso auténtico a los pensamientos de una persona ni fabriques citas.

Define el papel, los límites del escenario, el objetivo de aprendizaje y la reflexión final. Ofrece una salida clara del papel y acceso a una explicación. Adapta la intensidad emocional y la temática al alumnado y al contexto; proporciona una actividad alternativa para escenarios sensibles. Evalúa el razonamiento o la comunicación previstos según criterios explícitos, sin premiar el acuerdo con el personaje.

## Reference: runtime-ai

Sección de origen: IA durante el uso de aplicaciones educativas


Consulta esta referencia solo cuando la aplicación terminada llame a un servicio de IA durante su uso. Utilizar IA para escribir código o generar contenido revisado por docentes no requiere IA durante el uso. Mantén las actividades sin conexión salvo que el objetivo necesite un servicio.

### IA durante el uso: Define una función docente acotada

Especifica qué puede hacer el modelo, qué contenido revisado o fuentes puede usar y cómo debe actuar ante evidencias ausentes. Donde importe el fundamento factual, identifica materiales aprobados y conserva su procedencia. No generes citas de apariencia verosímil. Permite incertidumbre y corrección; evita diagnósticos o afirmaciones tajantes sobre capacidades del estudiante a partir de una interacción breve.

Elige la ayuda según la actividad. La práctica puede usar preguntas orientadoras, pistas progresivas, ejemplos resueltos y explicación directa cuando se solicite o cuando preguntar deje de ayudar. Una evaluación puede restringirla según las reglas declaradas por el docente. No impongas un bucle socrático interminable ni una prohibición universal de dar respuestas. Permite solicitar ayuda, detenerse o acudir al docente.

Utiliza rúbricas explícitas para la retroalimentación y las respuestas abiertas. Compara los juicios del modelo con ejemplos revisados por docentes antes de confiar en ellos. Las decisiones importantes de calificación, asignación de nivel o disciplina requieren revisión humana con responsabilidad definida; una única respuesta del modelo no debe decidir por sí sola. Registra la incertidumbre y permite corregir el juicio al docente.

### IA durante el uso: Minimiza los datos del alumnado

Enumera los datos enviados al proveedor, qué se conserva, quién tiene acceso y cómo funciona el borrado. Recoge solo lo necesario. No añadas automáticamente cuentas, nombres reales, perfiles persistentes ni registro de conversaciones. Utiliza identificadores anónimos o seudónimos de actividad cuando basten, reconociendo que no garantizan anonimato.

Antes del despliegue con menores, comprueba con la institución responsable la edad destinataria, las disposiciones del centro, las condiciones y ajustes del proveedor y los requisitos locales aplicables. No inventes una edad universal de consentimiento ni una norma jurídica universal. Explica el tratamiento de datos al alumnado y al profesorado con lenguaje adecuado.

### IA durante el uso: Usa protecciones de arquitectura

Conserva las credenciales en un componente protegido del servidor cuando el servicio remoto requiera claves secretas. Nunca las expongas en código del navegador. Aplica autorización, límites de solicitudes y permisos de herramientas fuera del prompt. Trata las entradas del alumnado, los documentos recuperados y las salidas del modelo como datos no confiables.

Separa las instrucciones del contenido suministrado, restringe herramientas y destinos, valida salidas estructuradas y sanea el contenido mostrado. Impide que el texto generado se convierta directamente en código ejecutable u operaciones privilegiadas. Decirle al modelo que ignore inyecciones no garantiza seguridad. Realiza una revisión de seguridad específica de la arquitectura implementada.

### IA durante el uso: Planifica costes, fallos y continuidad

Fija un presupuesto realista, límites por sesión, tiempos de espera y cancelación. Muestra un estado comprensible durante la espera. Gestiona pérdidas de conexión, modelos no disponibles, salidas inválidas y cuotas agotadas sin perder el trabajo. Reintenta solo de manera segura y limitada.

Ofrece una alternativa adecuada: pistas revisadas, ejercicios estáticos, progreso guardado o ayuda docente. Identifica la retroalimentación no disponible en lugar de inventarla. Antes del uso en el aula, recorre el flujo principal, una respuesta incorrecta, una solicitud de ayuda, retroalimentación incierta y un fallo de servicio. Documenta las limitaciones pendientes y las responsabilidades de revisión del docente.

### IA durante el uso: Verifica el contenido generado dentro de límites definidos

Antes de publicar ejercicios generados, aplica comprobaciones pertinentes de exactitud, resolución, transiciones y presentación. Exige solución única solo cuando la tarea la promete. Aplica permisos y validación estructural fuera del modelo; un esquema no demuestra verdad y las comprobaciones deterministas garantizan solo las propiedades comprobadas. Rechaza o aparta contenido inválido para revisión y conserva una alternativa revisada. Para corregir ayudas, evaluación y progreso dependientes, aplica el procedimiento de `assessment.md`.

## Reference: model-profiles

Sección de origen: Modelos, esfuerzo, velocidad y adaptación al entorno


Utiliza esta referencia al recomendar un modelo, elegir velocidad o esfuerzo de razonamiento, o adaptar la carga del skill al entorno. Conserva las mismas instrucciones educativas entre proveedores. Las recomendaciones siguientes son configuraciones iniciales para este proceso, no resultados de una evaluación comparativa entre proveedores.

Documentación comprobada: 2026-11-04. Los nombres de modelos, ajustes disponibles, planes y precios cambian. Antes de usar un modelo identificado por su nombre, comprueba la lista real del usuario y la documentación oficial actual. No afirmes haber cambiado modelos o ajustes salvo que un control compatible los haya cambiado.

### Modelos y entornos: Elige por tarea antes que por nombre

Usa un modelo pequeño para ediciones acotadas con criterios explícitos, uno intermedio para diseño e implementación ordinarios y otro más potente para evidencias contradictorias, simulaciones complejas o revisiones con consecuencias. Son categorías de tareas, no capacidades garantizadas. Conserva la elección existente del usuario cuando cumpla los criterios.

La tabla con nombres es una **recomendación inicial no probada para este skill**, derivada de documentación, no una clasificación medida. No se ha establecido una comparación entre proveedores. Confirma una configuración con tareas representativas antes de llamarla validada.

### Modelos y entornos: Reglas de escalado y parada

Para una tarea clara, empieza con el esfuerzo predeterminado compatible o un ajuste que haya funcionado antes. Ante fuentes contradictorias o un modelo complejo, considera más esfuerzo desde el principio. Si la salida incumple una restricción explícita, contradice su propia puntuación, falla una comprobación de cálculo significativa o produce reiteradamente tareas inválidas, comprueba primero el acceso a la entrada y referencia pertinentes. Corrige una entrada ausente o un criterio ambiguo antes de cambiar de modelo.

Si tras una corrección dirigida sigue fallando el mismo criterio importante, recomienda un nivel superior de esfuerzo compatible y vuelve a evaluar ese criterio. Si persiste el fallo, recomienda un modelo disponible más potente o una revisión independiente según el impacto. No reintentes indefinidamente ni gastes más del presupuesto acordado. Las fuentes ausentes, herramientas no disponibles y caídas del servicio requieren resolver la dependencia o declarar la limitación; más razonamiento no aporta la evidencia ausente. Informa de los fallos pendientes. Cambia ajustes solo mediante controles autorizados del entorno.

Reduce el esfuerzo o usa un modelo más pequeño solo después de superar las comprobaciones pertinentes; conserva evidencias de la compensación. Trata la velocidad de servicio por separado: empieza con la estándar; la aceleración de pago necesita justificación de tiempo y coste y autorización.

### Modelos y entornos: Mantén actualizadas las recomendaciones

Revisa la orientación con nombres cuando cambie la versión del modelo o del entorno, falte un ajuste, el proveedor modifique la disponibilidad o el comportamiento documentado contradiga las observaciones. Hasta comprobarlo, marca esa combinación como no verificada y utiliza categorías de tareas y los ajustes predeterminados compatibles del entorno real. No inventes un ajuste equivalente para un modelo desconocido. Añade soluciones específicas de un proveedor a las instrucciones solo cuando un fallo reproducible demuestre su necesidad; registra la versión afectada y retíralas cuando dejen de justificarse.

### Modelos y entornos: Relaciona tarea y controles

| Trabajo | Punto de partida OpenAI | Punto de partida Claude | Punto de partida Gemini |
|---|---|---|---|
| Ediciones pequeñas y bien definidas de contenido o revisión de ítems estructurados | GPT-6 Luna, High; reducir el esfuerzo solo tras superar las comprobaciones | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low cuando sea compatible |
| Diseño e implementación de una actividad acotada | GPT-6.1 Sol, esfuerzo predeterminado o Medium | Sonnet 5.5, Medium para trabajo agéntico bien definido | Gemini 3.8 Flash, Medium |
| Auditoría didáctica difícil, fuentes contradictorias, simulación o arquitectura complejas | GPT-6 Astra, Light/Low o Medium; aumentar si hace falta | Opus 5.5, Medium y después High si hace falta | Gemini 4 Argon, Medium y después High si hace falta |

Estas combinaciones son recomendaciones del autor del skill inferidas de la orientación de los proveedores. No establecen equivalencia entre modelos ni prueban que una familia enseñe mejor. Si el modelo elegido no está disponible, recomienda una alternativa disponible e informa del cambio; no cambies una selección del usuario sin autorización. Por ejemplo, un proceso existente con Gemini 3.1 Pro puede conservar ese modelo y sus niveles compatibles de razonamiento. La tabla no predice latencias numéricas; mide una tarea representativa en el entorno real.

Distingue tres decisiones: modelo, cantidad de razonamiento y cualquier nivel prémium de velocidad de servicio. Un esfuerzo menor puede reducir el trabajo de razonamiento; el nivel Fast del proveedor es otro control y puede costar más. Flash es una familia de modelos, no un interruptor universal de modo rápido. Las mismas palabras Low, Medium y High no prometen igual razonamiento ni latencia entre productos.

Empieza con velocidad estándar. Recomienda un nivel Fast de pago solo cuando importe el tiempo de espera y lo justifiquen el acceso y las tarifas actuales. No lo actives ni compres capacidad sin autorización. La emisión progresiva hace visible el avance; no demuestra finalización más temprana ni calidad superior. Valora el tiempo completo, incluidas revisión, llamadas a herramientas y correcciones.

### Modelos y entornos: OpenAI y Codex

Usa el paquete nativo cuando el entorno admita skills y pueda leer referencias. En Codex, la invocación explícita puede indicar `$metodologias-de-aprendizaje` una vez descubierto. No presupongas el mismo descubrimiento en disco en un chat ordinario; aporta el Markdown independiente como entrada accesible.

La guía comprobada recomienda Sol para trabajo sustancial, Luna para tareas delimitadas y Astra para procesos exigentes; Luna High y Astra Light/Low son ajustes iniciales documentados. En Codex, Fast es una elección de velocidad de servicio distinta del esfuerzo. La disponibilidad y las tasas de consumo dependen del modelo, cuenta y cliente. Comprueba los valores compatibles antes de proponer configuración; una etiqueta de interfaz no es necesariamente un identificador de modelo de API.

Da un entregable concreto, alcance, archivos pertinentes y criterios observables de aceptación. Pide decisiones concisas y evidencias, no revelar la cadena de pensamiento privada. Utiliza las herramientas y permisos del entorno; no inventes acceso a terminal o navegador a partir del nombre del modelo.

Fuentes: [modelos](https://learn.chatgpt.com/docs/models), [velocidad](https://learn.chatgpt.com/docs/agent-configuration/speed), [skills](https://developers.openai.com/plugins/concepts/skills).

### Modelos y entornos: Claude y Claude Code

Claude Code admite paquetes `SKILL.md` y archivos auxiliares. Tras el descubrimiento, puede usarse `/metodologias-de-aprendizaje`. En otro entorno Claude, verifica el mecanismo de skills o aporta la edición independiente. No añadas hooks exclusivos de Claude, sustituciones de shell ni cambios de modelo a los metadatos comunes.

Para trabajo agéntico con Sonnet 5.5, la documentación de esfuerzo recomienda Medium en tareas bien definidas y niveles superiores en las difíciles. Opus 5.5 tiene Medium como valor predeterminado; modelos anteriores y clientes pueden diferir. El control de esfuerzo de API y el modo de pensamiento son conceptos diferentes. No todas las generaciones admiten las mismas combinaciones. Prefiere los controles compatibles del entorno a copiar un parámetro API en una instrucción de chat. El modo Fast de Claude es una función distinta, dependiente del modelo y con precio prémium.

Delimita explícitamente tarea, materiales y resultado esperado. Declara dónde puede decidir el agente y qué requiere evidencia. Proporciona un ejemplo útil cuando resuelva ambigüedad; evita repetir todo el skill o prescribir una larga transcripción de pensamiento. Esta forma de presentar las instrucciones favorece la portabilidad; no afirma un rasgo cognitivo específico de Claude.

Fuentes: [skills](https://code.claude.com/docs/en/skills), [modelos](https://platform.claude.com/docs/en/models/overview), [esfuerzo](https://platform.claude.com/docs/en/build-with-claude/effort), [modo Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Modelos y entornos: Gemini y Gemini CLI

Gemini CLI descubre skills nativos en las ubicaciones compatibles, incluido el alias `.agents/skills`. Comprueba con `/skills list` y recarga con `/skills reload` cuando sea necesario. La confianza del espacio de trabajo y las aprobaciones de activación corresponden al entorno; no las eludas. AI Studio u otro chat deben recibir el archivo independiente cuando no dispongan de carga nativa.

La guía comprobada enumera Low, Medium y High para Gemini 4 Argon y Gemini 3.8 Flash. Otras versiones tienen valores predeterminados y niveles diferentes. Usa solo los compatibles con el modelo y API o cliente reales; no traduzcas literalmente un parámetro de esfuerzo de OpenAI o Claude. Un nombre de vista previa y uno estable no son intercambiables.

Para `gemini-3.1-pro-preview`, la tabla API comprobada enumera Low, Medium y High, con High predeterminado. Para ese endpoint, prueba Medium en diseño ordinario y High en una auditoría difícil como recomendación del autor, si el entorno expone esos controles. Una etiqueta como Gemini 3.1 Pro no demuestra qué endpoint o controles utiliza el cliente.

Mantén instrucciones concisas y especifica objetivo, restricciones y evidencias de salida. Adjunta los materiales para que el modelo pueda acceder; una ruta en el chat no proporciona acceso. Conserva el estado necesario de conversación con herramientas al implementar una aplicación con Gemini API, siguiendo su documentación actual. Este skill no implementa esa capa API ni autoriza añadirla.

Fuentes: [modelos](https://ai.google.dev/gemini-api/docs/models), [pensamiento](https://ai.google.dev/gemini-api/docs/thinking), [skills de Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Modelos y entornos: Uso portátil y verificación

Mantén metadatos obligatorios sencillos: `name` y `description`, seguidos de Markdown ordinario. Los metadatos opcionales describen la edición; no dependas de un campo específico del entorno para imponer un límite de seguridad. Usa referencias relativas del paquete con un agente capaz de leer archivos o la edición independiente completa en un chat. No cargues por defecto varias ediciones lingüísticas. Tras perder contexto, vuelve a aportar el alcance esencial y el trabajo pendiente en lugar de suponer que todos los entornos lo conservan.

Los emoji pueden transmitir significado, pero no deben ser la única instrucción o señal de prioridad. Conserva etiquetas textuales explícitas. La investigación sobre [semántica de emoji](https://arxiv.org/abs/2409.10760) y [ambigüedad contextual](https://arxiv.org/abs/2511.07193) no demuestra que decorar este skill mejore el cumplimiento. Prueba ese cambio con los modelos y tareas reales antes de afirmar un beneficio.

Antes de llamar probada una combinación de modelo y entorno, verifica el descubrimiento o la carga independiente, el acceso a referencias pertinentes, un entregable representativo y los límites críticos. Registra identificador exacto del modelo o etiqueta visible, entorno y versión, idioma, esfuerzo, velocidad, herramientas, fecha, artefactos y fallos. Distingue compatibilidad documental de ejecución observada. Nunca extrapoles el éxito de un modelo a todos los de su familia.

Para comparar, usa la misma tarea y materiales originales y pide a un revisor valorar los resultados reales con los mismos criterios educativos. Incluye reutilización del contexto conocido, ayuda acotada, una respuesta alternativa correcta, afirmaciones curriculares sin respaldo, un límite entre modelo y datos y un fallo de herramienta o servicio cuando corresponda. Reduce esfuerzo o elige un modelo menor solo mientras sigan superándose las comprobaciones importantes. Si no tienes acceso directo a un proveedor, márcalo como no probado en lugar de inventar resultados.

## Reference: decision-examples

Sección de origen: Ejemplos de decisión


Utiliza el ejemplo pertinente para resolver una ambigüedad concreta. Adapta la materia y la edad; conserva el principio de decisión.

### Ejemplos de decisiones: Aceptar una respuesta equivalente

Tarea: expresar 1,5 A en miliamperios. El estudiante introduce `1500 mA`; el comprobador espera `1500`. Acepta la cantidad equivalente comprobando la unidad y el valor numérico. Si el objetivo evalúa específicamente la notación de unidades, evalúala por separado. No trates todas las cadenas como equivalentes eliminando caracteres: `1500 A` es incorrecto aquí. Motivo: el formato no debe sustituir la evidencia prevista de conversión de unidades.

### Ejemplos de decisiones: Terminar un bucle socrático improductivo

Durante la práctica, después de una pregunta sobre corriente y resistencia, el estudiante dice: «Sigo sin entenderlo; por favor, muéstramelo». Proporciona una explicación breve o un ejemplo resuelto con tensión constante y ofrece después una predicción nueva con apoyo opcional. No sigas preguntando como condición para recibir ayuda. Registra el ejemplo resuelto como aprendizaje con apoyo; un problema nuevo y autónomo puede aportar evidencia separada. Motivo: las preguntas deben ayudar a avanzar, sin bloquear la enseñanza. Una evaluación declarada puede tener reglas de ayuda diferentes.

### Ejemplos de decisiones: Corregir una explicación de Feynman inexacta

Un estudiante explica: «Las plantas obtienen su alimento del suelo; la luz solar lo calienta». Reconoce que la expresión es comprensible sin aceptar su contenido científico. Identifica la concepción errónea concreta, proporciona o consulta una fuente adecuada y verificada, distingue el agua y los minerales de los azúcares producidos en la fotosíntesis e invita a revisar la explicación sencilla. Comprueba la transferencia con un caso nuevo, como qué cambia sin luz. Motivo: la fluidez y la sencillez no demuestran corrección. No inventes observaciones experimentales ni atribuyas todo el crecimiento de la planta a un solo factor.

### Ejemplos de decisiones: Trabajar con un currículo no disponible

Un docente solicita «alineación completa con el currículo de nuestro centro», pero no aporta el documento. Utiliza el objetivo declarado para producir una actividad provisional. Solicita el fragmento pertinente solo cuando importe la alineación exacta; identifica lo que sigue sin verificar. Nunca inventes códigos de resultados locales ni certifiques la cobertura. Para los centros checos, una referencia general al RVP no demuestra alineación con el ŠVP concreto. Motivo: se puede avanzar con una propuesta útil y mantener acotadas las afirmaciones documentales.

## Reference: tutor-state

Sección de origen: Modos del tutor y continuidad del aprendizaje


Consulta esta referencia al diseñar un tutor de varios pasos, una actividad reanudable o preparación para exámenes. Estas reglas también sirven para aplicaciones deterministas sin conexión; no requieren IA durante el uso, cuentas ni almacenamiento persistente.

### Estado del tutor: Modela modos y transiciones explícitos

Separa explicación, práctica y evaluación donde la actividad lo necesite. La explicación puede mostrar un ejemplo resuelto. La práctica pide una respuesta, espera, proporciona retroalimentación según criterios y ofrece ayuda. La evaluación sigue reglas declaradas sobre ayuda y momento de la retroalimentación. Permite pausar, pedir ayuda o salir; una evaluación restringida puede terminar o marcar el intento como realizado con apoyo cuando se solicite ayuda sobre el contenido. Conserva las adaptaciones de accesibilidad que no revelen contenido.

En la práctica conversacional, mantén pendiente una sola pregunta accionable salvo que la tarea requiera un conjunto. No generes la respuesta del estudiante ni reveles la solución mientras esperas. Distingue, cuando haga falta, los estados de inactividad, espera de respuesta, evaluación, retroalimentación y pausa. Desactiva los envíos duplicados o asócialos al mismo intento; una respuesta tardía del servicio no debe calificar una pregunta nueva ni sobrescribir un cambio de modo. Trata la salida del modelo como respuesta propuesta, no como permiso para cambiar calificaciones o reglas de evaluación.

Conserva en el estado de la aplicación el modo, objetivo, tarea actual, identificador del intento, exposición a la respuesta y estado de retroalimentación. Muestra un indicador breve de progreso si es útil; repetir una línea decorativa de estado no es gestionar el estado. Ante un cambio explícito de modo, explica las nuevas condiciones de ayuda y conserva la exposición anterior. Una tarea cuya solución se ha revelado no se convierte en evaluación autónoma por cambiarle la etiqueta. Usa una tarea nueva y adecuada cuando necesites evidencia autónoma nueva.

### Estado del tutor: Reanuda desde las evidencias, no desde una afirmación de dominio

Añade guardado o exportación solo cuando continuar entre sesiones sirva al usuario. Una actividad breve y anónima puede no necesitar ninguno. Para actividades reanudables, conserva un punto de control mínimo adaptado a la implementación:

- Versión del formato, versión de actividad o contenido e identificadores de fuentes pertinentes.
- Objetivo, modo actual, identificador de tarea o intento y paso pendiente.
- Evidencias observadas con sus condiciones: autónoma, con apoyo o solución revelada; una evaluación pendiente sigue pendiente.
- Errores o incertidumbres específicos y siguiente paso didáctico.
- Información temporal solo cuando sea necesaria para el repaso espaciado o la interpretación de evidencias.

Evita diagnósticos, identidades innecesarias y transcripciones completas. Indica dónde se guardan los datos, quién puede verlos y cómo borrarlos; quienes compartan dispositivo necesitan una forma explícita de terminar y eliminar el progreso local. Un punto de control exportado puede contener información personal de aprendizaje aunque no incluya un nombre. No exportes claves secretas, claves de respuesta ocultas ni contenido confidencial de exámenes.

Trata los puntos de control importados como datos no confiables. Valida el esquema, tamaños, identificadores y compatibilidad de versiones; nunca ejecutes instrucciones incrustadas ni aceptes puntuaciones importadas como calificaciones oficiales. Cuando importen las calificaciones, valida contra el registro autorizado con controles de acceso adecuados. Si cambió el contenido o no puede resolverse una tarea, explica la discrepancia y reanuda desde un punto seguro y revisado; no restablezcas silenciosamente los logros ni certifiques evidencias obsoletas. Restaurar un intento pendiente no debe volver a enviarlo automáticamente ni otorgar crédito dos veces.

Una entrega de continuidad indica qué demostró el estudiante, en qué tarea y con qué apoyo. No afirma «dominio completo» a partir de una sesión. Una tarea nueva posterior puede comprobar retención o transferencia. Las correcciones confirmadas por el estudiante y las intervenciones docentes deben seguir distinguiéndose de la observación original.

### Estado del tutor: Corrige de forma dirigida sin atrapar al estudiante

Prioriza los errores por su pertinencia para el objetivo y los prerrequisitos, tratando la gravedad como interpretación provisional. Ofrece una pista específica, un caso de contraste o una explicación y después una nueva aplicación. Permite posponer y retomar más tarde. No impongas umbrales arbitrarios de 8/10 o 90 %, prohíbas explicaciones ni asignes puntos a toda interacción. Usa criterios declarados cuando puntuar resulte útil; la calificación de exámenes oficiales necesita su especificación real.

### Estado del tutor: Comprobaciones de implementación

Comprueba solo recorridos pertinentes: pregunta → respuesta → retroalimentación; ayuda → evidencia con apoyo; cambio de modo tras revelar la respuesta; pausa y reanudación sin perder ni contar dos veces un intento; punto de control obsoleto o mal formado; respuesta tardía después de cambiar de tarea; retroalimentación sin resolver tras un fallo. Verifica que coincidan los estados guardados y visibles. Estas comprobaciones establecen el comportamiento, no la eficacia educativa.

## Reference: didactic-rationale

Sección de origen: Por qué incluir métodos didácticos al desarrollar aplicaciones con IA


Consulta esta referencia al explicar el propósito del skill o decidir cómo un método debe cambiar una aplicación. El skill ayuda a desarrolladores y docentes a utilizar IA para diseñar y crear aplicaciones educativas. También orienta aplicaciones con IA durante el aprendizaje cuando procede. El método debe reflejarse en las acciones del estudiante, la retroalimentación y las evidencias; mencionarlo en un prompt o en el nombre de una función resulta insuficiente.

### Justificación didáctica: De la decisión didáctica al comportamiento observable

| Método o perspectiva | Propósito didáctico | Decisión en la aplicación | Evidencia que revisar |
|---|---|---|---|
| Preguntas socráticas | Examinar supuestos y razonamiento | Plantear una pregunta dirigida, esperar y responder a la respuesta real; explicar cuando haga falta | Justificación o revisión de una afirmación, incluida una alternativa correcta |
| Técnica Feynman y autoexplicación | Hacer examinable la explicación del estudiante | Permitir explicar, contrastar con criterios revisados, abordar una laguna y ofrecer un caso nuevo | Relaciones correctas y aplicación; la fluidez no basta |
| Ejemplos resueltos y andamiaje | Ayudar a empezar y avanzar hacia la autonomía | Mostrar pasos, proponer una tarea incompleta y otra nueva; mantener la ayuda solicitada | Diferenciar desempeño con apoyo e intento independiente posterior |
| Recuperación y repaso espaciado | Practicar la reconstrucción del conocimiento y retomarlo tras un intervalo | Preguntar antes de revelar, ofrecer corrección y programar revisiones, incluido material acertado | Desempeño antes de ver la solución, retención posterior y transferencia cuando se comprueben |
| Mapas conceptuales | Explicitar relaciones y prerrequisitos | Etiquetar relaciones, aceptar estructuras válidas equivalentes y facilitar edición accesible | Significado y justificación de los enlaces, no semejanza visual |
| Indagación y simulaciones | Contrastar predicciones con evidencias bajo supuestos explícitos | Mostrar variables, unidades, restricciones y límites del modelo; incluir reflexión | Revisión de explicaciones con observaciones o resultados del modelo identificados |
| Evaluación formativa y metacognición | Decidir el siguiente paso a partir de evidencias | Ofrecer retroalimentación concreta y comparar una predicción con el desempeño | Corrección útil y nuevas evidencias; puntos y confianza no bastan |
| Aprendizaje cooperativo y entre iguales | Apoyar comparación y explicación con responsabilidad | Tarea compartida, aportaciones individuales y resolución de desacuerdos | Razonamiento de cada estudiante; un clic compartido no demuestra comprensión del grupo |

La taxonomía de Bloom describe objetivos cognitivos y tipos de conocimiento; no prescribe dificultad ni seis niveles bloqueados. Un método es apropiado cuando responde al alumnado, al contenido y al obstáculo observado. El catálogo no exige implementar todos los métodos.

### Justificación didáctica: Por qué importa al generar una aplicación

La IA puede producir rápidamente una interfaz, un comprobador y retroalimentación. Esos componentes necesitan un acuerdo didáctico: qué hace el estudiante, qué cuenta como evidencia, qué ayuda recibió y cómo se decide el siguiente paso. Úsalo para delimitar código generado y contenido revisado. La recuperación cambia cuándo se revela la respuesta; el andamiaje modifica controles de ayuda y etiquetas de evidencia. Nombrar un método sin implementar ese comportamiento no cumple el objetivo.

Distingue IA durante la creación e IA durante el uso. Muchos comportamientos pueden funcionar sin conexión con contenido revisado y reglas deterministas. Si la IA resulta útil para respuestas abiertas o diálogo, delimita fuentes, criterios y herramientas, valida la salida y ofrece una alternativa ante fallos. Más conversación, puntuación más estricta o un modelo mayor no demuestran por sí mismos mejor aprendizaje.

### Justificación didáctica: Límites del razonamiento

Es una explicación de decisiones de diseño, no evidencia de que este skill o cada implementación mejore resultados. Exactitud, accesibilidad y viabilidad en el aula requieren comprobaciones apropiadas. Una prueba técnica no demuestra aprendizaje: hacen falta evidencias adecuadas y, para afirmar causalidad, una evaluación pertinente. La investigación enlazada en métodos informa decisiones concretas, no certifica todo el paquete. Mantén revisión docente responsable en decisiones importantes y adapta el currículo al contexto real.

## Reference: learning-games

Sección de origen: Juegos educativos y gamificación con propósito


Consulta esta referencia al diseñar mecánicas, motivación o cambios sustanciales en la relación entre juego y aprendizaje. Combina investigación y decisiones de diseño; no demuestra la eficacia de un producto nuevo. Fuentes comprobadas: 2026-11-14.

### Juegos educativos: Elige la actividad antes de la recompensa

Distingue el juego educativo (se aprende jugando), la gamificación (elementos de juego apoyan otra actividad) y la simulación (un modelo permite investigar sin ganar ni puntuar). Una herramienta puede funcionar sin recompensas.

Describe brevemente: alumnado y conocimientos previos; desempeño esperado; decisión del jugador; consecuencia y retroalimentación; evidencia independiente; siguiente paso. Para una actividad pequeña basta un párrafo. Busca atajos: adivinar, pulsar repetidamente, memorizar posiciones, copiar respuestas o depender de un compañero.

Prioriza mecánicas que exijan el razonamiento previsto. Para trabajar proporciones, permite ajustar una mezcla con restricciones, explicar una predicción y resolver otro caso. Un cuestionario puede servir para recuperar conocimientos; no todo contenido necesita un mundo simulado. Admite soluciones alternativas defendibles en tareas abiertas.

### Juegos educativos: Selecciona un conjunto coherente

| Necesidad | Mecánica e implementación posibles | Comprobación o señal de fallo |
|---|---|---|
| Empezar sin conocer los controles | Primera tarea segura; presentar herramientas cuando se necesitan | Una persona nueva actúa sin explicaciones del autor |
| Comprender un sistema | Predecir, cambiar una variable, observar y explicar | Manipular al azar no sustituye una nueva predicción |
| Retener conocimientos | Misiones de recuperación con retorno diferido y corrección | Desempeño posterior sin ayuda; repetir inmediatamente es reparación |
| Elegir un procedimiento | Alternar tipos confundibles después del apoyo inicial | Elegir y explicar una estrategia; mezclar temas al azar no basta |
| Superar la dificultad inicial | Ejemplo resuelto, completar pasos, reto independiente | Registrar la ayuda y permitir volver a ella |
| Ver el progreso | Mapa privado de habilidades, evidencias y próximos pasos | Distinguir finalización, éxito asistido y desempeño independiente |
| Tener autonomía | Elegir ruta, contexto o método dentro del objetivo | Opciones que cambian la experiencia; requisitos y alternativas claros |
| Despertar curiosidad | Misterio con pistas que sean evidencias disciplinares | La resolución responde a una cuestión del contenido |
| Colaborar | Roles complementarios y rotativos, resultado compartido | Cada participante explica o aplica algo individualmente |
| Reconocer logros | Insignias opcionales con criterios transparentes | Describen evidencias y no sustituyen el juicio de dominio |
| Competir | Retos comparables opcionales o mejora personal | Detectar desventaja, abandono y prisa; ofrecer una vía sin clasificación pública |
| Volver durante meses | Metas propias, sesiones reanudables, recordatorios solicitados | La ausencia no borra evidencias ni bloquea la ayuda |

Son hipótesis de diseño, no una clasificación de funciones de eficacia demostrada. Puntos, rachas, avatares y clasificaciones no tienen un efecto universal. Separa moneda de juego y evidencia educativa. Un error habitual no debe agotar el acceso a la enseñanza. Evita presionar con recompensas que caducan, recuperación de pago, compras de recompensas aleatorias o humillación pública. Son compromisos de diseño, no resultados de comparaciones experimentales de todas las variantes.

La dificultad debe proceder de la decisión objetivo. Lectura, precisión motora y presión temporal pueden distorsionar su medición. Usa velocidad cuando la fluidez o el tiempo de respuesta formen parte del objetivo; interpreta precisión y velocidad por separado. No existe un porcentaje universal de aciertos óptimo. Adapta apoyos usando varias observaciones y permite corregir una asignación inadecuada.

### Juegos educativos: Construye la secuencia

Implementa un problema jugable antes de una economía extensa. Tras la acción ofrece una consecuencia comprensible, retroalimentación útil, otra oportunidad y un punto natural para terminar. Explica el error en relación con la tarea o estrategia; una celebración no corrige una concepción equivocada.

Ofrece un ejemplo resuelto cuando falten conocimientos para un intento útil. Explorar antes de la explicación puede preparar el aprendizaje, pero el fracaso productivo requiere consolidación posterior. No justifica dejar atascado al principiante. Distingue introducción, práctica asistida y evaluación independiente. Mostrar la solución marca el intento como asistido; evalúa después otro caso.

Adapta recuperación, espaciamiento e intercalado al contenido. Retoma también material respondido correctamente. Para recuperar, solicita reconstruir antes de revelar. Alterna casos que exijan discriminación y usa retroalimentación acorde con la actividad. No declares óptimo un calendario fijo para cualquier materia y plazo de retención.

### Juegos educativos: Adapta edades y países

Parte de los conocimientos y apoyos necesarios. En primaria pueden ayudar representaciones concretas y apoyo lector; en secundaria, contrastar explicaciones; en universidad y adultos, autenticidad disciplinar y ritmo flexible. Son hipótesis iniciales: un adulto principiante puede necesitar mucho apoyo y un niño experto mayor desafío.

Comprueba terminología, formatos numéricos y unidades, dirección de lectura, referencias culturales, estructura escolar y dispositivos disponibles. Vincula el currículo a una jurisdicción y versión identificadas. El idioma no determina el currículo nacional. Considera dispositivos compartidos y mediación docente cuando proceda. Simular una acción profesional no certifica competencia práctica.

Proporciona teclado y alternativa con un solo puntero al arrastre, estados textuales además de color o sonido, foco visible, movimiento controlable y tiempos adecuados. Las respuestas alternativas deben conservar la habilidad evaluada. Comprueba accesibilidad y adecuación con usuarios previstos; mencionar UDL o WCAG no las demuestra.

### Juegos educativos: Implementa según la escala

Para actividades breves, usa contenido revisado, reglas deterministas y estado de sesión. Añade persistencia local si reanudar aporta valor. Para productos longitudinales, considera versiones de habilidades y tareas, intentos asistidos e independientes, repasos, exportación, borrado y corrección docente. Cuentas, servidores y telemetría necesitan una finalidad concreta.

Un registro de intento puede incluir `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` y `feedback_version`. Guarda solo campos necesarios; respuestas y horas no tienen por qué salir del dispositivo. Mantén moneda y apariencia en otro estado. Un fallo de red o envío repetido no debe duplicar recompensas ni cambiar una evaluación registrada.

Con IA durante el uso, define fuentes permitidas, límites de evaluación, alternativa ante fallos y revisión humana. Prueba explicaciones erróneas convincentes, respuestas correctas equivalentes e indisponibilidad. Evalúa aprendizaje sin asistencia. Los estudios de tutores concretos no demuestran que cualquier chatbot ayude ni que esperar obligatoriamente antes de pedir ayuda mejore el aprendizaje. Crear con IA no exige usar IA en el producto.

Al coordinar especialistas o agentes, comparte objetivo, ejemplos y reglas de evidencia. Separa revisión disciplinar, didáctica, jugabilidad e implementación. Resuelve desacuerdos con ejemplos o fuentes. Varias personas simuladas en un prompt no equivalen a validación independiente; usa agentes independientes solo cuando esté autorizado y sea útil.

### Juegos educativos: Comprueba tres resultados distintos

1. Funcionamiento: respuestas correctas y alternativas, concepción errónea, adivinación, solución revelada, reintento, reanudación y fallo de red si procede. El éxito asistido no puede convertirse silenciosamente en dominio independiente.
2. Uso y juego: observa a usuarios previstos empezando y recuperándose de un error. Registra confusión, decisiones y posibilidad de terminar. Un piloto pequeño detecta problemas; no demuestra efectos poblacionales.
3. Aprendizaje: tarea nueva sin ayuda, retención diferida cuando corresponda y transferencia fuera de la apariencia del juego. Para comparar eficacia, usa una alternativa creíble con contenido y tiempo comparables; considera conocimientos previos, abandono y participación desigual. Informa de incertidumbre. Tiempo de uso y disfrute no son aprendizaje.

Para proyectos pequeños, documenta la hipótesis y un piloto viable. Para productos de consecuencias importantes, define resultados y comparación antes de recoger datos. Separa métricas de juego y aprendizaje. Revisa o retira mecánicas que favorezcan atajos, desincentiven pedir ayuda o añadan esfuerzo sin función educativa.

### Juegos educativos: Fuentes y límites

- [Sailer y Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w): beneficios medios heterogéneos; efectos motivacionales y conductuales menos estables al exigir mayor rigor. No garantiza una insignia o clasificación concreta.
- [Clark et al., 2016](https://doi.org/10.3102/0034654315582065): las comparaciones de juegos y mejoras apoyan atender al diseño y al andamiaje. El medio no determina el resultado.
- [Li et al., 2024](https://doi.org/10.1007/s11423-023-10337-7): pequeño beneficio medio de motivación intrínseca en 35 intervenciones. Competencia percibida y dominio medido son diferentes.
- [Habgood y Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029): dos estudios de un juego matemático apoyan integrar contenido y acción central; muestras pequeñas y específicas limitan la generalización.
- [Agarwal et al., 2021](https://doi.org/10.1007/s10648-021-09595-9) y [Ruitenburg et al., 2026](https://doi.org/10.1007/s10648-026-10225-5): evidencia escolar sobre recuperación y práctica dependiente del contexto. El segundo distingue recuperación, espaciamiento e intercalado; algunos moderadores tienen pocos estudios.
- [Wisniewski et al., 2020](https://doi.org/10.3389/fpsyg.2019.03087): importan el contenido útil de la retroalimentación y su variabilidad. [Sinha y Kapur, 2021](https://doi.org/10.3102/00346543211019105): resolver antes de recibir instrucción puede ayudar bajo condiciones diseñadas y con límites de alumnado e implementación.
- [Almeida et al., 2023](https://doi.org/10.1016/j.infsof.2022.107142): documenta efectos adversos y atajos; los recuentos de informes negativos no estiman su frecuencia real.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf): marco que vincula objetivos, acciones y evidencias. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf): experiencia de introducción jugable. Son orientaciones de diseño, no estimaciones causales de aprendizaje.
- [Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122) y [Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6): experimentos diferentes sobre diseño del tutor y desempeño sin ayuda; difieren poblaciones, materias e intervenciones.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) ofrece criterios de accesibilidad y [CAST UDL 3.0](https://udlguidelines.cast.org/) un marco de diseño; su función probatoria difiere de la de un experimento educativo.

### Juegos educativos: Conecta experiencia, reglas y transferencia

Usa MDA como perspectiva de diseño: experiencia buscada, conducta esperada del jugador y reglas que la permiten. Descubrir puede requerir un modelo controlable y observaciones significativas; expresarse, varias construcciones válidas. No limites todas las materias a un género. SDT orienta autonomía, competencia y relaciones; MDA o una etiqueta de Octalysis no prueban eficacia.

En un reto de ingeniería abierto define restricciones y éxito verificable sin imponer la solución del autor. Ofrece comparar diseños propios válidos según criterios pertinentes en tensión, como recursos y precisión. Un histograma comunitario necesita datos reales adecuados y participación opcional; no inventes distribuciones. Optimizar no exige ganar moneda.

Conecta representaciones del juego con notación o decisiones reales y comprueba un caso nuevo fuera de sus pistas superficiales. No impongas pantalla dividida ni tres etapas a todo estudiante. La respuesta sensorial debe aclarar cambios significativos sin ocultar razonamiento. Rachas y premios son opcionales y no punitivos; interrumpir no elimina evidencia ni ayuda. Publicar progreso requiere elegir compartir.

[MDA de Hunicke, LeBlanc y Zubek](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) es un marco de diseño. Los estudios anteriores tienen poblaciones y resultados distintos; retención de usuarios no equivale a aprendizaje.

## Reference: design-dialogue

Sección de origen: Diálogo durante el diseño educativo


Úsalo en la primera elección pedagógica sustancial y cuando nueva evidencia o requisitos la reabran. Es un procedimiento de diseño, no una afirmación experimental sobre el aprendizaje.

### Diálogo de diseño: Identifica a quien aprende y sus condiciones

La edad, el papel educativo y la experiencia en la materia son atributos distintos. «Niño» describe un contexto de edad; «alumno» y «estudiante» designan papeles cuyo uso varía según el país. Las categorías se solapan. Usa «persona que aprende» o «participante» en el diseño general y términos locales adecuados en el producto. Los ejemplos escolares no limitan el skill a la infancia. Las instrucciones directas pueden decir «Prueba», «Explica» o «Compara».

Antes de elegir un método, forma un perfil breve del público con datos conocidos: grupo de edad y entorno; conocimientos del tema; lectura e idioma; autonomía y ayuda disponible; objetivo y consecuencias de evaluar; dispositivos y necesidades funcionales de acceso. Son datos de diseño del público, no un expediente personal obligatorio. No exijas fecha de nacimiento, diagnóstico ni historial escolar completo. Señala incógnitas y supuestos; «estudiante» no los determina.

| Contexto y denominación | Qué averiguar | Adaptación posible si hace falta |
| --- | --- | --- |
| Niño de preescolar, si se solicita | Lectura, manejo, acompañamiento adulto y finalidad de la pantalla | Instrucciones concretas breves, juego compartido y actividad fuera de pantalla; no suponer lectura autónoma |
| Alumno de primaria o equivalente | Conceptos, notación, lectura del enunciado y dispositivos | Representación concreta vinculada al concepto, demostración de controles y apoyo |
| Alumno de secundaria inferior o equivalente | Prerrequisitos, diferencias del grupo y cooperación | Comparar estrategias, explicar y elegir apoyo para un objetivo común |
| Estudiante de secundaria superior o formación profesional | Área académica o profesional, experiencia y evaluación | Problema disciplinar, argumentación o escenario profesional; la simulación no sustituye la evaluación práctica |
| Estudiante universitario | Prerrequisitos del área y experiencia en el tema | Tareas auténticas, pruebas y varias soluciones; ejemplos disponibles para temas nuevos |
| Participante adulto, autodidacta o trabajador | Objetivo propio, experiencia, tiempo y uso real | Situaciones pertinentes, saltar lo conocido, ritmo flexible y continuidad |
| Persona mayor, si es pertinente | Experiencia individual, idioma, manejo y acceso | Ajustar texto, tiempo o controles según necesidad; edad no implica poca experiencia digital |
| Grupo mixto | Necesidades comunes y variantes necesarias | Objetivo común, apoyo opcional, distintas entradas y evidencia individual |

Son opciones de diseño, no diagnósticos evolutivos ni asignaciones obligatorias por edad. Etapas y cursos varían entre países. Un niño puede ser avanzado y un adulto principiante. Apoyo lingüístico, accesibilidad y diferencias de ritmo pueden afectar a cualquier grupo. No asignes estilos visuales, auditivos u otros estilos fijos.

Distingue quién aprende, quién maneja la aplicación y quién ve resultados. Un docente puede usar una pantalla compartida, un familiar acompañar al niño y el creador ser otra persona. Un público infantil no determina automáticamente quién accede a sus resultados. Define roles y acceso para el uso concreto.

Si falta un dato que cambia el diseño, pregunta, por ejemplo: «¿Es para niños de primaria, alumnado mayor o adultos principiantes? ¿Qué saben hacer ya en este tema?» Ajusta opciones al encargo, sin repetir todos los grupos ni información conocida. Aclara «estudiantes» cuando su ambigüedad afecte al resultado.

Explica a quién ayuda la propuesta y por qué: «Para estos adultos principiantes recomiendo un ejemplo de su trabajo y retirar apoyo según los intentos autónomos». Niños experimentados pueden necesitar un reto abierto. Un cambio de público reabre idioma, contenido, apoyo, evaluación y controles afectados, no todo el proyecto automáticamente.


### Diálogo de diseño: Ofrece opciones cuando hacen falta

Recoge del proyecto alumnado, conocimientos previos, objetivo, país, dispositivos, tiempo y restricciones conocidos. Pregunta por datos ausentes solo si cambian la decisión. El modo inicial es el acompañamiento continuo. El creador puede delegar una elección o las decisiones habituales posteriores y recuperar después el acompañamiento.

| Momento | Opciones pertinentes que explicar |
| --- | --- |
| Objetivo y primera actividad | Ejemplo resuelto con retirada de apoyo, indagación guiada, recuperación, construcción o proyecto auténtico |
| Motivación y participación | Progreso propio, elección significativa, roles cooperativos, mecánicas opcionales |
| Errores y ayuda | Pista concreta, ejemplo contrastante, explicación directa y nuevo intento |
| Evaluación | Retroalimentación formativa, rúbrica, comprobación independiente, portafolio o revisión entre pares preparada |
| Continuidad | Estado de sesión, continuidad local, repaso espaciado o dificultad calibrada |
| Evidencia del prototipo | Corregir una representación engañosa, reducir apoyo, comprobar transferencia o retirar una recompensa explotada |

Son oportunidades, no paradas obligatorias. Combina decisiones relacionadas en proyectos pequeños. Ofrece alternativas viables con descripción breve, ejemplo en el producto y coste, datos necesarios o limitación relevante. Recomienda una y formula una pregunta concreta. Permite una versión sencilla o aplazamiento cuando proceda; no exijas conocer nombres teóricos. Amplía el catálogo a petición.

### Diálogo de diseño: Conserva las decisiones

En tareas pequeñas basta la conversación; en proyectos largos usa el registro de diseño existente. Conserva objetivo, restricciones, ID del método, motivo, estado, alternativas rechazadas y preguntas abiertas. Estados posibles: `offered`, `selected`, `implemented`, `verified`, `deferred`, `declined`. Separa este registro de los datos del alumnado. Un requisito nuevo reabre solo decisiones afectadas; explica el motivo. No interpretes la falta de respuesta como elección. Mientras una decisión importante espera respuesta, avanza en trabajo independiente.

### Diálogo de diseño: De la elección al producto

Utiliza acción, evidencia, apoyo y comprobación de la ficha del método. Construye una secuencia coherente y explica incompatibilidades. Un ejemplo resuelto puede preceder a la recuperación posterior; el fracaso productivo necesita consolidación. Ninguno exige evaluar en todas las pantallas.

Para fracciones sin conexión: «Recomiendo combinar piezas y mostrar la fracción correspondiente porque buscamos equivalencia. Una recta numérica destaca la misma posición; completar un ejemplo resuelto proporciona más apoyo inicial. ¿Cuál será la actividad principal?» Después ofrece una tarea nueva sin piezas o un análisis de errores para comprobar transferencia. No repitas la entrevista inicial.

El creador encarga una aplicación. No conviertas la conversación en tutoría obligatoria, deberes de programación ni TODO sin resolver. Al entregar, muestra dónde funcionan los métodos elegidos, qué comprobaste y qué sigue incierto. La selección automática del skill depende del entorno; compruébala por separado de su comportamiento una vez activado.

## Reference: cognitive-ux

Sección de origen: Interfaz cognitiva y representaciones


Consulta al diseñar diagramas, multimedia, instrucciones, ubicación de comentarios o interfaces que puedan ocultar la tarea de aprendizaje. Adapta al alumnado y los dispositivos, sin imponer un estilo visual.

### Interfaz cognitiva: Centra la atención en la decisión

Reduce movimiento y sonido irrelevantes durante tareas exigentes; conserva contexto y controles útiles. Coloca etiquetas y explicaciones cerca del objeto sin taparlo. En pantallas pequeñas usa resaltado vinculado, descripción accesible o vista secuencial cuando la proximidad no sea práctica. El color no debe ser el único indicador.

Divide operaciones complejas en pasos controlados por el estudiante. Introduce controles y términos nuevos antes de combinarlos. Mantén una vía directa para personas experimentadas y el regreso a la ayuda. La animación debe aclarar una acción o cambio; ofrece movimiento reducido y un estado estático equivalente y comprensible.

### Interfaz cognitiva: Conecta representaciones y comprueba transferencia

Cuando objetos concretos apoyan un concepto abstracto, muestra la misma relación mediante objetos, diagramas y notación del campo. Explica la correspondencia y pide una aplicación nueva con menos apoyo superficial. La pantalla dividida es una opción. Conserva vías equivalentes con teclado y sin arrastre. Comprueba que no baste emparejar colores o posiciones.

Ejemplo: manipular cantidades iguales, mostrar la igualdad correspondiente y explicar por qué se mantiene; después resolver una igualdad nueva sin manipulativos. Una persona experta puede empezar por la notación. Recupera la representación si ayuda. En otras materias, transferir puede significar evaluar una fuente nueva o aplicar un procedimiento en otro escenario.

### Interfaz cognitiva: Conserva acceso y evidencia útil

Evita flujos simultáneos innecesarios, pero conserva subtítulos, transcripción, repetición, apoyo lingüístico y acceso con lector de pantalla. La redundancia no prohíbe texto junto al audio. No escondas instrucciones esenciales en ayudas disponibles solo al pasar el ratón. Si audio o tiempo forman parte de la habilidad evaluada, explicita las condiciones y revisa las adaptaciones.

En una comprobación conceptual, un juicio opcional de confianza permite comparar creencia y desempeño. No equivale a dominio ni se exige tras cada acción. La retroalimentación explica el contraste pertinente y permite aplicar la corrección; no fabriques sorpresa o dudas sobre trabajo correcto.

Comprueba etiquetas legibles, orden del foco, zoom, pantallas estrechas, movimiento reducido y recorrido completo de ayuda y reintento. Examina la tarea real del estudiante, además de la apariencia. Declara comprobaciones no realizadas.

### Interfaz cognitiva: Fuentes y límites

[Waxman & Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf): orientaciones de diseño, no prohibiciones universales. [Matlen y Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf): concepto temprano orientado a transferencia, no validación de cualquier pantalla dividida. [W3C sobre subtítulos](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html): condiciones de accesibilidad. Verifica los requisitos normativos vigentes para la versión objetivo.

## Reference: adaptive-practice

Sección de origen: Práctica adaptativa y continuidad


Consulta para sesiones repetidas, planificación o selección de dificultad. Distingue cuándo repasar, qué tarea presentar y cuánta ayuda ofrecer. No requieren el mismo modelo.

| Necesidad | Implementación pequeña | Ampliación opcional y requisitos |
| --- | --- | --- |
| Una actividad | Tareas revisadas, secuencia explícita, ayuda y estado de sesión | Normalmente sin modelo persistente del estudiante |
| Recuperación tras días | Calendario explícito e historial local | FSRS para ítems estables y eventos de repaso interpretables |
| Elegir dificultad | Niveles revisados y reglas transparentes | Elo con datos adecuados, incertidumbre y calibración |
| Dependencias entre habilidades | Mapa con evidencia independiente | BKT o IRT con modelo defendible, datos y validación |
| Plan prolongado | Objetivo, tiempo disponible, fase actual y tarea siguiente | Hitos revisables, preguntas pendientes y fechas de repaso |

Explica la función antes del algoritmo. Conserva el stack existente; no instales planificador, servidor o cuentas por figurar aquí. Las reglas sencillas son válidas con límites explícitos. HLR es otro modelo entrenado para datos adecuados, no un requisito inicial.

### Práctica adaptativa: Condiciones para adaptar

Define ID estables de ítems y habilidades, versiones de contenido, interpretación de respuestas y condiciones de apoyo. Separa respuestas adivinadas, asistidas, reveladas e independientes. Respeta el significado de las valoraciones de la biblioteca; no conviertas respuestas asistidas en recuperación independiente. Separa moneda del juego y modelo de aprendizaje. Conserva datos mínimos y marcas temporales solo cuando la planificación las necesite.

Define el inicio sin historial y una alternativa útil cuando los datos falten, estén dañados o desactualizados. Revisa supuestos con datos representativos, incluidos idioma y accesibilidad. Permite corrección docente y acceso a ayuda. La predicción es incierta: ni un objetivo universal de 80–90 % de aciertos ni dos respuestas correctas miden la ZDP o prueban dominio. La retención deseada supone un equilibrio con la carga de trabajo, no una garantía educativa.

Si eliges un algoritmo, usa una implementación mantenida y verifica su versión. Comprueba actualizaciones, zonas horarias y cambio de día, envíos duplicados, cambios de contenido, exportación, recuperación y datos inválidos. Compara la ampliación con la base sencilla; precisión predictiva, participación y aprendizaje son resultados distintos. No infieras discapacidad o personalidad del tiempo de respuesta.

### Práctica adaptativa: Cierra o retoma una fase

Registra resultado, condiciones de ayuda, preguntas abiertas y siguiente paso viable. Completar una fase no equivale a demostrar dominio. Crear otra no completa automáticamente la anterior. Los resúmenes conservan enlaces necesarios a evidencias e incertidumbre, no transcripciones completas. Al volver, comprueba supuestos antiguos con una tarea proporcionada; una interrupción no borra el progreso.

### Práctica adaptativa: Fuentes

[Documentación Anki FSRS](https://docs.ankiweb.net/manual/deck-options), [Pelánek sobre Elo educativo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) y [Settles y Meeder sobre HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Describen modelos y contextos específicos, no la eficacia de una aplicación nueva. Verifica la documentación actual al integrar una biblioteca.

## Aviso de licencia

```text
MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
