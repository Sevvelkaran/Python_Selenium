import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import read_config

@pytest.fixture()
def setup_and_tear_down(request):
    browser = read_config.get_config("Basic Details", "browser")
    driver = None
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        print("Invalid browser name")
    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = read_config.get_config("Basic Details", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
