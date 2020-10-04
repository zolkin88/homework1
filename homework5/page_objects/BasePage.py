from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):
    TIME_TO_WAIT = 5

    def __init__(self, driver):
        self.driver = driver

    def _input(self, locator, value):
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def _click_element(self, locator):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.element_to_be_clickable(locator)).click()

    def _get_element_text_by_attr(self, locator, attr):
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        return element.get_attribute(attr)

    def _get_element_text(self, locator):
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        return element.text
