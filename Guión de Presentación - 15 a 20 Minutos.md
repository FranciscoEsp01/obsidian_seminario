---
title: "Guión de Presentación: Inteligencia Artificial Explicable (XAI) para la Clasificación de Malware"
tipo: guion-presentacion
autores:
  - "Rigoberto Ignacio Enrique Canales Puebla"
  - "Francisco Ignacio Espinoza Vasquez"
profesor_guia: "Pamela Hermosilla Monckton"
profesor_correferente: "Sebastian Berrios Vasquez"
fecha: 2026-09-12
duracion_objetivo: "17 a 18 minutos (Rango estipulado: 15 a 20 minutos)"
tags:
  - seminario
  - guion
  - presentacion
  - oratoria
  - xai
  - pucv
related: "[[Informe de Avance - Seminario de Título]], [[Presentación - Avance Seminario de Título]], [[Seminario de Título - MOC]]"
---

# GUIÓN DE PRESENTACIÓN: AVANCE DE SEMINARIO DE TÍTULO
## *Inteligencia Artificial Explicable (XAI) para la Clasificación de Malware: Diseño de un Framework Multinivel para la Optimización del Costo Computacional*

> [!IMPORTANT] **Estrategia de Tiempo (15 a 20 Minutos)**
> * **Tiempo Objetivo Ideal:** **17 minutos y 30 segundos** (margen seguro de $\pm 2$ minutos).
> * **Ritmo de Exposición:** Pausado, técnico y seguro (~125 palabras por minuto).
> * **Distribución de Roles:** Si exponen ambos integrantes (Rigoberto y Francisco), se indica en el guión el punto exacto de relevo (Diapositiva 8/9).

---

## ⏱️ Tabla Control de Tiempos por Diapositiva

![[cronometro_presentacion.png]]

| N° | Título de la Diapositiva | Tiempo Diapo | Tiempo Acumulado |
|:---:|:---|:---:|:---:|
| **1** | Portada y Presentación Protocolar | 0:50 | **0:00 – 0:50** |
| **2** | Contexto y Motivación: El Malware en los SOCs | 1:15 | **0:50 – 2:05** |
| **3** | El Problema de la «Caja Negra» en Ciberseguridad | 1:15 | **2:05 – 3:20** |
| **4** | La Paradoja de XAI: El Cuello de Botella Computacional | 1:25 | **3:20 – 4:45** |
| **5** | Preguntas de Investigación y Brecha en la Literatura | 1:15 | **4:45 – 6:00** |
| **6** | Objetivos: General y Específicos por Dimensión | 1:00 | **6:00 – 7:00** |
| **7** | Marco Teórico y Revisión Sistemática (PRISMA) | 1:20 | **7:00 – 8:20** |
| **8** | Análisis Comparativo del Estado del Arte *(Punto de Relevo)* | 1:15 | **8:20 – 9:35** |
| **9** | Arquitectura del Framework Multinivel Propuesto | 1:30 | **9:35 – 11:05** |
| **10** | Nivel 1: Selección Inteligente de Características | 1:15 | **11:05 – 12:20** |
| **11** | Nivel 2: Stacking Ensemble y Destilación de Conocimiento | 1:25 | **12:20 – 13:45** |
| **12** | Nivel 3: Explicabilidad Adaptativa y Motor de Caché | 1:35 | **13:45 – 15:20** |
| **13** | Diseño Experimental: Datasets, Métricas y Baselines | 1:15 | **15:20 – 16:35** |
| **14** | Plan de Trabajo y Estado de Avance Actual | 1:05 | **16:35 – 17:40** |
| **15** | Conclusiones y Ronda de Preguntas | 0:50 | **17:40 – 18:30** |

---

## 🎙️ Guión Paso a Paso (Palabra por Palabra)

---

### Diapositiva 1: Portada y Presentación
**Tiempo:** 0:00 – 0:50 (50 segundos)

> *"Muy buenos días, profesora Pamela Hermosilla, profesor Sebastian Berrios y presentes.*
> 
> *Junto a mi compañero [Nombre del compañero], quien les habla [Mi Nombre], tenemos el agrado de presentar nuestro Informe de Avance de Seminario de Título, titulado: **'Inteligencia Artificial Explicable (XAI) para la Clasificación de Malware: Diseño de un Framework Multinivel para la Optimización del Costo Computacional'**, desarrollado en la Escuela de Ingeniería Informática de la Pontificia Universidad Católica de Valparaíso.*
> 
> *A lo largo de esta presentación expondremos el problema operativo que enfrentan los centros de ciberseguridad modernos, la justificación formal de nuestra propuesta y toda la arquitectura y metodología estructurada durante esta primera fase."*

