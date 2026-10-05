---
tags: [modelo, ml, ensemble, arboles]
---

# Random Forest

- **Descripción:** Algoritmo de [[Machine Learning]] basado en un ensemble (bosque) de árboles de decisión.
- **Nivel de explicabilidad:** Relativamente interpretable; proporciona de manera nativa la importancia de cada característica (feature importance).
- **Uso en el dominio:** Frecuentemente usado como baseline en estudios de [[Clasificación de Malware]].
- **Resultados típicos:** En papers analizados (ej. [[MAL-XSEL Framework]]), alcanza métricas muy altas, rondando un ~99.33% de accuracy.
- **XAI:** Es compatible de forma muy eficiente con TreeSHAP, una variante específica de [[SHAP]] para métodos de ensemble basados en árboles, facilitando la aplicación de [[Inteligencia Artificial Explicable (XAI)]].
