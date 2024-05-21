from pytest import mark
from selenium.common import TimeoutException
import logging

from conftest import *
from pages.LoginPage import LoginPage
import configparser
import os
from pages.RegisterPage import RegisterPage

# Path to the config.ini file relative to the root folder
config_file_path = os.path.join(os.path.dirname(__file__), "..", "utils", "config.ini")

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read(config_file_path)

# Get values from the config.ini file
firstname = config['Registration']['firstname']
lastname = config['Registration']['lastname']
email = config['Registration']['email']
password = config['Registration']['password']
BaseUrl = config['Settings']['base_url']
productName = config['SearchBox']['productName']

@pytest.mark.usefixtures("browserSetup")
@pytest.mark.order(1)
class Test_Register:

    # Launching Website and Maximize Window Size
    def setup_class(self):
        self.driver.get(BaseUrl+"register")
        self.driver.maximize_window()
        self.register_page = RegisterPage(self.driver)

    # Test Case for Registering as New User
    @pytest.mark.register
    def test_registration(self):
        logging.info("Starting registration test...")
        status = self.register_page.register(firstname, lastname, email, password)
        # Assertion
        assert status, "User registration failed !!!"
        logging.info("Registration test completed successfully.")

    @pytest.mark.searchproduct
    # Test Case for Searching a Product on Search-Box
    def test_searchProduct(self):
        logging.info("Starting product search test...")
        status = self.register_page.searchProduct(productName)
        # Assertion
        assert status, "Product search failed !!!"
        logging.info("Product search test completed successfully.")

    # Closing Driver
    def teardown_class(self):
        self.driver.quit()