*(Transición fluida)*: *"Para comenzar, revisemos el contexto que motiva esta investigación..."*

---

### Diapositiva 2: Contexto y Motivación
**Tiempo:** 0:50 – 2:05 (1 min 15 s)

> *"Hoy en día, el panorama de la ciberseguridad enfrenta una crisis de volumen y sofisticación. Diariamente circulan cientos de miles de nuevas variantes de malware diseñadas específicamente para evadir controles mediante técnicas de polimorfismo, empaquetamiento y ataques de día cero (*zero-day*). Ante esto, los sistemas antivirus clásicos basados en firmas estáticas han quedado obsoletos.*
> 
> *Para contrarrestar esto, la industria ha adoptado masivamente modelos de Machine Learning y Deep Learning, los cuales alcanzan niveles de precisión sobresalientes, a menudo por sobre el 99%.*
> 
> *Sin embargo, el verdadero desafío ocurre cuando intentamos desplegar estos modelos en un Centro de Operaciones de Seguridad, conocido como SOC. En un SOC se reciben y analizan miles de eventos por segundo en tiempo real, donde cada milisegundo cuenta para contener una amenaza antes de que comprometa la red corporativa."*

*(Transición fluida)*: *"Y es precisamente en este escenario donde surge el primer gran obstáculo: la naturaleza opaca de estos modelos..."*

---

### Diapositiva 3: El Problema de la «Caja Negra» en Ciberseguridad
**Tiempo:** 2:05 – 3:20 (1 min 15 s)

> *"A pesar de su alta precisión, los modelos avanzados operan esencialmente como 'cajas negras'. Es decir, emiten una predicción, pero ocultan por completo los motivos internos que llevaron a esa decisión.*
> 
> *Para un analista de ciberseguridad en el SOC, saber únicamente que un archivo tiene un '99.8% de probabilidad de ser malware' es insuficiente. Antes de que el equipo active protocolos críticos —como desconectar un servidor de producción, aislar bases de datos o revocar credenciales— el analista necesita responder: **¿Por qué el modelo dice que es malware?**
> 
> *Comprender la causa de la alerta permite extraer lo que en seguridad llamamos Indicadores de Compromiso (IoCs): saber qué llamadas al sistema específicas, qué claves de registro alteradas o qué cabeceras sospechosas originaron la alerta. Si el modelo no puede justificarse, el equipo pierde confianza en la herramienta, se incrementa la fatiga por alertas y se ralentiza la respuesta a incidentes."*

*(Transición fluida)*: *"Para solucionar esta opacidad existe la Inteligencia Artificial Explicable, pero su aplicación genera una paradoja crítica..."*

---

### Diapositiva 4: La Paradoja de XAI y el Cuello de Botella Computacional
**Tiempo:** 3:20 – 4:45 (1 min 25 s)

> *"Para abrir estas cajas negras, la literatura científica recurre a técnicas de XAI como SHAP y LIME. SHAP, basado en la teoría de juegos cooperativos mediante Valores de Shapley, nos entrega una base matemática muy sólida sobre la importancia de cada variable. Y LIME nos aproxima el comportamiento local mediante perturbaciones.*
> 
> *Sin embargo, aquí nos encontramos con un cuello de botella de ingeniería sumamente severo: el **alto costo computacional**.*
> 
> *Algoritmos agnósticos como KernelSHAP tienen una complejidad combinatoria exponencial, del orden de $\mathcal{O}(2^n)$, donde $n$ es la cantidad de características. Por su parte, LIME requiere generar, simular y clasificar miles de muestras sintéticas perturbadas por cada archivo individual.*
> 
> *Si consideramos que un archivo ejecutable analizado en ciberseguridad se describe mediante cientos o miles de variables —como llamadas a la API de Windows o entropía de secciones PE—, calcular estas explicaciones para cada alerta satura la CPU y colapsa los tiempos de respuesta. En pocas palabras: **la explicabilidad profunda tradicional es incompatible con el monitoreo en tiempo real de un SOC**."*

*(Transición fluida)*: *"Al analizar qué soluciones existían para esto en la comunidad científica, descubrimos una importante brecha..."*

