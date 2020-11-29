from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonQaPage(BasePage):
    USER_NAME = (By.XPATH, "//*[@header2-menu__dropdown-text_name='Дмитрий Золкин']")
    MAIN_LESSONS = (By.CLASS_NAME, "lessons__page")
    LESSONS = (By.TAG_NAME, "a")
    PYTHON_QA = (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/a[2]/div/div[4]")
    CONTAINER = (By.CLASS_NAME, "container__row")
    CONTAINER_HEAD = (By.TAG_NAME, 'p')

    def get_nearest_courses_date(self):
        elements = self.driver.find_elements(*self.CONTAINER)
        elements = elements[3].find_elements(*self.CONTAINER_HEAD)
        return elements[7].text

    def get_nearest_courses_date_1(self):
        elements = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_all_elements_located(self.CONTAINER))
        elements = elements[3].find_elements(*self.CONTAINER_HEAD)
        return elements[7].text
