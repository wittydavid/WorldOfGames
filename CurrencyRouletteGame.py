from Game import Game
from currency_converter import CurrencyConverter


class CurrencyRouletteGame(Game):

    def __init__(self):
        super().__init__("CurrencyRouletteGame")

    def get_usd_sum_in_ils(self, amount: int) -> float:
        """Function gets a money amount in Dollars and returns their value in ILS

        :param amount: Amount in dollars
        :return: Amount of dollars in ILS
        """
        try:
            curr_conv = CurrencyConverter()
            ils_sum = curr_conv.convert(amount, 'USD', 'ILS')
            return round(ils_sum, 2)
        except BaseException as e:
            print(e.args)
            self.throw_error("An unexpected Error has occurred")

    def get_money_interval(self, difficulty_lvl: int) -> tuple:
        """Function gets a difficulty level and returns the range of mistake for the game

        :param difficulty_lvl: the game difficulty level
        :return: a tuple that marks a range of mistake for the game
        """
        usd_sum = self.generate_number(100)
        print(f"What do you think the is ILS sum for {usd_sum}$?")
        ils_sum = self.get_usd_sum_in_ils(usd_sum)
        return ils_sum - (5 - difficulty_lvl), ils_sum + (5 - difficulty_lvl)

    def check_user_guess_interval(self, money_intrvl: tuple, usr_guess: int) -> bool:
        """Funcion checks if the users guess is in the range of the game

        :param money_intrvl: The users margin of error where he can guess a number
        :param usr_guess: The users guess attempt
        :return: True if user in range, otherwise false
        """
        if money_intrvl[0] <= usr_guess <= money_intrvl[1]:
            return True
        else:
            return False

    def play(self, diff_lvl):
        """Function runs the game

        :param diff_lvl: User difficulty level
        :return: True if user won, otherswise False
        """
        money_interval = self.get_money_interval(diff_lvl)
        user_guess = self.get_guess_from_user()
        return self.check_user_guess_interval(money_interval, user_guess)
