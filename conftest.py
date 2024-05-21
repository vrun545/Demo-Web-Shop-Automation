from datetime import datetime
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from datetime import datetime
from pathlib import Path
import logging

# Import the necessary modules for capturing screenshots
from selenium.common.exceptions import WebDriverException

# Function to configure logging
def configure_logging():
    logs_dir = Path("logs")
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file_path = logs_dir / "test.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        handlers=[
            logging.FileHandler(log_file_path, mode='w')
        ]
    )
    logging.getLogger("wdm").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.ERROR)

# Call the configure_logging function to set up logging
configure_logging()


# Fixture
@pytest.fixture(scope="class", params=["firefox", "chrome", "headless"], autouse=True)
def browserSetup(request):
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        firefox_driver_path = GeckoDriverManager().install()
    elif request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif request.param == "headless":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    request.cls.driver = driver
    yield
    driver.quit()

# setup for html-report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("htmlReports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

# setup for title of report
def pytest_html_report_title(report):
    report.title = "WebShop Test Report"

# Hook function to log additional information when a test fails
# def pytest_runtest_makereport(item, call):
#     if call.when == "call" and call.excinfo is not None:
#         logging.error(f"Test case {item.name} failed. Details: {call.excinfo}")
# Hook function to attach screenshot on extent-report and log additional information when a test fails
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        # Capture screenshot on failure
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        screenshot_path = screenshot_dir / f"{item.name}_{now}.png"
        try:
            item.cls.driver.save_screenshot(str(screenshot_path))  # Convert Path object to string
            logging.info(f"Screenshot captured: {screenshot_path}")
        except WebDriverException:
            logging.error("Failed to capture screenshot")

        # Attach screenshot to the Extent Report
        with open(screenshot_path, "rb") as f:
            allure.attach(f.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

        # Log additional information about the failure
        logging.error(f"Test case {item.name} failed. Details: {call.excinfo}")
