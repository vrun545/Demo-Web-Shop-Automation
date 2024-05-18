from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Helper:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # This function finds an element
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # This function is for sending keys to Search-Box
    def webElement_Enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # This function is for clicking the Web-Element
    def webElement_Click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    # This function is for clearing the pre-written data on Search-Box
    def clear_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
