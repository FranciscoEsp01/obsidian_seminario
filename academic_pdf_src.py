import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
import textwrap
import os

pdf_path = "/Users/franciscoespinoza/Documents/Obsidian Vault/Seminario de Título/Presentacion_Avance_Seminario_XAI_Malware.pdf"

fig_w = 13.333
fig_h = 7.5
dpi = 220

# PUCV Academic Palette
BG_WHITE = "#ffffff"
NAVY_PUCV = "#003366"
BLUE_ACCENT = "#1d4ed8"
BLUE_LIGHT = "#eff6ff"
SLATE_DARK = "#0f172a"
SLATE_BODY = "#334155"
SLATE_MUTED = "#64748b"
BORDER_LIGHT = "#cbd5e1"
CARD_BG = "#f8fafc"
CARD_BG_HOVER = "#f1f5f9"
GREEN_DARK = "#15803d"
AMBER_DARK = "#b45309"
RED_DARK = "#b91c1c"

def base_slide(slide_num, total_slides, section_label, title, subtitle):
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
    fig.patch.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Top institutional header
    ax.text(0.05, 0.950, "PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO", color=NAVY_PUCV, fontsize=9, fontweight='bold', va='center')
    ax.text(0.05, 0.925, f"Escuela de Ingeniería Informática · Seminario de Título · {section_label}", color=SLATE_MUTED, fontsize=8.5, va='center')
    ax.text(0.95, 0.938, f"{slide_num:02d} / {total_slides:02d}", color=NAVY_PUCV, fontsize=9.5, fontweight='bold', fontfamily='sans-serif', ha='right', va='center')
    ax.plot([0.05, 0.95], [0.902, 0.902], color=BORDER_LIGHT, linewidth=0.9)

    # Title & Subtitle
    ax.text(0.05, 0.852, title, color=SLATE_DARK, fontsize=16.5, fontweight='bold', va='center')
    if subtitle:
        ax.text(0.05, 0.812, subtitle, color=SLATE_MUTED, fontsize=9.8, va='center')

    # Footer
    ax.plot([0.05, 0.95], [0.062, 0.062], color=BORDER_LIGHT, linewidth=0.9)
    ax.text(0.05, 0.038, "Autores: Rigoberto Canales Puebla · Francisco Espinoza Vasquez", color=SLATE_MUTED, fontsize=8, va='center')
    ax.text(0.95, 0.038, "Profesores: Pamela Hermosilla Monckton · Sebastian Berrios Vasquez", color=SLATE_MUTED, fontsize=8, ha='right', va='center')

    return fig, ax

def draw_academic_card(ax, x, y, w, h, title, bullets, strip_color=NAVY_PUCV, bg_color=CARD_BG, wrap_w=46):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.005,rounding_size=0.008",
        facecolor=bg_color, edgecolor=BORDER_LIGHT, linewidth=0.9
    )
    ax.add_patch(rect)
    
    # Left solid accent strip
    strip = patches.Rectangle((x, y), 0.005, h, facecolor=strip_color)
    ax.add_patch(strip)
    
    ax.text(x + 0.02, y + h - 0.038, title, color=strip_color, fontsize=10.5, fontweight='bold', va='center')
    
    y_pos = y + h - 0.082
    for b in bullets:
        lines = textwrap.wrap(b, width=wrap_w)
        ax.text(x + 0.02, y_pos, "•", color=strip_color, fontsize=9.5, fontweight='bold', va='top')
        for line in lines:
            ax.text(x + 0.036, y_pos, line, color=SLATE_BODY, fontsize=8.6, va='top')
            y_pos -= 0.023
        y_pos -= 0.012
    return y_pos

def draw_banner_box(ax, x, y, w, h, label, text, border_color=NAVY_PUCV, bg_color="#f8fafc", wrap_w=108):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.006",
        facecolor=bg_color, edgecolor=BORDER_LIGHT, linewidth=0.9
    )
    ax.add_patch(rect)
    strip = patches.Rectangle((x, y), 0.005, h, facecolor=border_color)
    ax.add_patch(strip)

    full_text = f"{label}: {text}" if label else text
    lines = textwrap.wrap(full_text, width=wrap_w)
    
    start_y = y + h*0.5 + (len(lines)-1)*0.011
    for line in lines:
        ax.text(x + 0.018, start_y, line, color=SLATE_DARK, fontsize=8.7, va='center')
        start_y -= 0.022

