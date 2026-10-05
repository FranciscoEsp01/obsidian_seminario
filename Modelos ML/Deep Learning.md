---
tags: [modelo, dl, caja-negra]
---

# Deep Learning

- **Descripción:** Subcampo del [[Machine Learning]] basado en redes neuronales profundas con múltiples capas de representación.
- **Arquitecturas comunes en malware:**
  - CNNs ([[Redes Neuronales Convolucionales]])
  - RNNs y LSTMs (para análisis de secuencias como API calls)
  - Transformers (que hacen uso de [[Mecanismos de Atención]])
- **Desempeño:** Tienen una altísima capacidad para detectar patrones complejos ocultos en la [[Clasificación de Malware]].
- **Problema principal:** Son arquitecturas de "caja negra", lo cual genera desconfianza en analistas de seguridad, como se discute en el survey extenso de la ACM ([[ACM Computing Survey (3677374)]]).
- **Solución:** Necesitan imperativamente de técnicas de [[Inteligencia Artificial Explicable (XAI)]] (como [[SHAP]], [[LIME]], o [[Grad-CAM]]) para justificar sus predicciones.
