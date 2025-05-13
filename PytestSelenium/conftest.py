# import time
# from pickle import TRUE
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

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