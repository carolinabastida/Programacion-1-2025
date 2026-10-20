# Desafío 3: Promedio, nota más baja y más alta

# Solicitamos al usuario que ingrese las calificaciones separadas por comas
entrada = input("Ingresá las calificaciones separadas por comas: ")

# Convertimos la cadena en una lista de números (floats)
calificaciones = [float(nota.strip()) for nota in entrada.split(",")]

# 1️⃣ Calcular el promedio general
promedio = sum(calificaciones) / len(calificaciones)

# 2️⃣ Encontrar la nota más baja y la más alta
nota_minima = min(calificaciones)
nota_maxima = max(calificaciones)

# Mostramos los resultados
print(f"Promedio general de la clase: {promedio:.2f}")
print(f"Nota más baja: {nota_minima}")
print(f"Nota más alta: {nota_maxima}")

# Agregamos un breve análisis del desempeño general
if promedio >= 9:
    print("Excelente rendimiento grupal.")
elif promedio >= 7:
    print("Buen rendimiento general.")
else:
    print("El grupo necesita mejorar su desempeño.")
