#!/usr/bin/env python3
"""Modulo que contiene la funcion write_file."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo de texto (UTF-8)

    y devuelve el numero de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
