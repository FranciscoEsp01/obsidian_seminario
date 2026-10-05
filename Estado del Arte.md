---
tags: [seminario, estado-del-arte, xai, malware, revisión-literaria]
status: borrador
fecha: 2025-08-15
tema: Inteligencia Artificial Explicable en la Clasificación de Malware
related: "[[Seminario de Título - MOC]]"
---

# Estado del Arte: Inteligencia Artificial Explicable en la Clasificación de Malware

## 1. Introducción

El malware constituye una de las amenazas más persistentes y dañinas en el panorama actual de la ciberseguridad. Su impacto afecta a individuos, organizaciones y gobiernos, causando pérdidas financieras multimillonarias, robo de datos sensibles y la interrupción de infraestructuras críticas (Baghirov, 2025; Saqib et al., 2024). Según el reporte de Malwarebytes de 2024, los ataques de ransomware documentados aumentaron un 68% durante 2023, mientras que el instituto AV-TEST registra más de 450.000 nuevas instancias de software malicioso cada día (Baghirov, 2025). Esta realidad evidencia la necesidad imperativa de desarrollar mecanismos de detección robustos, adaptativos y, crucialmente, comprensibles para los profesionales de la ciberseguridad.

En respuesta a esta creciente amenaza, los enfoques basados en [[Machine Learning]] (ML) y [[Deep Learning]] (DL) han emergido como herramientas poderosas para la detección y clasificación de malware, demostrando capacidades superiores a los métodos tradicionales basados en firmas (Manthena et al., 2025; Saqib et al., 2024). Sin embargo, estos modelos frecuentemente operan como "cajas negras" (*black boxes*), ofreciendo alta precisión pero escasa transparencia en sus procesos de toma de decisiones (Thompson et al., 2025). Esta opacidad plantea desafíos significativos en contextos de alta criticidad donde comprender *por qué* una detección ocurrió es tan importante como la detección misma.

La [[Inteligencia Artificial Explicable (XAI)]] surge como un paradigma que busca cerrar la brecha entre el rendimiento de los modelos de ML/DL y la necesidad de transparencia, interpretabilidad y confianza en los sistemas de detección de malware (Manthena et al., 2025; Saqib et al., 2024; Hemdan et al., 2025). El presente estado del arte revisa la literatura reciente sobre la aplicación de técnicas XAI en la clasificación de malware, examinando los métodos de análisis, los modelos utilizados, las técnicas de explicabilidad empleadas y los desafíos abiertos en este campo de investigación.

---

## 2. Métodos de Análisis de Malware

La detección de malware se sustenta en tres enfoques fundamentales de análisis, cada uno con fortalezas y limitaciones particulares que condicionan su aplicabilidad.

### 2.1 Análisis Estático

El [[Análisis Estático]] consiste en examinar el código o archivo ejecutable de un programa sin ejecutarlo. Este método inspecciona características como firmas de archivos, metadatos, llamadas a API, secuencias de *opcodes*, *byte n-grams* y cabeceras PE (*Portable Executable*) para identificar indicadores potenciales de comportamiento malicioso (Baghirov, 2025; Manthena et al., 2025). Entre sus ventajas se cuentan la rapidez de procesamiento, la escalabilidad para grandes volúmenes de archivos y el mínimo riesgo de activar acciones maliciosas inadvertidamente. No obstante, el análisis estático presenta dificultades frente a malware polimórfico u ofuscado que altera activamente su código o estructura para evadir la detección (Baghirov, 2025). Además, su dependencia de heurísticas y firmas estáticas puede generar falsos positivos, clasificando incorrectamente archivos benignos como maliciosos.

### 2.2 Análisis Dinámico

El [[Análisis Dinámico]] implica ejecutar el malware en un entorno controlado, como una máquina virtual o *sandbox*, para observar su comportamiento en tiempo real (Baghirov, 2025; Manthena et al., 2025). Este método permite monitorear actividades como cambios en el sistema de archivos, comunicaciones de red y llamadas al sistema (*system calls*). A diferencia del análisis estático, el dinámico puede detectar potencialmente malware polimórfico y amenazas previamente no vistas al observar su comportamiento efectivo. Sin embargo, requiere recursos computacionales significativos, puede introducir retardos en la detección y es susceptible a técnicas de evasión sofisticadas como la detección de entornos virtualizados y ataques de temporización (*timing attacks*) (Baghirov, 2025).

### 2.3 Análisis Híbrido

El [[Análisis Híbrido]] combina las técnicas estáticas y dinámicas, aprovechando las fortalezas de ambos enfoques para lograr una detección más robusta contra la evasión (Manthena et al., 2025; Saqib et al., 2024). Si bien ofrece mayor cobertura y precisión, también conlleva un mayor costo computacional. Baghirov (2025) señala que los avances futuros en detección de malware probablemente se centren en desarrollar enfoques híbridos que aborden las limitaciones respectivas de cada método individual.

