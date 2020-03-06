from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

link_1 = "https://suninjuly.github.io/selects1.html"
link_2 = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link_2)

    result = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    browser.find_element_by_css_selector(".btn.btn-default").click()
    time.sleep(5)

finally:
    browser.quit()

# 28.88048050992915
