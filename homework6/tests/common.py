from selenium.webdriver.support.events import AbstractEventListener
import logging


class MyListener(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.DEBUG)
        self.ch = logging.FileHandler('opencart_with_listener.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

    def before_navigate_to(self, url, driver):
        self.logger.info('Переходим на страницу на страницу:' + url)

    def before_find(self, by, value, driver):
        self.logger.info('Пытаем найти {0} {1}'.format(by, value))

    def after_quit(self, driver):
        self.logger.info('Закрываем браузер!!!')

    def before_click(self, element, driver):
        self.logger.info('Нажимаем на Элемент: ' + element.text)
