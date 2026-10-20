import pandas as pd # Importa la librería pandas, para manejar datos en formato CSV

# Carga el archivo CSV en un DataFrame, cargando la info del csv en la variable df.
df = pd.read_csv("calificaciones.csv")

# Inicializa variables para calcular el promedio general
total_calificaciones = 0
numero_calificaciones = 0
aprobados=0
reprobados=0
minimos=0
# Utiliza un bucle for para sumar todas las calificaciones
for index, row in df.iterrows():
    nombre = row['Nombre'] 
    calificacion = int(row['Calificacion']) 
    if calificacion >= 7:
        aprobados=aprobados+1
    elif calificacion == 1:
        minimos=minimos+1
    else:
        reprobados=reprobados+1
       
    total_calificaciones = total_calificaciones + calificacion 
    numero_calificaciones = numero_calificaciones + 1 
    print(f"La calificación de {nombre} es: {calificacion}")

# Calcula el promedio general
promedio_general = total_calificaciones / numero_calificaciones
print(f"El promedio general de las calificaciones es: {promedio_general:.2f}")
print(f"La cantidad de aprobados es: {aprobados}")
print(f"La cantidad de REPROBADOS es: {reprobados}")
print(f"Los alumnos con nota minima (1): {minimos}")

# 