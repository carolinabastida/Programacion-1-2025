import math

class NegativeNumberError(Exception):
    """
    Excepción personalizada para manejar intentos de calcular
    la raíz cuadrada de un número negativo.
    """
    def __init__(self, message="No es posible calcular la raíz cuadrada de un número negativo."):
        self.message = message
        super().__init__(self.message)

def calcular_raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    Lanza NegativeNumberError si el número es negativo.
    """
    if numero < 0:
        raise NegativeNumberError
    return math.sqrt(numero)

def main():
    """
    Función principal para solicitar un número al usuario y
    calcular su raíz cuadrada, manejando posibles errores.
    """
    try:
        entrada_usuario = input("Ingresa un número para calcular su raíz cuadrada: ")
        numero = float(entrada_usuario)
        
        resultado = calcular_raiz_cuadrada(numero)
        
        print(f"La raíz cuadrada de {numero} es: {resultado}")

    except ValueError:
        print("Error: Por favor, introduce un número válido.")
    except NegativeNumberError as e:
        print(f"Error personalizado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()