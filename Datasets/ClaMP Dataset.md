---
tags: [dataset, malware, pe-headers, estatico]
---

# ClaMP Dataset

- **Significado:** Classification of Malware with PE (Portable Executable) headers.
- **Enfoque:** Dataset basado íntegramente en features extraídas mediante [[Análisis Estático]] de los encabezados PE de archivos de Windows.
- **Desempeño reportado:** Usado extensivamente en el paper [[MAL-XSEL Framework]], logrando un accuracy impresionante del 99.62%.
- **Modelos:** Se ha probado contra algoritmos como [[LightGBM]], [[Random Forest]] y arquitecturas de [[Ensemble Learning]].
- Es un dataset clave para validar la explicabilidad de las características estáticas mediante herramientas de [[Inteligencia Artificial Explicable (XAI)]] como [[SHAP]].
