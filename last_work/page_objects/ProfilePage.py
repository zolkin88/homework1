from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    USER_NAME = (By.XPATH, "//*[@title='user']")
    LOG_OUT_BUTTON = (By.XPATH, "//span[text() = 'Logout']")

    def check_user_name(self):
        return self._get_element_text_by_attr(self.USER_NAME, 'alt')

    def log_out(self):
        self._click_element(self.LOG_OUT_BUTTON)
