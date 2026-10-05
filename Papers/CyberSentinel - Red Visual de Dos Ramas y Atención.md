---
title: "CyberSentinel: A Transparent Defense Framework for Malware Detection in High-Stakes Operational Environments"
tags: ["paper", "mdpi", "revisado", "cnn", "atencion", "malimg", "bodmas", "eficiencia"]
status: "revisado-en-texto-completo"
autores: ["Mainak Basak", "Myung-Mook Han"]
anio: 2024
fecha_publicacion: "2024-05-25"
fecha_revision: "2026-10-04"
doi: "10.3390/s24113406"
url: "https://www.mdpi.com/1424-8220/24/11/3406"
pdf: "Papers/PDF/Basak-2024-s24113406.pdf"
paginas: 23
citekey: "Basak2024CyberSentinel"
prioridad: "Alta: contraste visual y reporte de recursos"
---

# CyberSentinel: A Transparent Defense Framework for Malware Detection in High-Stakes Operational Environments

## Referencia y acceso

Basak, M., & Han, M.-M. (2024). CyberSentinel: A Transparent Defense Framework for Malware Detection in High-Stakes Operational Environments. *Sensors*, 24(11), 3406. https://doi.org/10.3390/s24113406

- [Página editorial](https://www.mdpi.com/1424-8220/24/11/3406) · [DOI](https://doi.org/10.3390/s24113406).
- [[Papers/PDF/Basak-2024-s24113406.pdf|PDF local completo (23 páginas)]].
- Licencia indicada en el PDF: **CC BY**. Descargado del servidor oficial de MDPI el 2026-10-04.
- Revisión bibliográfica basada en el texto completo; no se reprodujeron sus experimentos.

## Problema y método

Transforma binarios de malware en imágenes y propone una red de dos ramas (AAN): una base DenseNet con atención espacial asimétrica y una rama auxiliar para recuperar rasgos faltantes. Incluye optimización de hiperparámetros por quantum swarm. Evalúa Malimg, Microsoft Malware Classification y el subconjunto BODMAS-14.

## Resultados reportados

| Benchmark | Accuracy | F1 informado |
|---|---:|---:|
| Malimg | 99,47 % | 0,9948 |
| Microsoft Malware | 98,47 % | 0,9848 |
| BODMAS-14 | 98,24 % | 0,9825 |

La tabla 11 informa **12,12 millones de parámetros**, memoria **20,32 MB**, complejidad **2,9 Gmac** e inferencia **0,2 ms**. Son cifras reportadas por el artículo en su configuración; no equivalen a costo de explicación por muestra y requieren replicar condiciones antes de compararlas con CPU local. Gmac mide operaciones acumuladas, no operaciones por segundo.

## Lectura crítica

Atención y diseño visual no demuestran automáticamente fidelidad, comprensión humana o utilidad forense. No presenta un benchmark separado de SHAP/LIME ni una validación con analistas. Reconoce limitaciones de diversidad de datos; despliegue edge es trabajo futuro. BODMAS-14 no equivale a evaluar todo BODMAS en detección binaria.

## Uso en el seminario — interpretación

Es un antecedente que **sí reporta recursos e inferencia**: no conviene afirmar que toda la literatura visual ignora eficiencia. La brecha más precisa es la medición y optimización del costo de explicación bajo calidad controlada. Se puede usar para distinguir costos del clasificador, extracción y explicador, y para contrastar atención integrada con XAI post-hoc tabular.

## Localizadores de evidencia

- Resumen: p. 1; arquitectura: §3.
- Datasets e implementación: §4.1–4.2, pp. 12–15.
- Rendimiento: tablas 4–7, pp. 15–18.
- Recursos y limitaciones: §5, tabla 11, pp. 20–21.
- Conclusiones: p. 21.

Abrir primera página: [[Papers/PDF/Basak-2024-s24113406.pdf#page=1|Referencia original]]. Los localizadores anteriores usan la numeración impresa del PDF.

## Notas relacionadas

- [[Integración MDPI - Octubre 2026]]
- [[Estado del Arte]]
- [[Seminario de Título - MOC]]
- [[Mecanismos de Atención]]
- [[Redes Neuronales Convolucionales]]
- [[Malimg Dataset]]
- [[BODMAS Dataset]]
- [[Costo Computacional de XAI]]
