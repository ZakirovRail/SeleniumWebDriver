from selenium import webdriver
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_value = browser.find_element_by_id("input_value").text
    number = calc(int(number_value))
    browser.find_element_by_id("answer").send_keys(number)

    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()


    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-primary").click()

except Exception as error:
    print(' The following exception happened: ', error)
    time.sleep(5)

finally:
    browser.quit()

# 28.881842593755163
