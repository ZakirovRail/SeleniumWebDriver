import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def calc_answer():
    answer = math.log(int(time.time()))
    yield answer


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_check_pages(calc_answer, browser, link):
    # browser.implicitly_wait(2)
    browser.get(link)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    browser.find_element_by_css_selector("textarea").send_keys(str(calc_answer))
    browser.find_element_by_css_selector("button.submit-submission").click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".attempt-message_correct")))
    browser.find_element_by_css_selector("span.attempt-wrapper__result-icon.svg-icon.correct_icon.ember-view")

    feedback = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert feedback == "Correct!", f"Expected message is 'Correct!', but got '{feedback}' "



# The owls are not what they seem! Ovo