---

### Diapositiva 5: Preguntas de Investigación y Brecha en la Literatura
**Tiempo:** 4:45 – 6:00 (1 min 15 s)

> *"Al estudiar el estado del arte, constatamos que prácticamente todos los trabajos se concentran en mejorar la precisión del clasificador o en verificar que SHAP y LIME generen gráficos comprensibles. Sin embargo, **la literatura científica prácticamente omite el costo computacional y la latencia** que estas técnicas introducen en producción.*
> 
> *Ante este vacío, formulamos nuestra **Pregunta General de Investigación**:*
> *¿En qué medida es posible reducir el costo computacional de XAI en la clasificación de malware mediante un enfoque multinivel que integre selección de características, destilación de conocimiento y explicabilidad adaptativa, sin comprometer la precisión de la detección ni la fidelidad de las explicaciones?*
> 
> *De esta interrogante se desprenden tres preguntas específicas que atacan directamente los tres focos del problema:*
> 1. *Primero: ¿Cómo influye la reducción previa de variables en los tiempos de SHAP y LIME?*
> 2. *Segundo: ¿Es viable transferir el conocimiento de un ensamble complejo a un modelo más ligero mediante destilación, permitiendo usar TreeSHAP en tiempo polinomial?*
> 3. *Y tercero: ¿En qué proporción un esquema adaptativo según la confianza del modelo, asistido por una caché de firmas, reduce el costo computacional promedio?"*

*(Transición fluida)*: *"A partir de estas preguntas, estructuramos formalmente los objetivos del proyecto..."*

---

### Diapositiva 6: Objetivos: General y Específicos por Dimensión
**Tiempo:** 6:00 – 7:00 (1 min 00 s)

> *"Nuestro **Objetivo General** es diseñar, construir y validar un framework multinivel para reducir el costo computacional de la XAI en la clasificación de malware, con el propósito de viabilizar el uso de modelos transparentes en operaciones de ciberseguridad que exigen respuestas rápidas.*
> 
> *Para cumplirlo, dividimos el proyecto en tres dimensiones metodológicas claras:*
> 
> *En la **Dimensión Estudio**:*
> * *OE1: Ejecutar una revisión sistemática de literatura sobre los cuellos de botella de XAI en malware.*
> * *OE2: Definir el marco formal de referencia y las métricas para evaluar costo computacional y calidad explicativa.*
> 
> *En la **Dimensión Desarrollo**:*
> * *OE3: Diseñar la arquitectura multinivel y sus interacciones.*
> * *OE4: Construir el prototipo funcional integrado compatible con clasificadores y librerías XAI.*
> 
> *Y en la **Dimensión Validación**:*
> * *OE5: Evaluar experimentalmente el sistema sobre datasets públicos frente a las líneas base tradicionales."*

*(Transición fluida)*: *"Veamos a continuación el marco teórico y la revisión sistemática que fundamenta este trabajo..."*

---

### Diapositiva 7: Marco Teórico y Revisión Sistemática (PRISMA)
**Tiempo:** 7:00 – 8:20 (1 min 20 s)

> *"Para garantizar la rigurosidad científica de nuestro estado del arte, ejecutamos una Revisión Sistemática de Literatura siguiendo de manera estricta el estándar internacional **PRISMA**.*
> 
> *Definimos dos preguntas de investigación focalizadas: qué técnicas XAI se usan hoy en malware y cuáles son los cuellos de botella computacionales reportados.*
> 
> *La recolección de literatura cubrió las 5 bases científicas más reconocidas en informática: **IEEE Xplore, Scopus, ACM Digital Library, ScienceDirect y Web of Science**.*
> 
> *Aplicamos cadenas de búsqueda booleanas cruzando los términos obligatorios de ciberseguridad, XAI y costo/latencia, y ejecutamos un protocolo de filtrado en cuatro fases: primero eliminamos duplicados; luego cribamos por título y resumen descartando formatos no válidos o dominios ajenos; después evaluamos los textos completos excluyendo aquellos que no reportaran métricas cuantitativas reproducibles; y finalmente seleccionamos los estudios primarios para la síntesis comparativa."*

*(Transición fluida)*: *"Los resultados de esta comparación se resumen en la siguiente matriz..."*

---

### Diapositiva 8: Análisis Comparativo del Estado del Arte
**Tiempo:** 8:20 – 9:35 (1 min 15 s)
*(Nota: Si exponen dos personas, aquí puede tomar la palabra el segundo expositor).*

