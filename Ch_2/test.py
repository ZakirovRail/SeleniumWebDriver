from selenium import webdriver

#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True


# import os
#
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
#
# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write("test line")


import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))
print(answer)
link = "https://stepik.org/lesson/236895/step/1"

browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get(link)
time.sleep(1)
print("sleep 1 sec")
browser.find_element_by_css_selector("textarea").send_keys(str(answer))
# browser.find_element_by_id("ember68").send_keys(answer)
# browser.find_element_by_css_selector("textarea").send_keys(answer)
# browser.find_element_by_css_selector("ember-text-area.ember-view").send_keys(answer)
time.sleep(1)
print("sleep 1 sec")
browser.find_element_by_css_selector("button.submit-submission").click()
WebDriverWait(browser, 2).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, ".attempt-message_correct")))
browser.find_element_by_css_selector("span.attempt-wrapper__result-icon.svg-icon.correct_icon.ember-view")

feedback = browser.find_element_by_css_selector(".smart-hints__hint").text
assert feedback == "Correct!", "You put wrong answer!"