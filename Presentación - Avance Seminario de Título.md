---
title: "Presentación de Avance: Inteligencia Artificial Explicable (XAI) para la Clasificación de Malware"
tipo: presentacion-slides
autores:
  - "Rigoberto Ignacio Enrique Canales Puebla"
  - "Francisco Ignacio Espinoza Vasquez"
profesor_guia: "Pamela Hermosilla Monckton"
profesor_correferente: "Sebastian Berrios Vasquez"
fecha: 2026-09-12
duracion_estimada: "15 a 20 minutos"
diapositivas_totales: 15
tags:
  - seminario
  - presentacion
  - slides
  - xai
  - malware
  - pucv
related: "[[Informe de Avance - Seminario de Título]], [[Guión de Presentación - 15 a 20 Minutos]], [[Seminario de Título - MOC]]"
---

# DIAPOSITIVAS: PRESENTACIÓN DE AVANCE DE SEMINARIO DE TÍTULO

> [!TIP] **Modo de Uso**
> Estas diapositivas están formateadas con separadores estándar `---` compatibles con **Obsidian Slides**, **Marp** y herramientas de presentación Markdown. Además, puedes copiar y pegar su contenido directamente en Microsoft PowerPoint o Google Slides. Cada diapositiva incluye:
> * **Diseño Visual Sugerido:** Distribución de elementos y diagramas.
> * **Contenido en Pantalla:** Textos concisos, métricas y fórmulas clave.
> * **Notas del Orador (`<!-- Note -->`):** Puntos de apoyo y tiempo objetivo.

---

## Diapositiva 1: Portada

**Título:**
# INTELIGENCIA ARTIFICIAL EXPLICABLE (XAI) PARA LA CLASIFICACIÓN DE MALWARE
### Diseño de un Framework Multinivel para la Optimización del Costo Computacional

**Subtítulo:** Informe de Avance de Seminario de Título — Escuela de Ingeniería Informática

* **Autores:**
  - Rigoberto Ignacio Enrique Canales Puebla
  - Francisco Ignacio Espinoza Vasquez
* **Profesora Guía:** Pamela Hermosilla Monckton
* **Profesor Correferente:** Sebastian Berrios Vasquez
* **Institución:** Pontificia Universidad Católica de Valparaíso
* **Fecha:** Septiembre 2026

<!-- Note
Tiempo objetivo: 0:00 - 1:00 (1 min)
Objetivo: Saludo protocolar, presentación del equipo, agradecimiento a los profesores Pamela Hermosilla y Sebastian Berrios, e introducción del título y alcance del proyecto.
-->

---

## Diapositiva 2: Contexto y Motivación

### El Desafío del Malware en Operaciones Críticas de Ciberseguridad

* **Crecimiento Exponencial de Amenazas:**
  * Cientos de miles de variantes diarias con técnicas de evasión, polimorfismo y ataques *zero-day*.
  * Los antivirus tradicionales basados en firmas estáticas son insuficientes.
* **El Rol del Machine Learning y Deep Learning:**
  * Permiten modelar patrones de comportamiento complejos.
  * Tasas de detección empíricas superiores al **99%**.
* **La Realidad de un SOC (Security Operations Center):**
  * Flujos continuos de eventos de red y análisis de endpoints.
  * **Exigencia operativa crítica:** Detección en tiempo real y alta tasa de procesamiento (*throughput*).

> **Premisa inicial:** Aunque los modelos detectan eficazmente el malware, su implementación en entornos de producción enfrenta barreras operativas severas.

<!-- Note
Tiempo objetivo: 1:00 - 2:15 (1 min 15 s)
Objetivo: Establecer la relevancia del problema en el mundo real. Conectar la precisión de los modelos con la dinámica de trabajo de un SOC.
-->

---

## Diapositiva 3: El Problema de la «Caja Negra»

### La Necesidad de Explicabilidad en la Respuesta a Incidentes