---

## 3. Aplicación de Machine Learning y Deep Learning en la Clasificación de Malware

### 3.1 Modelos de Machine Learning Tradicional

Los modelos de ML tradicional han sido extensamente aplicados en la clasificación de malware. Las máquinas de soporte vectorial (SVM), los árboles de decisión y los métodos de *ensemble* fueron los primeros en emplearse para la clasificación basada en características estáticas (Thompson et al., 2025; Saqib et al., 2024). Entre los modelos más relevantes identificados en la literatura se encuentran:

- **[[Random Forest]]**: Ampliamente utilizado como modelo *baseline* en detección de malware, ofreciendo interpretabilidad inherente a través de la importancia de *features*. Hemdan et al. (2025) reportan una precisión de 99.33% en el dataset ClaMP.
- **[[LightGBM]]**: Framework de *gradient boosting* eficiente y rápido, compatible con TreeSHAP para explicabilidad. Baghirov (2025) lo emplea como uno de los modelos principales en su estudio, mientras que Hemdan et al. (2025) reportan 99.52% de precisión.
- **[[Regresión Logística]]**: Modelo inherentemente interpretable cuyos coeficientes indican directamente la importancia de las *features*. Baghirov (2025) lo utiliza como modelo *baseline* en su evaluación con el dataset CICMalDroid.
- **[[Ensemble Learning]]**: Hemdan et al. (2025) proponen MAL-XSEL, un framework basado en *stacking ensemble learning* que alcanza precisiones de 99.62% (ClaMP) y 99.16% (MalwareDataSet), superando a modelos individuales.

### 3.2 Modelos de Deep Learning

Los modelos de [[Deep Learning]] han mejorado significativamente el rendimiento en clasificación de malware al aprender representaciones complejas y jerárquicas de los datos (Thompson et al., 2025; Saqib et al., 2024):

- **[[Redes Neuronales Convolucionales]] (CNN)**: Aplicadas a la representación de binarios de malware como imágenes en escala de grises. Saqib et al. (2024) documentan que las CNN alcanzan hasta 99.44% de precisión en ciertos estudios, aunque señalan que la arquitectura Transformer tuvo el rendimiento más bajo (48.6%) en su análisis comparativo.
- **Redes Neuronales Recurrentes (RNN) y LSTM**: Empleadas para el análisis de secuencias de llamadas a API y *opcodes*, capturando dependencias temporales en el comportamiento del malware.
- **Transformers y BERT**: Modelos basados en atención que han demostrado hasta 99.40% de fidelidad en detección de malware, según la revisión de Saqib et al. (2024).

### 3.3 El Problema de la Caja Negra

A pesar de su alto rendimiento, estos modelos —particularmente los de DL— operan como cajas negras que dificultan la comprensión de sus procesos de decisión (Manthena et al., 2025; Saqib et al., 2024; Thompson et al., 2025). Esta falta de interpretabilidad plantea preocupaciones sobre la confianza, la responsabilidad (*accountability*) y la usabilidad. Los analistas de seguridad, administradores de sistemas y organismos reguladores requieren transparencia para validar el comportamiento de los sistemas de detección, especialmente en escenarios de respuesta a incidentes o investigaciones legales (Thompson et al., 2025). En 2016, la Agencia de Proyectos de Investigación Avanzados de Defensa (DARPA) introdujo el concepto de Inteligencia Artificial Explicable (XAI) para reducir la opacidad de los modelos de DL y fortalecer la transparencia, interpretabilidad y explicabilidad (Saqib et al., 2024).

---

## 4. Inteligencia Artificial Explicable (XAI) Aplicada a la Clasificación de Malware

### 4.1 Distinción entre Interpretabilidad y Explicabilidad

Manthena et al. (2025) establecen una distinción fundamental entre modelos *interpretables* y *explicables*. Los primeros son inherentemente transparentes (como árboles de decisión y regresión lineal), mientras que los segundos emplean técnicas *post-hoc* aplicadas a modelos opacos para generar explicaciones comprensibles. Esta taxonomía es central para comprender el panorama de XAI en la detección de malware.

### 4.2 Técnicas XAI Principales

La literatura identifica cuatro técnicas XAI predominantes en la clasificación de malware:

#### 4.2.1 SHAP (SHapley Additive exPlanations)

[[SHAP]] se basa en los valores de Shapley de la teoría de juegos cooperativos para cuantificar la contribución marginal de cada *feature* a una predicción específica (Baghirov, 2025; Hemdan et al., 2025; Thompson et al., 2025). Sus variantes incluyen TreeSHAP (optimizado para modelos basados en árboles), KernelSHAP (agnóstico al modelo) y DeepSHAP (para redes neuronales profundas). SHAP ofrece consistencia teórica y la capacidad de generar tanto explicaciones locales (por instancia) como globales (del modelo completo). Baghirov (2025) lo emplea para identificar las *features* más críticas en la clasificación de malware Android, mientras que Hemdan et al. (2025) lo integran en el framework MAL-XSEL para explicar las predicciones de su modelo de *stacking ensemble*.

