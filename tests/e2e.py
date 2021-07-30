from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from time import sleep
from shared_func import throw_error
from Utils import BAD_RETURN_CODE


def test_scores_service(url: str, port: int = None) -> bool:
    """Function opens web page with given URL and port number (via selenium).
    Opens score web page and locates user's score. (via element id).

    :param url: Webpage URL
    :param port: Webpage port number
    :return: True if user score is in 1-1000 range, otherwise False.
    """
    if port is None:
        url_string = url
    else:
        try:
            int(port)
        except ValueError as e:
            print(e.args)
            throw_error("URL formatting failed - port must be a number")
        else:
            url_string = url + ":" + str(port)
    chrome_driver = webdriver.Chrome(executable_path="C:\David\selenium\chromedriver_win32\chromedriver.exe")
    try:
        chrome_driver.get(url_string)
        sleep(1)
        chrome_driver.find_element_by_id("score_link").click()
        sleep(1)
        player_score = chrome_driver.find_element_by_id("score").text
        int(player_score)
    except NoSuchElementException as e:
        print(e.args)
        throw_error("Failed to locate element in web page by it's id")
    except WebDriverException as e:
        print(e.args)
        throw_error(f"URL - {url_string} is unreachable")
    except ValueError as e:
        print(e.args)
        throw_error(f"Score expected to be numeric, got {player_score} instead")
    else:
        sleep(1)
        chrome_driver.close()
        if 1 < int(player_score) < 1000:
            return True
        return False


def main_function():
    """Function calls 'test_scores_service' function with given arguments.
    If 'test_scores_service' returns True -> exit code is 0,
    otherwise exit code is BAD_RETURN_CODE (-1)
    """
    if test_scores_service("http://127.0.0.1", 5000):
        exit(0)
    else:
        exit(BAD_RETURN_CODE)


main_function()
# todo 1. solve driver location dependency
# todo 2. check the difference between driver close and quit
# todo 3. solve getting to url using gcp
# todo 4. clean up aws configuration and installation from this venv and project
