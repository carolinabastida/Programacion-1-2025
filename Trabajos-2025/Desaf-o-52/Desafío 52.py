class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
    
    # Métodos getter
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn
    
    # Métodos setter
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    # Método para mostrar información del libro
    def mostrar_informacion(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nISBN: {self.__isbn}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de Libro
    mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", "978-8437604947")
    
    # Obtener valores usando getters
    print("Título:", mi_libro.get_titulo())
    print("Autor:", mi_libro.get_autor())
    print("ISBN:", mi_libro.get_isbn())
    
    print("\n" + "="*40 + "\n")
    
    # Modificar valores usando setters
    mi_libro.set_titulo("El amor en los tiempos del cólera")
    mi_libro.set_isbn("978-0307474728")
    
    # Mostrar información completa
    print(mi_libro.mostrar_informacion())