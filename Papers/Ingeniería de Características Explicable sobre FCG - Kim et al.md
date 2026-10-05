---
title: "Representation-Centric Approach for Android Malware Classification: Interpretability-Driven Feature Engineering on Function Call Graphs"
tags: ["paper", "mdpi", "revisado", "android", "gnn", "seleccion_caracteristicas", "xai"]
status: "revisado-en-texto-completo"
autores: ["Gyumin Kim", "Dongmin Yoon", "NaeJoung Kwak", "ByoungYup Lee"]
anio: 2026
fecha_publicacion: "2026-03-11"
fecha_revision: "2026-10-04"
doi: "10.3390/app16062670"
url: "https://www.mdpi.com/2076-3417/16/6/2670"
pdf: "Papers/PDF/Kim-2026-app16062670.pdf"
paginas: 26
citekey: "Kim2026FCG"
prioridad: "Alta: selección de características y medición de costos"
---

# Representation-Centric Approach for Android Malware Classification: Interpretability-Driven Feature Engineering on Function Call Graphs

## Referencia y acceso

Kim, G., Yoon, D., Kwak, N., & Lee, B. (2026). Representation-Centric Approach for Android Malware Classification: Interpretability-Driven Feature Engineering on Function Call Graphs. *Applied Sciences*, 16(6), 2670. https://doi.org/10.3390/app16062670

- [Página editorial](https://www.mdpi.com/2076-3417/16/6/2670) · [DOI](https://doi.org/10.3390/app16062670).
- [[Papers/PDF/Kim-2026-app16062670.pdf|PDF local completo (26 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

Estudia cómo la representación de entrada afecta la clasificación de malware Android mediante grafos de llamadas a funciones (FCG). Combina cinco atributos locales LDP con ocho atributos estructurales globales. Usa IG, GradCAM y SHAP para ordenar su importancia y seleccionar siete dimensiones. Compara GCN, GIN, GraphSAGE y JK-GraphSAGE sobre MalNet-Tiny: 5.000 grafos, cinco categorías; repite los experimentos con cinco semillas.

## Resultados reportados

- JK-GraphSAGE con siete dimensiones: **94,47 ± 0,25 % de accuracy**; baseline LDP: 94,15 %. La mejora es de **0,32 puntos porcentuales**.
- Reducción de 13 a 7 dimensiones: aproximadamente **46 %**. Son atributos por nodo, no la eliminación del 46 % de las funciones del APK.
- Tabla 11: preprocesamiento medio 54,17 ± 78,64 ms por grafo; mediana 22,82 ms. Inferencia media 3,60 ± 2,16 ms; mediana 3,14 ms, sobre 1.000 grafos.

## Lectura crítica

La evaluación se limita a MalNet-Tiny. El artículo reconoce que faltan validación en MalNet completo, explicaciones por instancia y evaluación adversarial. El algoritmo 1 denomina su entrada «Test dataset Dval»: esta ambigüedad exige aclarar qué partición se usó para seleccionar atributos antes de reproducir el protocolo. En nuestro diseño la selección debe aprenderse exclusivamente en entrenamiento/validación.

Los tiempos de la tabla 11 corresponden a extracción sobre grafos disponibles e inferencia; no constituyen una medición completa desde APK bruto ni del costo de IG/SHAP. Aunque los autores clasifican la extracción como costo offline, procesar un archivo nuevo requiere contabilizar la generación de su representación.

## Uso en el seminario — interpretación

Es un antecedente directo del **nivel 1**: la selección guiada por explicabilidad ya existe y debe reconocerse. Sustenta medir extracción e inferencia por separado. Corrige la caracterización del informe que solo lo presenta como una transformación costosa: también reporta reducción dimensional y tiempos. No demuestra la eficacia de nuestra destilación ni del motor adaptativo.

## Localizadores de evidencia

- Resumen y alcance: p. 1.
- Selección: §3.3 y algoritmo 1, pp. 12–13.
- Protocolo y resultados: §4, pp. 14–22.
- Costos: §4.7, tabla 11, pp. 22–23.
- Limitaciones y conclusiones: §5, pp. 23–25.

Abrir primera página: [[Papers/PDF/Kim-2026-app16062670.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[SHAP]]
- [[Grad-CAM]]
- [[Análisis Estático]]
- [[Costo Computacional de XAI]]
