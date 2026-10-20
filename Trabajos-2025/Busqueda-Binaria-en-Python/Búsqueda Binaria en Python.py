def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Se toma el punto medio
        if lista[medio] == elemento:
            return medio  # Se encontró el elemento
        elif lista[medio] < elemento:
            inicio = medio + 1  # Buscar en la mitad derecha
        else:
            fin = medio - 1  # Buscar en la mitad izquierda

    return -1  # Si no se encuentra

# Lista ordenada de ejemplo
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# Número a buscar
buscado = int(input("Ingrese el número que desea buscar: "))

resultado = busqueda_binaria(numeros, buscado)

if resultado != -1:
    print(f"El número {buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El número {buscado} no está en la lista.")