#### 4.2.2 LIME (Local Interpretable Model-agnostic Explanations)

[[LIME]] genera perturbaciones alrededor de una instancia de interés y entrena un modelo interpretable local (típicamente un modelo lineal) para aproximar las decisiones del modelo complejo en esa vecindad (Baghirov, 2025; Hemdan et al., 2025; Thompson et al., 2025). Su principal ventaja es ser agnóstico al modelo, funcionando con cualquier clasificador. Sin embargo, presenta limitaciones en la estabilidad de las explicaciones generadas. Tanto Baghirov (2025) como Hemdan et al. (2025) emplean LIME complementariamente a SHAP, proporcionando explicaciones a nivel de instancia que permiten a los analistas comprender decisiones individuales del modelo.

#### 4.2.3 Grad-CAM (Gradient-weighted Class Activation Mapping)

[[Grad-CAM]] visualiza las regiones más relevantes en los datos de entrada que influyen en la predicción del modelo, siendo particularmente útil cuando el malware se representa como imágenes (Manthena et al., 2025; Saqib et al., 2024). Saqib et al. (2024) reportan un 96% de precisión en estudios que emplean Grad-CAM para la detección de malware basada en imágenes.

#### 4.2.4 Mecanismos de Atención

Los [[Mecanismos de Atención]] permiten al modelo asignar pesos diferenciados a distintas partes del *input*, revelando qué elementos son más relevantes para la predicción (Thompson et al., 2025; Manthena et al., 2025). Son particularmente útiles en el análisis de secuencias de llamadas a API y *opcodes*, y ofrecen un grado inherente de interpretabilidad en arquitecturas como los Transformers.

### 4.3 Evaluación de la Explicabilidad

Saqib et al. (2024) proponen un marco (*framework*) para evaluar la explicabilidad de los modelos XAI en análisis de malware, basado en diferentes niveles de explicación y una taxonomía para evaluar la comprensibilidad. Los criterios de evaluación incluyen fidelidad, robustez, expresividad, completitud, dispersión (*sparsity*), estabilidad/consistencia y eficiencia. Su análisis revela que la mayoría de los estudios existentes carecen de una evaluación formal de la interpretabilidad, representando una brecha significativa en la literatura.

---

## 5. Resultados y Hallazgos Principales

### 5.1 Rendimiento de Modelos con XAI y Complejidad Computacional

La tabla siguiente sintetiza los principales resultados reportados en la literatura revisada, incorporando tanto modelos de alta capacidad como arquitecturas optimizadas y destiladas:

| Estudio | Modelo | Dataset | Accuracy | F1-Score | Técnica XAI / Explicabilidad |
|---------|--------|---------|----------|----------|-------------------------------|
| Baghirov (2025) | LightGBM + tree-based | [[CICMalDroid]] | ~94.00% | 94.00% | [[SHAP]], [[LIME]] |
| Hemdan et al. (2025) | Stacking Ensemble (MAL-XSEL) | [[ClaMP Dataset]] | 99.62% | — | [[SHAP]], [[LIME]] |
| Hemdan et al. (2025) | Stacking Ensemble (MAL-XSEL) | MalwareDataSet | 99.16% | — | [[SHAP]], [[LIME]] |
| Hemdan et al. (2025) | [[LightGBM]] | [[ClaMP Dataset]] | 99.52% | — | — |
| Hemdan et al. (2025) | [[Random Forest]] | [[ClaMP Dataset]] | 99.33% | — | — |
| Chimeleze et al. (2024) | FCMSA + [[LightGBM]] | Android Permissions | 99.21% | 99.70% (P) | Clusters FCMSA + Feature Importance |
| Guan & Zhang (2025, MC-KDFF) | [[Destilación de Conocimiento]] (Student Net) | PE Malware | 98.8% retención | — | Atribución latente transferida (-82% latencia) |
| Arp et al. (2014, DREBIN) | Linear SVM | DREBIN | 94.00% | 94.00% | Pesos lineales directos (Inherente por diseño) |
| Sun et al. (2023) | Cross-Modal CNN (Bytes + Entropía) | [[BODMAS Dataset]] / [[Malimg Dataset]] | >98.00% | >98.00% | [[Mecanismos de Atención]] cruzada |
| Al-rimy et al. (2025, MIDALF) | Multimodal Image + Audio | [[BODMAS Dataset]] | 99.70% | 99.70% | Late Fusion multi-dominio |
| Awan et al. (2021, SACNN) | VGG19 + Spatial Attention | [[Malimg Dataset]] | 97.40% | 97.40% | Spatial Attention Maps |
| Chaganti et al. (2022) | EfficientNet (Compound Scaling) | [[Malimg Dataset]] | 98.50% | 98.50% | Mapas convolucionales eficientes |
| Nazim et al. (2025) | Deep Multimodal Ensemble | Windows PE | >99.40% | >99.40% | Representación jerárquica multimodal |
| Thompson et al. (2025) | Múltiples | Real-world dataset | Modesta reducción | — | [[SHAP]], [[LIME]], Atención |
| Saqib et al. (2024) | XGBoost | Varios | 99.85% | 99.85% | — |
| Saqib et al. (2024) | CNN | Varios | Hasta 99.44% | 99.44% | [[Grad-CAM]] (96.0% precisión en visión) |