* **La Falacia de la Alerta Aislada:**
  * Un analista de ciberseguridad **no puede actuar** con una simple etiqueta binaria ("Malware: 99.8%").
  * Pregunta clave del analista: *¿Por qué el modelo determinó que este ejecutable es malicioso?*
* **Implicancias Operativas en el SOC:**
  1. **Contención y Aislamiento:** Validar si se justifica aislar un servidor crítico o cortar un servicio.
  2. **Extracción de IoC (Indicadores de Compromiso):** Identificar qué llamadas a la API o cabeceras PE representan la firma del ataque.
  3. **Auditoría Forense y Cumplimiento:** Justificar decisiones ante comités de seguridad y normativas técnicas.
* **El Riesgo de la Falta de Confianza:**
  * Modelos opacos generan desconfianza en el equipo operativo, elevando la fatiga de alertas y los tiempos de respuesta.

<!-- Note
Tiempo objetivo: 2:15 - 3:30 (1 min 15 s)
Objetivo: Explicar por qué la interpretabilidad no es un lujo teórico, sino un requisito funcional indispensable para operar un SOC.
-->

---

## Diapositiva 4: La Paradoja de XAI y el Cuello de Botella

### El Alto Costo Computacional de SHAP y LIME

* **Herramientas Estándar de la Industria:**
  * **SHAP (Shapley Additive exPlanations):** Fundamento en teoría de juegos cooperativos; atribución robusta global y local.
  * **LIME (Local Interpretable Model-agnostic Explanations):** Modelado local lineal mediante perturbaciones.
* **El Conflicto Técnico de Ingeniería:**
  * **KernelSHAP:** Complejidad combinatoria exponencial $\mathcal{O}(2^n)$, donde $n$ es la cantidad de características.
  * **LIME:** Exige evaluar miles de perturbaciones sintéticas por cada binario sospechoso.
  * Los ejecutables modernos poseen **cientos o miles de variables** (llamadas a la API de Windows, secciones PE, permisos).
* **El Cuello de Botella:**
  * Explicar una sola muestra toma segundos o minutos $\rightarrow$ En un SOC con miles de alertas diarias, el sistema **colapsa**.

```
Alta Precisión (ML/DL) + Explicabilidad Profunda (KernelSHAP/LIME) = Colapso de Latencia en SOC
```

<!-- Note
Tiempo objetivo: 3:30 - 4:45 (1 min 15 s)
Objetivo: Llegar al núcleo del problema técnico: la tensión matemática y computacional entre la cantidad de variables y el cálculo de valores Shapley/perturbaciones.
-->

---

## Diapositiva 5: Preguntas de Investigación y Brecha

### Brecha en la Literatura Científica y Preguntas Guía

#### La Brecha Identificada
* Los estudios previos se centran en **maximizar la precisión** ($>99\%$) o en demostrar que XAI *funciona*.
* **Casi ningún trabajo aborda la escalabilidad computacional** ni el tiempo de respuesta de XAI en pipelines continuos de detección.

#### Pregunta General de Investigación
> *¿En qué medida es posible reducir el costo computacional de XAI en la clasificación de malware mediante un enfoque multinivel que integre selección de características, destilación de conocimiento y explicabilidad adaptativa sin comprometer la precisión de detección ni la fidelidad de las explicaciones?*

#### Preguntas Específicas
1. **PI1 (Reducción Dimensional):** ¿Cómo impacta el filtrado previo de variables en los tiempos de SHAP y LIME?
2. **PI2 (Destilación y TreeSHAP):** ¿Es viable transferir conocimiento de un ensamble complejo a un modelo ligero habilitando TreeSHAP en tiempo polinomial?
3. **PI3 (Adaptabilidad y Caché):** ¿Cuánto costo promedio ahorra un esquema adaptativo por certidumbre junto a una caché vectorial?

<!-- Note
Tiempo objetivo: 4:45 - 6:00 (1 min 15 s)
Objetivo: Formular con claridad formal la brecha y cómo las 3 preguntas específicas guían exactamente los 3 niveles del framework propuesto.
-->

