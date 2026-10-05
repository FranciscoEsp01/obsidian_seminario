---
tags: [concepto, optimización, costo-computacional, xai]
related: "[[SHAP]], [[LIME]], [[Trade-offs en XAI]], [[Inteligencia Artificial Explicable (XAI)]]"
---

# Costo Computacional de XAI

## El problema central

Las técnicas de [[Inteligencia Artificial Explicable (XAI)]] como [[SHAP]] y [[LIME]] añaden un **overhead computacional significativo** a los pipelines de clasificación de malware, dificultando su uso en entornos de producción y detección en tiempo real.

## Complejidad por técnica y su Impacto Operacional

| Enfoque / Técnica | Complejidad | Impacto Operacional en Ciberseguridad |
| :--- | :--- | :--- |
| **Modelos Lineales (Regresión)** | O(n) | Interpretabilidad nativa e inmediata, pero insuficiente precisión para clasificar malware moderno. |
| **LIME (Post-hoc)** | O(Nm * P) | Sobrecarga temporal alta; requiere generar "P" perturbaciones (usualmente >5000) por cada muestra "Nm" analizada. |
| **KernelSHAP (Post-hoc)** | O(2^n) | Costo intratable para datasets de malware con alta dimensionalidad; imposible de usar en detección en tiempo real. |
| **TreeSHAP (Post-hoc)** | O(T * L * D^2) | Mejora significativa sobre KernelSHAP, pero aún exige un overhead polinomial prohibitivo para procesamiento masivo de alertas. |
| **[[Grad-CAM]]** | O(forward + backward pass) | Relativamente eficiente, pero limitado a arquitecturas de Redes Neuronales Convolucionales (CNNs). |
| **[[Mecanismos de Atención]]** | O(n²) para self-attention | Inherente al modelo; no requiere procesamiento explicativo secundario pero eleva el costo base de inferencia. |

## Factores que agravan el costo

1. **Alta dimensionalidad**: Datasets de malware pueden tener cientos o miles de features
2. **Volumen**: >450.000 nuevas muestras diarias (AV-TEST Institute)
3. **Requisito de tiempo real**: SOCs necesitan clasificación en milisegundos
4. **Múltiples plataformas**: Android, Windows, Linux, IoT — cada una con features distintas

## Estrategias de mitigación

→ Ver la propuesta completa en [[Propuesta - Optimización del Costo Computacional de XAI en Clasificación de Malware]]

1. **Reducción de dimensionalidad** pre-explicación
2. **TreeSHAP/FastSHAP** en vez de KernelSHAP
3. **Knowledge Distillation** a modelos ligeros
4. **Explicación adaptativa** según nivel de confianza
5. **Modelos inherentemente interpretables** ([[Ensemble Learning]] de árboles)

## Relación con otros conceptos

- [[Trade-offs en XAI]] — El costo computacional es uno de los trade-offs principales
- [[SHAP]] — Técnica más costosa pero más fidedigna
- [[LIME]] — Más rápido que SHAP pero menos estable
- [[Machine Learning]] — Los modelos basados en árboles son más eficientes de explicar
- [[Deep Learning]] — Los modelos de DL son los más costosos de explicar


## Fuentes MDPI revisadas (octubre de 2026)

- [[Ingeniería de Características Explicable sobre FCG - Kim et al]]
- [[Comparación ML y DL sobre Llamadas API - Cannarile et al]]
- [[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al]]
- [[CyberSentinel - Red Visual de Dos Ramas y Atención]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
