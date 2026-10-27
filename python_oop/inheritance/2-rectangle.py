#!/usr/bin/env python3
"""Módulo 2-rectangle.

Define la clase Rectangle que hereda de BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Altura del rectángulo.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo.

        Returns:
            int: El área del rectángulo.
        """
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación en cadena del rectángulo.

        Returns:
            str: Descripción en formato [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
