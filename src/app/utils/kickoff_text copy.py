DOC = """
# Emisiones de CO2 y su impacto ambiental
> Propuesta de análisis por __LookMyData__

## Marco Teórico
El dióxido de  carbono (CO2) es un gas perteneciente a la clase de gases llamados “de efecto invernadero” dada su capacidad de contribuir a la retención de calor en la atmósfera.
Sin embargo, éste no es su único efecto ya que, dependiendo de las concentraciones en las que se encuentre, puede ocasionar daños ambientales que van más allá del calentamiento global, como lo son las lluvias ácidas.
La evidencia con respecto a un proceso de calentamiento global es de larga data pero su vinculación directa con las actividades humanas como causantes de emisiones de gases de efecto invernadero es más reciente e incluso controvertida ya que hay quienes cuestionan que el aumento de CO2 atmosférico se deba a la actividad humana y que éste sea el principal causante del calentamiento global. Dentro de estas actividades, destaca la generación y el consumo de energía dado que son actividades tradicional y mayormente dependientes de la quema de combustibles fósiles.
A través de un análisis profundo de datos disponibles sobre actividad económica, emisiones de CO2 y salud, proponemos en este análisis dilucidar la relación entre estos tres factores y establecer si existe causalidad entre la actividad económica y las emisiones.

## Objetivos y métricas

### Objetivo general
Describir la relación entre el consumo y generación de energía, y las emisiones de CO2 a nivel global, como así también su impacto sobre el medio ambiente y la salud humana, generando herramientas para su estudio en forma analítica y visual.

### Objetivos particulares
- Estudiar la relación entre consumo/generación de energía, emisiones de CO2 y PBI. 
Permitirá establecer un punto de partida para el análisis determinando el grado de dependencia entre actividad económica y la demanda de energía, con las emisiones asociadas.
- Estudiar la relación entre emisiones de CO2 y frecuencia de desastres ambientales relacionados al clima.
Estudiar la relación entre emisiones de CO2 y PBI de los principales países según actividad económica. 
Permitirá conocer la forma en la que varía la emisión de CO2  con respecto a la actividad económica. Al mismo tiempo, tomando como KPI la cantidad de m3 por 1M USD de PBI para cada país, podremos tener un parámetro comparativo de cuán “limpio” es su actividad económica.
- Analizar la calidad del aire en los países con mayor y menor nivel de emisión de CO2
- Estudiar la relación entre emisiones de CO2 y prevalencia de enfermedades respiratorias en los países con mayor nivel de emisiones.
El impacto ambiental afecta directa e indirectamente a las personas y una posible medida de ello es la prevalencia de enfermedades relacionadas a la calidad del aire.

### KPI’s y métricas

- Reducción al 45% de las emisiones de Dióxido de carbono para 2030
- Reducción al 95% del uso de carbón para 2030
- Reducción al 45% del uso de gas para 2050
- Reducción al 60% del uso de petroleo para 2050

- Productores de enegías limpias 
- Calidad del aire 
- Evolución histórica de generación de energía y emisión de CO2  en top 10 países emisores de CO2 
- Evolución del índice de calidad de aire (AQI) en relación al nivel de emisión de CO2  en los 10 países de mayor emisión
- m3 CO2 / GWh generado
- Ranking países según m3 CO2/ 1M USDPBI
- Casos de cáncer de pulmón por m3 de CO2  en países top 10 según emisiones
- Frecuencia de desastres naturales / m3 CO2

## Metodología y Stack Tecnológico

1. Busqueda de datasets a trabajar y análisis exploratorio
    Durante esta etapa el equipo se encargó de buscar los datasets necesarios y se analizaron cuales iban a ser los KPIs y métricas necesarias para llevar a cabo el desarrollo del producto.

2. Limpieza y normalización de datos y automatización de los procesos
    Con el uso de Python y librerías como Pandas y Numpy se realizaron los procesos de Extracción y Transformación de los datos, luego con Airflow se automatizaron los procesos para hacer la carga de los mismos dentro del servicios cloud de Amazon.

3. Modelos y aprendizaje automático
    Luego de preparar los datos con los procesos de ETL, se realizaron diferentes analisis elaborando métricas 

4. Reporte y conclusiones
    Durante en esta última etapa el equipo estuvo encargado de ensamblar el producto, acá se pusieron los datos dentro de una API accesible, asimismo se diseñó el dashboard de Streamlit.




### Ingesta de datos y montaje de servicio de datos basado en la nube

En esta etapa se montará un data lakehouse a partir de datos de diferentes fuentes y se realizará una limpieza y normalización de los mismos para ser usados en el análisis. Se utilizará principalmente Python (manejo y limpieza de datos), Airflow (automatización y control de flujos de trabajo), Databricks (data lakehouse) y spark (gestor de base de datos).

### Análisis, métricas y KPI’s
A partir del servicio de datos montado, los mismos se consultarán mediante queries SQL en Hive para la elaboración de las métricas propuestas anteriormente y se plasmarán en un dashboard generado a partir de Streamlit.

### Modelos y aprendizaje automático
Con el conocimiento de lo que ha pasado, adquirido en la etapa anterior, y con la incertidumbre de lo que pasará. Crearemos modelos predictivos basados en poder de cómputo (machine learning). De ser posible, continuaremos experimentando con redes neuronales (deep learning)

### Reporte y conclusiones
Con el dashboard generado y a partir de las métricas y KPI’s creadas se elaborará un informe resumiendo los principales insights  de los datos recopilados y se proporcionarán recomendaciones de acción para minimizar las emisiones de CO2 y por consiguiente, su impacto, en los países donde sea más factible y provechoso hacerlo.
"""
