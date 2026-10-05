---
tags: [seminario, objetivos, investigación, propuesta]
status: finalizado
related: "[[Informe de Avance - Seminario de Título]], [[Propuesta - Optimización del Costo Computacional de XAI en Clasificación de Malware]], [[Seminario de Título - MOC]]"
---

# Objetivos del Seminario

## Objetivo General

Diseñar, construir y validar un *framework* multinivel para reducir el costo computacional de la [[Inteligencia Artificial Explicable (XAI)]] en la [[Clasificación de Malware]], con el fin de viabilizar el uso de modelos transparentes en operaciones de ciberseguridad que exigen respuestas rápidas.

## Objetivos Específicos

Los objetivos de esta investigación se dividen en tres etapas metodológicas (**Estudio**, **Desarrollo** y **Validación**), las cuales cubren desde la revisión del conocimiento actual hasta las pruebas experimentales del sistema.

### Dimensión: Estudio

| ID | Objetivo Específico |
|---|---|
| **OE1** | Realizar una revisión sistemática de la literatura sobre el uso de la Inteligencia Artificial Explicable (XAI) en la detección de malware, para identificar los cuellos de botella computacionales y problemas de escalabilidad actuales. |
| **OE2** | Definir un marco de referencia que establezca cómo se medirá el [[Costo Computacional de XAI]] (latencia, consumo de memoria, volumen de procesamiento) y la utilidad de las explicaciones (fidelidad y estabilidad) en escenarios de monitoreo continuo. |

### Dimensión: Desarrollo

| ID | Objetivo Específico |
|---|---|
| **OE3** | Diseñar la arquitectura del *framework*, definiendo cómo interactúan sus tres componentes principales: la reducción de dimensionalidad, la destilación de conocimiento hacia modelos más ligeros y la estrategia de explicación adaptativa. |
| **OE4** | Construir un prototipo funcional que integre estos tres niveles, asegurando que sea compatible con clasificadores de malware y con librerías estándar de explicabilidad (como [[SHAP]] y [[LIME]]). |

### Dimensión: Validación

| ID | Objetivo Específico |
|---|---|
| **OE5** | Evaluar el sistema mediante experimentos sobre conjuntos de datos públicos (como [[CICMalDroid]] o [[ClaMP Dataset]]), para comprobar cuánta carga computacional se logra reducir en comparación a los enfoques de XAI tradicionales, sin sacrificar la precisión de la detección. |
