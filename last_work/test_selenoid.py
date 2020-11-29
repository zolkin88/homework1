from selenium import webdriver

capabilities = {
    "browserName": "firefox",
    "browserVersion": "82.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get("https://otus.ru")
