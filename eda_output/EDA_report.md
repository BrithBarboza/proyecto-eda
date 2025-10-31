# Reporte EDA — 2025-10-30 19:03:46

## 📊 Exploración con Pandas
Herramientas para exploración y análisis estadístico

### Resultado de df.info()
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 4 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id_producto      100 non-null    int64 
 1   nombre_producto  100 non-null    object
 2   categoria        100 non-null    object
 3   precio_unitario  100 non-null    int64 
dtypes: int64(2), object(2)
memory usage: 3.3+ KB

```

| Función          | Propósito              | Resultado                          |
|:-----------------|:-----------------------|:-----------------------------------|
| .describe()      | Resumen completo       | Todas las estadísticas principales |
| .info()          | Información general    | Tipos y valores nulos              |
| .value_counts()  | Frecuencias            | Conteo por categoría               |
| .groupby().agg() | Estadísticas agrupadas | Métricas por segmento              |

## 📈 Medidas descriptivas
Resumen numérico de características principales

| Medida              | Comando                | Descripción            |
|:--------------------|:-----------------------|:-----------------------|
| Media               | df['columna'].mean()   | Promedio aritmético    |
| Mediana             | df['columna'].median() | Valor central ordenado |
| Moda                | df['columna'].mode()   | Valor más frecuente    |
| Desviación estándar | df['columna'].std()    | Dispersión promedio    |

### Resultados obtenidos por columna
|                 |   Media |   Mediana |   Moda |   Desviación estándar |   Asimetría (skew) |   Curtosis (kurt) | Distribución estimada   |
|:----------------|--------:|----------:|-------:|----------------------:|-------------------:|------------------:|:------------------------|
| id_producto     |   50.5  |      50.5 |      1 |                29.011 |              0     |            -1.2   | Bimodal                 |
| precio_unitario | 2718.55 |    2516   |   2512 |              1381.63  |              0.152 |            -1.165 | Indefinida              |

## 📉 Tipos de distribuciones de datos
Muestran la forma en que se organizan los valores dentro de un conjunto de datos.

- **Normal**: campana simétrica
- **Sesgada a la izquierda**: cola hacia valores pequeños
- **Sesgada a la derecha**: cola hacia valores grandes
- **Bimodal**: dos picos de frecuencia
- **Multimodal**: múltiples picos de frecuencia
- **Uniforme**: frecuencias similares

### 🧠 Interpretación automática
- **id_producto**: Distribución con dos picos principales, posibles grupos o segmentos en los datos.
- **precio_unitario**: No se detectó una forma de distribución clara (posiblemente uniforme o datos discretos).


## 📊 Correlaciones (Pearson)
|                 |   id_producto |   precio_unitario |
|:----------------|--------------:|------------------:|
| id_producto     |         1     |            -0.038 |
| precio_unitario |        -0.038 |             1     |

## 📉 Outliers (Método IQR)
|    | Columna         |   Outliers detectados |   Porcentaje |
|---:|:----------------|----------------------:|-------------:|
|  0 | id_producto     |                     0 |            0 |
|  1 | precio_unitario |                     0 |            0 |

_Gráficos guardados en carpeta figs/_