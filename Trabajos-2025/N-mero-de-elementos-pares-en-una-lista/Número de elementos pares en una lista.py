def contar_pares(lista):
    # Cuenta cuántos números pares hay en la lista
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador

# --- Programa principal ---
numeros = [1, 2, 3, 4, 5, 6, 8]  # Podés cambiar esta lista por cualquier otra
print("La cantidad de números pares es:", contar_pares(numeros))
