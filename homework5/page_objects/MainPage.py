from .BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    TITLE = 'Your Store'

    def check_title(self):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.title_is(self.TITLE))
