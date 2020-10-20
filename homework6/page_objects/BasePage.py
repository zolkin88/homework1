from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class BasePage(object):
    TIME_TO_WAIT = 5

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.DEBUG)
        self.ch = logging.FileHandler('opencart.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

    def _input(self, locator, value):
        self.logger.info(u'Ждем появления элемента ' + locator[1])
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        self.logger.info(u'Очищаем элемент ' + locator[1])
        element.clear()
        self.logger.info(u'Вводим в элемент значение ' + value)
        element.send_keys(value)

    def _click_element(self, locator):
        self.logger.info(u'Нажимаем на элемент ' + locator[1])
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.element_to_be_clickable(locator)).click()

    def _get_element_text_by_attr(self, locator, attr):
        self.logger.info(u'Получаем значение атрибута {0} у локатора {1} '.format(attr, locator[1]))
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        return element.get_attribute(attr)

    def _get_element_text(self, locator):
        self.logger.info(u'Получаем текст у локатора {0} '.format(locator[1]))
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(locator))
        return element.text
