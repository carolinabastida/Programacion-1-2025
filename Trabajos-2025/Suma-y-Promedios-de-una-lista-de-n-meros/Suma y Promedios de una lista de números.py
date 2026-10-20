# --- Desafío 1: Suma y promedio de una lista de números ---

def suma_y_promedio(numeros):
    """
    Recibe una lista de números y devuelve la suma total y el promedio.
    """
    if not numeros:  # Si la lista está vacía
        return 0, 0

    suma_total = sum(numeros)
    promedio = suma_total / len(numeros)
    return suma_total, promedio


# --- Programa principal ---
# El usuario ingresa los números separados por comas
entrada = input("Ingrese una lista de números separados por comas: ")

# Convertir la entrada a una lista de números (float)
numeros = [float(n.strip()) for n in entrada.split(",") if n.strip() != ""]

# Calcular resultados
suma_total, promedio = suma_y_promedio(numeros)

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"Lista de números: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
