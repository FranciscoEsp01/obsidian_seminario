---
tags: [tecnica, xai, grad-cam, visualizacion, cnn]
---

# Grad-CAM

- **Significado:** Gradient-weighted Class Activation Mapping.
- **Función:** Visualiza las regiones más importantes de una entrada que llevan a un modelo a tomar una decisión, usando los gradientes de la clase objetivo que fluyen hacia la última capa convolucional.
- **Aplicación:** Específico para arquitecturas basadas en [[Redes Neuronales Convolucionales]] (CNNs).
- **Uso en Malware:** Muy útil cuando el binario del malware se convierte y representa como imágenes (grayscale images). Permite a los analistas ver qué "partes" del binario son indicativas de código malicioso.
- Es una técnica fundamental de [[Inteligencia Artificial Explicable (XAI)]] en escenarios de clasificación visual o de secuencias transformadas.
- En comparación con [[SHAP]] y [[LIME]], es inherentemente específico para redes convolucionales.
