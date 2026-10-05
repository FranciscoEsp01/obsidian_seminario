---
tags: [tecnica, xai, lime, modelo-agnostico]
---

# LIME

- **Significado:** Local Interpretable Model-agnostic Explanations.
- **Funcionamiento:** Genera perturbaciones en torno a una instancia específica para crear un conjunto de datos local. Luego, entrena un modelo inherentemente interpretable (como un modelo lineal o árbol de decisión) sobre este vecindario.
- **Ventaja principal:** Model-agnostic, es decir, funciona con cualquier clasificador, ya sea [[Random Forest]], [[Redes Neuronales Convolucionales]] o [[Ensemble Learning]].
- **Limitación:** Puede sufrir de inestabilidad en las explicaciones, donde instancias muy similares reciben explicaciones diferentes.
- **Uso en investigación de Malware:**
  - [[XAI for Malware Analysis Survey]]
  - [[Investigación Comprehensiva Detección de Malware con XAI]]
  - [[MAL-XSEL Framework]]
  - [[XAI en Detección de Malware - Thompson et al]]
- Junto con [[SHAP]], es una de las técnicas de [[Inteligencia Artificial Explicable (XAI)]] más predominantes en el estado del arte.

## Fuentes MDPI revisadas (octubre de 2026)

- [[Malware Android con BERT y Representación Visual - Ullah et al]]
- [[Malware Android con Word2vec y Tráfico de Red - Ullah et al]]
- [[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