---

## Diapositiva 6: Objetivos del Proyecto

### Alineación Estratégica en 3 Dimensiones Metodológicas

#### Objetivo General
> Diseñar, construir y validar un **framework multinivel** para reducir el costo computacional de XAI en la clasificación de malware, viabilizando el uso de modelos transparentes en operaciones de ciberseguridad de alta exigencia temporal.

#### Objetivos Específicos por Dimensión
* **Dimensión 1: Estudio**
  * **OE1:** Realizar revisión sistemática de literatura (SLR) sobre cuellos de botella de XAI en malware.
  * **OE2:** Definir marco de referencia para medir costo computacional (latencia, RAM) y utilidad de explicaciones.
* **Dimensión 2: Desarrollo**
  * **OE3:** Diseñar la arquitectura técnica del framework multinivel.
  * **OE4:** Construir prototipo funcional integrado compatible con clasificadores y librerías XAI estándar.
* **Dimensión 3: Validación**
  * **OE5:** Evaluar experimentalmente el sistema en datasets públicos frente a baselines del estado del arte.

<!-- Note
Tiempo objetivo: 6:00 - 7:00 (1 min)
Objetivo: Presentar de forma concisa y estructurada los objetivos, mostrando cómo cada uno tiene un entregable y dimensión concreta.
-->

---

## Diapositiva 7: Marco Teórico y Revisión Sistemática (PRISMA)

### Rigurosidad Metodológica en el Estado del Arte

```
Bases Consultadas: IEEE Xplore, Scopus, ACM Digital Library, ScienceDirect, Web of Science (WoS)
```

* **Preguntas de Investigación Bibliográfica:**
  * **PI-A:** ¿Qué técnicas de XAI se aplican actualmente en malware?
  * **PI-B:** ¿Cuáles son los cuellos de botella y limitaciones operativas reportadas?
* **Protocolo de Selección en 4 Fases (PRISMA):**
  1. **Identificación:** Búsqueda booleana cruzando XAI + Malware + Costo/Latencia; deduplicación.
  2. **Cribado (Screening):** Filtrado por título/resumen (exclusión de trabajos sin XAI o fuera de malware).
  3. **Idoneidad (Eligibility):** Revisión de texto completo (exclusión por falta de métricas de reproducibilidad/costo).
  4. **Inclusión:** Síntesis cualitativa y cuantitativa de la literatura primaria.

<!-- Note
Tiempo objetivo: 7:00 - 8:15 (1 min 15 s)
Objetivo: Demostrar el rigor académico del seminario a través del estándar PRISMA.
-->

---

## Diapositiva 8: Análisis Comparativo del Estado del Arte

### Matriz de Trabajos Relacionados y Oportunidades de Mejora

| Estudio | Modelos | Técnicas XAI | Dataset | Limitación Crítica Detectada |
|:---|:---|:---|:---|:---|
| **Ullah et al.** | Stacking Ensemble | SHAP y LIME | Binarios Windows (PE) | **Alto costo computacional** para explicaciones continuas en producción. |
| **Kim et al.** | Deep Learning sobre Grafos | Mapas de activación visual | Android (FCG) | La conversión a Grafos de Llamadas a Funciones (FCG) **demanda excesivo cómputo**. |
| **Alotaibi** | Fusión Multimodal Profunda | Mecanismos de atención interna | Tabular estático + Imágenes | Arquitectura hipercompleja que **opera como modelo cerrado y pesado**. |

#### Brechas Clave Identificadas:
1. **Exceso de complejidad:** Redes profundas con sobrecarga innecesaria.
2. **Costosas transformaciones:** Convertir ejecutables a imágenes o grafos añade latencia previa.
3. **Omisión de la latencia explicativa:** Ninguno propone mecanismos de reducción de costo en tiempo de explicación.

