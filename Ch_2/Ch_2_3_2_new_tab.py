from selenium import webdriver
import time
import math
import random
import re


link = "https://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_tab = browser.window_handles[0]

    # click on the crazy button
    time.sleep(1)
    browser.find_element_by_tag_name("button").click()
    time.sleep(2)

    # switch to a new window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    variable = browser.find_element_by_id("input_value").text
    value_to_put = calc(int(variable))
    browser.find_element_by_id("answer").send_keys(str(value_to_put))

    # click on the Submit button
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    time.sleep(5)

    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    print(text)

    # alternative way to copy value
    # print(browser.switch_to.alert.text.split(': ')[-1])

except Exception as error:
    print('The following exception occured: ', error)

finally:
    browser.quit()

#  28.926385351066294
