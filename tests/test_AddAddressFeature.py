import pytest
import logging
import os
import configparser
from selenium.webdriver.common.by import By
from conftest import *
from pages.AddAddressPage import AddAddressPage
from pages.LoginPage import LoginPage

# Path to the config.ini file relative to the root folder
config_file_path = os.path.join(os.path.dirname(__file__), "..", "utils", "config.ini")

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read(config_file_path)

# Get values from the config.ini file
firstname = config['Address']['firstname']
lastname = config['Address']['lastname']
email = config['Address']['email']
company = config['Address']['company']
country = config["Address"]["country"]
city = config['Address']['city']
address1 = config['Address']['address1']
address2 = config['Address']['address2']
postalcode = config['Address']['postalcode']
phoneno = config['Address']['phoneno']
BaseUrl = config['Settings']['base_url']
loginemail = config['ValidCredentials']['email']
loginpassword = config['ValidCredentials']['password']

@pytest.mark.usefixtures("browserSetup")
@pytest.mark.order(3)
class Test_Address:

    # Launching Website and Maximize Window Size
    def setup_class(self):
        self.driver.get(BaseUrl + "login")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.add_address_page = AddAddressPage(self.driver)

    @pytest.mark.addaddress
    # Test Case for Adding new address field
    def test_addAddress(self):
        logging.info("Starting test_addAddress...")
        # Login before adding address
        self.login_page.valid_login(loginemail, loginpassword)
        self.add_address_page.click_addresses_link()
        self.add_address_page.add_Address(firstname, lastname, email, company, country, city, address1, address2, postalcode, phoneno)
        # Assertion
        actual_name = self.add_address_page.getName()
        expected_name = firstname + " " + lastname
        assert actual_name == expected_name, "Address not Added successfully !!!"
        logging.info("Test test_addAddress completed successfully.")

    @pytest.mark.deleteaddress
    # Test Case for Deleting Address
    def test_deleteAddress(self):
        logging.info("Starting test_deleteAddress...")
        status = self.add_address_page.delete_address()
        assert status, "Address not deleted yet !!!"
        logging.info("Test test_deleteAddress completed successfully.")

    # Closing driver
    def teardown_class(self):
        logging.info("Tearing down the test class...")
        self.driver.quit()
