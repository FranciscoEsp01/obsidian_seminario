---
title: "An Explainable Hybrid Pipeline for Malware Classification: Benchmark Construction, Feature Reduction, and Security-Oriented Evaluation"
tags: ["paper", "mdpi", "revisado", "hibrido", "seleccion_caracteristicas", "calibracion", "data_leakage", "shap", "lime"]
status: "revisado-en-texto-completo"
autores: ["Carmelo Ardito", "Giuseppe Loseto", "Riccardo Di Pietro", "Nicola Epicoco", "Alessandro Massaro"]
anio: 2026
fecha_publicacion: "2026-06-22"
fecha_revision: "2026-10-04"
doi: "10.3390/jcp6030105"
url: "https://www.mdpi.com/2624-800X/6/3/105"
pdf: "Papers/PDF/Ardito-2026-jcp6030105.pdf"
paginas: 35
citekey: "Ardito2026Hybrid"
prioridad: "Muy alta: antecedente cercano y control experimental"
---

# An Explainable Hybrid Pipeline for Malware Classification: Benchmark Construction, Feature Reduction, and Security-Oriented Evaluation

## Referencia y acceso

Ardito, C., Loseto, G., Di Pietro, R., Epicoco, N., & Massaro, A. (2026). An Explainable Hybrid Pipeline for Malware Classification: Benchmark Construction, Feature Reduction, and Security-Oriented Evaluation. *Journal of Cybersecurity and Privacy*, 6(3), 105. https://doi.org/10.3390/jcp6030105

- [Página editorial](https://www.mdpi.com/2624-800X/6/3/105) · [DOI](https://doi.org/10.3390/jcp6030105).
- [[Papers/PDF/Ardito-2026-jcp6030105.pdf|PDF local completo (35 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

Construye un benchmark público con variables estáticas y dinámicas alineadas por ejecutable y un espacio común de siete clases, basado en Windows Malwares v1.0. Combina RF estático, XGBoost dinámico calibrado y fusión tardía ponderada por weighted F1 de validación. Contrasta fusión temprana y otras variantes. Ajusta preprocesamiento y selección en entrenamiento; reserva prueba para evaluación final.

## Resultados reportados

- Características estáticas: **771 → 258**; dinámicas: **21.918 → 374**.
- Tabla 5, benchmark corregido sin fuga: fusión temprana XGBoost **89,69 % accuracy, macro F1 0,8983**; híbrido ponderado **88,54 %, macro F1 0,8825**.
- Tabla 6, al colapsar clases a benigno/malware: híbrido ponderado con **recall malware 0,9998, recall benigno 0,8053 y un falso negativo**. El alto recall binario no equivale a 99,98 % de accuracy multiclase.
- Tabla 8: preprocesamiento/reducción 816,98 s; entrenamiento estático 10,02 s; dinámico 147,68 s; fusión ponderada 3,54 s. Son tiempos de fases, no latencia por explicación.

## Explicabilidad y límites

Usa rankings y SHAP global en ramas, y una explicación local LIME de un falso negativo. La capa XAI se presenta como auditoría diagnóstica. No proporciona evaluación sistemática de utilidad con analistas ni una validación completa de calidad de explicaciones. La división es aleatoria estratificada, sin prueba temporal/OOD ni ataques adversariales.

## Uso en el seminario — interpretación

Es un **antecedente cercano** de integración entre reducción, clasificación y XAI. Debe aparecer en la matriz de trabajos relacionados y obliga a precisar la brecha: no basta afirmar que no existen pipelines integrados. Nuestra comparación puede centrarse en costo incremental de explicar, destilación y explicación adaptativa/caché. El objetivo operacional debe guiar selección de métricas: recall malware y falsos positivos junto a macro F1.

Sus tiempos de fases no demuestran un ahorro de SHAP. Para validar nuestro aporte hacen falta ablaciones y comparación con TreeSHAP completo sobre un estudiante entrenado directamente.

## Localizadores de evidencia

- Benchmark: §3, pp. 4–6.
- Método y auditoría XAI: §4, pp. 6–9.
- Protocolo y tablas 5–6: §5, pp. 9–11.
- Tabla 8 y explicación local: pp. 13–14.
- Límites y conclusiones: §7–8, pp. 16–17.

Abrir primera página: [[Papers/PDF/Ardito-2026-jcp6030105.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[Análisis Híbrido]]
- [[Random Forest]]
- [[SHAP]]
- [[LIME]]
- [[Metodología]]
- [[Costo Computacional de XAI]]
