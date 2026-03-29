import config

def run_analysis():
    print("--- Iniciando sistema de Customer Intelligence ---")

    customers = [       # Simulacion de datos complejos
        {"id": 1, "nombre": "Alex", "gasto_mensual": 1200.50, "servicios": ["internet", "streaming"]},
        {"id": 2, "nombre": "Marta", "gasto_mensual": 450.00, "servicios": ["internet"]},
        {"id": 3, "nombre": "Juan", "gasto_mensual": 890.20, "servicios": ["internet", "streaming"]},
        {"id": 4, "nombre": "Lucia", "gasto_mensual": 1500.00, "servicios": ["celular", "internet", "internet"]},
        {"id": 5, "nombre": "Martin", "gasto_mensual": 900.00, "servicios": ["streaming"]},
        {"id": 6, "nombre": "Daniel", "gasto_mensual": 780.50, "servicios": ["celular"]}
    ]

    print(f"Buscando clientes VIP (Gasto > ${config.VIP_THRESHOLD_SPEND}) ...")

    vips = []
    for cliente in customers:
        gasto = cliente["gasto_mensual"]
        if gasto > config.VIP_THRESHOLD_SPEND:
            vips.append(cliente["nombre"])

    print(f"Los clientes VIP son {vips}")
    print(f"Los datos se guardaran en: {config.PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    run_analysis()
