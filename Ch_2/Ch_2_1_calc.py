from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = ("https://suninjuly.github.io/math.html")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number = browser.find_element_by_id("input_value")
    number_text = number.text
    print(number_text)

    result_calc = calc(int(number_text))
    print(result_calc)
    # вставляем полученный оезультат в поле
    put_result = browser.find_element_by_css_selector("input#answer").send_keys(str(result_calc))
    check_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    check_radiobutton = browser.find_element_by_css_selector("[for='robotsRule']").click()
    button_click = browser.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(5)

finally:
    browser.quit()

# 28.82548063489082
