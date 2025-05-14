import pytest
from selenium import webdriver
from Utils import read_config 

@pytest.fixture(scope="class")
def setup_andtear_down(request):
    browser = read_config.get_config("Basic Info", "browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported!")

    driver.maximize_window()
    driver.implicitly_wait(10)

    app_url = read_config.get_config("Basic Info", "url")
    driver.get(app_url)

    # Assign the driver to the test class
    request.cls.driver = driver

    yield
    driver.quit()
