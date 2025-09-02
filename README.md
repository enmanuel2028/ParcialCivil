# Diseño de Estructuras de Concreto

Aplicación web interactiva para el diseño y cálculo de estructuras de concreto. Esta herramienta permite a ingenieros civiles y estudiantes realizar cálculos estructurales de manera rápida y precisa.

## Características

- Cálculo de parámetros de sección de concreto
- Análisis de materiales y propiedades
- Configuración de refuerzo de acero
- Visualización de croquis con dimensiones
- Cálculo de resistencia y momentos
- Importación/exportación de datos en formato Excel

## Uso

La aplicación está desplegada en Streamlit Cloud y puede accederse mediante el siguiente enlace:

[Enlace a la aplicación](https://parcialcivil.streamlit.app/)

## Requisitos

Para ejecutar localmente, se requieren las siguientes dependencias:

```
streamlit
pandas
matplotlib
openpyxl
xlsxwriter
```

Instale las dependencias con:

```
pip install -r requirements.txt
```

## Ejecución Local

```
streamlit run app.py
```

## Despliegue

Esta aplicación puede ser desplegada en Streamlit Cloud siguiendo estos pasos:

1. Crear una cuenta en [Streamlit Cloud](https://streamlit.io/cloud)
2. Conectar tu cuenta de GitHub
3. Crear un repositorio con este código
4. Desplegar la aplicación desde el dashboard de Streamlit Cloud
