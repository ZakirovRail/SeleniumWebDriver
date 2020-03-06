from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el_treasure = browser.find_element_by_id("treasure")
    value_treasure = el_treasure.get_attribute("valuex")
    put_value = calc(int(value_treasure))
    # print(value_treasure)

    browser.find_element_by_id("answer").send_keys(str(put_value))
    # time.sleep(2)

    check_checkbox = browser.find_element_by_id("robotCheckbox").click()
    check_radio = browser.find_element_by_id("robotsRule").click()
    click_button = browser.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(4)

finally:
    browser.quit()

#28.835919021821447