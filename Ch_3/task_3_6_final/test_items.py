import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_check_basket_button(browser):
    browser.get(link)
    button_here = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button_here, "Button not found"
    time.sleep(7)