<!-- Note
Tiempo objetivo: 8:15 - 9:30 (1 min 15 s)
Objetivo: Posicionar nuestro proyecto respecto a la vanguardia. Resaltar cómo nuestro enfoque aborda exactamente las debilidades de los papers referentes.
-->

---

## Diapositiva 9: Arquitectura del Framework Multinivel

### Visión General del Pipeline Integrado de Optimización

```
                    ┌──────────────────────────────────────────┐
                    │            MUESTRA ENTRANTE              │
                    └─────────────────────┬────────────────────┘
                                          │
                                          ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ NIVEL 1: SELECCIÓN DE CARACTERÍSTICAS                                  │
  │ • Filtro por importancia de variables (Tree-based: Random Forest/LGBM) │
  │ • Reducción del espacio factorial de O(2^n) antes de la inferencia     │
  └───────────────────────────────────────┬────────────────────────────────┘
                                          │
                                          ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ NIVEL 2: CLASIFICACIÓN Y DESTILACIÓN DE CONOCIMIENTO                   │
  │ • Modelo Profesor: Stacking Ensemble heterogéneo (Alta generalización) │
  │ • Modelo Estudiante: LightGBM optimizado                               │
  │ • Habilita TreeSHAP polinomial: O(TLD^2) vs KernelSHAP O(2^n)          │
  └───────────────────────────────────────┬────────────────────────────────┘
                                          │
                                          ▼
  ┌────────────────────────────────────────────────────────────────────────┐
  │ NIVEL 3: EXPLICABILIDAD ADAPTATIVA Y MOTOR DE CACHÉ                    │
  │ • Caché Vectorial Indexada (Distancia Coseno δ = 0.03) -> O(1)        │
  │ • Enrutamiento por Certidumbre Posterior P(ŷ | x):                     │
  │   - P ≥ 0.95: Triage Ligero (Top-5 TreeSHAP)                           │
  │   - 0.80 ≤ P < 0.95: Perfil Estándar (TreeSHAP Completo)               │
  │   - P < 0.80: Auditoría Profunda (TreeSHAP + LIME Perturbaciones)      │
  └───────────────────────────────────────┬────────────────────────────────┘
                                          │
                                          ▼
                    ┌──────────────────────────────────────────┐
                    │        ALERTA EXPLICADA PARA EL SOC      │
                    └──────────────────────────────────────────┘
```

> **Principio de Diseño:** Desacoplar la alta capacidad predictiva del clasificador del costo computacional de su explicabilidad.

<!-- Note
Tiempo objetivo: 9:30 - 11:00 (1 min 30 s)
Objetivo: Presentar la "joya de la corona" del seminario: el diagrama arquitectónico multinivel y cómo se encadenan armónicamente los 3 niveles.
-->

---

## Diapositiva 10: Nivel 1 — Selección de Características

### Reducción Dimensional Previa a la Fase de Explicación

* **El Problema Matemático:**
  * Si un binario tiene $n = 1000$ variables, el espacio de combinaciones para valores Shapley exactos es $2^{1000}$.
  * Muchas características son redundantes, ruidosas o constantes.
* **Estrategia de Dos Vías:**
  1. **Filtrado Basado en Árboles (Random Forest / LightGBM):**
     * Cálculo rápido de importancia de variables (*split* y *gain*).
     * Eliminación de variables de bajo o nulo aporte discriminativo.
  2. **Exploración Metaheurística (WOA / Algoritmos Genéticos):**
     * Algoritmo de Optimización de Ballenas (*Whale Optimization Algorithm*).
     * Función de aptitud multi-objetivo: Minimizar número de features mientras se preserva el $F_1$-Score.
* **Impacto Directo:** Reduce drásticamente la dimensión de entrada $n$, aliviando la carga computacional antes de que intervenga XAI.

<!-- Note
Tiempo objetivo: 11:00 - 12:15 (1 min 15 s)
Objetivo: Detallar el Nivel 1 y justificar matemáticamente por qué la selección previa reduce directamente el costo de los niveles subsiguientes.
-->

