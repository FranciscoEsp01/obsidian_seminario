---
tags: [moc, bibliografia, mdpi, revision]
fecha: 2026-10-04
status: integrado
---

# Integración MDPI - Octubre 2026

Los **12 artículos solicitados** se descargaron desde el servidor oficial de MDPI y se revisaron en texto completo. Cada ficha contiene metadatos contrastados con el PDF, métodos, resultados, lectura crítica, relación con el seminario y localizadores de evidencia. Los hallazgos se atribuyen a los autores; las implicaciones para nuestro diseño se identifican como interpretación. No se reprodujeron los experimentos.

Los documentos se conservan en `Papers/PDF/`. Bibliografía reutilizable: [[Papers/Referencias MDPI.bib|12 referencias BibTeX]]. Esta incorporación es una ampliación bibliográfica dirigida, **no una revisión sistemática PRISMA por sí sola**.

## Inventario en el orden solicitado

| Nº | Artículo / ficha | Publicación | DOI | PDF local | Prioridad |
|---|---|---|---|---|---|
| 1 | [[Ingeniería de Características Explicable sobre FCG - Kim et al]] | 2026 | [10.3390/app16062670](https://doi.org/10.3390/app16062670) | [[Papers/PDF/Kim-2026-app16062670.pdf|26 pp.]] | Alta: selección de características y medición de costos |
| 2 | [[Fusión Multimodal ConvNeXt y Calibración - Alotaibi]] | 2025 | [10.3390/app152111635](https://doi.org/10.3390/app152111635) | [[Papers/PDF/Alotaibi-2025-app152111635.pdf|14 pp.]] | Media: fusión visual y calibración |
| 3 | [[Malware Android con BERT y Representación Visual - Ullah et al]] | 2022 | [10.3390/s22186766](https://doi.org/10.3390/s22186766) | [[Papers/PDF/Ullah-2022-s22186766.pdf|23 pp.]] | Alta: XAI y datasets Android |
| 4 | [[Malware Android con Word2vec y Tráfico de Red - Ullah et al]] | 2022 | [10.3390/s22155883](https://doi.org/10.3390/s22155883) | [[Papers/PDF/Ullah-2022-s22155883.pdf|26 pp.]] | Alta: corregir caracterización del informe |
| 5 | [[Comparación ML y DL sobre Llamadas API - Cannarile et al]] | 2022 | [10.3390/app12031645](https://doi.org/10.3390/app12031645) | [[Papers/PDF/Cannarile-2022-app12031645.pdf|16 pp.]] | Alta: baseline tabular y tiempos |
| 6 | [[De Caja Negra a Caja de Cristal - Revisión XAI - Liu et al]] | 2025 | [10.3390/ai6110285](https://doi.org/10.3390/ai6110285) | [[Papers/PDF/Liu-2025-ai6110285.pdf|19 pp.]] | Alta: marco teórico y DOI correcto |
| 7 | [[XAI Ciberseguridad Diseño Humano y Edge - Cecchi et al]] | 2026 | [10.3390/jcp6030091](https://doi.org/10.3390/jcp6030091) | [[Papers/PDF/Cecchi-2026-jcp6030091.pdf|29 pp.]] | Alta: motivación SOC y evaluación humana |
| 8 | [[Explicabilidad en CNN - Revisión Sistemática - Tayari y Zaied]] | 2026 | [10.3390/make8080220](https://doi.org/10.3390/make8080220) | [[Papers/PDF/Tayari-2026-make8080220.pdf|38 pp.]] | Media-alta: taxonomía y métricas de explicación |
| 9 | [[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al]] | 2026 | [10.3390/jcp6030105](https://doi.org/10.3390/jcp6030105) | [[Papers/PDF/Ardito-2026-jcp6030105.pdf|35 pp.]] | Muy alta: antecedente cercano y control experimental |
| 10 | [[C-GUARD - Enrutamiento Adaptativo frente a Malware Evasivo]] | 2026 | [10.3390/fi18080431](https://doi.org/10.3390/fi18080431) | [[Papers/PDF/Imran-2026-fi18080431.pdf|26 pp.]] | Muy alta: límites de la confianza y enrutamiento |
| 11 | [[CyberSentinel - Red Visual de Dos Ramas y Atención]] | 2024 | [10.3390/s24113406](https://doi.org/10.3390/s24113406) | [[Papers/PDF/Basak-2024-s24113406.pdf|23 pp.]] | Alta: contraste visual y reporte de recursos |
| 12 | [[RFS-MD - Reglas Explicables y Robustez Android]] | 2026 | [10.3390/electronics15102167](https://doi.org/10.3390/electronics15102167) | [[Papers/PDF/Alhawari-2026-electronics15102167.pdf|44 pp.]] | Muy alta: alternativa explicable y evaluación de fidelidad |

## Qué cambia para el informe final del Seminario

1. **Selección de características con antecedentes directos.** Kim et al. (2026) reduce 13 dimensiones a 7 usando XAI y mide extracción/inferencia. Ardito et al. (2026) combina reducción con clasificación híbrida y auditoría SHAP/LIME. La brecha debe formularse como evaluación del costo específico de explicación, integración con destilación y adaptabilidad bajo controles de calidad.
2. **Confianza no equivale a ausencia de errores.** C-GUARD documenta malware evasivo clasificado como benigno con alta confianza. Los umbrales 0,95/0,80 son decisiones a calibrar y evaluar, no garantías de seguridad. C-GUARD adapta detección; no constituye validación de explicación adaptativa.
3. **Recursos de clasificación y recursos XAI son diferentes.** Cannarile reporta entrenamiento/predicción; CyberSentinel parámetros, memoria e inferencia; Ardito tiempos por fase. No atribuir esas cifras al tiempo de SHAP/LIME. Nuestro OE2 debe medir extracción, inferencia y explicación por separado.
4. **Calidad técnica y utilidad humana son diferentes.** Cecchi y Tayari muestran carencias de evaluación humana en sus corpus. Fidelidad por perturbación o mapas de atención no demuestran confianza del analista ni explicaciones causales del malware.
5. **Explicación adaptativa tiene antecedentes conceptuales.** Liu ya la contempla en su hoja de ruta. Nuestro aporte se puede delimitar por arquitectura, aplicación y validación en malware, sin atribuir novedad absoluta al concepto.
6. **Reglas explicables como alternativa.** RFS-MD incorpora selección, scoring, robustez y explicaciones RXAI; sirve para comparar alternativas y detallar fidelidad. No aporta un speedup XAI transferible a nuestra propuesta.

## Correcciones verificadas para la siguiente redacción

| Ubicación actual | Problema | Corrección respaldada |
|---|---|---|
| Informe de Avance, tabla 4.1, fila Ullah; presentación y guion derivados | PE Windows + stacking | s22155883 evalúa tráfico Android en CIC-AAGM2017/CICMalDroid con votación. s22186766 usa BERT y también votación; son artículos distintos. |
| Informe de Avance, referencia Liu | DOI ai611028 y 6(1) | **10.3390/ai6110285**, *AI*, **6(11), 285**. |
| Tabla 4.1, Kim | Solo se afirma conversión costosa | Incluir selección por IG/GradCAM/SHAP, MalNet-Tiny y costos reportados; no equiparar costo de representación a costo de explicación. |
| Tabla 4.1, Alotaibi | Limitación de alto consumo sin cifra propia | ConvNeXt-Tiny, Malimg/Fusion, atención cruzada; SHAP es trabajo futuro. No asignar un costo XAI medido inexistente. |
| Afirmación de ausencia de soluciones integradas | Demasiado amplia con los nuevos antecedentes | Reconocer Kim, Ardito y RFS-MD y contrastar componentes, métricas y protocolos. |
| Afirmación de que nadie evalúa eficiencia | No representa los artículos nuevos | CyberSentinel, Kim y Cannarile reportan recursos/tiempos; distinguirlos de un benchmark de explicadores. |

El informe y las presentaciones ya entregados se conservan como antecedentes históricos. Esta nota registra correcciones para el informe final; la integración no reescribe esos documentos ni cambia los objetivos aprobados.

## Matriz de uso en la redacción

| Parte del informe | Fuentes prioritarias | Qué permiten fundamentar |
|---|---|---|
| Contexto SOC y motivación | Cecchi; Liu | Restricciones operacionales, utilidad y costo; alcance de las afirmaciones. |
| Marco teórico XAI | Liu; Tayari | Taxonomía, métodos, fidelidad/estabilidad y necesidad de protocolos. |
| Estado del arte tabular e híbrido | Cannarile; Ardito; RFS-MD | Baselines, reducción, auditoría y alternativas explicables. |
| Estado del arte Android multimodal | Ullah 5883; Ullah 6766; Kim | Datasets Android, votación, representaciones y selección. |
| Modelos visuales y recursos | Alotaibi; CyberSentinel | Fusión/atención, métricas de clasificación y costos declarados. |
| Diseño adaptativo y limitaciones | C-GUARD; Liu | Enrutamiento selectivo y límites de probabilidades/seguridad. |

## Verificación de archivos

Se comprobó que los doce archivos son PDF legibles, que cada texto contiene el DOI esperado, y que las portadas coinciden con los artículos solicitados. Los enlaces internos de fichas y PDF se verificaron en el vault. La descarga se hizo desde MDPI porque sus páginas HTML respondían 403/429 a las herramientas; la revisión usa los PDF completos, no resultados de búsqueda como sustituto del artículo.

### Huellas SHA-256 de los PDF descargados

Sirven para identificar exactamente las copias consultadas; no prueban autenticidad editorial por sí solas.

| Archivo | SHA-256 |
|---|---|
| `Kim-2026-app16062670.pdf` | `984a87dbd5ea20019200a922b9a8824f795956ee62a9c13f56535447d124fd06` |
| `Alotaibi-2025-app152111635.pdf` | `4001ec10da6978fe3564cb4bd6e25f0ce92910cbe5e1f224f6dd6ced052bed58` |
| `Ullah-2022-s22186766.pdf` | `a70b6eb7fb135ec4ccfa0d837bd06f1377182e2db8356508050e2909cf111e82` |
| `Ullah-2022-s22155883.pdf` | `b8dd5ad88206784819c01ced774252749f5c24643bc8bbe62da940dac3b5407c` |
| `Cannarile-2022-app12031645.pdf` | `c241bf425293108dc6a0dab30d66f2186c3ee5e5a5f756246832653067976614` |
| `Liu-2025-ai6110285.pdf` | `8c6141472f1f928acb41d35e630001315700504b9eecff67d6e44832382c6148` |
| `Cecchi-2026-jcp6030091.pdf` | `0640a2558415b96e6bf6f877dbbdd9a7840f648b251dc19b2bdf1115c5d6c9ea` |
| `Tayari-2026-make8080220.pdf` | `3b565eb9752edc389a270500198a9c41b2a43dd2c18da0342824b5f2b04f55ae` |
| `Ardito-2026-jcp6030105.pdf` | `6e1af778bc419ffd8551a3d18ca2aa1437c4642d4a2b664ad7e0380960d6549e` |
| `Imran-2026-fi18080431.pdf` | `a7e68ebd96d76bb450eb5db2b53051487fb38a3d8558891a1fb946f63b533591` |
| `Basak-2024-s24113406.pdf` | `8631c73939145794531c9501397f4b75910ee7216eebfca2f3efca307f7c1cfb` |
| `Alhawari-2026-electronics15102167.pdf` | `39d8b2b8d3a9cc21655f0fb81190d9f4903ba74775e158e2cf329446ce452eae` |

## Navegación

- [[Seminario de Título - MOC]]
- [[Estado del Arte]]
- [[Metodología]]
- [[Informe de Avance - Seminario de Título]]
