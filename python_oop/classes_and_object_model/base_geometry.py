#!/usr/bin/env python3
"""Módulo base_geometry.

Define la clase BaseGeometry para figuras geométricas.
"""


class BaseGeometry:
    """Clase base para la jerarquía de geometría."""

    def area(self):
        """Calcula el área de la figura geométrica.

        Raises:
            Exception: Si el método no ha sido implementado.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida si un valor es un entero positivo mayor que cero.

        Args:
            name (str): Nombre del atributo.
            value (int): Valor a validar.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor o igual a cero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
