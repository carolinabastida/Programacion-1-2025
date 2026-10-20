import contador

def main():
    """
    Archivo principal que solicita un número al usuario
    y llama a la función de cuenta regresiva.
    """
    try:
        numero_ingresado = int(input("Ingresa un número entero positivo para la cuenta regresiva: "))
        if numero_ingresado < 0:
            print("Por favor, ingresa un número entero positivo.")
            return
        
        print("\nIniciando cuenta regresiva...\n")
        contador.cuenta_regresiva(numero_ingresado)
        
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main