def draw_academic_table(ax, x, y, w, h, headers, rows, col_weights, align_left_cols=[0, 1]):
    total_w = sum(col_weights)
    col_widths = [w * (cw / total_w) for cw in col_weights]
    
    header_h = 0.042
    curr_y = y + h - header_h
    
    h_bg = patches.Rectangle((x, curr_y), w, header_h, facecolor="#003366", edgecolor=BORDER_LIGHT, linewidth=0.8)
    ax.add_patch(h_bg)
    
    col_x = x
    for idx, (head, cw) in enumerate(zip(headers, col_widths)):
        if idx in align_left_cols:
            ax.text(col_x + 0.012, curr_y + header_h*0.5, head, color=BG_WHITE, fontsize=8.5, fontweight='bold', va='center', ha='left')
        else:
            ax.text(col_x + cw*0.5, curr_y + header_h*0.5, head, color=BG_WHITE, fontsize=8.5, fontweight='bold', va='center', ha='center')
        col_x += cw

    num_rows = len(rows)
    row_h = (curr_y - y) / num_rows
    curr_y -= row_h
    
    for r_idx, row in enumerate(rows):
        is_even = (r_idx % 2 == 0)
        bg = "#ffffff" if is_even else "#f8fafc"
        r_box = patches.Rectangle((x, curr_y), w, row_h, facecolor=bg, edgecolor=BORDER_LIGHT, linewidth=0.5)
        ax.add_patch(r_box)
        
        col_x = x
        for c_idx, (val, cw) in enumerate(zip(row, col_widths)):
            # highlight special cells
            txt_color = SLATE_DARK if c_idx in align_left_cols else SLATE_BODY
            weight = 'normal'
            if "TreeSHAP" in val or "O(TLD" in val:
                txt_color = NAVY_PUCV
                weight = 'bold'
            elif "Ligero" in val or "Completada" in val:
                txt_color = GREEN_DARK
                weight = 'bold'
            elif "Profundo" in val or "Alto costo" in val:
                txt_color = RED_DARK
                weight = 'bold'
                
            if c_idx in align_left_cols:
                ax.text(col_x + 0.012, curr_y + row_h*0.5, val, color=txt_color, fontsize=8.1, fontweight=weight, va='center', ha='left')
            else:
                ax.text(col_x + cw*0.5, curr_y + row_h*0.5, val, color=txt_color, fontsize=8.1, fontweight=weight, va='center', ha='center')
            col_x += cw
        curr_y -= row_h

