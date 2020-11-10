from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class LoginClient:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/index.php?route=account/login")

    def login_to_client(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "input-email"))).send_keys('user')
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "input-password"))).send_keys('bitnami1')
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
        print('Это из методка ЛогинКлиент')
