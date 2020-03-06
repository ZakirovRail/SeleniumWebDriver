import os
from selenium import webdriver
import random
import time

variable = "".join(map(str, [random.randint(0, 10) for i in range(5)]))  # генератор произвольного числа из 5 цифр
email = "test+" + str(variable) + "@gmail.com"  # составляем произвольный адресс почты

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name='firstname']").send_keys('Vasiliy')
    browser.find_element_by_css_selector("[name='lastname']").send_keys('Ivanov')
    browser.find_element_by_css_selector("[name='email']").send_keys(email)

    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write("test line")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_css_selector(".btn.btn-primary").click()

    time.sleep(7)

except Exception as error:
    print('The following exception appeared: ', error)

finally:
    browser.quit()

# 28.882751722070946
