#!/usr/bin/env python3
"""Módulo 1-square.

Este módulo define una clase Square con un atributo de instancia privado size.
"""


class Square:
    """Clase que define un cuadrado."""

    def __init__(self, size):
        """Inicializa una nueva instancia de Square.

        Args:
            size: El tamaño del lado del cuadrado.
        """
        self.__size = size
