from shared_func import throw_error as out_source_error_throw
import random


class Game:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is a {self.name} object"

    def get_guess_from_user(self):
        """Function gets the users input

        :return: The users choice number
        """
        try:
            user_number = int(input("Please enter your guess: "))
        except ValueError as e:
            print(e.args)
            out_source_error_throw("Invalid input - must be natural number")
        return user_number

    def generate_number(self, difficulty_lvl):
        """Function returns a random number in a given range

        :param difficulty_lvl: random number range
        :return: The generated random number
        """
        return random.randint(1, difficulty_lvl)

    def throw_error(self, err_msg):
        out_source_error_throw(err_msg)
