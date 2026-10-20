# --- Desafío 5: Contador de Palabras ---

def contador_palabras():
    texto = input("Ingrese un texto: ").strip()
    palabras = texto.split()
    cantidad = len(palabras)
    print(f"\nEl texto contiene {cantidad} palabra(s).\n")

# Ejecutar
contador_palabras()