### 5.2 Trade-offs Identificados

Los [[Trade-offs en XAI]] constituyen el núcleo de la problemática actual:

1. **Accuracy vs. Interpretabilidad**: Modelos masivos (como ensembles profundos o Transformers) alcanzan precisiones >99.5%, pero operan como cajas negras completas. Los modelos inherentemente interpretables ([[Regresión Logística]], SVM lineal, árboles de baja profundidad) ofrecen transparencia total pero pueden sufrir degradación en escenarios no lineales complejos (Thompson et al., 2025).
2. **Complejidad Computacional y Latencia**: Las técnicas XAI post-hoc añaden un sobrecoste computacional masivo. [[SHAP]] (KernelSHAP) requiere miles de evaluaciones marginales de inferencia por muestra, lo cual es impracticable en un Security Operations Center (SOC) que procesa cientos de miles de muestras diarias (Baghirov, 2025; [[Costo Computacional de XAI]]).
3. **Optimización mediante Destilación**: Trabajos pioneros como [[MC-KDFF - Clasificación de Malware con Destilación de Conocimiento y Fusión]] (Guan & Zhang, 2025) demuestran que la [[Destilación de Conocimiento]] es una vía prometedora para resolver este trade-off, reduciendo el 78% de los parámetros y el 82% de la latencia sin perder fidelidad explicativa.
4. **Granularidad (Local vs. Global)**: Las explicaciones locales ([[LIME]]) permiten justificar alertas individuales de incidentes, mientras que las explicaciones globales ([[SHAP]] summary) permiten a los ingenieros de detección auditar reglas generales y dependencias de features.
5. **Vulnerabilidad Adversarial de Explicadores**: Estudios como [[AFA-MalGAN - Generación Adversarial Adaptativa con Optimización de Variedades]] y Saqib et al. (2024) advierten que tanto la predicción como los mapas de explicación pueden ser burlados mediante optimización de saliencia por gradiente si el atacante conoce los pesos del modelo.

### 5.3 Valor de XAI más allá de la Precisión

Un hallazgo transversal en la literatura es que el valor de XAI trasciende la mera mejora de precisión. Baghirov (2025) y Vásquez Berríos et al. (2025) concluyen que las técnicas XAI aportan *insights* forenses esenciales para analistas de malware, permitiendo verificar si la detección se fundamenta en código malicioso genuino o en artefactos espurios del compilador (*spurious correlations*).

---

## 6. Desafíos Abiertos y Direcciones Futuras

La revisión sistemática de la literatura permite estructurar los siguientes desafíos abiertos:

### 6.1 Sesgo hacia Plataformas Específicas
Manthena et al. (2025) y Vásquez Berríos et al. (2025) identifican una concentración dominante en Windows PE y Android APK, con escasez de estudios rigurosos de XAI en firmware IoT, Linux y formatos de documentos (PDF, macros de Office).

### 6.2 Reducción del Overhead Computacional de XAI en Tiempo Real
La aplicación de técnicas XAI en pipelines de producción permanece como el mayor obstáculo de ingeniería. El coste computacional de calcular Shapley values o perturbaciones locales restringe su uso interactivo ([[Costo Computacional de XAI]]). La arquitectura jerárquica de 3 niveles formulada en nuestro seminario apunta directamente a resolver esta brecha.

### 6.3 Estandarización de Métricas de Explicabilidad
No existe un estándar matemático unificado para calificar la fidelidad, estabilidad y comprensibilidad de una explicación en ciberseguridad (Saqib et al., 2024).

### 6.4 Robustez Adversarial en Explicaciones
Garantizar que un atacante no pueda generar perturbaciones que mantengan la etiqueta de "benigno" mientras manipulan la máscara de saliencia para engañar al analista forense ([[AFA-MalGAN - Generación Adversarial Adaptativa con Optimización de Variedades]]).

---

## 7. Síntesis y Conclusiones

