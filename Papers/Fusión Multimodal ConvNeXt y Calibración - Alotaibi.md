---
title: "Multimodal Deep Learning Fusion for Accurate and Explainable Malware Family Classification"
tags: ["paper", "mdpi", "revisado", "multimodal", "convnext", "calibracion", "malware"]
status: "revisado-en-texto-completo"
autores: ["Bandar Alotaibi"]
anio: 2025
fecha_publicacion: "2025-10-31"
fecha_revision: "2026-10-04"
doi: "10.3390/app152111635"
url: "https://www.mdpi.com/2076-3417/15/21/11635"
pdf: "Papers/PDF/Alotaibi-2025-app152111635.pdf"
paginas: 14
citekey: "Alotaibi2025Multimodal"
prioridad: "Media: fusión visual y calibración"
---

# Multimodal Deep Learning Fusion for Accurate and Explainable Malware Family Classification

## Referencia y acceso

Alotaibi, B. (2025). Multimodal Deep Learning Fusion for Accurate and Explainable Malware Family Classification. *Applied Sciences*, 15(21), 11635. https://doi.org/10.3390/app152111635

- [Página editorial](https://www.mdpi.com/2076-3417/15/21/11635) · [DOI](https://doi.org/10.3390/app152111635).
- [[Papers/PDF/Alotaibi-2025-app152111635.pdf|PDF local completo (14 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

Clasifica familias de malware fusionando imágenes en escala de grises y vectores estáticos mediante ConvNeXt-Tiny y atención cruzada. En Malimg combina snapshots, ocho vistas de aumento en prueba y ajustes de sesgo por clase aprendidos en validación. En Fusion Malware utiliza un checkpoint; el vector híbrido incluye estadísticas de intensidad, LBP y un embedding visual.

## Resultados reportados

| Dataset | Accuracy | Macro F1 |
|---|---:|---:|
| Malimg | 99,69 % | 99,22 % |
| Fusion Malware | 98,67 % | 98,12 % |

Los resultados corresponden a protocolos diferentes. No deben tratarse como una comparación controlada entre datasets. El apéndice A informa entrenamiento en una NVIDIA T4 de 16 GB y detalla hiperparámetros.

## Lectura crítica

Persisten dificultades con familias poco representadas y polimórficas. La atención cruzada ofrece una vía de inspección, pero no equivale por sí sola a una explicación fiel validada. El texto deja SHAP como trabajo futuro. No presenta un benchmark dedicado de latencia de explicación ni permite afirmar que el modelo tiene un costo prohibitivo en un SOC. Las múltiples vistas y snapshots hacen pertinente medir el costo, sin cuantificarlo por inferencia.

La normalización del vector estático se describe con media/desviación de muestras disponibles; al reproducirlo se deben ajustar esos parámetros solo con entrenamiento. Los valores de accuracy son resultados de sus benchmarks, no garantías de generalización a amenazas nuevas.

## Uso en el seminario — interpretación

Sirve para discutir representación multimodal y rendimiento, y para distinguir **calibración orientada a clasificación** de calibración probabilística fiable para nuestro enrutamiento. No prueba que una probabilidad de 0,95 implique un error inferior al 1 %. La necesidad de evaluar el costo total de TTA/ensembles es una inferencia metodológica nuestra.

## Localizadores de evidencia

- Resumen: p. 1.
- Arquitectura, normalización y protocolos: §3, pp. 4–6.
- Evaluación y discusión: §4, pp. 6–12.
- SHAP como trabajo futuro, conclusiones e hiperparámetros: pp. 11–13.

Abrir primera página: [[Papers/PDF/Alotaibi-2025-app152111635.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[Malimg Dataset]]
- [[Mecanismos de Atención]]
- [[Deep Learning]]
- [[Trade-offs en XAI]]
