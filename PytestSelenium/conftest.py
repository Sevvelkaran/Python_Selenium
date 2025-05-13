# import time
# from pickle import TRUE
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import read_config
# @pytest.fixture(params = ["chrome", "firefox"], scope="class")
# def setup_and_tear_down(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://www.google.co.in")
#     request.cls.driver=driver
#     yield
#     driver.quit()

@pytest.fixture()
def setup_and_tear_down(request):
    browser = read_config.get_config("Basic Details", "browser")
    driver = None
    if browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("chrome"):
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
    