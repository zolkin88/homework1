from .BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterAccount(BasePage):
    LOGIN_TITLE = (By.XPATH, "//strong[text()='Register Account']")

    def is_it_registration_page(self):
        login = self.driver.find_element(*RegisterAccount.LOGIN_TITLE)
        if login.text == u'Register Account':
            return True
        else:
            return False