> *"En la tabla comparativa podemos apreciar las limitaciones de los trabajos más representativos de la literatura:*
> 
> *Por ejemplo, el trabajo de **Ullah et al.** utiliza un ensamble Stacking sobre ejecutables PE alcanzando más del 99% de exactitud con SHAP y LIME, pero los propios autores reconocen el altísimo costo computacional de generar explicaciones de forma continua.*
> 
> *Por su parte, **Kim et al.** en el ecosistema Android transforman código a Grafos de Llamadas a Funciones (FCG). Si bien logran explicabilidad visual, la conversión y manipulación de grafos genera una sobrecarga previa enorme en tiempo de cómputo.*
> 
> *Finalmente, **Alotaibi** utiliza fusión multimodal profunda con mecanismos de atención interna, pero su arquitectura resulta hipercompleja y demanda un consumo de recursos prohibitivo.*
> 
> *Esto nos confirma tres brechas esenciales: exceso de complejidad en los modelos, transformaciones de datos demasiado pesadas y una total falta de optimización en la etapa de explicación. Frente a esto, nuestra investigación plantea una alternativa de ingeniería concreta."*

*(Transición fluida)*: *"Y esa alternativa es nuestra arquitectura de framework multinivel..."*

---

### Diapositiva 9: Arquitectura del Framework Multinivel Propuesto
**Tiempo:** 9:35 – 11:05 (1 min 30 s)

> *"En esta lámina presentamos el núcleo conceptual de nuestro proyecto: la **Arquitectura Multinivel del Framework**.*
> 
> *El principio rector detrás de este diseño es **desacoplar la alta capacidad de detección del clasificador del costo computacional de su explicabilidad**.*
> 
> *El flujo opera de manera secuencial ante una muestra entrante sospechosa:*
> * *Primero ingresa al **Nivel 1: Selección de Características**, donde podamos el espacio dimensional antes de la inferencia.*
> * *Luego pasa al **Nivel 2: Clasificación y Destilación**, donde empleamos un modelo 'estudiante' optimizado que replica la exactitud de un ensamble pero permite cálculos analíticos rápidos.*
> * *Y finalmente ingresa al **Nivel 3: Explicabilidad Adaptativa y Motor de Caché**, el cual modula la profundidad del análisis según la certidumbre de la detección.*
> 
> *El resultado final es una **Alerta Explicada** entregada al analista del SOC con mínima latencia y máximo valor técnico.*
> 
> *A continuación, profundizaremos en el funcionamiento y justificación técnica de cada uno de estos tres niveles."*

*(Transición fluida)*: *"Comencemos revisando el Nivel 1..."*

---

### Diapositiva 10: Nivel 1 — Selección Inteligente de Características
**Tiempo:** 11:05 – 12:20 (1 min 15 s)

> *"El Nivel 1 aborda el problema de la dimensionalidad. En ciberseguridad, un binario puede descomponerse en miles de características: llamadas al sistema, librerías dinámicas, permisos y metadatos.*
> 
> *Como vimos, algoritmos como KernelSHAP tienen una complejidad que escala exponencialmente respecto a $n$, el número de variables ($\mathcal{O}(2^n)$). Si intentamos calcular explicaciones sobre todas las variables, el cómputo se vuelve intratable.*
> 
> *Para resolver esto, implementamos una estrategia de selección previa en dos vertientes:*
> 1. *Primero, un filtrado rápido basado en modelos de árboles (Random Forest y LightGBM) que descarta atributos constantes, redundantes o con nulo aporte discriminativo.*
> 2. *Y segundo, la exploración de metaheurísticas de optimización, como el Algoritmo de Optimización de Ballenas (WOA) o algoritmos genéticos, configurados con una función de aptitud multiobjetivo que minimiza el número de variables manteniendo intacto el $F_1$-Score.*
> 
> *Al reducir $n$ antes de invocar la explicabilidad, aliviamos directamente la carga combinatoria de todo el pipeline."*

*(Transición fluida)*: *"Con el espacio de características acotado, pasamos al Nivel 2: la clasificación y destilación..."*

---

### Diapositiva 11: Nivel 2 — Stacking Ensemble y Destilación de Conocimiento
**Tiempo:** 12:20 – 13:45 (1 min 25 s)

