class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Lista de libros

    def agregar_libro(self, titulo):
        """Agrega un libro si no existe"""
        if titulo not in self.libros:
            self.libros.append(titulo)
            print(f"El libro '{titulo}' fue agregado.")
            return True  # Retorna éxito
        else:
            print(f"El libro '{titulo}' ya está en la lista.")
            return False  # Retorna fracaso

    def eliminar_libro(self, titulo):
        """Elimina un libro si existe"""
        if titulo in self.libros:
            self.libros.remove(titulo)
            print(f"El libro '{titulo}' fue eliminado.")
            return True  # Retorna éxito
        else:
            print(f"El libro '{titulo}' no se encuentra en la lista.")
            return False  # Retorna fracaso

    def tiene_libros(self):
        """Verifica si tiene libros"""
        return len(self.libros) > 0

    def mostrar_info(self):
        """Muestra la información completa del autor"""
        print(f"Autor: {self.nombre}")
        if self.tiene_libros():
            print("Libros escritos:")
            for i, libro in enumerate(self.libros, 1):
                print(f"  {i}. {libro}")
        else:
            print("No tiene libros registrados.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear autor
    autor = Autor("Gabriel García Márquez")
    
    # Agregar libros
    autor.agregar_libro("Cien años de soledad")
    autor.agregar_libro("El amor en los tiempos del cólera")
    autor.agregar_libro("Cien años de soledad")  # Intento de duplicado
    
    # Mostrar información
    autor.mostrar_info()
    
    # Eliminar libro
    autor.eliminar_libro("El amor en los tiempos del cólera")
    
    # Mostrar información actualizada
    autor.mostrar_info()
    
    # Intentar eliminar libro que no existe
    autor.eliminar_libro("Crónica de una muerte anunciada")