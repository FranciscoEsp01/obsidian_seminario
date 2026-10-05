---
title: "Comparing Deep Learning and Shallow Learning Techniques for API Calls Malware Prediction: A Study"
tags: ["paper", "mdpi", "revisado", "api_calls", "arboles", "shap", "benchmark"]
status: "revisado-en-texto-completo"
autores: ["Angelo Cannarile", "Vincenzo Dentamaro", "Stefano Galantucci", "Andrea Iannacone", "Donato Impedovo", "Giuseppe Pirlo"]
anio: 2022
fecha_publicacion: "2022-02-04"
fecha_revision: "2026-10-04"
doi: "10.3390/app12031645"
url: "https://www.mdpi.com/2076-3417/12/3/1645"
pdf: "Papers/PDF/Cannarile-2022-app12031645.pdf"
paginas: 16
citekey: "Cannarile2022API"
prioridad: "Alta: baseline tabular y tiempos"
---

# Comparing Deep Learning and Shallow Learning Techniques for API Calls Malware Prediction: A Study

## Referencia y acceso

Cannarile, A., Dentamaro, V., Galantucci, S., Iannacone, A., Impedovo, D., & Pirlo, G. (2022). Comparing Deep Learning and Shallow Learning Techniques for API Calls Malware Prediction: A Study. *Applied Sciences*, 12(3), 1645. https://doi.org/10.3390/app12031645

- [Página editorial](https://www.mdpi.com/2076-3417/12/3/1645) · [DOI](https://doi.org/10.3390/app12031645).
- [[Papers/PDF/Cannarile-2022-app12031645.pdf|PDF local completo (16 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

Compara RF, CatBoost, XGBoost y ExtraTrees con TabNet y NODE sobre dos datasets tabulares de llamadas API: malware-analysis-datasets-api-call-sequences y APIMDS. Usa validación cruzada estratificada de diez folds, submuestreo, codificación y normalización. Emplea SHAP para identificar API asociadas a las decisiones. La tarea evaluada es binaria.

## Resultados reportados

| Dataset | Modelo | F1 informado | AUC ROC informado |
|---|---|---:|---:|
| API call sequences | CatBoost | 0,877 | 0,8201 |
| APIMDS | XGBoost | 0,9779 | 0,9632 |

Las tablas 4–5 informan tiempos de entrenamiento y predicción en segundos. En API call sequences, CatBoost: 6,70016 s / 0,00566 s; TabNet: 38,97393 s / 0,16049 s. Son tiempos del experimento descrito, **no latencias por muestra de XAI**. NODE se reporta con una medición individual de entrenamiento debido a su duración, según la nota de tabla.

## Lectura crítica

Los datos están muy desbalanceados. El artículo presenta cantidades distintas para APIMDS entre descripción y resultados; conviene verificar el archivo concreto al reproducirlo. La tabla 3 incluye AUC ROC 0,0022 para NODE, una cifra llamativa que no debe corregirse por suposición ni usarse sin aclaración. F1 aparece rotulado de manera general en tablas y como macro F1 en el texto.

El estudio respalda considerar árboles como baselines competitivos frente a DL en estos datos. No demuestra que todos los modelos profundos sean más lentos en cualquier escenario, ni mide el costo separado de explicar con SHAP.

## Uso en el seminario — interpretación

Ayuda a justificar entrenar directamente un modelo de árboles como **baseline exigente**, antes de atribuir mejoras a la destilación. La utilidad de destilar debe demostrarse frente al estudiante entrenado con etiquetas reales. Aporta un ejemplo de reporte de tiempos y limitaciones, además de explicaciones con atributos semánticos de API.

## Localizadores de evidencia

- Datasets: §3, p. 5.
- Modelos y protocolo: §4, pp. 6–8.
- Métricas y tiempos: tablas 2–5, pp. 9–10.
- SHAP y API relevantes: §6, pp. 10–14.
- Conclusiones: pp. 14–15.

Abrir primera página: [[Papers/PDF/Cannarile-2022-app12031645.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[SHAP]]
- [[Random Forest]]
- [[Deep Learning]]
- [[Costo Computacional de XAI]]
- [[Análisis Dinámico]]
