---
tags: [paper, transformer, real_time, computational_efficiency, wevj]
---

# An Algorithmic Study of Transformer-Based Road Scene Segmentation in Autonomous Driving

**Referencia Bibliográfica:**
World Electric Vehicle Journal, MDPI (2024). An Algorithmic Study of Transformer-Based Road Scene Segmentation in Autonomous Driving. *World Electric Vehicle Journal*, 15(11), 516. DOI: [10.3390/wevj15110516](https://doi.org/10.3390/wevj15110516)
- **Enlace Oficial:** https://www.mdpi.com/2032-6653/15/11/516

---

## 1. Resumen Ejecutivo
- **Optimización de Latencia en Tiempo Real:** Estudia el comportamiento algorítmico de modelos basados en visión por Transformers bajo restricciones estrictas de hardware y latencia de inferencia en tiempo real.
- **Técnicas de Poda y Reducción:** Analiza cómo la poda de cabezas de atención, la cuantización de pesos y la reducción de resolución afectan el compromiso entre exactitud de segmentación y tiempo de procesamiento por cuadro.
- **Métricas de Eficiencia:** Formaliza el análisis de presupuesto computacional (tiempo de GPU/NPU vs. métricas de calidad de salida).

---

## 2. Metodología y Enfoque Técnico
- Perfilado sistemático de latencia por capa en arquitecturas Vision Transformer (ViT).
- Estrategias de compresión de modelos y destilación de conocimiento para aceleración en inferencia.
- Medición de consumo energético y estabilidad en hardware embebido.

---

## 3. Datasets y Benchmarks
- Datasets de benchmark de visión en tiempo real y conducción autónoma.

---

## 4. Conexión con el Seminario de Título
- Aporta un marco metodológico muy valioso para nuestro estudio de **[[Costo Computacional de XAI]]**: el enfoque de perfilar sistemáticamente la latencia por capa y medir los **[[Trade-offs en XAI]]** entre coste computacional y precisión analítica es exactamente la metodología experimental que adoptamos en el seminario.

---

## 5. Conceptos y Notas Relacionadas
- [[Deep Learning]]
- [[Mecanismos de Atención]]
- [[Costo Computacional de XAI]]
- [[Trade-offs en XAI]]
- [[Destilación de Conocimiento]]