La intersección entre XAI y la clasificación de malware ha madurado desde un enfoque meramente exploratorio hacia una necesidad operativa ineludible:
1. Las arquitecturas de ML y DL superan el 99% de exactitud en benchmarks estándar ([[CICMalDroid]], [[ClaMP Dataset]], [[BODMAS Dataset]], [[Malimg Dataset]]), pero su opacidad impide validar la lógica forense de la decisión.
2. El desafío fundamental ya no es elevar marginalmente el accuracy, sino **democratizar el acceso a la explicabilidad reduciendo el costo computacional** que imponen explicadores post-hoc como SHAP y LIME.
3. La combinación de modelos interpretables por diseño (Nivel 1), compresión mediante destilación de conocimiento (Nivel 2, validado por Guan & Zhang, 2025), y boosters optimizados como LightGBM con TreeSHAP acelerado (Nivel 3, validado por Chimeleze et al., 2024) constituye la respuesta metodológica idónea para este desafío.

---

## 8. Actualización con textos completos MDPI (4 de octubre de 2026)

Se incorporaron doce artículos con sus PDF y fichas críticas, accesibles desde [[Integración MDPI - Octubre 2026]]. Esta ampliación dirigida no completa por sí sola el protocolo de revisión sistemática. Las referencias y conclusiones previas deben contrastarse con los textos originales antes de incorporarlas al informe final.

### 8.1. Antecedentes de reducción, explicabilidad y eficiencia

[[Ingeniería de Características Explicable sobre FCG - Kim et al|Kim et al. (2026)]] selecciona siete de trece dimensiones usando IG, GradCAM y SHAP, con 94,47 % de accuracy en JK-GraphSAGE y tiempos separados de extracción e inferencia. [[Comparación ML y DL sobre Llamadas API - Cannarile et al|Cannarile et al. (2022)]] compara clasificadores tabulares y reporta entrenamiento/predicción; [[CyberSentinel - Red Visual de Dos Ramas y Atención|Basak y Han (2024)]] reporta recursos e inferencia en clasificación visual. Estos trabajos impiden generalizar que toda la literatura omite eficiencia. Sus tiempos no equivalen al costo aislado de generar explicaciones.

[[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al|Ardito et al. (2026)]] combina reducción, clasificación estática/dinámica calibrada y auditoría SHAP/LIME. En su benchmark corregido, la fusión temprana obtiene 89,69 % de accuracy multiclase; el híbrido ponderado alcanza recall binario de malware 0,9998, con recall benigno 0,8053. La elección depende de la prioridad operacional. [[RFS-MD - Reglas Explicables y Robustez Android|Alhawari y Ebadinezhad (2026)]] integra scoring por reglas y RXAI, con evaluación de fidelidad por eliminación. Son antecedentes relevantes para precisar la contribución del proyecto.

### 8.2. Precisión de la caracterización multimodal

[[Malware Android con Word2vec y Tráfico de Red - Ullah et al|Ullah et al. (2022, s22155883)]] y [[Malware Android con BERT y Representación Visual - Ullah et al|Ullah et al. (2022, s22186766)]] emplean tráfico Android, características textuales/visuales, votación y SHAP/LIME. No corresponden a stacking sobre cabeceras PE. [[Fusión Multimodal ConvNeXt y Calibración - Alotaibi|Alotaibi (2025)]] usa ConvNeXt-Tiny y atención cruzada en Malimg/Fusion Malware; deja SHAP como trabajo futuro. No se debe atribuirles un benchmark de costo XAI que no reportan.

### 8.3. Alcance y límites de la propuesta adaptativa

[[C-GUARD - Enrutamiento Adaptativo frente a Malware Evasivo|Imran et al. (2026)]] documenta malware evasivo clasificado como benigno con alta confianza. Su enrutamiento selectivo activa un detector de rescate; SHAP es diagnóstico offline. Es un antecedente para analizar control de riesgo, pero no valida nuestros umbrales ni el ahorro de explicaciones. [[De Caja Negra a Caja de Cristal - Revisión XAI - Liu et al|Liu et al. (2025)]] ya considera explicaciones adaptativas en su hoja de ruta.

[[XAI Ciberseguridad Diseño Humano y Edge - Cecchi et al|Cecchi et al. (2026)]] y [[Explicabilidad en CNN - Revisión Sistemática - Tayari y Zaied|Tayari y Zaied (2026)]] señalan carencias de validación humana y protocolos comparables en sus respectivos corpus. El proyecto debe distinguir fidelidad/estabilidad de utilidad humana, costo de clasificación de costo de explicación y resultados propios de expectativas.

**Brecha provisional refinada:** evaluar una integración de selección de características, destilación y explicación adaptativa/caché que reduzca el costo específico de explicar predicciones de malware, comparada con baselines eficientes y con controles explícitos de rendimiento y calidad de explicación. La novedad definitiva exige ampliar y documentar la revisión; estos doce artículos no prueban ausencia universal de propuestas equivalentes.

