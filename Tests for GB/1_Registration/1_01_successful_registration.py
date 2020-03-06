"""
Описание теста для ручного тестирования.

Название - Успешная решистрация используя валидные логин и пароль

Предварительное условие:
Используемый логи не существует в базе (не использовался ранее для регистрации)

Щаги
1. Открыть страницу https://geekbrains.ru/
2. В поле E-mail  ввести валидный адресс электронной почты
3. В поле Пароль ввести пароль, не менее 6-и символов, например qwerty
4. Нажать на кнопку "Зарегистрироваться"

Ожидаемый результат:
1. Пользователь перенаправлен на новую страницу с сообщением о необходимости активировать аккаунт
"Активируйте аккаунт!"
2. На странице есть текст "Чтобы окунуться в море полезных материалов об IT и digital, найдите письмо от GeekBrains
в своем почтовом ящике и перейдите по ссылке"
3. На странице есть текст "Не получили письмо?"
4. На странице есть ссылка для отпарвки формы повторно "Отправить повторно"
5. На странице есть ссылка на главную страницу GeekBrains
6. На странице есть счетчик, сколько на платформе зарегистрировано пользователей
7. На странице в футере страницы есть указание о защите авторских прав
8. На странице есть ссылка на пользвоательское соглашение
9. На странцие есть ссылка на политику конфиденциальности

"""
from selenium import webdriver
import time
import math
import random

link = "https://geekbrains.ru/"
variable = "".join(map(str, [random.randint(0, 10) for i in range(5)]))  # генератор произвольного числа из 5 цифр
email = "test+" + str(variable) + "@gmail.com"  # составляем произвольный адресс почты
print(email)
password = "qwerty"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    email_input = browser.find_element_by_name("user[email]")
    email_input.send_keys(email)
    name_filed = browser.find_element_by_name("user[password]")
    name_filed.send_keys(password)
    reg_button = browser.find_element_by_id("registration-form-button")
    time.sleep(2)
    reg_button.click()

    time.sleep(3)
    new_page_conf = browser.find_element_by_class_name("confirm-page__body-item-title")
    new_page_conf_text = new_page_conf.text
    assert "Активируйте аккаунт!" == new_page_conf_text, "Отсутствует или не верен элемент 'Активируйте аккаунт!'"

    new_page_conf_long = browser.find_element_by_class_name("confirm-page__body-item-text")
    new_page_conf_long_text = new_page_conf_long.text
    assert "Чтобы окунуться в море полезных материалов об IT и digital, найдите письмо от GeekBrains в своем почтовом ящике и перейдите по ссылке" == new_page_conf_long_text, "Отсутствует или не верен элемент 'Чтобы окунуться в море полезных материалов...'"

    new_page_conf_question = browser.find_element_by_css_selector(".confirm-page__body-item-text-help p")
    new_page_conf_question_text = new_page_conf_question.text
    assert "Не получили письмо?" == new_page_conf_question_text, "Отсутствует или не верен  элемент 'Не получили письмо?'"

    # new_page_conf_link = browser.find_element_by_css_selector(".text-primary href='//confirmation//new'")
    new_page_conf_link = browser.find_element_by_link_text("Отправить повторно")
    new_page_conf_link_text = new_page_conf_link.text
    assert "Отправить повторно" == new_page_conf_link_text, "Отсутствует кнопка 'Отправить повторно'"

    # надо добавить проверку наличия Лого со ссылкой на главную страницу
    new_page_conf_counter = browser.find_element_by_class_name("header-tel-number")
    new_page_conf_counter_text = new_page_conf_counter.text
    assert new_page_conf_counter_text

    new_page_conf_coun_txt = browser.find_element_by_class_name("header-tel-info")
    new_page_conf_coun_txt_text = new_page_conf_coun_txt.text
    assert "Человек уже с нами" == new_page_conf_coun_txt_text, "Отсутствует или не верен элемент 'Человек уже с нами'"

    new_page_conf_coun_right = browser.find_element_by_css_selector(
        "div.confirm-page__footer-wrapper-item:nth-child(1)")
    new_page_conf_coun_right_text = new_page_conf_coun_right.text
    assert "© 2010 - 2020 Geekbrains." == new_page_conf_coun_right_text, "Отсутствует или не верен элемент '© 2010 - 2020 Geekbrains.'"

    # добавить проверку, что есть ссылка на пользовательское соглашение
    # css selector = div.confirm-page__footer-wrapper-item:nth-child(2)

    # добавить проверку, что есть ссылка на политику конфиденциальности
    # css selector = div.confirm-page__footer-wrapper-item:nth-child(3)
finally:
    browser.quit()
