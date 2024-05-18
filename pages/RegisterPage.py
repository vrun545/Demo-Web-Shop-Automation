import time
from selenium.webdriver.common.by import By
from helper.selenium_helper import Selenium_Helper

class RegisterPage(Selenium_Helper):

    gender_RadioBtn = (By.XPATH, '//input[@id="gender-male"]')
    firstName_WebElement = (By.XPATH, '//input[@id="FirstName"]')
    lastName_WebElement = (By.XPATH, '//input[@id="LastName"]')
    email_WebElement = (By.XPATH, '//input[@id="Email"]')
    password_WebElement = (By.XPATH, '//input[@id="Password"]')
    confirmPassword_WebElement = (By.XPATH, '//input[@id="ConfirmPassword"]')
    registerBtn = (By.XPATH, '//input[@id="register-button"]')
    continueBtn = (By.XPATH, '//input[@class="button-1 register-continue-button"]')
    searchBox_WebElement = (By.XPATH, '//input[@id="small-searchterms"]')
    searchBtn = (By.XPATH, '//input[@class="button-1 search-box-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def register(self, firstname, lastname, email, password):
        self.webElement_Click(self.gender_RadioBtn)
        self.webElement_Enter(self.firstName_WebElement, firstname)
        self.webElement_Enter(self.lastName_WebElement, lastname)
        self.webElement_Enter(self.email_WebElement, email)
        self.webElement_Enter(self.password_WebElement, password)
        self.webElement_Enter(self.confirmPassword_WebElement, password)
        self.webElement_Click(self.registerBtn)
        self.webElement_Click(self.continueBtn)
        time.sleep(1)

    def searchProduct(self, productName):
        self.webElement_Enter(self.searchBox_WebElement, productName)
        self.webElement_Click(self.searchBtn)
        time.sleep(1)
