import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper

class LoginPage(Selenium_Helper):

    email_WebElement = (By.XPATH, '//input[@id="Email"]')
    password_WebElement = (By.XPATH, '//input[@id="Password"]')
    loginBtn_WebElement = (By.XPATH, '//input[@value="Log in"]')
    logoutBtn_WebElement = (By.XPATH, '//a[@class="ico-logout"]')
    loginIcon_WebElement = (By.XPATH, '//a[@class="ico-login"]')
    error_WebElement = (By.XPATH, '//div[@class="validation-summary-errors"]')
    emailElement = (By.XPATH, '//a[@href="/customer/info"]')

    def __init__(self, driver):
        super().__init__(driver)

    def valid_login(self, username, password):
        try:
            self.webElement_Enter(self.email_WebElement, username)
            self.webElement_Enter(self.password_WebElement, password)
            self.webElement_Click(self.loginBtn_WebElement)
        except TimeoutException as e:
            print(f"Exception occurred: {e}")
            return False

    def invalid_login(self, username, password):
        try:
            self.webElement_Enter(self.email_WebElement, username)
            self.webElement_Enter(self.password_WebElement, password)
            self.webElement_Click(self.loginBtn_WebElement)
            self.clear_text(self.email_WebElement)
            self.clear_text(self.password_WebElement)
        except TimeoutException as e:
            print(f"Exception occurred: {e}")
            return False

    def get_error_message(self):
        error_element = self.find_element(self.error_WebElement)
        return error_element.text

    def get_email(self):
        email_element = self.find_element(self.emailElement)
        return email_element.text