---

## Diapositiva 11: Nivel 2 — Stacking y Destilación de Conocimiento

### Desacoplando Complejidad Predictiva de Costo Explicativo

#### 1. El Dilema del Clasificador
* Malware moderno (polimorfo/empaquetado) requiere alta capacidad de generalización.
* **Stacking Ensemble (Profesor):** Combina múltiples algoritmos base (Random Forest, SVM, Redes Neuronales).
* **Problema:** Explicar directamente un ensamble apilado mediante XAI colapsa cualquier CPU.

#### 2. La Solución: Knowledge Distillation
* Se entrena un modelo **Estudiante ligero (LightGBM)** transfiriendo las probabilidades y representaciones aprendidas por el Ensamble Profesor.
* El estudiante replica la frontera de decisión sin arrastrar la sobrecarga de múltiples submodelos.

#### 3. El Beneficio Matemático: De Exponencial a Polinomial
$$\text{KernelSHAP: } \mathcal{O}(2^n) \quad \Longrightarrow \quad \text{TreeSHAP en LightGBM: } \mathcal{O}(T \cdot L \cdot D^2)$$
*(Donde $T$ = árboles, $L$ = número de hojas, $D$ = profundidad máxima).*

<!-- Note
Tiempo objetivo: 12:15 - 13:30 (1 min 15 s)
Objetivo: Demostrar el valor conceptual de la destilación de conocimiento y el salto cuantitativo de complejidad computacional al utilizar TreeSHAP.
-->

---

## Diapositiva 12: Nivel 3 — Explicabilidad Adaptativa y Caché

### Distribución Inteligente de Recursos según Confianza y Similitud

#### Caché de Firmas Explicativas Vectorial
* En campañas de malware activas, miles de archivos son variantes mínimas de la misma familia.
* Se indexa un vector de muestras ya explicadas.
* Si una nueva muestra tiene **distancia coseno $\delta < 0.03$**, se reutiliza la explicación: **Tiempo de cálculo $\mathcal{O}(1)$**.

#### Esquema Operativo de Umbrales de Confianza

| Régimen | Confianza $P(\hat{y} \mid x)$ | Método XAI Despachado | Rol Operativo en el SOC |
|:---:|:---:|:---:|:---|
| **Ligero** | $P \ge 0.95$ | **Top-5 TreeSHAP** | *Triage instantáneo:* Confirma alertas evidentes sin calcular miles de features. |
| **Estándar** | $0.80 \le P < 0.95$ | **TreeSHAP Completo** | *Auditoría técnica:* Vector completo para binarios sospechosos con packers. |
| **Profundo** | $P < 0.80$ | **TreeSHAP + LIME** | *Análisis forense crítico:* Revisión prioritaria de muestras limítrofes. |

> Los umbrales basales (0.95 y 0.80) se calibrarán empíricamente mediante **Diagramas de Fiabilidad (Reliability Diagrams)**.

<!-- Note
Tiempo objetivo: 13:30 - 15:00 (1 min 30 s)
Objetivo: Explicar cómo el sistema emula la toma de decisiones humana en un SOC (lo evidente se despacha rápido; lo dudoso se audita a fondo). Explicar la caché vectorial.
-->

---

## Diapositiva 13: Diseño Experimental: Datasets, Métricas y Baselines

### Marco de Validación Empírica

#### Datasets Públicos Seleccionados
1. **[[CICMalDroid]] 2020 (Android):** $>17.000$ muestras (Adware, Banking, Ransomware, Riskware, Benigno). Análisis estático + dinámico.
2. **[[ClaMP Dataset]] (Windows):** Archivos ejecutables PE, 68 atributos de cabeceras, tablas y secciones.
* *Partición estratificada:* 70% entrenamiento, 15% validación, 15% prueba.

