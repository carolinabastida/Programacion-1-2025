# --- Invertir palabras en una oración usando recursión ---

def invertir_palabras(oracion):
    """
    Función recursiva que invierte el orden de las palabras en una oración.
    No utiliza funciones incorporadas de inversión.
    """
    palabras = oracion.split()

    # Caso base: si la oración tiene una sola palabra o está vacía
    if len(palabras) <= 1:
        return oracion

    # Tomar la última palabra y combinar con la recursión del resto
    ultima_palabra = palabras[-1]
    resto_oracion = " ".join(palabras[:-1])

    # Llamada recursiva
    return ultima_palabra + " " + invertir_palabras(resto_oracion)


# --- Programa principal ---
frase = input("Ingrese una oración: ")
resultado = invertir_palabras(frase)

print("\n=== RESULTADO ===")
print("Oración original:", frase)
print("Oración invertida:", resultado)
