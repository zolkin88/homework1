import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions, ChromeOptions, IeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--base_url", default="http://localhost")


@pytest.fixture
def browser(request):
    if "chrome" == request.config.getoption("--browser"):
        chrome_options = ChromeOptions
        chrome_options.headless = True
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.maximize_window()
    else:
        firefox_options = FirefoxOptions()
        firefox_options.headless = False
        driver = webdriver.Firefox(executable_path='./geckodriver', options=firefox_options)
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def get_base_url(request):
    base_url = request.config.getoption("--base_url")
    return base_url
