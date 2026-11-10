#!/usr/bin/env python3
"""Modulo main.

Punto de entrada principal para ejecutar el juego del ahorcado.
"""

from game import HangmanGame
from utils import get_random_word


def draw_hangman(errors):
    """Devuelve la representacion visual ASCII del ahorcado.

    Args:
        errors (int): Cantidad actual de errores cometidos.

    Returns:
        str: Dibujo ASCII correspondiente.
    """
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         ========="""
    ]
    return stages[errors]


def validate_input(user_input, guessed_letters):
    """Valida la entrada introducida por el jugador.

    Args:
        user_input (str): Entrada recibida.
        guessed_letters (list): Lista de letras ya intentadas.

    Returns:
        tuple: (bool, str) Validez y mensaje o letra procesada.
    """
    cleaned = user_input.strip()
    if len(cleaned) != 1:
        return False, "Ingresa solo un caracter a la vez."
    if not cleaned.isalpha():
        return False, "Entrada invalida. Solo se aceptan letras."

    guessed_lowers = [g.lower() for g in guessed_letters]
    if cleaned.lower() in guessed_lowers:
        return False, f"Ya intentaste la letra '{cleaned}'. Prueba otra."

    return True, cleaned


def play_game():
    """Ejecuta una ronda completa del juego del ahorcado."""
    secret_word = get_random_word("wordlist.txt")
    game = HangmanGame(secret_word)

    print("\n" + "=" * 45)
    print("        ¡BIENVENIDO AL JUEGO DEL AHORCADO!")
    print("=" * 45)

    while not game.is_won() and not game.is_lost():
        print(draw_hangman(game.errors))
        print(f"\nPalabra: {game.display_progress()}")
        print(f"Errores cometidos: {game.errors}/{game.max_errors}")
        print(f"Intentos restantes: {game.max_errors - game.errors}")
        if game.guessed_letters:
            letters_str = ", ".join(sorted(set(game.guessed_letters)))
            print(f"Letras intentadas: {letters_str}")

        raw_input = input("\nIngresa una letra: ")
        is_valid, message_or_letter = validate_input(
            raw_input, game.guessed_letters
        )

        if not is_valid:
            print(f"\n[!] Error: {message_or_letter}")
            continue

        is_correct = game.process_guess(message_or_letter)
        if is_correct:
            print(f"\n[+] ¡Bien hecho! La letra '{message_or_letter}' esta.")
        else:
            print(f"\n[-] La letra '{message_or_letter}' no esta.")

    print("\n" + "=" * 45)
    print(draw_hangman(game.errors))
    if game.is_won():
        print(f"\n¡FELICIDADES! Adivinaste la palabra: '{game.word}'")
    else:
        print(f"\n¡FIN DEL JUEGO! La palabra era: '{game.word}'")
    print("=" * 45)


def main():
    """Bucle principal que permite jugar multiples partidas."""
    while True:
        play_game()
        again = input("\n¿Quieres volver a jugar? (s/n): ").strip().lower()
        if again != 's':
            print("\n¡Gracias por jugar! Hasta pronto.\n")
            break


if __name__ == "__main__":
    main()
