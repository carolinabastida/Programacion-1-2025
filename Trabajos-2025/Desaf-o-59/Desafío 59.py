# -*- coding: utf-8 -*-

"""
Solución al ejercicio de herencia con Libros, Libros Digitales y EBooks.
Este script define una jerarquía de clases para gestionar diferentes tipos de libros.
"""

class Libro:
    """
    Clase base que representa un libro con sus atributos fundamentales.
    """
    def __init__(self, titulo: str, autor: str, año_publicacion: int):
        """
        Constructor de la clase Libro.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            año_publicacion (int): El año en que se publicó el libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        """
        Muestra la información básica y común de cualquier libro.
        Este método será extendido o sobrescrito por las clases hijas.
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.año_publicacion}")


class LibroDigital(Libro):
    """
    Subclase que hereda de Libro y añade características específicas
    de los libros en formato digital.
    """
    def __init__(self, titulo: str, autor: str, año_publicacion: int, formato: str, tamaño_archivo: float):
        """
        Constructor de la clase LibroDigital.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            año_publicacion (int): El año de publicación.
            formato (str): El formato del archivo (ej. 'PDF', 'EPUB').
            tamaño_archivo (float): El tamaño del archivo en MB.
        """
        # Llamamos al constructor de la clase padre (Libro) para inicializar sus atributos
        super().__init__(titulo, autor, año_publicacion)
        
        # Añadimos los nuevos atributos específicos de esta subclase
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_info(self):
        """
        Extiende el método de la clase padre para mostrar también la información digital.
        """
        print("--- Información del Libro Digital ---")
        # Primero, ejecutamos el método original de la clase padre
        super().mostrar_info()
        # Luego, añadimos la nueva información
        print(f"Formato: {self.formato}")
        print(f"Tamaño de Archivo: {self.tamaño_archivo:.2f} MB")


class EBook(LibroDigital):
    """
    Subclase que hereda de LibroDigital y representa un tipo específico de libro digital
    que se puede comprar y descargar, por lo que tiene un enlace de descarga.
    """
    def __init__(self, titulo: str, autor: str, año_publicacion: int, formato: str, tamaño_archivo: float, enlace_descarga: str):
        """
        Constructor de la clase EBook.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            año_publicacion (int): El año de publicación.
            formato (str): El formato del archivo.
            tamaño_archivo (float): El tamaño del archivo en MB.
            enlace_descarga (str): La URL para descargar el EBook.
        """
        # Llamamos al constructor de la clase padre (LibroDigital)
        super().__init__(titulo, autor, año_publicacion, formato, tamaño_archivo)
        
        # Atributo propio de la clase EBook
        self.enlace_descarga = enlace_descarga

    def mostrar_info(self):
        """
        Sobrescribe completamente el método de las clases padres para proporcionar
        una visualización de la información específica y adaptada para un EBook,
        incluyendo su enlace de descarga.
        """
        print("--- Información del EBook (con enlace) ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.año_publicacion}")
        print(f"Formato: {self.formato}")
        print(f"Tamaño: {self.tamaño_archivo:.2f} MB")
        # Información específica y crucial de esta subclase
        print(f"Enlace de Descarga: {self.enlace_descarga}")


# --- Bloque de Ejecución Principal ---
# Este código se ejecutará solo cuando el script se corra directamente.
if __name__ == "__main__":
    
    # 1. Creación de un objeto de la clase base
    libro_fisico = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    print(">>> Probando la clase base: Libro")
    libro_fisico.mostrar_info()
    print("\n" + "="*40 + "\n")
    
    # 2. Creación de un objeto de la primera subclase
    libro_pdf = LibroDigital(
        titulo="Python Crash Course",
        autor="Eric Matthes",
        año_publicacion=2015,
        formato="PDF",
        tamaño_archivo=15.5
    )
    print(">>> Probando la subclase: LibroDigital")
    libro_pdf.mostrar_info()
    print("\n" + "="*40 + "\n")

    # 3. Creación de un objeto de la segunda subclase (EBook)
    ebook_comprado = EBook(
        titulo="Automate the Boring Stuff with Python",
        autor="Al Sweigart",
        año_publicacion=2019,
        formato="EPUB",
        tamaño_archivo=8.23,
        enlace_descarga="https://inventwithpython.com/automatestuff/"
    )
    print(">>> Probando la subclase que sobrescribe el método: EBook")
    ebook_comprado.mostrar_info()