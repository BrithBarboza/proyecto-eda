# 🧠 Exploratory Data Analysis (EDA) — Productos Limpios

Proyecto de análisis exploratorio de datos (EDA) de la tienda Aurelion desarrollado en Python.

## 📋 Descripción
Este análisis evalúa un conjunto de datos de productos (`productos_limpios.xlsx`), calculando estadísticas básicas, identificando distribuciones de datos (Normal, Sesgada, Bimodal, etc.), correlaciones y outliers.  
Genera automáticamente un reporte en formato **Markdown** y gráficos univariados.

## 📂 Estructura
├── data/ # Archivo fuente
├── eda_output/ # Resultados y gráficos generados
├── eda.py # Script principal de análisis
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto


## 🚀 Ejecución
1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/proyecto-eda.git
   cd proyecto-eda

2. Instala dependencias:
pip install -r requirements.txt

3. Ejecuta el script:
python eda.py

4. Revisa los resultados en eda_output/EDA_report.md.
📊 Ejemplo de resultados
Clasificación de distribuciones (Normal, Sesgada, Uniforme, etc.)
Estadísticas descriptivas (Media, Mediana, Moda, Desviación estándar)
Detección de outliers (método IQR)
Gráficos de distribución por variable