> *"En la detección de malware moderno, un clasificador simple no es suficiente: necesitamos la robustez de un **Stacking Ensemble**, que combina múltiples clasificadores base para detectar malware polimórfico y empaquetado. Este ensamble actúa como nuestro **Modelo Profesor**, estableciendo el techo de rendimiento predictivo del proyecto.*
> 
> *Sin embargo, auditar directamente con XAI un ensamble apilado de múltiples capas colapsaría la CPU del SOC.*
> 
> *¿Cómo resolvemos este dilema? Mediante **Destilación de Conocimiento (Knowledge Distillation)**. Transferimos las probabilidades y representaciones aprendidas por el profesor hacia un modelo individual y liviano: nuestro **Modelo Estudiante**, para el cual seleccionamos **LightGBM**.*
> 
> *Esta decisión técnica es fundamental: LightGBM no solo tiene inferencia casi instantánea en CPU, sino que habilita el uso de **TreeSHAP**.*
> 
> *TreeSHAP es un algoritmo que calcula Valores de Shapley matemáticamente exactos en **tiempo polinomial**: del orden de $\mathcal{O}(T \cdot L \cdot D^2)$, donde $T$ es el número de árboles, $L$ las hojas y $D$ la profundidad. Pasamos de una complejidad exponencial a una polinomial, reduciendo el tiempo de cálculo de minutos a milisegundos."*

*(Transición fluida)*: *"Pero aún podemos ser más eficientes. Esto nos lleva al Nivel 3..."*

---

### Diapositiva 12: Nivel 3 — Explicabilidad Adaptativa y Caché de Firmas
**Tiempo:** 13:45 – 15:20 (1 min 35 s)

> *"En la operación diaria de un SOC, la gran mayoría de los eventos son tráfico normal o familias de malware conocidas y evidentes. Es ineficiente gastar el mismo poder de cómputo en una muestra obvia que en una muestra dudosa.*
> 
> *Por esto, diseñamos un esquema de **Explicabilidad Adaptativa gobernado por la probabilidad posterior $P(\hat{y} \mid x)$**, dividido en tres regímenes:*
> 1. *Si la confianza es muy alta ($P \ge 0.95$), estamos ante un caso claro. Se despacha un **Régimen Ligero**: un cálculo rápido del Top-5 de variables mediante TreeSHAP vectorizado para triage instantáneo.*
> 2. *Si la confianza es intermedia (entre $0.80$ y $0.95$), activamos el **Régimen Estándar**: una explicación completa de todas las variables con TreeSHAP, ideal para binarios empaquetados o con firmas ambiguas.*
> 3. *Y si la certidumbre cae por debajo de $0.80$, la muestra se marca como crítica y se activa el **Régimen Profundo**: combinamos TreeSHAP con perturbaciones locales de LIME para una auditoría forense exhaustiva.*
> 
> *Estos umbrales se calibrarán formalmente mediante Diagramas de Fiabilidad.*
> 
> *Además, integramos una **Caché de Firmas Explicativas Vectorial**: como los ciberdelincuentes lanzan campañas con miles de variantes casi idénticas, si una muestra entrante presenta una distancia coseno menor a $\delta = 0.03$ respecto a un vector ya explicado, retornamos la explicación almacenada en **tiempo constante $\mathcal{O}(1)$**."*

*(Transición fluida)*: *"Veamos ahora cómo validaremos empíricamente este diseño..."*

---

### Diapositiva 13: Diseño Experimental: Datasets, Métricas y Baselines
**Tiempo:** 15:20 – 16:35 (1 min 15 s)

> *"Para la fase de laboratorio seleccionamos dos conjuntos de datos públicos de referencia que cubren los dos ecosistemas más atacados:*
> * *Para Android: **CICMalDroid 2020**, con más de 17.000 muestras que incluyen Adware, Banking, Ransomware, Riskware y Benigno, con análisis estático y dinámico.*
> * *Para Windows: **ClaMP Dataset**, con ejecutables PE estructurados en 68 características de cabeceras y secciones.*
> * *Ambos datasets se particionarán de forma estratificada en 70% entrenamiento, 15% validación y 15% prueba.*
> 
> *Para evaluar el sistema definimos tres categorías de métricas:*
> * *En **Rendimiento**: Accuracy, Macro $F_1$ y AUC-ROC, para asegurar que no haya degradación en la detección.*
> * *En **Costo Computacional**: Latencia de inferencia ($t_{\text{inf}}$), latencia de explicación ($t_{\text{exp}}$), memoria RAM pico, throughput y el Factor de Aceleración o Speedup ($S$).*
> * *Y en **Calidad XAI**: Mediremos la Fidelidad (*Faithfulness*) mediante pruebas de perturbación, y la Estabilidad (*Stability*) ante variaciones mínimas.*
> 
> *Todo esto se contrastará contra dos baselines: un enfoque tradicional sin optimización (Baseline 1) y el estado del arte representado por arquitecturas tipo MAL-XSEL (Baseline 2)."*

