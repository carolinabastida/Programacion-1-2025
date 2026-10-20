def es_par_o_impar(n: int) -> str:
    if n % 2 == 0:
        return f"{n} - par"
    else:
        return f"{n} - impar"


def cuenta_regresiva(n: int) -> None:
    if n < 0:
        return
    print(es_par_o_impar(n))
    if n == 0:
        print("🚀 ¡Despegue completado! Fin de la cuenta regresiva.")
    else:
        cuenta_regresiva(n - 1)
