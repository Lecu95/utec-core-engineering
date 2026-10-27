#!/usr/bin/env python3
"""Módulo 5-square.

Este módulo define una clase Square con atributos privados, validaciones,
propiedades getter/setter, cálculo de área e impresión por consola.
"""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado (por defecto 0).
        """
        self.size = size

    @property
    def size(self):
        """Obtiene el tamaño actual del cuadrado.

        Returns:
            int: El tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado validando tipo y valor.

        Args:
            value (int): El nuevo tamaño del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula el área del cuadrado.

        Returns:
            int: El área actual del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado con el carácter #.

        Si size es igual a 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
