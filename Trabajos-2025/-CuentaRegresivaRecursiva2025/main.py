import contador

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        print("\nIniciando cuenta regresiva...\n")
        contador.cuenta_regresiva(numero)
    except ValueError:
        print("Error: debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
