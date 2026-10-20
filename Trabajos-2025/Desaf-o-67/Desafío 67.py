def division_segura():
    """
    Función que solicita dos números al usuario y realiza una división
    con manejo de errores para división por cero y valores no numéricos.
    """
    try:
        # Solicitar el primer número
        num1 = input("Ingresa el primer número entero: ")
        num1 = int(num1)  # Intentar convertir a entero
        
        # Solicitar el segundo número
        num2 = input("Ingresa el segundo número entero: ")
        num2 = int(num2)  # Intentar convertir a entero
        
        # Realizar la división
        resultado = num1 / num2
        print(f"El resultado de {num1} ÷ {num2} = {resultado}")
        
    except ValueError:
        # Manejar error cuando el usuario ingresa algo que no es un número
        print("Error: Debes ingresar números enteros válidos.")
        
    except ZeroDivisionError:
        # Manejar error de división por cero
        print("Error: No se puede dividir por cero.")
        
    except Exception as e:
        # Manejar cualquier otro error inesperado
        print(f"Error inesperado: {e}")

# Ejecutar la función
if __name__ == "__main__":
    division_segura()