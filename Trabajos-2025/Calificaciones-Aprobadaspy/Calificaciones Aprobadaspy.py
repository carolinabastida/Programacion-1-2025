# --- Desafío 1: Calificaciones Aprobadas ---

# Este programa pide al usuario varias calificaciones
# y calcula cuántos estudiantes aprobaron (nota >= 7)
# y cuántos desaprobaron (nota < 7)

def calificaciones_aprobadas():
    aprobados = 0
    desaprobados = 0

    cantidad = int(input("Ingrese la cantidad de estudiantes: "))

    for i in range(1, cantidad + 1):
        nota = float(input(f"Ingrese la calificación del estudiante {i}: "))
        if nota >= 7:
            aprobados += 1
        else:
            desaprobados += 1

    print("\n=== RESULTADOS ===")
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes desaprobados: {desaprobados}")

# Ejecutar el programa
calificaciones_aprobadas()
