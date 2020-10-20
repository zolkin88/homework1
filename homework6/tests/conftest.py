import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions
import logging
import pytest
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from .common import MyListener


@pytest.fixture
def create_logger():
    logger = logging.getLogger('test_console_logger')
    ch = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--base_url", default="http://localhost")
    parser.addoption("--path", default="/admin")
    parser.addoption("--selenoid", action="store", default="127.0.0.1")


@pytest.fixture
def get_base_url(request):
    base_url = request.config.getoption("--base_url")
    return base_url


@pytest.fixture
def get_path(request):
    path = request.config.getoption("--path")
    return path


@pytest.fixture
def browser(request, get_base_url, get_path):
    selenoid = request.config.getoption("--selenoid")
    executor_url = f"http://{selenoid}:4444/wd/hub"
    if "chrome" == request.config.getoption("--browser"):
        chrome_options = ChromeOptions
        caps = {"browserName": request.config.getoption("--browser")
                }
        chrome_options.headless = True
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.maximize_window()
        driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    else:
        firefox_options = FirefoxOptions()
        firefox_options.headless = False
        driver = webdriver.Firefox(executable_path='./geckodriver',
                                   options=firefox_options)
        driver.maximize_window()
        driver = EventFiringWebDriver(driver, MyListener())
        #Раскоментировать если нужно запуск на selenoid
        # caps = {"browserName": request.config.getoption("--browser")
        #         }
        # driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)

    def open(path=get_path):
        return driver.get(get_base_url + path)

    driver.open = open
    driver.open()
    yield driver
    driver.quit()
