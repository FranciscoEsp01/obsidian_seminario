---
title: "AI-Driven Rule-Based Feature Scoring for Explainable and Adversarially Robust Android Malware Detection"
tags: ["paper", "mdpi", "revisado", "android", "reglas_asociacion", "fidelidad", "adversarial", "seleccion_caracteristicas"]
status: "revisado-en-texto-completo"
autores: ["Assem Alhawari", "Sahar Ebadinezhad"]
anio: 2026
fecha_publicacion: "2026-05-18"
fecha_revision: "2026-10-04"
doi: "10.3390/electronics15102167"
url: "https://www.mdpi.com/2079-9292/15/10/2167"
pdf: "Papers/PDF/Alhawari-2026-electronics15102167.pdf"
paginas: 44
citekey: "Alhawari2026RFSMD"
prioridad: "Muy alta: alternativa explicable y evaluación de fidelidad"
---

# AI-Driven Rule-Based Feature Scoring for Explainable and Adversarially Robust Android Malware Detection

## Referencia y acceso

Alhawari, A., & Ebadinezhad, S. (2026). AI-Driven Rule-Based Feature Scoring for Explainable and Adversarially Robust Android Malware Detection. *Electronics*, 15(10), 2167. https://doi.org/10.3390/electronics15102167

- [Página editorial](https://www.mdpi.com/2079-9292/15/10/2167) · [DOI](https://doi.org/10.3390/electronics15102167).
- [[Papers/PDF/Alhawari-2026-electronics15102167.pdf|PDF local completo (44 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

RFS-MD pondera características estáticas Android mediante reglas de asociación de clasificación obtenidas con FP-Growth. RXAI genera explicaciones por patrones de reglas. Extrae una muestra balanceada de AndroZoo: **4.500 APK malignos y 4.500 benignos**, con criterios VirusTotal >30 detecciones y cero detecciones, respectivamente. Usa información mutua para seleccionar atributos y evalúa clasificadores ML/DL, ataques PGD y ataques basados en consultas.

## Resultados reportados

El artículo informa mejora de recall en seis clasificadores bajo diez folds, con significación en cuatro; tras ajuste, alcanza hasta **98,58 % accuracy y 98,81 % recall**. Incluye prueba temporal sobre el 20 % más reciente del corpus y reporta menor tasa de éxito de ataques en modelos evaluados. Son resultados de su muestra y configuración, no garantías universales.

Para fidelidad toma **200 muestras de test**, 100 por clase, y mide diferencia absoluta de probabilidad tras retirar rasgos de reglas relevantes. Tabla 8: media **0,133** en malware y **0,0185** en benignos. Son cambios de probabilidad, **no porcentajes de «explicaciones correctas»**.

## Lectura crítica

Los criterios estrictos de VirusTotal excluyen grayware, amenazas recientes con pocas detecciones y posibles zero-day. La evaluación adversarial sobre vectores requiere distinguir perturbación matemática de APK funcional. No se reporta una comparación dedicada de latencia de RXAI frente a SHAP/LIME.

El protocolo describe selección, minería y scoring dentro del entrenamiento de cada fold, un control útil de fuga. La prueba temporal usa el mismo corpus y no sustituye validación independiente en otro dataset. La fidelidad por eliminación puede crear entradas fuera de distribución; debe explicitarse cómo se alteran las variables.

## Uso en el seminario — interpretación

Es un antecedente de integración de selección, clasificación y explicabilidad por diseño. Permite ampliar el contraste más allá de SHAP/LIME y formular un baseline por reglas. Su evaluación concreta de fidelidad ayuda al OE2, aunque nuestro estudio debe añadir estabilidad y costo del explicador. No respalda afirmar ausencia total de sistemas integrados explicables.

## Localizadores de evidencia

- Datos y selección: §3.1–3.2, pp. 7–10.
- Protocolo sin fuga: §3.5.3.
- Definición de fidelidad: §3.7.2, pp. 19–20.
- Muestra y resultados de fidelidad: §4.3.2, tabla 8.
- Limitaciones y generalización: §5.4–5.5.
- Síntesis: §6, pp. 40–42.

Abrir primera página: [[Papers/PDF/Alhawari-2026-electronics15102167.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[Análisis Estático]]
- [[Inteligencia Artificial Explicable (XAI)]]
- [[Trade-offs en XAI]]
- [[Metodología]]
- [[Costo Computacional de XAI]]
