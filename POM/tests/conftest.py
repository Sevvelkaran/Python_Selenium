import pytest
from selenium import webdriver
from Utils import read_config  # Adjust this path if needed

@pytest.fixture(scope="class")
def setupandteardown(request):
    browser = read_config.get_config("Basic Details", "browser")
    
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported!")

    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = read_config.get_config("Basic Details", "url")
    driver.get(app_url)

    request.cls.driver = driver
    yield
    driver.quit()
