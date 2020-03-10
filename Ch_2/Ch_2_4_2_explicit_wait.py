from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "https://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    time.sleep(1)
    # scroll page down
    field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    # browser.execute_script("window.scrollBy(0, 300);")

    value = browser.find_element_by_id("input_value").text

    value_to_put = calc(int(value))
    print('Value calculated and it is: ', value_to_put)
    # put value into the field
    browser.find_element_by_id("answer").send_keys(str(value_to_put))

    # click the Submit button
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "solve")))
    button.click()
    print(browser.switch_to.alert.text.split(': ')[-1])

except Exception as error:
    print('The following exception appeared: ', error)
finally:
    browser.quit()

#  28.969673955423403