*(Transición fluida)*: *"A continuación, revisemos el estado de avance y la planificación temporal..."*

---

### Diapositiva 14: Plan de Trabajo y Estado de Avance Actual
**Tiempo:** 16:35 – 17:40 (1 min 05 s)

> *"El desarrollo del proyecto está planificado a lo largo de los dos semestres reglamentarios:*
> 
> *Al día de hoy, en este **Semestre I de Seminario de Título**, hemos completado con éxito:*
> * *La Tarea 1: Planteamiento del problema y contexto en SOCs.*
> * *La Tarea 2: La revisión sistemática de literatura bajo protocolo PRISMA (cumpliendo el Objetivo Específico 1).*
> * *La Tarea 3: La formulación formal de objetivos y alcance.*
> * *Y nos encontramos finalizando la Tarea 4: El diseño metodológico y la formulación técnica de la arquitectura y métricas.*
> 
> *Para los meses restantes de este semestre (octubre a diciembre), tenemos planificada la preparación y limpieza de los datasets (Tarea 5) y la implementación de los benchmarks de las líneas base (Tarea 6), culminando con la entrega del Informe Final de Seminario (Hito 1).*
> 
> *Posteriormente, durante el Semestre II en Trabajo Final de Título, ejecutaremos el desarrollo del prototipo, las pruebas experimentales comparativas, la redacción de la memoria y la defensa final ante comisión."*

*(Transición fluida)*: *"Para concluir nuestra presentación..."*

---

### Diapositiva 15: Conclusiones y Ronda de Preguntas
**Tiempo:** 17:40 – 18:30 (50 segundos)

> *"A modo de conclusión:*
> * *Este informe de avance consolida las bases teóricas, arquitectónicas y procedimentales para resolver un problema crítico y real en la ciberseguridad moderna: la incompatibilidad entre la transparencia de los modelos y las exigencias de velocidad operativa de un SOC.*
> * *Nuestra propuesta no es una simple suma de algoritmos, sino una respuesta de ingeniería encadenada que ataca el costo computacional reduciendo dimensiones, acelerando el modelo mediante destilación y aplicando explicabilidad solo con la intensidad que cada muestra requiere.*
> * *Con este avance, el proyecto queda en una posición óptima y con un cronograma riguroso para comenzar la etapa experimental.*
> 
> *Agradecemos sinceramente su atención y quedamos a disposición de la profesora Pamela Hermosilla y el profesor Sebastian Berrios para sus preguntas y comentarios. Muchas gracias."*

---

## 🛡️ Guía Táctica para la Ronda de Preguntas (Comisión)

Esta sección contiene las respuestas preparadas ante las preguntas técnicas más probables de la comisión evaluadora:

### Pregunta 1: *¿Por qué usar destilación de conocimiento en vez de entrenar directamente un LightGBM desde cero?*
* **Respuesta del expositor:**
  > *"Excelente pregunta, profesor(a). El motivo es la capacidad de generalización. El malware moderno utiliza técnicas avanzadas de evasión y polimorfismo. La literatura demuestra que un clasificador individual como LightGBM entrenado directamente sobre datos crudos tiende a sobreajustar o a no capturar patrones complejos no lineales tan bien como un ensamble apilado (Stacking) que combina árboles, SVMs y redes neuronales.*
  > *Al utilizar destilación de conocimiento, el ensamble actúa como 'Profesor' aprendiendo las fronteras suaves de decisión (las 'dark knowledge' o probabilidades calibradas). Luego, LightGBM aprende a imitar esa distribución suave. Obtenemos lo mejor de dos mundos: la capacidad de generalización del ensamble, pero con la velocidad de inferencia y la compatibilidad con TreeSHAP de LightGBM."*

---

