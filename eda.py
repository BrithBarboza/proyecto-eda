import os
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------------------------------------
# CONFIGURACIÓN BÁSICA
# ---------------------------------------------
INPUT_PATH = "data/productos_limpios.xlsx"
OUTPUT_DIR = "eda_output"
FIG_DIR = os.path.join(OUTPUT_DIR, "figs")
os.makedirs(FIG_DIR, exist_ok=True)

# ---------------------------------------------
# 1️⃣ CARGAR DATASET
# ---------------------------------------------
df = pd.read_excel(INPUT_PATH)
print("Shape:", df.shape)
print(df.dtypes)

# Determinar columnas numéricas
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Columnas numéricas detectadas:", numeric_cols)

# ---------------------------------------------
# 2️⃣ ESTADÍSTICAS BÁSICAS
# ---------------------------------------------
buffer = io.StringIO()
df.info(buf=buffer)
info_text = buffer.getvalue()

# Tabla descriptiva de medidas (para mostrar en el reporte)
descriptive_stats = pd.DataFrame({
    "Medida": ["Media", "Mediana", "Moda", "Desviación estándar"],
    "Comando": [
        "df['columna'].mean()",
        "df['columna'].median()",
        "df['columna'].mode()",
        "df['columna'].std()"
    ],
    "Descripción": [
        "Promedio aritmético",
        "Valor central ordenado",
        "Valor más frecuente",
        "Dispersión promedio"
    ]
})

# Cálculo de estadísticas reales
if len(numeric_cols) > 0:
    basic_stats = df[numeric_cols].agg([
        'mean',
        'median',
        lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan,
        'std',
        'skew',
        'kurt'
    ]).T

    basic_stats.columns = [
        'Media', 'Mediana', 'Moda', 'Desviación estándar', 'Asimetría (skew)', 'Curtosis (kurt)'
    ]
    basic_stats = basic_stats.round(3)
else:
    basic_stats = pd.DataFrame(columns=[
        'Media', 'Mediana', 'Moda', 'Desviación estándar', 'Asimetría (skew)', 'Curtosis (kurt)'
    ])

# ---------------------------------------------
# 3️⃣ CLASIFICACIÓN DE DISTRIBUCIÓN
# ---------------------------------------------
def classify_distribution(series):
    s = series.dropna()
    if len(s) < 5:
        return "Sin datos suficientes"

    skew = s.skew()
    kurt = s.kurt()

    # Detección de número de picos (modos)
    counts, bins = np.histogram(s, bins="auto")
    peaks = np.sum((counts[1:-1] > counts[:-2]) & (counts[1:-1] > counts[2:]))

    if peaks >= 3:
        return "Multimodal"
    elif peaks == 2:
        return "Bimodal"

    # Clasificación por forma
    if abs(skew) < 0.3 and -1 < kurt < 1:
        return "Normal"
    elif skew < -0.3:
        return "Sesgada a la izquierda"
    elif skew > 0.3:
        return "Sesgada a la derecha"

    # Distribución uniforme (frecuencias similares)
    if np.std(counts) < 0.1 * np.mean(counts):
        return "Uniforme"

    return "Indefinida"

if not basic_stats.empty:
    basic_stats["Distribución estimada"] = [
        classify_distribution(df[col]) for col in basic_stats.index
    ]

# ---------------------------------------------
# 4️⃣ CORRELACIONES
# ---------------------------------------------
if len(numeric_cols) > 1:
    pearson = df[numeric_cols].corr(method="pearson")
else:
    pearson = pd.DataFrame()

# ---------------------------------------------
# 5️⃣ OUTLIERS (MÉTODO IQR)
# ---------------------------------------------
outliers = []
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask = (df[col] < lower) | (df[col] > upper)
    outliers.append({
        "Columna": col,
        "Outliers detectados": int(mask.sum()),
        "Porcentaje": round(mask.mean() * 100, 2)
    })
outliers_df = pd.DataFrame(outliers)

