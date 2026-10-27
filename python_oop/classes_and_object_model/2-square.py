#!/usr/bin/env python3
"""Módulo 2-square.

Este módulo define una clase Square con atributo privado size y validación.
"""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado (por defecto 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
