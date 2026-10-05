---
tags: [tecnica, xai, shap, feature-importance]
---

# SHAP

- **Significado:** SHapley Additive exPlanations.
- **Origen:** Basado en los valores de Shapley derivados de la teoría de juegos cooperativos.
- **Función:** Mide la contribución marginal de cada característica (feature) a la predicción final de un modelo de [[Machine Learning]].
- **Tipos de implementaciones:** TreeSHAP (optimizado para [[Random Forest]], [[LightGBM]] y otros algoritmos de árboles), KernelSHAP (agnóstico al modelo), DeepSHAP (para [[Deep Learning]]).
- **Ventajas:** Ofrece consistencia teórica y permite generar explicaciones tanto locales como globales de manera unificada.
- **Aplicación en Malware:** Muy utilizado en la [[Clasificación de Malware]] para identificar qué API calls o features estáticas fueron determinantes.
- **Usado en los siguientes estudios:**
  - [[XAI for Malware Analysis Survey]]
  - [[Investigación Comprehensiva Detección de Malware con XAI]]
  - [[MAL-XSEL Framework]]
  - [[XAI en Detección de Malware - Thompson et al]]
- A menudo se compara y utiliza junto a [[LIME]] y [[Grad-CAM]] dentro del marco de la [[Inteligencia Artificial Explicable (XAI)]].

## Fuentes MDPI revisadas (octubre de 2026)

- [[Ingeniería de Características Explicable sobre FCG - Kim et al]]
- [[Malware Android con BERT y Representación Visual - Ullah et al]]
- [[Malware Android con Word2vec y Tráfico de Red - Ullah et al]]
- [[Comparación ML y DL sobre Llamadas API - Cannarile et al]]
- [[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al]]
- [[C-GUARD - Enrutamiento Adaptativo frente a Malware Evasivo]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
