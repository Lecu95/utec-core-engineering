#!/usr/bin/env python3
"""Modulo utils.

Contiene funciones auxiliares para el juego del ahorcado.
"""

import random


def get_random_word(filepath="wordlist.txt"):
    """Lee el archivo wordlist y devuelve una palabra aleatoria.

    Args:
        filepath (str): Ruta al archivo de texto.

    Returns:
        str: Palabra seleccionada al azar.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
        return random.choice(words)
    except FileNotFoundError:
        return "python"
