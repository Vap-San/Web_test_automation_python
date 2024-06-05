import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    url = testdata["base_url"]
#Реализация базового класса работы со страницей. Здесь только основные элементы -поиск элемента и определение его свойств

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Element '{locator}' not found")
    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        return element.value_of_css_property(prop)

    def go_to_site(self):
        return self.driver.get(self.base_url)
