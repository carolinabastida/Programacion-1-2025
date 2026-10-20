# --- Mejora del cálculo de promedio y aprobación ---

def analisis_calificaciones():
    # El usuario ingresa las calificaciones separadas por comas
    entrada = input("Ingrese todas las calificaciones separadas por comas: ")

    # Convertimos el texto en una lista de números (floats)
    calificaciones = [float(nota.strip()) for nota in entrada.split(",") if nota.strip() != ""]

    # Verificamos que haya calificaciones
    if not calificaciones:
        print("No se ingresaron calificaciones válidas.")
        return

    # Cálculo del promedio
    promedio = sum(calificaciones) / len(calificaciones)

    # Contar aprobados y desaprobados
    aprobados = sum(1 for nota in calificaciones if nota >= 7)
    desaprobados = len(calificaciones) - aprobados

    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Total de estudiantes: {len(calificaciones)}")
    print(f"Promedio general: {promedio:.2f}")
    print(f"Estudiantes aprobados (nota >= 7): {aprobados}")
    print(f"Estudiantes desaprobados (nota < 7): {desaprobados}")

# Ejecutar el programa
analisis_calificaciones()
