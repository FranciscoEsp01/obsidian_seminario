---
tags: [seminario, metodologia, xai, malware, investigacion, informe]
status: en-desarrollo
fecha: 2026-08-27
related: "[[Informe de Avance - Seminario de Título]], [[Seminario de Título - MOC]], [[Objetivos del Seminario]], [[Propuesta - Optimización del Costo Computacional de XAI en Clasificación de Malware]], [[Estado del Arte]]"
tipo: metodologia
---

# 5. METODOLOGÍA

Para cumplir con los objetivos planteados y abordar el cuello de botella computacional que presenta la [[Inteligencia Artificial Explicable (XAI)]] en este ámbito, se definió una metodología de carácter cuantitativo y experimental. El trabajo se estructura en una serie de etapas secuenciales que van desde la selección y tratamiento de los datos hasta el diseño y evaluación del *framework* de optimización.

```
+-----------------------------------------------------------------------------------+
|                            FLUJO METODOLÓGICO                                     |
+-------------------+--------------------+--------------------+---------------------+
|      ETAPA 1      |      ETAPA 2       |      ETAPA 3       |       ETAPA 4       |
|  Preprocesamiento |  Selección y       |  Entrenamiento y   |  Explicabilidad     |
|  y Datasets       |  Reducción (Dim.)  |  Destilación (ML)  |  Adaptativa + Valid.|
+-------------------+--------------------+--------------------+---------------------+
```

---

### 5.1. Enfoque y Diseño Experimental

La investigación sigue un diseño experimental comparativo. La meta no es únicamente medir la capacidad de detección del malware (evaluada mediante métricas tradicionales de clasificación), sino contrastar de forma empírica el [[Costo Computacional de XAI]] (tiempo de ejecución y memoria) y la fidelidad de las explicaciones generadas entre un enfoque XAI tradicional y el *framework* optimizado propuesto.

---

### 5.2. Fuentes de Datos y Preprocesamiento

Para validar el comportamiento del sistema frente a distintos tipos de amenazas y estructuras de datos, se seleccionaron dos conjuntos de datos públicos ampliamente utilizados en la literatura:

1. **[[CICMalDroid]] 2020:** Dataset enfocado en el ecosistema Android con más de 17.000 muestras que abarcan cinco categorías principales (Adware, Banking, Ransomware, Riskware y Benigno). Proporciona características derivadas de [[Análisis Estático]] y [[Análisis Dinámico]] (permisos, llamadas al sistema y comportamientos en ejecución).
2. **[[ClaMP Dataset]]:** Dataset orientado al entorno Windows que analiza archivos ejecutables en formato PE (*Portable Executable*), estructurado en 68 características obtenidas de las cabeceras, tablas de importación y secciones del binario.

#### Procedimiento de preparación de datos:
* **Limpieza y normalización:** Eliminación de registros duplicados, tratamiento de valores nulos e imputación cuando corresponda, junto con el escalamiento de variables numéricas para evitar sesgos en el entrenamiento.
* **Codificación:** Conversión de atributos categóricos mediante técnicas estándar (*One-Hot Encoding* o *Target Encoding* según la cardinalidad de la variable).
* **Partición de datos:** División estratificada de los datos en subconjuntos de entrenamiento (70%), validación (15%) y prueba (15%), preservando la proporción original de cada familia de malware.

---

### 5.3. Fases de Desarrollo del Framework

El desarrollo técnico del sistema se organiza en tres niveles modulares que interactúan de forma directa para reducir el costo de cómputo:

```
                  ┌─────────────────────────────────────────┐
                  │            Muestra de Entrada           │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  Nivel 1: Selección de Características  │
                  │  - Filtro por importancia (Tree-based)  │
                  │  - Reducción previa a la explicación    │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  Nivel 2: Clasificación y Destilación   │
                  │  - Modelo profesor (Ensemble / Complejo)│
                  │  - Modelo estudiante (LightGBM ligero)  │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │  Nivel 3: Explicación Adaptativa        │
                  │  - Alta confianza  -> Top-K (Rápido)    │
                  │  - Baja confianza  -> SHAP/LIME Profundo│
                  │  - Sistema de caché para variantes      │
                  └────────────────────┬────────────────────┘
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │     Alerta Explicada para el SOC        │
                  └─────────────────────────────────────────┘
```

#### Nivel 1: Reducción de Dimensionalidad Previa a la Explicación
Dado que métodos como KernelSHAP presentan una complejidad exponencial respecto a la cantidad de características ($n$), este nivel busca reducir el espacio de búsqueda antes de pasar al módulo de explicabilidad:
* Se aplica una selección basada en la importancia de variables de modelos de árboles de decisión ([[Random Forest]], [[LightGBM]]) para descartar atributos redundantes o con nulo aporte discriminativo.
* Se evalúa la integración de algoritmos de optimización metaheurísticos (como *Whale Optimization Algorithm* - WOA o algoritmos genéticos) con una función de evaluación que equilibre la minimización de variables con la retención del puntaje F1.

