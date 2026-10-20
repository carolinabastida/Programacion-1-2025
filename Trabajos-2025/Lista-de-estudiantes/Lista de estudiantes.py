# Lista de estudiantes
estudiantes = []

# Función para agregar un estudiante
def agregar_estudiante(nombre):
    estudiantes.append(nombre)

# Función para eliminar un estudiante
def eliminar_estudiante(nombre):
    if nombre in estudiantes:
        estudiantes.remove(nombre)
    else:
        print("El estudiante no está en la lista.")

# Función para mostrar la lista de estudiantes
def mostrar_estudiantes():
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)

# Programa principal
agregar_estudiante("Juan")
agregar_estudiante("María")
mostrar_estudiantes()

eliminar_estudiante("Juan")
mostrar_estudiantes()
