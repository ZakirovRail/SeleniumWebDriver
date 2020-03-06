# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True


import os

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

with open('test.txt', 'w', encoding='utf-8') as file:
    file.write("test line")
