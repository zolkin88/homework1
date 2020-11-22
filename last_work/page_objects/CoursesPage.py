from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CoursesPage(BasePage):
    USER_NAME = (By.XPATH, "//*[@header2-menu__dropdown-text_name='Дмитрий Золкин']")
    MAIN_LESSONS = (By.CLASS_NAME, "lessons__page")
    LESSONS = (By.TAG_NAME, "a")

    def get_number_of_courses(self):
        elements = self.driver.find_element(*self.MAIN_LESSONS)
        elements = elements.find_elements(*self.LESSONS)
        return len(elements)
