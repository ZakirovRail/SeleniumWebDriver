from selenium import webdriver
import time
import math
import os
import random

link = "https://suninjuly.github.io/alert_accept.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # click on the button
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    browser.switch_to.alert.accept()
    variable = browser.find_element_by_id("input_value").text
    # print(variable)
    # time.sleep(1)
    value_to_put = calc(int(variable))
    # print(value_to_put)

    # time.sleep(1)
    # put an answer
    browser.find_element_by_id("answer").send_keys(str(value_to_put))

    # click on the button
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    time.sleep(4)

except Exception as error:
    print('The following exception occured: ', error)

finally:
    browser.quit()
