from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata.get("username")

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):
    def enter_text_intro_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get tst from {element_name}")
            return None
        logging.debug(f"We finde text {text} in field {element_name}")
        return text


# методы ввода текста
    def enter_login(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description=f"Send {word} to element LOGIN_FIELD")
    def enter_pass(self, word):
        self.enter_text_intro_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description=f"Send {word} to element PASS_FIELD")

# Методы, когда мы нажимаем на кнопки или ссылки
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Click login button")
    def click_about(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT"], description="Click About")

#Методы получения текста
    def get_user_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO"])
    def get_about_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ABOUT_PAGE"])
    def get_about_property(self):
        return self.get_element_property(TestSearchLocators.ids["LOCATOR_ABOUT_PAGE"], "font-size")
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])






