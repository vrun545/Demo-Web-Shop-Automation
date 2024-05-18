import pytest
from selenium.webdriver.common.by import By
from conftest import *
from pages.LoginPage import LoginPage
import configparser
import os

# Path to the config.ini file relative to the root folder
config_file_path = os.path.join(os.path.dirname(__file__), "..", "utils", "config.ini")

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read(config_file_path)

# Get values from the config.ini file
email1 = config['ValidCredentials']['email']
password1 = config['ValidCredentials']['password']
email2 = config['InvalidCredentials']['email']
password2 = config['InvalidCredentials']['password']
BaseUrl = config['Settings']['base_url']


@pytest.mark.usefixtures("browserSetup")
@pytest.mark.order(2)
class Test_Login:

    # Launching Website and Maximize Window Size
    def setup_class(self):
        self.driver.get(BaseUrl+"login")
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    @pytest.mark.invalidlogin
    # Test Case for testing login-feature with Invalid Credentials
    def test_invalidLogin(self):
        self.login_page.invalid_login(email2, password2)
        error_text = self.login_page.get_error_message()
        expected_errors = ["Login was unsuccessful. Please correct the errors and try again.",
                           "No customer account found"]
        # Assertion
        assert any(
            expected_error in error_text for expected_error in expected_errors), "Login was unsuccessful"


    @pytest.mark.validlogin
    # Test Case for testing login-feature with Valid Credentials
    def test_validLogin(self):
        self.login_page.valid_login(email1, password1)
        actual_text = self.login_page.get_email()
        expected_text = email1
        # Assertion
        assert actual_text == expected_text, "Email does not match after login"

    # Closing driver
    def teardown_class(self):
        self.driver.quit()
