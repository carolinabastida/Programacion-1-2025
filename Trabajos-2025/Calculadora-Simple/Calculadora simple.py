# --- Desafío 2: Calculadora Simple ---

try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    print("\nResultados:")
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")

    if b != 0:
        print(f"División: {a / b:.2f}")
    else:
        print("División: No se puede dividir entre cero.")

except ValueError:
    print("Error: Debe ingresar valores numéricos válidos.")
