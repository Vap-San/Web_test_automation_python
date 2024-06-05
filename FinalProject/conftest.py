import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException
import logging


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser_name = testdata["browser"]

@pytest.fixture(scope="session")
def browser():
    if browser_name == "chrome":
        try:
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)
        except WebDriverException as e:
            logging.error(f"Ошибка при инициализации Chrome WebDriver: {e}")
            raise
    elif browser_name == "firefox":
        try:
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=service, options=options)
        except WebDriverException as e:
            logging.error(f"Ошибка при инициализации Firefox WebDriver: {e}")
            raise
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    yield driver
    driver.quit()






