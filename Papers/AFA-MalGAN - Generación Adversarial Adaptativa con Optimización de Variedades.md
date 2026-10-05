---
tags: [paper, gan, adversarial, bodmas, lightgbm, saliency_mask]
---

# AFA-MalGAN: Generación de Muestras Adversariales con Optimización de Variedades

**Referencia Bibliográfica:**
Journal of King Saud University - Computer and Information Sciences (2024). AFA-MalGAN: adaptive adversarial sample generation for high-dimensional malware features via constrained manifold optimization. DOI: [10.1016/j.jksuci.2024.102194](https://doi.org/10.1016/j.jksuci.2024.102194)
- **Enlace Oficial:** https://www.sciencedirect.com/science/article/pii/S1319157824002532?via%3Dihub

---

## 1. Resumen Ejecutivo
- **Ataques Adversariales Físicamente Válidos:** Uno de los grandes problemas en ciberseguridad es que las perturbaciones adversariales matemáticas frecuentemente rompen la estructura de los ejecutables PE, volviéndolos inejecutables. AFA-MalGAN resuelve esto mediante optimización en variedades restringidas (*constrained manifold optimization*).
- **Máscara de Saliencia Inteligente (ISM):** Implementa un módulo (*Intelligent Feature Saliency Mask*) que calcula gradientes suavizados con momento para descubrir qué características son más determinantes para el clasificador víctima.
- **Evasión de Detectores Industriales:** Logra una tasa de evasión del **95.6% frente a detectores de nivel de producción basados en [[LightGBM]]** sobre las 57.293 muestras del [[BODMAS Dataset]], manteniendo un puntaje de consistencia de características del 0.985.

---

## 2. Metodología y Enfoque Técnico
- Red Generativa Antagónica (GAN) con función de pérdida multi-objetivo sujeta a restricciones de preservación del formato ejecutable PE.
- Ponderación dinámica de presupuesto de perturbación (*Dynamic Annealing Budget*).
- Uso de retroalimentación de gradientes para focalizar la manipulación en las features más sensibles.

---

## 3. Datasets y Benchmarks
- [[BODMAS Dataset]] (57.293 muestras de malware y 77.142 benignas).

---

## 4. Conexión con el Seminario de Título
- **Doble Conexión Crucial:**
  1. Utiliza **[[LightGBM]]** como detector víctima de referencia, demostrando que es el estándar de la industria en detección tabular/estática (el mismo modelo que integra nuestro Nivel 3).
  2. La máscara de saliencia basada en gradientes es matemáticamente análoga a las técnicas de atribución de **[[Inteligencia Artificial Explicable (XAI)]]**, evidenciando cómo la explicabilidad permite tanto auditar la robustez del modelo como entender sus puntos ciegos ante ataques adversariales.

---

## 5. Conceptos y Notas Relacionadas
- [[LightGBM]]
- [[BODMAS Dataset]]
- [[Trade-offs en XAI]]
- [[Inteligencia Artificial Explicable (XAI)]]
- [[Clasificación de Malware]]
- [[Costo Computacional de XAI]]
- [[SHAP]]
