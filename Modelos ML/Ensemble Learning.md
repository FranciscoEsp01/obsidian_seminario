---
tags: [modelo, ml, ensemble, stacking]
---

# Ensemble Learning

- **Descripción:** Estrategia de [[Machine Learning]] que combina las predicciones de múltiples modelos base para mejorar la robustez y generalización general.
- **Tipos principales:**
  - *Bagging:* (ej. [[Random Forest]])
  - *Boosting:* (ej. [[LightGBM]])
  - *Stacking:* Entrena un meta-modelo usando las salidas de múltiples modelos base.
- **Uso en Malware:** El framework propuesto en [[MAL-XSEL Framework]] utiliza stacking ensemble learning para lograr sobre el 99.6% de accuracy en el [[ClaMP Dataset]].
- **Relación con explicabilidad:** Mayor accuracy generalmente conlleva una menor interpretabilidad inherente. Por tanto, el uso de técnicas de [[Inteligencia Artificial Explicable (XAI)]] como [[SHAP]] o [[LIME]] es crítico para justificar sus decisiones (ver [[Trade-offs en XAI]]).
