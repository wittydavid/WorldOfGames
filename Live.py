from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from shared_func import throw_error
from Score import add_score
from Utils import SCORES_FILE_NAME


def get_user_number_input() -> int:
    """Function gets an input from the user

    :return: User number input
    """
    try:
        user_number = int(input())
    except ValueError as e:
        print(e.args)
        throw_error("Invalid input - must be natural number")
    return user_number


def check_number_in_range(start_range: int, end_range: int, num: int) -> bool:
    """Function checks if a number is within a given range

    :return: True if number in range, False if number not in range
    """
    if start_range > end_range:
        throw_error("In a 'range' - The starting point can not be higher than the end point")
    if start_range <= num <= end_range:
        return True
    else:
        return False


def welcome(name: str) -> str:
    """Function returns a welcome message with provided user name.

    :return: Welcome message with provided user name.
    :param name: Username.
    """
    return f"""Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
"""


def run_game(game_pick, diff_pick):
    if game_pick == 1:
        memory_game = MemoryGame()
        return memory_game.play(diff_pick)
    elif game_pick == 2:
        guess_game = GuessGame()
        return guess_game.play(diff_pick)
    elif game_pick == 3:
        curr_game = CurrencyRouletteGame()
        return curr_game.play(diff_pick)


def load_game() -> bool:
    """Function gets user inputs: game choice, difficulty level

    :return: True if player won, otherwise - False
    """
    print(f"""Please choose a game to play:
\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
\t2. Guess Game - guess a number and see if you chose like the computer
\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    game_choice = get_user_number_input()
    if check_number_in_range(1, 3, game_choice):
        print("Please choose game difficulty from 1 to 5:")
    else:
        throw_error("Invalid input - number must be in 1-3 range")
    level_choice = get_user_number_input()
    if check_number_in_range(1, 5, level_choice):
        if run_game(game_choice, level_choice):
            add_score(level_choice, SCORES_FILE_NAME)
            return True
        else:
            return False
    else:
        throw_error("Invalid input - number must be in 1-5 range")
