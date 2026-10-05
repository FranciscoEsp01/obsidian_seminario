---
tags: [concepto, xai, trade-offs, rendimiento]
---

# Trade-offs en XAI

Al implementar técnicas de [[Inteligencia Artificial Explicable (XAI)]] en sistemas de [[Clasificación de Malware]], surgen varios compromisos importantes:

- **Accuracy vs Interpretability:** Existe una tendencia donde los modelos más explicables por diseño (como la [[Regresión Logística]]) suelen ser menos precisos para tareas complejas en comparación con modelos "caja negra" de [[Deep Learning]].
- **Latencia:** La aplicación de técnicas post-hoc como [[SHAP]] o [[LIME]] añade un overhead computacional, lo cual es crítico en sistemas de detección en tiempo real.
- **Granularidad:** Existe una tensión entre ofrecer explicaciones locales (por instancia individual) versus globales (comportamiento general del modelo).
- **Confianza del analista vs complejidad del modelo:** Generar explicaciones demasiado complejas puede reducir la confianza del analista en lugar de aumentarla.
- **Cumplimiento regulatorio:** Marcos como GDPR y AI Act exigen transparencia, lo que fuerza a aceptar ciertos trade-offs en rendimiento en favor de la explicabilidad, impactando directamente las arquitecturas basadas en [[Machine Learning]].

## Fuentes MDPI revisadas (octubre de 2026)

- [[XAI Ciberseguridad Diseño Humano y Edge - Cecchi et al]]
- [[Explicabilidad en CNN - Revisión Sistemática - Tayari y Zaied]]
- [[C-GUARD - Enrutamiento Adaptativo frente a Malware Evasivo]]
- [[RFS-MD - Reglas Explicables y Robustez Android]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
