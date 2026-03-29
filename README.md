# Proyecto de Customer Intelligence and Churn Prediction Toolkit

Una herramienta modular diseñada para identificar clientes en riesgo de fuga
y optimizar la retención mediante el análisis de datos.

## Características

- **Arquitectura Modular:** Separación clara entre la configuración y el código principal.
- **Detección Automatizada:** Clasificación de clientes VIP basada en umbrales dinámicos.
- **Persistencia de Datos:** Generación de reportes automáticos en formato CSV.

## Stack tecnológico

- **Lenguaje:** Python 3.10+
- **Entorno virtual:** venv
- **Control de versiones:** Git / GitHub

## Arquitectura del proyecto

```text
churn_project/
├── data/               # Archivos CSV (ignorados en Git)
├── .gitignore          # Archivos excluidos del repositorio
├── config.py           # Configuración centralizada
├── main.py             # Código principal del proyecto
└── requirements.txt    # Librerías necesarias

## Instalación y uso

1. Clonar el repositorio
2. Crear y activar el entorno virtual
3. Instalar dependencias: pip install -r requirements.txt
4. Ejecutar: python main.py

## Próximas actualizaciones

- Integración con PANDAS para análisis de datos masivos
- Creación de modelos de Machine Learning con Scikit-Learn