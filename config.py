import os

# ----- CONFIGURACION DE PATHS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_DATA_PATH = os.path.join(DATA_DIR, "raw_customers.csv")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "clean_customers.csv")

# ----- LOGICA DE NEGOCIO (CONSTANTES) -----

VIP_THRESHOLD_SPEND = 1000.0    # Gasto minimo para ser VIP
CHURN_MONTHS_INACTIVE = 6       # Meses de inactividad para considerarse "Fuga"

CATEGORIES = {
    "A": {"label": "Alto valor", "priority": 1},
    "B": {"label": "Medio valor", "priority": 2},
    "C": {"label": "Bajo valor", "priority": 3}
}