with PdfPages(pdf_path) as pdf:
    # ----------------------------------------------------
    # SLIDE 1: Portada
    # ----------------------------------------------------
    fig, ax = base_slide(1, 15, "Informe de Avance",
                         "Inteligencia Artificial Explicable (XAI) para la Clasificación de Malware",
                         "Diseño y Validación de un Framework Multinivel para la Optimización del Costo Computacional")
    
    card_hero = patches.FancyBboxPatch(
        (0.08, 0.25), 0.84, 0.50,
        boxstyle="round,pad=0.015,rounding_size=0.015",
        facecolor=CARD_BG, edgecolor=BORDER_LIGHT, linewidth=1.2
    )
    ax.add_patch(card_hero)
    
    strip_hero = patches.Rectangle((0.08, 0.25), 0.007, 0.50, facecolor=NAVY_PUCV)
    ax.add_patch(strip_hero)

    ax.text(0.5, 0.70, "PONTIFICIA UNIVERSIDAD CATÓLICA DE VALPARAÍSO", color=NAVY_PUCV, fontsize=12.5, fontweight='bold', ha='center', va='center')
    ax.text(0.5, 0.66, "Facultad de Ingeniería · Escuela de Ingeniería Informática", color=SLATE_MUTED, fontsize=10, ha='center', va='center')
    ax.plot([0.15, 0.85], [0.62, 0.62], color=BORDER_LIGHT, linewidth=0.9)
    
    # Left column: Authors
    ax.text(0.16, 0.54, "Autores del Proyecto:", color=NAVY_PUCV, fontsize=10, fontweight='bold')
    ax.text(0.16, 0.49, "Rigoberto Ignacio Enrique Canales Puebla", color=SLATE_DARK, fontsize=10.5, fontweight='bold')
    ax.text(0.16, 0.44, "Francisco Ignacio Espinoza Vasquez", color=SLATE_DARK, fontsize=10.5, fontweight='bold')
    
    # Right column: Committee
    ax.text(0.54, 0.54, "Comisión Evaluadora:", color=NAVY_PUCV, fontsize=10, fontweight='bold')
    ax.text(0.54, 0.49, "Profesora Guía: Pamela Hermosilla Monckton", color=SLATE_DARK, fontsize=10)
    ax.text(0.54, 0.44, "Profesor Correferente: Sebastian Berrios Vasquez", color=SLATE_DARK, fontsize=10)

    ax.plot([0.15, 0.85], [0.38, 0.38], color=BORDER_LIGHT, linewidth=0.9)
    ax.text(0.5, 0.31, "Informe de Avance · Seminario de Título · 11 de Septiembre de 2026", color=SLATE_MUTED, fontsize=9.5, ha='center')

    draw_banner_box(ax, 0.08, 0.10, 0.84, 0.095, "Propósito de la Exposición",
                    "Presentar formalmente la fundamentación teórica, revisión sistemática PRISMA, objetivos aprobados y la arquitectura multinivel de optimización computacional.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 2: Contexto y Motivación
    # ----------------------------------------------------
    fig, ax = base_slide(2, 15, "Contexto y Motivación",
                         "Contexto y Motivación de la Investigación",
                         "El crecimiento del malware avanzado y los requerimientos de respuesta en Centros de Operaciones de Seguridad (SOC)")

    draw_academic_card(ax, 0.05, 0.22, 0.43, 0.54, "Evolución y Complejidad del Malware", [
        "Crecimiento acelerado de nuevas variantes con técnicas de polimorfismo, empaquetamiento y evasión activa.",
        "Aparición constante de amenazas de día cero (zero-day) no catalogadas.",
        "Insuficiencia de antivirus tradicionales basados en firmas estáticas.",
        "Adopción masiva de modelos de Machine Learning y Deep Learning.",
        "Tasas de detección empíricas superiores al 99% en entornos de investigación."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.22, 0.43, 0.54, "Realidad Operativa en Centros de Seguridad (SOC)", [
        "Un SOC procesa diariamente cientos de miles de eventos y alertas continuas.",
        "Exigencia estricta de tiempo real: cada milisegundo es crítico para aislar y contener la amenaza.",
        "Sobrecarga de trabajo en los analistas de seguridad frente a falsos positivos (fatiga de alertas).",
        "La precisión predictiva matemática no es suficiente si la latencia del sistema imposibilita la respuesta.",
        "Necesidad de conciliar alta exactitud con mínima sobrecarga computacional."
    ], strip_color=BLUE_ACCENT)

    draw_banner_box(ax, 0.05, 0.095, 0.90, 0.085, "Premisa de Investigación",
                    "La alta precisión de detección es inviable operacionalmente si el tiempo de respuesta colapsa la infraestructura del SOC.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 3: El Problema de la Caja Negra
    # ----------------------------------------------------
    fig, ax = base_slide(3, 15, "Definición del Problema",
                         "El Problema de la «Caja Negra» en Ciberseguridad",
                         "Por qué una alerta predictiva aislada es insuficiente para la toma de decisiones operativas")

    draw_academic_card(ax, 0.05, 0.22, 0.43, 0.54, "Límites de la Alerta Predictiva Aislada", [
        "Una etiqueta binaria ('Malware: 99.8%') no aporta explicaciones sobre la naturaleza del ataque.",
        "¿Cuáles llamadas al sistema o cabeceras PE justifican la clasificación?",
        "Imposibilidad de extraer Indicadores de Compromiso (IoCs) inmediatos para la contención.",
        "Falta de trazabilidad para aislar selectivamente procesos o servidores afectados.",
        "Riesgo de falsos positivos que interrumpen servicios comerciales críticos."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.22, 0.43, 0.54, "Decisiones Críticas en Respuesta a Incidentes", [
        "Aislamiento de infraestructura: Desconectar un servidor exige justificación fehaciente.",
        "Auditoría técnica y forense: Obligación de cumplimiento regulatorio y normativas.",
        "Generación de confianza: Los analistas desconfían de alertas opacas sin fundamento.",
        "Reducción de tiempos medios de contención (Mean Time to Respond - MTTR).",
        "La explicabilidad no es un accesorio teórico, sino un requerimiento operacional."
    ], strip_color=BLUE_ACCENT)

    draw_banner_box(ax, 0.05, 0.095, 0.90, 0.085, "Conclusión Operativa",
                    "Comprender la causa técnica de una alerta en un SOC es tan relevante como detectarla oportunamente.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 4: La Paradoja de XAI y Cuello de Botella
    # ----------------------------------------------------
    fig, ax = base_slide(4, 15, "Definición del Problema",
                         "El Cuello de Botella Computacional de las Técnicas XAI",
                         "La sobrecarga algorítmica de SHAP y LIME frente a muestras de malware de alta dimensionalidad")

    draw_academic_card(ax, 0.05, 0.28, 0.43, 0.48, "Métodos Agnósticos Estándar (SHAP y LIME)", [
        "SHAP (Shapley Additive exPlanations): Basado en teoría de juegos cooperativos.",
        "Valores de Shapley: Atribución axiomática local y global matemáticamente fundamentada.",
        "LIME: Aproximación subrogada lineal local mediante perturbaciones sintéticas.",
        "Ambas técnicas son ampliamente recomendadas pero de alto consumo."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.28, 0.43, 0.48, "Complejidad Algorítmica y Escalabilidad", [
        "KernelSHAP exhibe complejidad factorial/exponencial: O(2^n), con n variables.",
        "LIME requiere predecir y evaluar miles de variaciones sintéticas por binario sospechoso.",
        "Los archivos ejecutables poseen cientos o miles de variables (cabeceras PE, APIs).",
        "Explicar una sola muestra toma segundos o minutos: colapso en tiempo real."
    ], strip_color=RED_DARK)

    # Clean academic formula box
    f_box = patches.FancyBboxPatch(
        (0.05, 0.095), 0.90, 0.14,
        boxstyle="round,pad=0.005,rounding_size=0.008",
        facecolor="#eff6ff", edgecolor=NAVY_PUCV, linewidth=1.1
    )
    ax.add_patch(f_box)
    ax.text(0.5, 0.185, "TENSIÓN OPERATIVA PRINCIPAL DE INGENIERÍA", color=NAVY_PUCV, fontsize=10, fontweight='bold', ha='center')
    ax.text(0.5, 0.135, "Alta Precisión Predictiva (ML/DL) + Explicabilidad Profunda Agnóstica = Colapso de Latencia en el SOC",
            color=SLATE_DARK, fontsize=9.8, fontfamily='monospace', ha='center')
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 5: Preguntas de Investigación y Brecha
    # ----------------------------------------------------
    fig, ax = base_slide(5, 15, "Preguntas de Investigación",
                         "Preguntas de Investigación y Brecha en la Literatura",
                         "La carencia de soluciones orientadas a la latencia de explicación y las preguntas que guían el proyecto")

    draw_banner_box(ax, 0.05, 0.63, 0.90, 0.14, "Pregunta General de Investigación",
                    "¿En qué medida es posible reducir el costo computacional de las técnicas de XAI en la clasificación de malware mediante un enfoque multinivel que integre selección de características, destilación de conocimiento y explicabilidad adaptativa sin comprometer la precisión de la detección ni la fidelidad de las explicaciones?",
                    border_color=NAVY_PUCV, bg_color="#f8fafc", wrap_w=108)

    draw_academic_card(ax, 0.05, 0.15, 0.28, 0.44, "PI1: Reducción Dimensional", [
        "¿Cómo influye la selección previa de variables en los tiempos de cómputo de SHAP y LIME al evaluar muestras complejas?"
    ], strip_color=NAVY_PUCV, wrap_w=32)

    draw_academic_card(ax, 0.36, 0.15, 0.28, 0.44, "PI2: Destilación y TreeSHAP", [
        "¿Es viable transferir conocimiento de un ensamble a un modelo más ligero, habilitando TreeSHAP polinomial sin degradar el F1?"
    ], strip_color=BLUE_ACCENT, wrap_w=32)

    draw_academic_card(ax, 0.67, 0.15, 0.28, 0.44, "PI3: Adaptabilidad y Caché", [
        "¿En qué proporción un esquema adaptativo por certidumbre junto a una caché vectorial reduce el costo computacional promedio?"
    ], strip_color=GREEN_DARK, wrap_w=32)

    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 6: Objetivos del Proyecto
    # ----------------------------------------------------
    fig, ax = base_slide(6, 15, "Objetivos del Seminario",
                         "Objetivos del Proyecto de Título",
                         "Alineación metodológica estructurada en tres dimensiones: Estudio, Desarrollo y Validación")

    draw_banner_box(ax, 0.05, 0.65, 0.90, 0.12, "Objetivo General",
                    "Diseñar, construir y validar un framework multinivel para reducir el costo computacional de la XAI en la Clasificación de Malware, con el fin de permitir el uso de modelos transparentes en operaciones de ciberseguridad que exigen respuestas rápidas.",
                    border_color=NAVY_PUCV, wrap_w=112)

    t_headers = ["Dimensión", "ID", "Objetivo Específico", "Entregable Esperado"]
    t_rows = [
        ["Estudio", "OE1", "Revisión sistemática de literatura (SLR) sobre cuellos de botella de XAI en malware.", "Capítulo 3 Marco Teórico (PRISMA)"],
        ["Estudio", "OE2", "Definir marco de referencia para medir costo computacional y utilidad de explicaciones.", "Marco formal de métricas y baselines"],
        ["Desarrollo", "OE3", "Diseñar la arquitectura del framework integrando selección, destilación y adaptabilidad.", "Especificación técnica y diagramas"],
        ["Desarrollo", "OE4", "Construir prototipo funcional que integre los 3 niveles con librerías estándar.", "Prototipo de software ejecutable"],
        ["Validación", "OE5", "Evaluar experimentalmente el sistema en datasets públicos frente a baselines.", "Matriz de resultados y auditoría XAI"]
    ]
    draw_academic_table(ax, 0.05, 0.11, 0.90, 0.50, t_headers, t_rows, [0.15, 0.08, 0.52, 0.25], align_left_cols=[0, 1, 2, 3])

    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 7: Marco Teórico y Revisión PRISMA
    # ----------------------------------------------------
    fig, ax = base_slide(7, 15, "Marco Teórico",
                         "Revisión Sistemática de Literatura (Protocolo PRISMA)",
                         "Rigor metodológico aplicado a la búsqueda y selección en cinco bases de datos científicas")

    draw_academic_card(ax, 0.05, 0.24, 0.43, 0.52, "Bases Científicas Indexadas", [
        "IEEE Xplore Digital Library",
        "Scopus (Elsevier)",
        "ACM Digital Library",
        "ScienceDirect",
        "Web of Science (WoS)",
        "Cadenas de búsqueda booleanas cruzando: XAI + Malware + Costo/Latencia.",
        "Criterio de inclusión: Investigaciones con métricas reproducibles de costo y desempeño."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.24, 0.43, 0.52, "Fases del Protocolo PRISMA", [
        "1. Identificación: Búsqueda exhaustiva en bases de datos y eliminación sistemática de duplicados.",
        "2. Cribado (Screening): Filtrado por título y resumen; exclusión de aplicaciones ajenas a malware o sin XAI.",
        "3. Idoneidad (Eligibility): Evaluación de texto completo; exclusión por falta de métricas de costo/latencia.",
        "4. Inclusión: Síntesis comparativa final de estudios primarios relevantes."
    ], strip_color=BLUE_ACCENT)

    draw_banner_box(ax, 0.05, 0.095, 0.90, 0.10, "Hallazgo Metodológico",
                    "Se constató un sesgo general en la literatura: los autores buscan maximizar exactitud sobre datasets estáticos, omitiendo la sobrecarga computacional de XAI en flujos continuos de monitoreo.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 8: Análisis Comparativo del Estado del Arte
    # ----------------------------------------------------
    fig, ax = base_slide(8, 15, "Estado del Arte",
                         "Análisis Comparativo de Trabajos Relacionados",
                         "Evidencia empírica de las limitaciones operativas reportadas en la literatura referente")

    t_headers = ["Estudio", "Modelos", "Técnicas XAI", "Dataset", "Métricas", "Limitación Crítica"]
    t_rows = [
        ["Ullah et al.", "Stacking Ensemble", "SHAP y LIME", "Binarios PE (Windows)", "Exactitud > 99%", "Alto costo computacional para generar explicaciones continuas."],
        ["Kim et al.", "DL sobre Grafos", "Activación visual", "Ecosistema Android", "Alta precisión en FCG", "Conversión a Grafos de Llamadas exige excesivo cómputo previo."],
        ["Alotaibi", "Fusión Multimodal", "Atención interna", "Tabular PE + Imágenes", "Alta exactitud multiclase", "Arquitectura hipercompleja de alto consumo e inferencia lenta."]
    ]
    draw_academic_table(ax, 0.05, 0.38, 0.90, 0.38, t_headers, t_rows, [0.13, 0.17, 0.15, 0.17, 0.15, 0.23], align_left_cols=[0, 1, 2, 3, 5])

    draw_academic_card(ax, 0.05, 0.11, 0.90, 0.23, "Brechas Estructurales Identificadas", [
        "1. Exceso de complejidad: Modelos profundos pesados que operan como cajas negras difícilmente auditables.",
        "2. Costosas transformaciones de datos: Convertir código a imágenes o grafos añade retardos previos inaceptables.",
        "3. Omisión del costo explicativo: Ningún estudio integra mecanismos de optimización activa en tiempo de respuesta."
    ], strip_color=NAVY_PUCV, wrap_w=100)

    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 9: Arquitectura del Framework Multinivel
    # ----------------------------------------------------
    fig, ax = base_slide(9, 15, "Propuesta de Solución",
                         "Arquitectura del Framework Multinivel Propuesto",
                         "Estructura modular encadenada en tres niveles para abatir el costo computacional")

    steps = [
        ("Nivel 1: Selección de Características", 
         "Filtro por importancia (Tree-based: Random Forest/LightGBM) y algoritmos metaheurísticos (WOA).\nReduce el espacio factorial de O(2^n) antes de la inferencia.", NAVY_PUCV),
        ("Nivel 2: Clasificación y Destilación de Conocimiento", 
         "Modelo Profesor (Stacking Ensemble) transferido a Modelo Estudiante (LightGBM).\nPermite inferencia veloz y cálculo exacto de TreeSHAP en tiempo polinomial O(TLD^2).", BLUE_ACCENT),
        ("Nivel 3: Explicabilidad Adaptativa y Motor de Caché", 
         "Caché vectorial indexada (delta=0.03) para O(1). Enrutamiento por certidumbre P(y):\nLigero (Top-5 TreeSHAP), Estándar (TreeSHAP Completo) o Profundo (TreeSHAP + LIME).", GREEN_DARK)
    ]

    y_p = 0.58
    for idx, (s_title, s_desc, s_color) in enumerate(steps):
        p_box = patches.FancyBboxPatch(
            (0.08, y_p), 0.84, 0.15,
            boxstyle="round,pad=0.008,rounding_size=0.01",
            facecolor="#f8fafc", edgecolor=BORDER_LIGHT, linewidth=1.1
        )
        ax.add_patch(p_box)
        
        strip = patches.Rectangle((0.08, y_p), 0.006, 0.15, facecolor=s_color)
        ax.add_patch(strip)
        
        num_circ = patches.Circle((0.13, y_p + 0.075), 0.032, facecolor=s_color)
        ax.add_patch(num_circ)
        ax.text(0.13, y_p + 0.075, str(idx+1), color=BG_WHITE, fontsize=11, fontweight='bold', ha='center', va='center')
        ax.text(0.18, y_p + 0.105, s_title, color=s_color, fontsize=10.5, fontweight='bold', va='center')
        ax.text(0.18, y_p + 0.045, s_desc, color=SLATE_BODY, fontsize=8.5, va='center')
        
        if idx < 2:
            ax.annotate('', xy=(0.5, y_p - 0.03), xytext=(0.5, y_p),
                        arrowprops=dict(facecolor=NAVY_PUCV, edgecolor='none', width=1.5, headwidth=6))
        y_p -= 0.18

    draw_banner_box(ax, 0.08, 0.10, 0.84, 0.085, "Principio Rector",
                    "Desacoplar la alta capacidad de detección del clasificador del costo computacional de su explicabilidad.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 10: Nivel 1: Selección de Características
    # ----------------------------------------------------
    fig, ax = base_slide(10, 15, "Desarrollo Metodológico",
                         "Nivel 1: Selección Inteligente de Características",
                         "Reducción dimensional previa a la fase de explicación para acotar el espacio factorial")

    draw_academic_card(ax, 0.05, 0.24, 0.43, 0.52, "El Desafío Factorial", [
        "Muestras de malware con cientos o miles de variables (APIs, cabeceras PE, permisos).",
        "KernelSHAP escala de forma combinatoria exponencial O(2^n).",
        "Variables irrelevantes aumentan la varianza de las perturbaciones en LIME.",
        "Reducir n antes de la explicabilidad disminuye directamente el tiempo de cálculo.",
        "Eliminación sistemática de atributos redundantes, colineales o con varianza nula."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.24, 0.43, 0.52, "Estrategia Híbrida de Dos Vías", [
        "1. Filtrado rápido por árboles de decisión (Random Forest y LightGBM):",
        "   - Importancia por ganancia (gain) y número de divisiones (split).",
        "   - Poda de variables con nulo aporte discriminativo en microsegundos.",
        "2. Optimización Metaheurística:",
        "   - Whale Optimization Algorithm (WOA) y Algoritmos Genéticos.",
        "   - Función multiobjetivo: Minimizar variables reteniendo el F1-Score."
    ], strip_color=BLUE_ACCENT)

    draw_banner_box(ax, 0.05, 0.095, 0.90, 0.10, "Aporte al Framework",
                    "Acota el espacio de búsqueda matemático antes de la inferencia, aliviando de forma decisiva la carga computacional de los niveles siguientes.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 11: Nivel 2: Stacking y Destilación
    # ----------------------------------------------------
    fig, ax = base_slide(11, 15, "Desarrollo Metodológico",
                         "Nivel 2: Clasificación y Destilación de Conocimiento",
                         "Desacoplamiento entre la complejidad del modelo y la velocidad de su auditoría XAI")

    draw_academic_card(ax, 0.05, 0.30, 0.43, 0.46, "Modelo Profesor (Stacking Ensemble)", [
        "Ensamble heterogéneo apilado que combina múltiples clasificadores base.",
        "Alta capacidad de generalización frente a malware polimórfico y empaquetado.",
        "Establece el techo de rendimiento predictivo del proyecto (> 99% exactitud).",
        "Limitación: Auditar directamente un ensamble multicapa con XAI colapsa la CPU."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.30, 0.43, 0.46, "Modelo Estudiante (LightGBM Ligero)", [
        "Knowledge Distillation: Transfiere probabilidades suaves y representaciones.",
        "El estudiante retiene la frontera de decisión con rápida inferencia en CPU.",
        "Habilita el algoritmo analítico especializado TreeSHAP.",
        "Calcula valores de Shapley exactos en tiempo polinomial sin muestreos pesados."
    ], strip_color=BLUE_ACCENT)

    f_box = patches.FancyBboxPatch(
        (0.05, 0.095), 0.90, 0.16,
        boxstyle="round,pad=0.005,rounding_size=0.008",
        facecolor="#eff6ff", edgecolor=NAVY_PUCV, linewidth=1.1
    )
    ax.add_patch(f_box)
    ax.text(0.5, 0.20, "REDUCCIÓN CUANTITATIVA DE COMPLEJIDAD ALGORÍTMICA", color=NAVY_PUCV, fontsize=10, fontweight='bold', ha='center')
    ax.text(0.5, 0.14, "KernelSHAP: O(2^n) [Exponencial]   ====>   TreeSHAP en LightGBM: O(T · L · D^2) [Polinomial]",
            color=SLATE_DARK, fontsize=10.5, fontfamily='monospace', ha='center')
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 12: Nivel 3: Explicabilidad Adaptativa y Caché
    # ----------------------------------------------------
    fig, ax = base_slide(12, 15, "Desarrollo Metodológico",
                         "Nivel 3: Explicabilidad Adaptativa y Motor de Caché",
                         "Asignación dinámica de recursos de cómputo según certidumbre y similitud vectorial")

    t_headers = ["Régimen", "Rango Confianza P(y)", "Método XAI Despachado", "Acción Operativa en el SOC"]
    t_rows = [
        ["Ligero", "P(y) >= 0.95", "Top-5 TreeSHAP vectorizado", "Triage instantáneo en alertas evidentes sin calcular miles de variables."],
        ["Estándar", "0.80 <= P(y) < 0.95", "TreeSHAP completo", "Auditoría técnica ordinaria ante software empaquetado o firmas ambiguas."],
        ["Profundo", "P(y) < 0.80", "TreeSHAP + LIME", "Revisión forense prioritaria cruzada de muestras limítrofes críticas."]
    ]
    draw_academic_table(ax, 0.05, 0.44, 0.90, 0.32, t_headers, t_rows, [0.15, 0.22, 0.28, 0.35], align_left_cols=[0, 1, 2, 3])

    draw_academic_card(ax, 0.05, 0.10, 0.43, 0.29, "Caché de Firmas Explicativas", [
        "Las campañas masivas generan miles de variantes casi idénticas.",
        "Si distancia coseno delta < 0.03 respecto a un vector previo:",
        "Retorna la explicación almacenada en tiempo constante O(1)."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.10, 0.43, 0.29, "Calibración de Umbrales", [
        "Umbrales basales: 0.95 y 0.80 basados en calibración de gradient boosting.",
        "Ajuste formal en validación con Reliability Diagrams.",
        "Optimiza el compromiso entre reducción de latencia y falsos positivos."
    ], strip_color=BLUE_ACCENT)

    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 13: Diseño Experimental y Baselines
    # ----------------------------------------------------
    fig, ax = base_slide(13, 15, "Diseño Experimental",
                         "Diseño Experimental, Datasets y Baselines",
                         "Marco de contraste empírico tripartito sobre conjuntos de datos públicos")

    draw_academic_card(ax, 0.05, 0.44, 0.43, 0.32, "Datasets de Prueba", [
        "CICMalDroid 2020 (Android): > 17.000 muestras (Adware, Banking, Ransomware, Riskware, Benigno); estático y dinámico.",
        "ClaMP Dataset (Windows): Binarios PE con 68 características de cabeceras, tablas y secciones.",
        "Partición estratificada: 70% Train, 15% Val, 15% Test."
    ], strip_color=NAVY_PUCV)

    draw_academic_card(ax, 0.52, 0.44, 0.43, 0.32, "Métricas Tripartitas", [
        "1. Rendimiento: Accuracy, Macro F1, AUC-ROC.",
        "2. Eficiencia: Latencia t_inf y t_exp (ms), RAM pico (MB), Throughput y Speedup S = t_baseline / t_framework.",
        "3. Calidad XAI: Fidelidad (perturbación) y Estabilidad sintáctica."
    ], strip_color=BLUE_ACCENT)

    t_headers = ["Configuración", "Clasificador", "Método XAI", "Selección Features"]
    t_rows = [
        ["Baseline 1 (Tradicional)", "LightGBM / Random Forest", "KernelSHAP / LIME estándar", "Sin selección (todas)"],
        ["Baseline 2 (Estado del Arte)", "Stacking Ensemble", "TreeSHAP / LIME directo", "Selección estática convencional"],
        ["Propuesta (Multinivel)", "Modelo Destilado Ligero", "XAI Adaptativo + TreeSHAP / Caché", "Selección Metaheurística / Importancia"]
    ]
    draw_academic_table(ax, 0.05, 0.10, 0.90, 0.30, t_headers, t_rows, [0.25, 0.25, 0.25, 0.25], align_left_cols=[0, 1, 2, 3])

    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 14: Plan de Trabajo y Estado de Avance
    # ----------------------------------------------------
    fig, ax = base_slide(14, 15, "Plan de Trabajo",
                         "Plan de Trabajo y Estado de Avance Actual",
                         "Distribución temporal y avance cronológico en los dos semestres lectivos")

    draw_academic_card(ax, 0.05, 0.24, 0.43, 0.52, "Avance Consolidado (Semestre I)", [
        "T1: Planteamiento del problema y contexto en SOCs [Completada].",
        "T2: Revisión sistemática de literatura bajo PRISMA [Completada].",
        "T3: Formulación de objetivos y alcance formal [Completada].",
        "T4: Diseño metodológico, métricas y baselines [En curso / Cierre].",
        "Cumplimiento pleno de los Objetivos Específicos OE1 y OE2."
    ], strip_color=GREEN_DARK)

    draw_academic_card(ax, 0.52, 0.24, 0.43, 0.52, "Próximos Hitos (Cierre Semestre I & II)", [
        "T5 (Octubre 2026): Limpieza, preprocesamiento y EDA de datasets.",
        "T6 (Noviembre 2026): Implementación empírica de Baselines 1 y 2.",
        "H1 (Diciembre 2026): Entrega formal del Informe de Seminario de Título.",
        "Semestre II (2027-1):",
        "  - Desarrollo del framework multinivel (T7-T10) [OE4].",
        "  - Validación experimental y auditoría XAI (T11-T13) [OE5].",
        "  - Redacción final, memoria y examen de título (T14-T15, H2)."
    ], strip_color=NAVY_PUCV)

    draw_banner_box(ax, 0.05, 0.095, 0.90, 0.10, "Cumplimiento de Cronograma",
                    "La investigación avanza en estricta conformidad a la Carta Gantt planificada para el período 2026-2027 de titulación.")
    pdf.savefig(fig)
    plt.close()

    # ----------------------------------------------------
    # SLIDE 15: Conclusiones y Ronda de Preguntas
    # ----------------------------------------------------
    fig, ax = base_slide(15, 15, "Conclusiones",
                         "Conclusiones del Avance y Ronda de Preguntas",
                         "Síntesis del aporte conceptual y apertura del diálogo con la comisión evaluadora")

    draw_academic_card(ax, 0.05, 0.38, 0.43, 0.38, "Síntesis del Aporte", [
        "Se formalizó la brecha de inviabilidad operativa de XAI en SOCs.",
        "Se diseñó una arquitectura multinivel integral que ataca el costo en 3 frentes:",
        "  • Reducción previa de dimensión (Nivel 1).",
        "  • Destilación hacia modelos compatibles con TreeSHAP (Nivel 2).",
        "  • Explicabilidad adaptativa con caché de firmas O(1) (Nivel 3)."
    ], strip_color=GREEN_DARK)

    draw_academic_card(ax, 0.52, 0.38, 0.43, 0.38, "Impacto en Ciberseguridad", [
        "Viabiliza la adopción de modelos transparentes en monitoreo continuo.",
        "Provee explicaciones técnicas ágiles preservando la calidad forense.",
        "Bases teóricas y metodológicas sólidas para la fase de laboratorio experimental."
    ], strip_color=NAVY_PUCV)

    qa_card = patches.FancyBboxPatch(
        (0.05, 0.095), 0.90, 0.24,
        boxstyle="round,pad=0.01,rounding_size=0.012",
        facecolor=CARD_BG, edgecolor=BORDER_LIGHT, linewidth=1.1
    )
    ax.add_patch(qa_card)
    qa_strip = patches.Rectangle((0.05, 0.095), 0.007, 0.24, facecolor=NAVY_PUCV)
    ax.add_patch(qa_strip)

    ax.text(0.5, 0.25, "¡MUCHAS GRACIAS POR SU ATENCIÓN!", color=NAVY_PUCV, fontsize=15, fontweight='bold', ha='center')
    ax.text(0.5, 0.18, "Q&A · Abrimos la ronda de preguntas y comentarios de la comisión", color=SLATE_DARK, fontsize=11, ha='center')
    ax.text(0.5, 0.13, "Profesores: Pamela Hermosilla Monckton & Sebastian Berrios Vasquez", color=SLATE_MUTED, fontsize=9.5, ha='center')

    pdf.savefig(fig)
    plt.close()

print("Academic PDF generated successfully:", pdf_path)