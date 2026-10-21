#!/usr/bin/env python3
"""Modulo que contiene la funcion append_write."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo de texto (UTF-8)

    y devuelve el numero de caracteres añadidos.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
