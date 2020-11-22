from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SamsungPage(BasePage):
    CONTENT = (By.ID, "content")
    SAMSUNG_TITLE = (By.TAG_NAME, "h1")

    def is_samsung_title(self):
        element = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.CONTENT))
        element = element.find_element(*SamsungPage.SAMSUNG_TITLE)
        if u'Samsung Galaxy Tab 10.1' == element.text:
            return True
        else:
            return False



