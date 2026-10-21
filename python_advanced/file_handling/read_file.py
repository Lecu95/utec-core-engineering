#!/usr/bin/env python3
"""Modulo que contiene la funcion read_file."""


def read_file(filename=""):
    """Lee un archivo de texto (UTF-8) e imprime su contenido en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
