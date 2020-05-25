import time
from selenium import webdriver


try:
    # инициализируем драйвер браузера
    driver = webdriver.Chrome()

    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
    time.sleep(5)

    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get("https://geekbrains.ru")
    time.sleep(5)
finally:
    # После выполнения всех действий мы не должны забыть закрыть окно браузера
    driver.quit()

