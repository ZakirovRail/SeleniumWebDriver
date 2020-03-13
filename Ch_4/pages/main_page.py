from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(browser):
        login_link = browser.find_element_bycss_selector("#login_link")
        login_link.click()
