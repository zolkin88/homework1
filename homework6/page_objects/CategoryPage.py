from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryPage(BasePage):
    LIST_GROUP = (By.CLASS_NAME, "list-group")
    ITEMS_IN_GROUP = (By.CLASS_NAME, "list-group-item")

    def check_number_of_categories(self):
        elements = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.LIST_GROUP))
        elements = elements.find_elements(*CategoryPage.ITEMS_IN_GROUP)
        return len(elements)

    def check_first_category_name(self):
        elements = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.LIST_GROUP))
        elements = elements.find_elements(*CategoryPage.ITEMS_IN_GROUP)
        return elements[0].text