La arquitectura de referencia sigue siendo: **nivel 1, selección de características; nivel 2, destilación/clasificación; nivel 3, explicación adaptativa**. Los artículos son antecedentes y contrastes, no validación experimental de nuestro sistema.

---

## Referencias Bibliográficas

1. **Al-rimy, B. A. S., et al.** (2025). MIDALF—multimodal image and audio late fusion for malware detection. *EURASIP Journal on Information Security*, 2025, 188. [[MIDALF - Fusión Multimodal de Imagen y Audio para Malware]]
2. **Amponis, G., Radoglou-Grammatikis, P., Lagkas, T., et al.** (2023). Generating full-stack 5G security datasets: IP-layer and core network persistent PDU session attacks. *AEU - International Journal of Electronics and Communications*, 171, 154913. [[Generación de Datasets de Seguridad 5G - Amponis et al]]
3. **Anand, A., Rani, S., Anand, D., Aljahdali, H. M., & Kerr, D.** (2021). An Efficient CNN-Based Deep Learning Model to Detect Malware Attacks (CNN-DMA) in 5G-IoT Healthcare Applications. *Sensors*, 21(19), 6346. [[CNN-DMA - Modelo Ligero para Detección de Malware en IoT-5G]]
4. **Arp, D., Spreitzenbarth, M., Huebner, M., Wressnegger, C., & Rieck, K.** (2014). DREBIN: Effective and Explainable Detection of Android Malware in Your Pocket. *NDSS 2014*. [[DREBIN - Detección y Explicabilidad de Malware Android]]
5. **Awan, M. J., Masood, O. A., Mohammed, M. A., et al.** (2021). Image-Based Malware Classification Using VGG19 Network and Spatial Convolutional Attention. *Electronics*, 10(19), 2444. [[SACNN - Clasificación de Imágenes de Malware con VGG19 y Atención Espacial]]
6. **Baghirov, E.** (2025). A comprehensive investigation into robust malware detection with explainable AI. *Cyber Security and Applications*, 3, 100072. [[Investigación Comprehensiva Detección de Malware con XAI]]
7. **Chaganti, R., Ravi, V., & Pham, T. D.** (2022). Image-Based Malware Representation Approach With EfficientNet Convolutional Neural Networks for Effective Malware Classification. *Journal of Information Security and Applications*, 69, 103306. [[EfficientNet CNN para Clasificación de Malware Basada en Imágenes]]
8. **Chimeleze, C. U., Jamil, N., Alturki, N., & Zain, Z. M.** (2024). A Lightweight malware detection technique based on hybrid fuzzy simulated annealing clustering in Android apps. *Egyptian Informatics Journal*, 28, 100560. [[Detección Ligera de Malware Android con FCMSA y LightGBM]]
9. **Data Mining and Knowledge Discovery, Springer.** (2025). MIRACLE: Malware image recognition and classification by layered extraction. *Data Mining and Knowledge Discovery*, 39, 1078. [[MIRACLE - Reconocimiento de Imágenes de Malware por Extracción en Capas]]
10. **Electronics, MDPI.** (2023). Mitigating the Risks of Malware Attacks with Deep Learning Techniques. *Electronics*, 12(14), 3166. [[Mitigación de Riesgos de Malware con Deep Learning]]
11. **Gaber, M. G., Ahmed, M., & Janicke, H.** (2024). Malware Detection with Artificial Intelligence: A Systematic Literature Review. *ACM Computing Surveys*, 56(7), Article 185. [[Revisión Sistemática de Detección de Malware con IA - Gaber et al]]
12. **Gibert, D., Mateu, C., & Planes, J.** (2020). The rise of machine learning for detection and classification of malware: Research developments, trends and challenges. *Journal of Network and Computer Applications*, 153, 102526. [[Evolución del Machine Learning en Detección de Malware - Gibert et al]]
13. **Guan, X., & Zhang, G.** (2025). A Malware Classification Method Based on Knowledge Distillation and Feature Fusion. *IEEE Access*, 13. [[MC-KDFF - Clasificación de Malware con Destilación de Conocimiento y Fusión]]
14. **Hemdan, E.E.-D., Alshathri, S., Elwahsh, H., Ghoneim, O.A., & Sayed, A.** (2025). MAL-XSEL: Enhancing industrial web malware detection with an explainable stacking ensemble model. *Processes*, 13(5), 1329. [[MAL-XSEL Framework]]
15. **Journal of King Saud University - Computer and Information Sciences.** (2024). AFA-MalGAN: adaptive adversarial sample generation for high-dimensional malware features via constrained manifold optimization. *JKSUCIS*. [[AFA-MalGAN - Generación Adversarial Adaptativa con Optimización de Variedades]]
16. **Kumar, S., Janet, B., & Neelakantan, S.** (2024). IMCNN: Intelligent Malware Classification using Deep Convolution Neural Networks as Transfer learning and ensemble learning in honeypot enabled organizational network. *Computer Communications*, 216, 16–33. [[IMCNN - Clasificación Inteligente de Malware con CNNs y Ensembles]]
17. **Manthena, S. et al.** (2025). Explainable Artificial Intelligence (XAI) for Malware Analysis: A Survey of Techniques, Applications, and Open Challenges. *arXiv:2409.13723v2*. [[XAI for Malware Analysis Survey]]
18. **Nazim, S., et al.** (2025). Multimodal malware classification using proposed ensemble deep neural network framework. *Scientific Reports*, 15, 96203. [[Ensemble Deep Neural Network Multimodal para Malware]]
19. **Ni, J., Huang, K., et al.** (2020). Analysis of Malware Communities Using Multi-Modal Features. *IEEE Access*, 8, 9076000. [[Análisis de Comunidades de Malware con Características Multimodales]]
20. **Panda, P., Kumar C U, O., Marappan, S., et al.** (2023). Transfer Learning for Image-Based Malware Detection for IoT. *Sensors*, 23(6), 3253. [[Transfer Learning para Detección de Malware Basada en Imágenes en IoT]]
21. **Rahali, A., Lashkari, A. H., et al.** (2020). DIDroid: Android Malware Classification and Characterization Using Deep Image Learning. *ACM ICCNS '20*, 11–17. [[DIDroid - Clasificación de Malware Android con Deep Image Learning]]
22. **Ravi, V., & Alazab, M.** (2023). Attention-based convolutional neural network deep learning approach for robust malware classification. *Computational Intelligence*, 39(4), 582–604. [[CNN Basada en Atención para Clasificación Robusta de Malware - Ravi y Alazab]]
23. **Remote Sensing, MDPI.** (2022). An Improved End-to-End Multi-Target Tracking Method Based on Transformer Self-Attention. *Remote Sensing*, 14(24), 6354. [[Seguimiento Multi-Objetivo con Transformer y Auto-Atención]]
24. **Saqib, M., Mahdavifar, S., Fung, B.C.M., & Charland, P.** (2024). A Comprehensive Analysis of Explainable AI for Malware Hunting. *ACM Computing Surveys*, 56(12), Article 314. [[ACM Computing Survey (3677374)]]
25. **Sun, S., Zhang, T., Wang, Y., et al.** (2023). Attention-Based Cross-Modal CNN Using Non-Disassembled Files for Malware Classification. *IEEE Access*, 11, 25298–25310. [[Attention-Based Cross-Modal CNN - Detección de Malware sin Desensamblado]]
26. **Thompson, S., Malhotra, R., Chen, M., Evans, C., & El-Sayed, A.** (2025). Explainable AI in Malware Detection. [[XAI en Detección de Malware - Thompson et al]]
27. **Vásquez Berríos, S., et al.** (2025). Systematic Review: Malware Detection and Classification in Cybersecurity. *Applied Sciences*, 15(14), 7747. [[Revisión Sistemática de Detección de Malware - Vásquez Berríos et al]] ⭐ *(Profesor Correferente PUCV)*
28. **World Electric Vehicle Journal, MDPI.** (2024). An Algorithmic Study of Transformer-Based Road Scene Segmentation in Autonomous Driving. *WEVJ*, 15(11), 516. [[Segmentación de Escenas Basada en Transformers y Restricciones de Tiempo Real]]
29. **Xiao, X., Zhang, S., Mercaldo, F., Hu, G., & Sangaiah, A. K.** (2022). Efficient Deep Learning Network With Multi-Streams for Android Malware Family Classification. *IEEE TII / Access*. [[Multi-Stream CNN para Clasificación de Familias de Malware Android]]
30. **Zhang, D., Song, Y., Xiang, Q., & Wang, Y.** (2025). Imcmkcnn: A lightweight convolutional neural network with multi-scale kernels for image-based malware classification. *Alexandria Engineering Journal*, 111, 203–220. [[IMCMKCNN - CNN Ligera Multi-Escala para Malware]]
31. **Applied Sciences, MDPI.** (2024). Examining the Performance of Various Pretrained Convolutional Neural Network Models in Malware Detection. *Applied Sciences*, 14(6), 2614. [[Evaluación de Modelos CNN Preentrenados en Detección de Malware]]

