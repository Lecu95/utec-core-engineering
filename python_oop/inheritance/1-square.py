#!/usr/bin/env python3
"""Módulo 1-square.

Define la clase Square que hereda de Rectangle.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Clase Square que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): Tamaño del lado del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calcula y devuelve el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size * self.__size
