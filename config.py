# ----- LOGICA DE NEGOCIO (CONSTANTES) -----

VIP_THRESHOLD_SPEND = 1000.0    # Gasto minimo para ser VIP
CHURN_MONTHS_INACTIVE = 6       # Meses de inactividad para considerarse "Fuga"

CATEGORIES = {
    "A": {"label": "Alto valor", "priority": 1},
    "B": {"label": "Medio valor", "priority": 2},
    "C": {"label": "Bajo valor", "priority": 3}
}
