---
tags: [concepto, machine_learning, deep_learning, optimizacion, destilacion]
---

# Destilación de Conocimiento (Knowledge Distillation)

La **Destilación de Conocimiento** (*Knowledge Distillation*, KD) es una técnica de compresión de modelos propuesta fundamentalmente por Geoffrey Hinton et al. (2015), en la cual el conocimiento adquirido por un modelo complejo, voluminoso y computacionalmente costoso (**modelo profesor** o *teacher*) es transferido a un modelo más compacto, rápido y ligero (**modelo estudiante** o *student*).

## Mecanismo de Funcionamiento
1. **Teacher Network:** Un modelo de alta capacidad (como un ensamble profundo o una red neuronal compleja) entrena sobre el dataset objetivo, capturando representaciones intrincadas y distribuciones de probabilidad ricas sobre las clases (*soft targets*).
2. **Student Network:** Un modelo compacto con menor número de parámetros es entrenado no sólo con las etiquetas binarias directas (*hard targets*), sino forzando a que su salida replique las probabilidades suavizadas (*soft labels*) generadas por el profesor mediante una pérdida combinada (usualmente Divergencia KL + Cross-Entropy con un parámetro de temperatura $T$).
3. **Destilación de Explicabilidad (XAI Distillation):** Extensiones recientes utilizan no sólo las predicciones de salida, sino también los mapas de saliencia o valores de atribución ([[SHAP]], [[Grad-CAM]], o gradientes de atención) para que el estudiante aprenda a fijarse en las mismas regiones críticas que el profesor.

## Relevancia en el Seminario de Título
- Representa el **Nivel 2 (Modelos Destilados)** de nuestra arquitectura jerárquica de 3 niveles para la [[Clasificación de Malware]].
- Permite mitigar drásticamente el [[Costo Computacional de XAI]] y la latencia de inferencia en tiempo real, reteniendo más del 98% del rendimiento del modelo complejo.
- Respaldado empíricamente en la literatura reciente por trabajos como [[MC-KDFF - Clasificación de Malware con Destilación de Conocimiento y Fusión]] (Guan & Zhang, IEEE Access 2025).

## Conceptos y Enlaces Relacionados
- [[Costo Computacional de XAI]]
- [[Trade-offs en XAI]]
- [[MC-KDFF - Clasificación de Malware con Destilación de Conocimiento y Fusión]]
- [[Deep Learning]]
- [[Ensemble Learning]]
- [[Propuesta - Optimización del Costo Computacional de XAI en Clasificación de Malware]]
