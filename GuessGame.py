from Game import Game


class GuessGame(Game):

    def __init__(self):
        super().__init__("GuessGame")

    def compare_results(self, user_guess: int, secret_number: int) -> bool:
        """Function checks if the user guess is the same as the automatically number

        :param user_guess: user guess number
        :param secret_number: Automatically generated number
        :return: True if same, otherwise False
        """
        if user_guess == secret_number:
            return True
        return False

    def play(self, diff_lvl):
        """Function runs the GuessGame

        :param diff_lvl: User difficulty level choice
        :return: True if user won, otherwise False
        """
        secret_number = self.generate_number(diff_lvl)
        user_num = self.get_guess_from_user()
        print(f"Your guess - {user_num} Lucky number - {secret_number}")
        return self.compare_results(user_num, secret_number)
