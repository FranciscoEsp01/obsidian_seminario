---
tags: [metodo, malware, estatico]
---

# Análisis Estático

- **Definición:** Examina el código o ejecutable SIN ejecutarlo.
- **Características (Features) extraídas:** Firmas (signatures), metadatos, secuencias de API calls, opcodes, byte n-grams, PE (Portable Executable) headers.
- **Ventajas:** Es rápido, de bajo riesgo (no se ejecuta el código) y altamente escalable para analizar grandes volúmenes de archivos.
- **Desventajas:** Altamente vulnerable a técnicas de ofuscación, empaquetado (packing) y polimorfismo.
- **Uso:** Es la base para datasets como el [[ClaMP Dataset]]. Es abordado en casi toda la literatura del seminario, como se ve en el [[XAI for Malware Analysis Survey]] y [[XAI en Detección de Malware - Thompson et al]].
- Para contrarrestar sus debilidades, suele complementarse con el [[Análisis Dinámico]] formando un [[Análisis Híbrido]].
- Es el input de entrada para algoritmos de [[Machine Learning]] para la [[Clasificación de Malware]].
