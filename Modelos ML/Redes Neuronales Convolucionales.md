---
tags: [modelo, dl, cnn, imagenes]
---

# Redes Neuronales Convolucionales

- **Descripción:** Las CNNs son un tipo de arquitectura de [[Deep Learning]] diseñadas primariamente para el procesamiento de imágenes.
- **Uso en Malware:** El enfoque más común convierte los binarios de malware en imágenes de escala de grises (grayscale images). Luego, la CNN clasifica la imagen.
- **Ventajas:** Excelente capacidad para extraer patrones complejos y espaciales; alta accuracy en [[Clasificación de Malware]].
- **Desventajas:** Modelos altamente opacos ("cajas negras"). Presentan baja interpretabilidad inherente.
- **Aplicación de XAI:** La técnica de [[Inteligencia Artificial Explicable (XAI)]] más natural para las CNNs es el uso de [[Grad-CAM]], aunque también se puede aplicar [[SHAP]] y [[LIME]].
