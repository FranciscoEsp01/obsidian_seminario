---
tags: [dataset, malware, pe_windows, benchmark]
---

# BODMAS Dataset

El dataset **BODMAS** (*Bi-Objective Detection of Malware and Analysis System*) es un conjunto de datos masivo y contemporáneo de malware PE (Portable Executable) para Windows publicado por Yang et al. (2021).

## Características Principales
- **Volumen:** Contiene 57.293 muestras de malware y 77.142 muestras benignas recolectadas con marcas de tiempo precisas entre agosto de 2019 y septiembre de 2020.
- **Familias y Familias Mapeadas:** Clasifica muestras en 581 familias de malware claramente documentadas.
- **Espacio de Características:** Proporciona vectores de 2.381 características estáticas por muestra (derivadas de EMBER: secciones PE, entropía por bloque, tablas de importación/exportación de API, secuencias de bytes y cadenas de texto).
- **Importancia:** Es el estándar moderno preferido para evaluar la evolución temporal del malware, evasión adversarial ([[AFA-MalGAN - Generación Adversarial Adaptativa con Optimización de Variedades]]) y modelos multimodales ([[Attention-Based Cross-Modal CNN - Detección de Malware sin Desensamblado]], [[MIDALF - Fusión Multimodal de Imagen y Audio para Malware]]).

## Conceptos y Enlaces Relacionados
- [[Clasificación de Malware]]
- [[Análisis Estático]]
- [[Trade-offs en XAI]]
- [[Attention-Based Cross-Modal CNN - Detección de Malware sin Desensamblado]]
- [[MIDALF - Fusión Multimodal de Imagen y Audio para Malware]]
- [[AFA-MalGAN - Generación Adversarial Adaptativa con Optimización de Variedades]]

## Fuentes MDPI revisadas (octubre de 2026)

- [[CyberSentinel - Red Visual de Dos Ramas y Atención]]

Consultar [[Integración MDPI - Octubre 2026]] para alcance, resultados y limitaciones de cada fuente.
