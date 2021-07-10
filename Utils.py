from os import system, name

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """Function cleans the terminal output of a running Python program
    NOTE: Dynamic and works on windows and linux
    """
    # for windows platforms
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix') platforms
    else:
        _ = system('clear')
