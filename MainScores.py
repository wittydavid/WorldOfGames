from flask import Flask, render_template
from shared_func import throw_error
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def get_score_from_file(score_file_name: str) -> int:
    """Function returns the saved player score from a given score file

    :param score_file_name: the score file name
    :return: score value if exists, else -1
    """
    try:
        score_file = open(score_file_name, mode='r')
        try:
            current_score = int(score_file.readlines()[0])
            score_file.close()
            return current_score
        except ValueError as e:
            print(e.args)
            throw_error("Reading score error - numeric value expected")
    except FileNotFoundError as e:
        print(e.args)
        throw_error("Score file doesn't exist")
    except BaseException as e:
        print(e.args)
        throw_error(f"An unexpected error has occurred while trying to access {score_file_name}")
    return BAD_RETURN_CODE


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result')
def result():
    current_score = get_score_from_file(SCORES_FILE_NAME)
    return render_template('result.html', result=current_score)


if __name__ == "__main__":
    app.run(debug=True)