# ---------------------------------------------
# 6️⃣ GRÁFICOS UNIVARIADOS
# ---------------------------------------------
for col in numeric_cols:
    plt.figure()
    plt.hist(df[col].dropna(), bins="auto", color="purple", edgecolor="black")
    plt.title(f"Distribución - {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    plt.savefig(os.path.join(FIG_DIR, f"{col}_hist.png"))
    plt.close()

# ---------------------------------------------
# 7️⃣ EXPORTAR RESULTADOS A MARKDOWN
# ---------------------------------------------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "EDA_report.md"), "w", encoding="utf-8") as f:
    f.write(f"# Reporte EDA — {timestamp}\n\n")

    # Exploración general
    f.write("## 📊 Exploración con Pandas\n")
    f.write("Herramientas para exploración y análisis estadístico\n\n")
    f.write("### Resultado de df.info()\n")
    f.write("```\n" + info_text + "\n```\n\n")

    exploracion = pd.DataFrame({
        "Función": [".describe()", ".info()", ".value_counts()", ".groupby().agg()"],
        "Propósito": [
            "Resumen completo",
            "Información general",
            "Frecuencias",
            "Estadísticas agrupadas"
        ],
        "Resultado": [
            "Todas las estadísticas principales",
            "Tipos y valores nulos",
            "Conteo por categoría",
            "Métricas por segmento"
        ]
    })
    f.write(exploracion.to_markdown(index=False))
    f.write("\n\n")

    # Medidas descriptivas
    f.write("## 📈 Medidas descriptivas\n")
    f.write("Resumen numérico de características principales\n\n")
    f.write(descriptive_stats.to_markdown(index=False))
    f.write("\n\n")

    f.write("### Resultados obtenidos por columna\n")
    if not basic_stats.empty:
        f.write(basic_stats.to_markdown())
    else:
        f.write("_No hay columnas numéricas para calcular estadísticas._")
    f.write("\n\n")

    # Tipos de distribuciones
    f.write("## 📉 Tipos de distribuciones de datos\n")
    f.write("Muestran la forma en que se organizan los valores dentro de un conjunto de datos.\n\n")
    f.write("- **Normal**: campana simétrica\n")
    f.write("- **Sesgada a la izquierda**: cola hacia valores pequeños\n")
    f.write("- **Sesgada a la derecha**: cola hacia valores grandes\n")
    f.write("- **Bimodal**: dos picos de frecuencia\n")
    f.write("- **Multimodal**: múltiples picos de frecuencia\n")
    f.write("- **Uniforme**: frecuencias similares\n\n")

    # Interpretación automática
    f.write("### 🧠 Interpretación automática\n")
    if not basic_stats.empty:
        for col, dist in zip(basic_stats.index, basic_stats["Distribución estimada"]):
            if dist == "Indefinida":
                msg = f"- **{col}**: No se detectó una forma de distribución clara (posiblemente uniforme o datos discretos)."
            elif "Sesgada" in dist:
                msg = f"- **{col}**: Distribución {dist.lower()}, los valores se concentran hacia un extremo del rango."
            elif dist == "Bimodal":
                msg = f"- **{col}**: Distribución con dos picos principales, posibles grupos o segmentos en los datos."
            elif dist == "Multimodal":
                msg = f"- **{col}**: Distribución con múltiples picos, sugiere heterogeneidad o subpoblaciones."
            elif dist == "Uniforme":
                msg = f"- **{col}**: Distribución casi uniforme, los valores ocurren con frecuencia similar."
            elif dist == "Normal":
                msg = f"- **{col}**: Distribución normal (campana simétrica)."
            else:
                msg = f"- **{col}**: Distribución {dist.lower()}."
            f.write(msg + "\n")
    else:
        f.write("_No hay datos numéricos para interpretar distribuciones._")
    f.write("\n\n")

    # Correlaciones
    if not pearson.empty:
        f.write("## 📊 Correlaciones (Pearson)\n")
        f.write(pearson.round(3).to_markdown())
    else:
        f.write("## 📊 Correlaciones\n_No se calcularon correlaciones (solo una variable numérica)._")
    f.write("\n\n")

    # Outliers
    f.write("## 📉 Outliers (Método IQR)\n")
    if not outliers_df.empty:
        f.write(outliers_df.to_markdown())
    else:
        f.write("_No se detectaron outliers._")
    f.write("\n\n_Gráficos guardados en carpeta figs/_")

print("✅ EDA completado. Revisa la carpeta eda_output/")
