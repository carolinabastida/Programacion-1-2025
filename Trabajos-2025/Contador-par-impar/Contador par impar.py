def es_par_o_impar(numero):
    """
    Función auxiliar que determina si un número es par o impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def cuenta_regresiva(n):
    """
    Función recursiva que imprime los números desde n hasta 0,
    indicando si cada número es par o impar.
    """
    if n < 0:
        return
    
    print(f"{n} - {es_par_o_impar(n)}")
    
    if n == 0:
        print("¡Despegue! 🚀")
        return
    else:
        cuenta_regresiva(n - 1)
