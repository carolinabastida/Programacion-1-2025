class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Construir árbol de 3 niveles
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)

# Recorrido preorden
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)

print("Preorden:")
preorden(raiz)
