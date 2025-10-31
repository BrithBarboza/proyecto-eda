# 🧠 Exploratory Data Analysis (EDA) — Productos Limpios

Proyecto de **Análisis Exploratorio de Datos (EDA)** desarrollado en **Python** para la tienda **Aurelion**.  
Este análisis examina el conjunto de productos, identificando patrones, distribuciones estadísticas, correlaciones y valores atípicos (outliers).

---

## 📋 Descripción

El script `eda.py` realiza un análisis completo sobre el archivo **`productos_limpios.xlsx`**, generando de forma automática un reporte en **Markdown** con:

- 📊 **Estadísticas descriptivas**: media, mediana, moda y desviación estándar.  
- 📈 **Clasificación de distribuciones**: Normal, Sesgada, Uniforme, Bimodal y Multimodal.  
- 🔗 **Correlaciones** entre variables numéricas (Pearson).  
- ⚠️ **Detección de outliers** mediante el método del rango intercuartílico (IQR).  
- 🖼️ **Visualizaciones** de histogramas para cada variable numérica.

Todo el proceso queda documentado automáticamente en `eda_output/EDA_report.md`, junto con los gráficos generados en `eda_output/figs/`.

---

## 📂 Estructura del proyecto

proyecto-eda/
├── data/ # Archivo fuente (productos_limpios.xlsx)
├── eda_output/ # Resultados del análisis y gráficos generados
│ ├── EDA_report.md
│ └── figs/
├── eda.py # Script principal de análisis exploratorio
├── requirements.txt # Dependencias necesarias
└── README.md # Documentación del proyecto
---

## 🚀 Ejecución
1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/proyecto-eda.git
   cd proyecto-eda

2. Instala dependencias:
   ```bash
    pip install -r requirements.txt

3. Ejecuta el script:
   ```bash
   python eda.py

4️. Revisa los resultados generados en:
    ```bash
    📄 eda_output/EDA_report.md
    🖼️ eda_output/figs/

📊 Ejemplo de resultados
Clasificación de distribuciones (Normal, Sesgada, Uniforme, etc.)
Estadísticas descriptivas (Media, Mediana, Moda, Desviación estándar)
Detección de outliers (método IQR)
Gráficos de distribución por variable


🧠 Autor
👩‍💻 Brith Barboza
🔗 GitHub: BrithBarboza