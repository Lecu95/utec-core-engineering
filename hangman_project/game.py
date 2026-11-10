#!/usr/bin/env python3
"""Modulo game.

Define la clase HangmanGame para gestionar el estado del juego.
"""


class HangmanGame:
    """Representa la logica y el estado del juego del ahorcado."""

    def __init__(self, word, max_errors=6):
        """Inicializa una nueva partida.

        Args:
            word (str): Palabra u oracion a adivinar.
            max_errors (int): Numero maximo de errores permitidos.
        """
        self.word = word
        self.guessed_letters = []
        self.max_errors = max_errors
        self.errors = 0

    def display_progress(self):
        """Devuelve el progreso visual de la palabra oculta.

        Returns:
            str: Cadena formateada con letras descubiertas y guiones.
        """
        result = []
        for char in self.word:
            if not char.isalpha():
                result.append(char)
            elif char.lower() in [g.lower() for g in self.guessed_letters]:
                result.append(char)
            else:
                result.append("_")
        return " ".join(result)

    def process_guess(self, letter):
        """Procesa una letra ingresada por el usuario.

        Args:
            letter (str): Letra ingresada por el usuario.

        Returns:
            bool: True si la letra esta en la palabra, False en otro caso.
        """
        letter_lower = letter.lower()
        if letter_lower not in [g.lower() for g in self.guessed_letters]:
            self.guessed_letters.append(letter_lower)

        if letter_lower in self.word.lower():
            return True

        self.errors += 1
        return False

    def is_won(self):
        """Verifica si todas las letras alfabeticas fueron adivinadas.

        Returns:
            bool: True si gano la partida, False de lo contrario.
        """
        guessed_lowers = [g.lower() for g in self.guessed_letters]
        for char in self.word:
            if char.isalpha() and char.lower() not in guessed_lowers:
                return False
        return True

    def is_lost(self):
        """Verifica si los errores alcanzaron el limite maximo.

        Returns:
            bool: True si perdio la partida, False de lo contrario.
        """
        return self.errors >= self.max_errors
