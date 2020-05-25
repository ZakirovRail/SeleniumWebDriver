import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FillRegPage:

    def fulfill_registration(self, link):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            # fulfill the registration form
            browser.find_element(By.CSS_SELECTOR, "div.first_block .first").send_keys("Test Name")
            browser.find_element(By.CSS_SELECTOR, "div.first_block .second").send_keys("Test Surname")
            browser.find_element(By.CSS_SELECTOR, "div.first_block .third").send_keys("test_email@gmail.com")
            browser.find_element(By.CSS_SELECTOR, "div.second_block .first").send_keys("+1-789456123")
            browser.find_element(By.CSS_SELECTOR, "div.second_block .second").send_keys("Test Address, test street")
            #  click on the Submit button
            browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

            # wait explicitly while appear a text of congratulations
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container h1")))
            congratulations = browser.find_element(By.CSS_SELECTOR, "div.container h1").text
            return congratulations

        finally:
            browser.quit()


class TestUniqueSelector(unittest.TestCase, FillRegPage):
    def test_first(self):
        link = ("https://suninjuly.github.io/registration1.html")
        # call to Class FillRegPage and  his method fulfill_registration()
        congratulations_text = FillRegPage().fulfill_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", congratulations_text)

    def test_second(self):
        link = ("https://suninjuly.github.io/registration2.html")
        # call to Class FillRegPage and  his method fulfill_registration()
        congratulations_text = FillRegPage().fulfill_registration(link)
        self.assertEqual("Congratulations! You have successfully registered!", congratulations_text)


# first_page = FillRegPage()
# print(first_page.fulfill_registration(link="https://suninjuly.github.io/registration1.html"))

if __name__ == "__main__":
    unittest.main()