#### Métricas de Evaluación
* **Rendimiento:** Accuracy, Precision, Recall, Macro $F_1$-Score, AUC-ROC.
* **Eficiencia Computacional:** Latencia de Inferencia ($t_{\text{inf}}$), Latencia de Explicación ($t_{\text{exp}}$), Memoria RAM pico (MB), Throughput, y Factor de Aceleración ($S = \frac{t_{\text{baseline}}}{t_{\text{framework}}}$).
* **Calidad XAI:** Fidelidad (*Faithfulness*) y Estabilidad (*Stability*).

#### Escenarios de Comparación (Baselines)
* **Baseline 1:** Modelo tradicional sin selección (KernelSHAP / LIME estándar sobre todas las variables).
* **Baseline 2:** Estado del arte (MAL-XSEL con Stacking Ensemble y TreeSHAP directo).
* **Propuesta:** Framework Multinivel Completo (Selección + Destilación + Adaptativo + Caché).

<!-- Note
Tiempo objetivo: 15:00 - 16:15 (1 min 15 s)
Objetivo: Presentar la solidez del diseño experimental: datos reales y heterogéneos, métricas tripartitas y baselines exigentes.
-->

---

## Diapositiva 14: Plan de Trabajo y Estado de Avance

### Cronograma y Entregables del Proyecto

```
Semestre I: Seminario de Título (2026-2) ────► Semestre II: Trabajo Final de Título (2027-1)
```

#### Estado de Avance al Día de Hoy (Semestre I):
* ✅ **T1 (Planteamiento del problema y contexto SOC):** Completada.
* ✅ **T2 (Revisión sistemática de literatura PRISMA [OE1]):** Completada.
* ✅ **T3 (Formulación de objetivos y alcance [OE2, OE3]):** Completada.
* 🔄 **T4 (Diseño metodológico, métricas y baselines):** En curso / finalizando.

#### Próximos Hitos Inmediatos (Cierre Seminario I):
* ⏳ **T5 (Octubre 2026):** Limpieza, preprocesamiento y EDA de CICMalDroid y ClaMP.
* ⏳ **T6 (Noviembre 2026):** Implementación empírica y benchmark de Baselines 1 y 2.
* 🎯 **H1 (Diciembre 2026):** Entrega formal del Informe de Seminario de Título.

#### Semestre II (2027-1):
* Desarrollo del framework (T7-T10), Validación experimental intensiva (T11-T13), Redacción y Defensa (T14-T15, H2).

<!-- Note
Tiempo objetivo: 16:15 - 17:30 (1 min 15 s)
Objetivo: Mostrar control absoluto de los tiempos y cumplimiento de hitos. Dar tranquilidad a la comisión de que se va exactamente según lo planificado.
-->

---

## Diapositiva 15: Conclusiones y Ronda de Preguntas

### Síntesis del Aporte y Proyección

#### Síntesis del Avance
* Se ha formalizado un marco teórico riguroso que evidencia la **ausencia de soluciones escalables** para XAI en ciberseguridad.
* Se diseñó una **arquitectura multinivel innovadora** que ataca el costo computacional en tres frentes: dimensionalidad previa, complejidad del modelo y adaptabilidad del cálculo.
* Las bases metodológicas, datasets, baselines y métricas están plenamente estructuradas para el inicio de la fase de laboratorio.

#### Impacto Esperado
* Transformar la explicabilidad en ciberseguridad de un concepto teórico costoso a una **herramienta operativa viable en tiempo real** para Centros de Operaciones de Seguridad.

---

### ¡Muchas gracias por su atención!
**Q&A — Abrimos la ronda de preguntas y comentarios de la comisión**

* Profesora Guía: Pamela Hermosilla Monckton
* Profesor Correferente: Sebastian Berrios Vasquez
* Estudiantes: Rigoberto Canales Puebla & Francisco Espinoza Vasquez

<!-- Note
Tiempo objetivo: 17:30 - 18:30 (1 min)
Objetivo: Cierre firme, reiterar el impacto del trabajo y abrir la ronda de preguntas mostrando seguridad y dominio del tema.
-->
