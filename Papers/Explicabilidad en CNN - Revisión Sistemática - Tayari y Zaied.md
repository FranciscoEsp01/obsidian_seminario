---
title: "From Black Box to Clarity: A Systematic Review of Explainability Methods in Deep Convolutional Neural Networks"
tags: ["paper", "mdpi", "revisado", "revision_sistematica", "cnn", "xai", "metricas"]
status: "revisado-en-texto-completo"
autores: ["Zina Tayari", "Mourad Zaied"]
anio: 2026
fecha_publicacion: "2026-07-23"
fecha_revision: "2026-10-04"
doi: "10.3390/make8080220"
url: "https://www.mdpi.com/2504-4990/8/8/220"
pdf: "Papers/PDF/Tayari-2026-make8080220.pdf"
paginas: 38
citekey: "Tayari2026Clarity"
prioridad: "Media-alta: taxonomía y métricas de explicación"
---

# From Black Box to Clarity: A Systematic Review of Explainability Methods in Deep Convolutional Neural Networks

## Referencia y acceso

Tayari, Z., & Zaied, M. (2026). From Black Box to Clarity: A Systematic Review of Explainability Methods in Deep Convolutional Neural Networks. *Machine Learning and Knowledge Extraction*, 8(8), 220. https://doi.org/10.3390/make8080220

- [Página editorial](https://www.mdpi.com/2504-4990/8/8/220) · [DOI](https://doi.org/10.3390/make8080220).
- [[Papers/PDF/Tayari-2026-make8080220.pdf|PDF local completo (38 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Alcance y método

Revisión sistemática de explicabilidad en CNN: **154 estudios** de 2017–2025 seleccionados de 4.421 registros recuperados de Web of Science, Scopus, IEEE Xplore y ACM Digital Library. Organiza métodos por momento de explicación, dependencia del modelo, tipo de salida y componente explicado. Incluye modificación/simplificación de arquitecturas, relevancia de características y visualización.

## Hallazgos reportados

Predominan métodos visuales post-hoc como Grad-CAM; entre los agnósticos destacan LIME y SHAP. El resumen informa que **98 de 154** trabajos evalúan objetivamente fidelidad, estabilidad o sensibilidad, y **menos de diez** usan evaluación centrada en personas. Propone reportar métricas técnicas junto con medidas humanas.

Identifica falta de benchmarks comparables, problemas de escalabilidad, vulnerabilidad adversarial y distancia entre explicación técnica y comprensión del usuario.

## Lectura crítica

El dominio es CNN en múltiples aplicaciones, no exclusivamente malware ni datos tabulares. Una distribución de técnicas en este corpus no demuestra su frecuencia en todos los sistemas de ciberseguridad. La propia revisión advierte que «fidelidad» puede medirse con perturbaciones y protocolos diferentes, impidiendo comparaciones directas entre trabajos.

## Uso en el seminario — interpretación

Sirve para delimitar el marco teórico y justificar la elección de métricas explícitas. Para SHAP/LIME tabular debemos especificar qué se perturba, con qué referencia, qué salida del modelo se mide y cómo se agrega el resultado. La revisión no demuestra que stacking sea intrínsecamente transparente ni que DL deba descartarse en cualquier caso.

## Localizadores de evidencia

- Resumen, cantidades y contribuciones: p. 1.
- Taxonomía y arquitecturas: §3–9.
- Métricas objetivas/humanas y falta de benchmarks: §10, pp. 25–30.
- Desafíos: §11; síntesis: §12.

Abrir primera página: [[Papers/PDF/Tayari-2026-make8080220.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[Grad-CAM]]
- [[SHAP]]
- [[LIME]]
- [[Redes Neuronales Convolucionales]]
- [[Trade-offs en XAI]]
