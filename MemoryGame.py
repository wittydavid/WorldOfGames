from Game import Game
from time import sleep


class MemoryGame(Game):

    def __init__(self):
        super().__init__("MemoryGame")

    def generate_sequence(self, difficulty_lvl: int) -> list:
        """Function returns a list of randomly generated numbers

        :param difficulty_lvl: Determines how many numbers will be generated
        :return: list of randomly generated numbers
        """
        secret_list = []
        for i in range(difficulty_lvl):
            secret_list.append(self.generate_number(101))
        return secret_list

    def get_list_from_user(self, difficulty_lvl: int) -> list:
        """Function returns a list of user generated numbers

        :param difficulty_lvl: Determines how many numbers will the user input
        :return: list of generated generated numbers
        """
        guess_list = []
        for i in range(difficulty_lvl):
            guess_list.append(self.get_guess_from_user())
        return guess_list

    def is_list_equal(self, first_list: list, second_list: list) -> bool:
        """Function gets two lists and checks if they are equal

        :param first_list: A list
        :param second_list: Another list
        :return: True if lists are same, otherwise False
        """
        try:
            first_list.sort()
            second_list.sort()
            if first_list == second_list:
                return True
            return False
        except AttributeError as e:
            print(e.args)
            self.throw_error("The function only works with lists")
        except TypeError as e:
            print(e.args)
            self.throw_error("List must only include numbers")

    def play(self, diff_lvl: int) -> bool:
        """Function runs the MemoryGame

        :param diff_lvl: User difficulty level choice
        :return: True if user won, otherwise False
        """
        print(f"Playing Memory Game on level - {diff_lvl}")
        secret_lst = self.generate_sequence(diff_lvl)
        print(secret_lst, end="\r")
        sleep(0.7)
        user_list = self.get_list_from_user(diff_lvl)
        return self.is_list_equal(secret_lst, user_list)
