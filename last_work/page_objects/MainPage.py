from .BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    TITLE = 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    ELEMENT_ENTER = (By.XPATH, "//*[@data-modal-id='new-log-reg']")
    INPUT_EMAIL = (By.ID, "//*[@placeholder='Электронная почта']")
    INPUT_PASSWD = (By.ID, "//*[@placeholder='Введите пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    HREF_FORGET_PASS = (By.XPATH, "//*[@title='Забыли пароль?']")
    LIST_OF_COURSES = (By.XPATH, "//p[text() = 'Курсы']")
    TEST_COURSES = (By.XPATH, "//*[@title='Тестирование']")
    TITLE_TESTING = (By.TAG_NAME, "h1")

    def check_testing_course(self):
        self._place_cursor(self.LIST_OF_COURSES[1])
        element = self.driver.find_element(*MainPage.TEST_COURSES)
        assert element.text == u'Тестирование'
        element.click()
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TITLE_TESTING))

    def check_title(self):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.title_is(self.TITLE))

    def open_registration_form(self):
        self._click_element(self.ELEMENT_ENTER)

    def input_email(self, name):
        self._wait_registration_form(self.HREF_FORGET_PASS)
        self._input(self.INPUT_EMAIL, name)

    def input_pass(self, passwd):
        self._input(self.INPUT_PASSWD, passwd)

    def click_submit_button(self):
        self._click_element(self.SUBMIT_BUTTON)

    def login_user(self, name, passwd):
        self._input(self.INPUT_EMAIL, name)
        self._input(self.INPUT_PASSWD, passwd)
        self.click_submit_button()

    def _wait_registration_form(self, locator):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.element_to_be_clickable(locator))
