import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

from helper.selenium_helper import Selenium_Helper

class AddAddressPage(Selenium_Helper):

    # WEB-ELEMENTS
    addBtn_WebElement = (By.XPATH, '//input[@class="button-1 add-address-button"]')
    firstName_WebElement = (By.XPATH, '//input[@id="Address_FirstName"]')
    lastName_WebElement = (By.XPATH, '//input[@id="Address_LastName"]')
    email_WebElement = (By.XPATH, '//input[@id="Address_Email"]')
    company_WebElement = (By.XPATH, '//input[@id="Address_Company"]')
    country_DropDown = (By.XPATH, '//select[@id="Address_CountryId"]')
    city_WebElement = (By.XPATH, '//input[@id="Address_City"]')
    address1_WebElement = (By.XPATH, '//input[@id="Address_Address1"]')
    address2_WebElement = (By.XPATH, '//input[@id="Address_Address2"]')
    postalCode_WebElement = (By.XPATH, '//input[@id="Address_ZipPostalCode"]')
    phoneno_WebElement = (By.XPATH, '//input[@id="Address_PhoneNumber"]')
    saveBtn = (By.XPATH, '//input[@class="button-1 save-address-button"]')
    deleteBtn = (By.XPATH, '//input[@class="button-2 delete-address-button"]')
    addresses_link = (By.XPATH, '//a[text()="Addresses"]')
    nameElement = (By.XPATH, '//strong[text()="John Doe"]')


    def __init__(self, driver):
        super().__init__(driver)

    def select_country(self, country):
        sel = Select(self.driver.find_element(*self.country_DropDown))
        sel.select_by_visible_text(country)

    def delete_address(self):
        self.webElement_Click(self.deleteBtn)
        time.sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        return True

    def add_Address(self, firstname, lastname, email, company, country, city, address1, address2, postalcode, phoneno):
        self.webElement_Click(self.addBtn_WebElement)
        self.webElement_Enter(self.firstName_WebElement, firstname)
        self.webElement_Enter(self.lastName_WebElement, lastname)
        self.webElement_Enter(self.email_WebElement, email)
        self.webElement_Enter(self.company_WebElement, company)
        self.webElement_Enter(self.city_WebElement, city)
        self.webElement_Enter(self.address1_WebElement, address1)
        self.webElement_Enter(self.address2_WebElement, address2)
        self.webElement_Enter(self.postalCode_WebElement, postalcode)
        self.webElement_Enter(self.phoneno_WebElement, phoneno)
        self.select_country(country)
        self.webElement_Click(self.saveBtn)
        time.sleep(1)

    def click_addresses_link(self):
        self.webElement_Click(self.addresses_link)

    def getName(self):
        name_element = self.find_element(self.nameElement)
        return name_element.text
