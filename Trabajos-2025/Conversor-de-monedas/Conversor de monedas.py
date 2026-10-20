# --- Desafío 4: Conversor de Moneda ---

def conversor_moneda():
    print("=== Conversor de Moneda ===")
    try:
        monto_local = float(input("Ingrese la cantidad en su moneda local: "))
        tasa_cambio = float(input("Ingrese la tasa de cambio (1 moneda local equivale a cuántas extranjeras): "))
        monto_convertido = monto_local * tasa_cambio
        print(f"\nMonto convertido: {monto_convertido:.2f} en la moneda extranjera.\n")
    except ValueError:
        print("Error: Ingrese solo valores numéricos.")

# Ejecutar
conversor_moneda()


