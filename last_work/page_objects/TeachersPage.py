from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TeachersPage(BasePage):
    TEACHERS_ON_PAGE = (By.CLASS_NAME, 'teachers')
    TEACHERS_NAME = (By.CLASS_NAME, 'teacher__name')

    def check_teacher_in_list(self, name):
        elements = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TEACHERS_ON_PAGE))
        elements = elements.find_elements(*self.TEACHERS_NAME)
        names = []
        for el in elements:
            names.append(el.text)
        assert name in names
        return name