---

> [!NOTE]
> La base previa contiene 31 fichas. El 4 de octubre de 2026 se añadieron 12 fichas MDPI revisadas con PDF local, alcanzando **43 fichas de artículos**. La verificación de esta incorporación no se extiende automáticamente a los 31 antecedentes anteriores. Las precisiones de la sección 8 prevalecen para la siguiente redacción sobre caracterizaciones históricas incompatibles.

> [!TIP]
> Para navegar la red completa de conceptos, modelos y datasets relacionados, consulta el [[Seminario de Título - MOC]].

### Referencias incorporadas desde texto completo (MDPI)

- Kim, G., Yoon, D., Kwak, N., & Lee, B. (2026). Representation-Centric Approach for Android Malware Classification: Interpretability-Driven Feature Engineering on Function Call Graphs. *Applied Sciences*, 16(6), 2670. https://doi.org/10.3390/app16062670 [[Ingeniería de Características Explicable sobre FCG - Kim et al]]
- Alotaibi, B. (2025). Multimodal Deep Learning Fusion for Accurate and Explainable Malware Family Classification. *Applied Sciences*, 15(21), 11635. https://doi.org/10.3390/app152111635 [[Fusión Multimodal ConvNeXt y Calibración - Alotaibi]]
- Ullah, F., Alsirhani, A., Alshahrani, M. M., Alomari, A., Naeem, H., & Shah, S. A. (2022). Explainable Malware Detection System Using Transformers-Based Transfer Learning and Multi-Model Visual Representation. *Sensors*, 22(18), 6766. https://doi.org/10.3390/s22186766 [[Malware Android con BERT y Representación Visual - Ullah et al]]
- Ullah, F., Ullah, S., Naeem, M. R., Mostarda, L., Rho, S., & Cheng, X. (2022). Cyber-Threat Detection System Using a Hybrid Approach of Transfer Learning and Multi-Model Image Representation. *Sensors*, 22(15), 5883. https://doi.org/10.3390/s22155883 [[Malware Android con Word2vec y Tráfico de Red - Ullah et al]]
- Cannarile, A., Dentamaro, V., Galantucci, S., Iannacone, A., Impedovo, D., & Pirlo, G. (2022). Comparing Deep Learning and Shallow Learning Techniques for API Calls Malware Prediction: A Study. *Applied Sciences*, 12(3), 1645. https://doi.org/10.3390/app12031645 [[Comparación ML y DL sobre Llamadas API - Cannarile et al]]
- Liu, X., Huang, D., Yao, J., Dong, J., Song, L., Wang, H., Yao, C., & Chu, W. (2025). From Black Box to Glass Box: A Practical Review of Explainable Artificial Intelligence (XAI). *AI*, 6(11), 285. https://doi.org/10.3390/ai6110285 [[De Caja Negra a Caja de Cristal - Revisión XAI - Liu et al]]
- Cecchi, G., Benelli, F., Caronna, M., Palma, G., & Rizzo, A. (2026). Connecting the Dots: A Systematic Literature Review of Explainable AI, Cybersecurity, Human-Centered Design and Edge Computing. *Journal of Cybersecurity and Privacy*, 6(3), 91. https://doi.org/10.3390/jcp6030091 [[XAI Ciberseguridad Diseño Humano y Edge - Cecchi et al]]
- Tayari, Z., & Zaied, M. (2026). From Black Box to Clarity: A Systematic Review of Explainability Methods in Deep Convolutional Neural Networks. *Machine Learning and Knowledge Extraction*, 8(8), 220. https://doi.org/10.3390/make8080220 [[Explicabilidad en CNN - Revisión Sistemática - Tayari y Zaied]]
- Ardito, C., Loseto, G., Di Pietro, R., Epicoco, N., & Massaro, A. (2026). An Explainable Hybrid Pipeline for Malware Classification: Benchmark Construction, Feature Reduction, and Security-Oriented Evaluation. *Journal of Cybersecurity and Privacy*, 6(3), 105. https://doi.org/10.3390/jcp6030105 [[Pipeline Híbrido Explicable y Benchmark sin Fuga - Ardito et al]]
- Imran, M., Al-Essa, M., Franchini, F., & Pirlo, G. (2026). C-GUARD: Context-Adaptive Conformal Gating for Improving Robustness Against Evasive Windows PE Malware. *Future Internet*, 18(8), 431. https://doi.org/10.3390/fi18080431 [[C-GUARD - Enrutamiento Adaptativo frente a Malware Evasivo]]
- Basak, M., & Han, M.-M. (2024). CyberSentinel: A Transparent Defense Framework for Malware Detection in High-Stakes Operational Environments. *Sensors*, 24(11), 3406. https://doi.org/10.3390/s24113406 [[CyberSentinel - Red Visual de Dos Ramas y Atención]]
- Alhawari, A., & Ebadinezhad, S. (2026). AI-Driven Rule-Based Feature Scoring for Explainable and Adversarially Robust Android Malware Detection. *Electronics*, 15(10), 2167. https://doi.org/10.3390/electronics15102167 [[RFS-MD - Reglas Explicables y Robustez Android]]
