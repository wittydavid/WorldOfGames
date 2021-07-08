from shared_func import throw_error


def add_score(difficulty: int, score_file_name: str) -> int:
    """Function gets game difficulty level and score file name, reads and updates current score from file if exists
    else, creates new file and places new score in file.

    :param difficulty: game difficulty level
    :param score_file_name: score file name
    :return: 0 if successful, 1 if failure
    """
    try:
        score_file = open(score_file_name, mode='r+')
    except FileNotFoundError as e:
        print("Creating a new score file just for you!")
        score_file = open(score_file_name, mode='w+')
        score_file.write("0")
    except BaseException as e:
        print(e.args)
        throw_error(f"An unexpected error has occurred while trying to access {score_file_name}")
    finally:
        try:
            score_file.seek(0)
            current_score = int(score_file.readlines()[0])
            new_score = current_score + (difficulty * 3) + 5
            score_file.seek(0)
            score_file.write(str(new_score) + "\n")
            score_file.close()
            return 0
        except ValueError as e:
            print(e.args)
            throw_error("Reading score from score file - numeric value expected")
        except BaseException as e:
            print(e.args)
            throw_error(f"An unexpected error has occurred while trying to access {score_file_name}")
    return 1
