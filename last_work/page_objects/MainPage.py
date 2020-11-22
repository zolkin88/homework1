from .BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):
    TITLE = 'OZON — интернет-магазин. Миллионы товаров по выгодным ценам'

    def check_title(self):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.title_is(self.TITLE))
