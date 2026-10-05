---
tags: [metodo, malware, dinamico, sandbox]
---

# Análisis Dinámico

- **Definición:** Ejecuta el malware en un entorno controlado y aislado (sandbox o Máquina Virtual).
- **Observaciones:** Monitorea el comportamiento en tiempo de ejecución: cambios en el filesystem, comunicaciones de red, y llamadas al sistema (system calls).
- **Ventajas:** Detecta el comportamiento real de la amenaza y es resistente a la ofuscación estática y al empaquetado.
- **Desventajas:** Costoso computacionalmente, toma tiempo y el malware sofisticado puede emplear técnicas de evasión (como detección de VM o timing attacks).
- **Relación con otros conceptos:** Los resultados de este análisis a menudo alimentan modelos complejos de [[Deep Learning]] u otros de [[Machine Learning]] en la [[Clasificación de Malware]].
- La interpretabilidad de estos comportamientos se logra mediante [[Inteligencia Artificial Explicable (XAI)]], tal como se discute en [[Investigación Comprehensiva Detección de Malware con XAI]].
- Se combina con [[Análisis Estático]] para formar el [[Análisis Híbrido]].