### Pregunta 2: *¿Cómo justifican los umbrales de certidumbre de 0.95 y 0.80 para el esquema adaptativo?*
* **Respuesta del expositor:**
  > *"Los umbrales de 0.95 y 0.80 son valores basales fundamentados en la calibración empírica de clasificadores de gradient boosting. En conjuntos de datos de malware, las muestras con probabilidad posterior sobre el 95% caen en regiones de alta densidad donde el riesgo de falso positivo es marginal (menor al 1%), por lo que basta una explicación ligera de triage.*
  > *Por debajo de 0.80 se concentra la mayor entropía en la frontera de decisión. Sin embargo, un aspecto metodológico clave de nuestro trabajo es que estos valores no quedarán fijos: durante la fase de validación experimental utilizaremos **Diagramas de Fiabilidad (Reliability Diagrams)** sobre el conjunto de validación para optimizar formalmente $\theta_{\text{alto}}$ y $\theta_{\text{bajo}}$, equilibrando la reducción de latencia con la tasa de falsos positivos no auditados."*

---

### Pregunta 3: *¿Por qué eligieron una distancia coseno de $\delta = 0.03$ para la caché de firmas?*
* **Respuesta del expositor:**
  > *"El umbral $\delta = 0.03$ representa una similitud coseno de al menos el 97% entre vectores de características. En ciberseguridad, los generadores automáticos de malware y los troyanos polimórficos crean miles de binarios que comparten prácticamente el 98% o 99% de su estructura (mismas APIs importadas y mismas secuencias de bytes), alterando solo variables superficiales para cambiar el hash criptográfico (MD5/SHA256).*
  > *Un umbral de 0.03 garantiza que solo se reutilicen explicaciones de muestras que pertenecen inequívocamente a la misma familia o campaña, asegurando que la explicación almacenada sea 100% representativa y responda en tiempo constante $\mathcal{O}(1)$."*

---

### Pregunta 4: *¿Cómo evaluarán cuantitativamente la fidelidad (Faithfulness) de las explicaciones?*
* **Respuesta del expositor:**
  > *"La fidelidad mide si las características que el método XAI marca como importantes realmente son las que hacen decidir al modelo. Lo evaluaremos mediante **pruebas de perturbación controlada**:*
  > *Tomamos las $k$ características con mayor valor Shapley o peso en LIME y las enmascaramos o alteramos (por ejemplo, seteándolas en cero o permutándolas). Si la explicación es fiel, la probabilidad predicha del modelo debe desplomarse drásticamente. Si alteramos esas variables y la predicción casi no cambia, significa que la explicación no era fiel.*
  > *Compararemos cuantitativamente la curva de caída de probabilidad de nuestro framework frente a la del Baseline tradicional."*

---

### Pregunta 5: *¿Qué librerías y entorno utilizarán para medir el consumo de recursos?*
* **Respuesta del expositor:**
  > *"Utilizaremos Python con las bibliotecas estándar de la industria (`scikit-learn`, `lightgbm`, `shap` y `lime`). Para medir el costo computacional con rigor utilizaremos `memory_profiler` para registrar la memoria RAM pico en megabytes, y módulos de alta precisión temporal para registrar $t_{\text{inf}}$ y $t_{\text{exp}}$ en milisegundos.*
  > *Para evitar que fluctuaciones del sistema operativo distorsionen las mediciones, cada prueba experimental se ejecutará en 10 repeticiones independientes en un entorno de cómputo local controlado, reportando promedios y desviaciones estándar."*

---

## 🎯 Consejos Finales para la Exposición

1. **Contacto Visual y Postura:** Mirar alternadamente a la profesora Pamela Hermosilla y al profesor Sebastian Berrios. No quedarse mirando fijamente la pantalla ni leer las diapositivas.
2. **Uso del Tiempo:** Llevar un cronómetro visible en la mesa o celular en modo avión. Al minuto 10 deben estar presentando la arquitectura del framework (Diapositiva 9). Si van en el minuto 12 y aún no llegan a la arquitectura, aceleren las transiciones.
3. **Manejo de Transiciones:** Usen las frases de enlace sugeridas en el guión; esto demuestra dominio conceptual y que la presentación cuenta una historia lógica continua.
4. **Seguridad en la Terminología:** Usar con naturalidad términos como *Valores de Shapley*, *Árboles de Decisión*, *Stacking Ensemble*, *Diagramas de Fiabilidad*, *Distancia Coseno* y *Tiempo Polinomial vs Exponencial*.
