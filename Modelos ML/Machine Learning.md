---
tags: [modelo, ml, clasificacion]
---

# Machine Learning

- **Definición:** Aplicación de algoritmos de inteligencia artificial que permiten a los sistemas aprender y mejorar a partir de la experiencia.
- **Uso en Ciberseguridad:** Representa el estado del arte moderno para la [[Clasificación de Malware]]. Supera a los métodos tradicionales (basados en firmas) al poder detectar malware tipo zero-day.
- **Tipos de tareas:**
  - *Clasificación binaria:* Determinar si un archivo es benigno o malicioso.
  - *Clasificación multiclase:* Asignar el malware a familias específicas.
- **Extracción de features:** Depende de si se usa [[Análisis Estático]] (ej. [[ClaMP Dataset]]), [[Análisis Dinámico]] o un [[Análisis Híbrido]] (ej. [[CICMalDroid]]).
- **Modelos típicos:** Incluyen [[Regresión Logística]], [[Random Forest]], [[LightGBM]] y técnicas combinadas de [[Ensemble Learning]]. El subset más avanzado se denomina [[Deep Learning]].
- **Desafíos:** Concept drift (evolución de las amenazas), ejemplos adversarios, y la necesidad fundamental de la [[Inteligencia Artificial Explicable (XAI)]] para validar el comportamiento.
