---
tags: [dataset, malware, vision, grayscale, benchmark]
---

# Malimg Dataset

El dataset **Malimg** (Nataraj et al., 2011) es el benchmark fundacional y más citado en la literatura científica para la clasificación de malware mediante técnicas de visión computacional y representaciones en escala de grises.

## Características Principales
- **Volumen:** 9.339 muestras de ejecutables binarios pertenecientes a 25 familias distintas de malware.
- **Representación Visual:** Cada archivo binario ejecutable (.exe o .dll) es interpretado como un vector unidimensional de bytes sin signo ($0-255$) y reestructurado en una matriz bidimensional con un ancho fijo dependiente del tamaño del archivo, visualizándose como una imagen en escala de grises.
- **Texturas Visuales:** Las distintas secciones del binario (.text, .data, .rsrc) producen patrones de textura y densidades características que permiten a las [[Redes Neuronales Convolucionales]] distinguir entre familias sin requerir desensamblado previo.

## Papers del Seminario que lo Utilizan
- [[IMCMKCNN - CNN Ligera Multi-Escala para Malware]]
- [[Attention-Based Cross-Modal CNN - Detección de Malware sin Desensamblado]]
- [[Evaluación de Modelos CNN Preentrenados en Detección de Malware]]
- [[SACNN - Clasificación de Imágenes de Malware con VGG19 y Atención Espacial]]
- [[EfficientNet CNN para Clasificación de Malware Basada en Imágenes]]
- [[MIRACLE - Reconocimiento de Imágenes de Malware por Extracción en Capas]]

## Conceptos y Enlaces Relacionados
- [[Redes Neuronales Convolucionales]]
- [[Deep Learning]]
- [[Análisis Estático]]
- [[Clasificación de Malware]]
- [[Grad-CAM]]

## Fuentes MDPI revisadas (octubre de 2026)

- [[Fusión Multimodal ConvNeXt y Calibración - Alotaibi]]
- [[CyberSentinel - Red Visual de Dos Ramas y Atención]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
