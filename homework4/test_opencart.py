from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Проверям, что мы находимся на главной странице Opencart
def test_title(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url)
    WebDriverWait(browser, 5).until(
        EC.title_is('Your Store'))


# Проверям, что мы находимся на странице категорий
def test_category_page(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/index.php?route=product/category&path=20")
    category = browser.find_element_by_class_name("list-group")
    category = category.find_elements_by_class_name('list-group-item')
    assert len(category) == 10
    assert category[0].text == u'Desktops (13)'


# Проверям, что мы находимся на страница товара "Samsung Galaxy Tab 10.1"
def test_samsung_card(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/index.php?route=product/product&path=57&product_id=49")
    samsung = browser.find_element_by_id('content')
    samsung = samsung.find_element_by_tag_name('h1')
    assert samsung.text == u'Samsung Galaxy Tab 10.1'


# Проверям, что мы находимся на страница логина
def test_login_page(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/index.php?route=account/login")
    login = browser.find_element(By.XPATH, "//strong[text()='Register Account']")
    login = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//strong[text()='Register Account']")))
    assert login.text == u'Register Account'


# Проверям, что мы находимся на страница админа
def test_admin_page(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/admin/")
    admin = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "panel-title")))
    assert admin.text == u'Please enter your login details.'


def test_login(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/admin/")
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-username"))).send_keys('user')
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-password"))).send_keys('bitnami1')
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
    user = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@alt = 'John Doe']")))
    assert user.get_attribute('alt') == u'John Doe'


def test_product_table(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/admin/")
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-username"))).send_keys('user')
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-password"))).send_keys('bitnami1')
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
    catalog = browser.find_element(By.ID, "menu-catalog")
    catalog.click()
    catalog.find_elements(By.TAG_NAME, "li")[1].click()
    table = browser.find_element(By.CLASS_NAME, "table-responsive")
    assert table is not None


def test_logout(browser, get_base_url):
    base_url = get_base_url
    browser.get(base_url + "/admin/")
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-username"))).send_keys('user')
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input-password"))).send_keys('bitnami1')
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = 'Logout']"))).click()
    admin = browser.find_element_by_class_name("panel-title")
    assert admin.text == u'Please enter your login details.'
