#!/usr/bin/env python3
"""Módulo 6-square.

Este módulo define una clase Square con atributos privados size y position,
validaciones, propiedades getter/setter, cálculo de área, representación en
cadena e impresión por consola.
"""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado (por defecto 0).
            position (tuple): Tupla de 2 enteros positivos para la posición.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Obtiene la posición del cuadrado.

        Returns:
            tuple: La posición del cuadrado (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado validando tipo y elementos.

        Args:
            value (tuple): Tupla de 2 enteros positivos.

        Raises:
            TypeError: Si position no es una tupla de 2 enteros positivos.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado.

        Returns:
            int: El área actual del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime en stdout el cuadrado con el carácter #."""
        if self.__size == 0:
            print()
            return
        print(self)

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado.

        Returns:
            str: El cuadrado formateado con espacios y líneas para imprimir.
        """
        if self.__size == 0:
            return ""

        res = []
        for _ in range(self.__position[1]):
            res.append("")
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(res)
