from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class LoginAdmin:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/admin/")

    def login_to_admin_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "input-username"))).send_keys('user')
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "input-password"))).send_keys('bitnami1')
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
        print('Это из методка ЛогинАдмин')