#### Nivel 2: Clasificación con Destilación de Conocimiento
Para evitar que la complejidad del modelo clasificador incremente el tiempo de inferencia y explicación:
* Se entrena inicialmente un modelo ensamblado de alto rendimiento ([[Ensemble Learning]] / modelo profesor).
* Mediante destilación de conocimiento, se transfiere su aprendizaje hacia un modelo más ligero (modelo estudiante, como [[LightGBM]]).
* Esto permite aprovechar implementaciones analíticas de alta velocidad como **TreeSHAP**, que reducen el cálculo de valores de Shapley a tiempo polinomial en lugar de requerir aproximaciones pesadas como KernelSHAP.

#### Nivel 3: Explicabilidad Adaptativa y Caché de Respuestas
No todas las alertas de un SOC demandan la misma profundidad explicativa. Este componente segmenta el cómputo según el nivel de certidumbre del clasificador:
* **Muestras con alta confianza ($P(\hat{y}) \ge 0.95$):** Se genera un resumen local ligero restringido a las $K$ características más determinantes.
* **Muestras en zona de incertidumbre ($P(\hat{y}) < 0.80$):** Se activa un análisis cruzado en profundidad ([[SHAP]] + [[LIME]]) y se emite una alerta prioritaria para análisis manual.
* **Mecanismo de Caché:** Para variantes de familias conocidas con alta similitud de atributos, se almacena y reutiliza la explicación base en lugar de recalcularla, ahorrando cómputo recurrente.

---

### 5.4. Métricas de Evaluación

Para validar integralmente la propuesta, se definieron tres categorías de métricas:

#### 1. Rendimiento del Clasificador
Permiten verificar que las optimizaciones no degraden la eficacia en la detección:
* **Accuracy, Precision, Recall y Macro F1-Score.**
* **Área bajo la curva ROC (AUC-ROC):** Para medir la robustez de separación entre clases en escenarios desbalanceados.

#### 2. Costo y Eficiencia Computacional
Constituyen las métricas centrales de la investigación:
* **Latencia de Inferencia ($t_{inf}$):** Tiempo promedio en milisegundos para predecir la clase de una muestra.
* **Latencia de Explicación ($t_{exp}$):** Tiempo promedio en milisegundos para calcular y formatear la justificación de la alerta.
* **Consumo de Memoria:** Memoria RAM pico (en MB) utilizada durante la fase de cálculo de XAI.
* **Tasa de Procesamiento (*Throughput*):** Cantidad de muestras procesadas y explicadas por segundo.
* **Factor de Aceleración (*Speedup*):** Razón entre el tiempo requerido por el enfoque base y el framework propuesto ($S = \frac{t_{\text{baseline}}}{t_{\text{framework}}}$).

#### 3. Calidad de las Explicaciones
* **Fidelidad (*Faithfulness*):** Verificación de que las variables señaladas como críticas por el método XAI realmente alteren la predicción del modelo al ser perturbadas u omitidas.
* **Estabilidad (*Stability*):** Comprobación de que muestras sintácticamente similares reciban explicaciones coherentes y consistentes entre sí.

---

### 5.5. Baselines y Escenarios de Comparación

Para medir objetivamente las mejoras, los experimentos se contrastan contra dos líneas base representativas del estado del arte:

| Configuración | Clasificador | Método XAI | Selección de Features |
| :--- | :--- | :--- | :--- |
| **Baseline 1 (Tradicional)** | [[LightGBM]] / [[Random Forest]] | KernelSHAP / [[LIME]] estándar | Sin selección (todas las variables) |
| **Baseline 2 (Estado del Arte / [[MAL-XSEL Framework\|MAL-XSEL]])** | [[Ensemble Learning\|Stacking Ensemble]] | TreeSHAP / [[LIME]] directo | Selección estática convencional |
| **Propuesta (Framework Multinivel)** | Modelo Destilado Ligero | XAI Adaptativo + TreeSHAP / Caché | Selección Metaheurística / Importancia |

---

### 5.6. Entorno de Ejecución y Herramientas

Las pruebas se desarrollan en lenguaje Python, utilizando las bibliotecas `scikit-learn`, `lightgbm`, `shap`, `lime`, `optuna` (para ajuste de hiperparámetros) y `memory_profiler` (para auditoría de consumo de RAM). Los experimentos se ejecutan en un entorno de cómputo local controlado, registrando promedios sobre 10 repeticiones independientes por prueba para evitar distorsiones por fluctuaciones del sistema operativo.
