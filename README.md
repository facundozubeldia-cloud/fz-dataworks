## Repositorio de Ciencia de Datos - Facundo Zubeldia

Bienvenido a mi repositorio de ciencia de datos. Recopila proyectos aplicados en análisis de datos, visualización estratégica y machine learning. Cada uno está orientado a resolver problemas reales y facilitar la toma de decisiones empresariales. En cada carpeta encontrarás un caso práctico con su propio README explicativo.

## Sobre mí
Soy Técnico en Ciencia de Datos e IA en ISTEA, con formación adicional en Coderhouse y Educación IT. Me especializo principalmente en Python, SQL, Power BI y análisis exploratorio.

## Herramientas que utilizo
- Python (Pandas, NumPy, Matplotlib, Seaborn, etc)
- Power BI (DAX, JSON themes, Power Query)
- SQL (SQLite, My SQL, SQL Server, Duckdb)
- Excel
- Jupyter Notebooks

---

## **Rendimiento y Economía: Modelos Automotores**

**Objetivo:** Análisis del mercado automotor para identificar patrones según perfil de cliente y gama de precios, facilitando decisiones estratégicas de negocio.

* **Tecnologías:** Excel, SQL Server, Power BI
* **Logros:**

  * Segmentación en perfiles: Familiar, Soltero, Eco Friendly, Corredores y Lujo.
  * Clasificación de vehículos en gamas desde económico hasta superlujo.
  * Análisis de procedencia geográfica y preferencias por segmento.
  * Conclusiones estratégicas para ingresar al mercado automotor.

---

## **Análisis de Ventas - ClassicModels**

# Proyecto BI: Análisis de Ventas – ClassicModels Ltda.

Este proyecto desarrolla un flujo completo de Business Intelligence a partir del dataset ClassicModels, combinando ingesta automatizada, transformación relacional y visualización en Power BI.  

## Pipeline de datos
- **Ingesta**: Descarga automatizada desde Kaggle con su API oficial. Uso de DuckDB para exploración rápida sobre archivos locales.  
- **Transformación**: El dataset ya incluía una base en SQLite, lo que permitió consolidar órdenes, productos, clientes y empleados en un único dataset limpio exportado a CSV para Power BI.  
- **Motivación**: Se utilizaron ambos motores porque DuckDB facilita la exploración inicial, mientras que SQLite permitió aprovechar el modelo relacional existente.  

## Dashboard en Power BI
Se construyó un tablero interactivo que responde a las principales preguntas de negocio:  
- **Ventas totales y transacciones válidas** mediante tarjetas resumen  
- **Ventas por categoría** con gráfico de columnas  
- **Ventas por empleado** con gráfico de barras horizontales  
- **Evolución temporal de ventas** con gráfico de líneas y segmentador de fechas  
- **Insights clave**: picos estacionales en enero, concentración 80/20 en productos, crecimiento interanual del 18%  

## Resultados principales
- 303 transacciones válidas  
- Ventas totales: 8.865.094,6  
- Classic Cars lidera con 3,6M en ventas  
- Tendencia de ventas con picos en enero y caídas en mar–may  
- Alta concentración de ingresos en un subconjunto reducido de productos  

## Tecnologías utilizadas
Python (pandas, sqlite3, DuckDB, Kaggle API) · SQL · Power BI (Power Query, DAX, visualizaciones) 

---

## Escuderias - Análisis de Formula 1

Este análisis en Python analiza los resultados de una carrera de Fórmula 1 de 52 vueltas con hasta 20 pilotos. Estructura los datos en un diccionario anidado, calcula posiciones y puntos, genera estadísticas descriptivas y exporta informes en distintos formatos, realizando gráficos luego.

#### Funcionalidades destacadas

- Transformación de datos en estructuras claras y jerárquicas.
- Identificación de finalistas, ganador y podio.
- Asignación de puntos reglamentarios y extra por vuelta rápida.
- Estadísticas de tiempos (media, mediana, desviación, etc.).
- Ranking de escuderías por puntos.
- Exportación en JSON, Excel y SQLite.
- Gráficos de vueltas mas rapidas y top escuderias.

#### Ejemplo de resultados

- **Ganador**: Max Verstappen – 5200 segundos (vuelta rápida: 85 segundos)  
- **Podio**: Verstappen, Norris, Piastri  
- **Top escuderías**: McLaren (33 ptos), Red Bull (27), Ferrari (20)  
- **Estadísticas (finishers)**:  
  - Media: 5652 segundos
  - Mediana: 5616 segundos
  - Mínimo: 5200 segundos
  - Máximo: 6084 segundos
  - Desviación estándar: 280.68 segundos
  - Gráficos de barras de top escuderias y vueltas mas rapidas.

---

## **Análisis del Sistema EcoBici**

**Objetivo:** Evaluar eficiencia, patrones de uso y optimización de recursos del sistema público de bicicletas en Buenos Aires.

* **Tecnologías:** Excel, Power Query, Power BI
* **Logros:**

  * Identificación de estaciones con baja rotación y propuesta de redimensionamiento.
  * Análisis de comportamiento por tipo de usuario, destacando viajes turísticos.
  * Detección de horas pico para optimizar logística operativa.

---

## **Dashboard Estratégico de Capital Humano**

**Objetivo:** Proporcionar una visión integral del ciclo de vida del empleado, identificando riesgos y oportunidades en la gestión del talento.

* **Tecnologías:** Power Query, Power BI
* **Logros:**

  * Análisis integral de headcount, adquisición de talento, capacitación, compromiso y rotación.
  * Identificación de causas clave de rotación y baja satisfacción.
  * Recomendaciones estratégicas para mejorar productividad y retención.

---  

## **Proyectos de Machine Learning**

### **Clasificación de Iris con Decision Tree**

* Modelo explicativo visual para clasificar especies según características florales.

### **Detección de Sarcasmo en Titulares**

* NLP pipeline para clasificar titulares usando Random Forest.

### **Reducción Dimensionalidad (PCA)**

* Aplicación de PCA en dataset Iris para optimización del análisis exploratorio.

### **Clasificación de Imágenes (CIFAR-10)**

* Comparativa entre red neuronal densa y CNN.
* CNN alcanzó 76.6% accuracy con análisis detallado mediante matriz de confusión.

### **Clustering: K-Means y DBSCAN**

* Comparación de algoritmos, evaluación visual y numérica para segmentación óptima.

---

Cierre y Próximos Pasos

Este repositorio reúne proyectos que reflejan mi práctica en análisis de datos y machine learning, así como mi capacidad para aprender nuevas herramientas y metodologías. Cada caso de estudio me ha permitido enfrentar desafíos reales, mejorar mi atención al detalle y colaborar con un enfoque orientado al negocio.

Estoy entusiasmado por seguir creciendo en entornos de Data Analysis o Data Engineering, contribuyendo con soluciones claras y efectivas. Agradezco tu tiempo revisando mi trabajo y quedo abierto a feedback para seguir mejorando.
