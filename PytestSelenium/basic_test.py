import pytest

# @pytest.mark.smoke   
# def test_d():
#     print('Hai')

# @pytest.mark.smoke
# @pytest.mark.regression
# @pytest.mark.xfail(reason="i wanted to check that")
# def test_c():
#     a = 10
#     b = 10
#     assert a != b

# @pytest.mark.skip(reason="This is a trial")
# def test_b():
#     a = 10
#     b = 20
#     assert a < b

# @pytest.mark.xfail(reason="i wanted to check that")
# def test_a():
#     a = "arun"
#     b = "arun"
#     assert a.__eq__(b)

# @pytest.mark.parametrize("ip, expected", [(1, 3), (3, 6), (4, 7)])
# def test_parameterize(ip, expected):
#     assert ip + 2 == expected
                        
# --------------------------------------------------------------------------------------#

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize("search_term", [('Selenium'), ('pytest'), ('Python')])
# def test_google_search(search_term):
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get("https://www.google.in")
#     driver.find_element(By.NAME, value="q").send_keys(search_term)
#     time.sleep(6)
#     driver.find_element(By.CLASS_NAME, value = "gNO89b").click()
#     time.sleep(6)
#     driver.quit()

# @pytest.mark.parametrize("browser",[('chrome'), ('firefox')])
# @pytest.mark.parametrize("url", [('https://www.flipkart.com'), ('https://www.amazon.in')])
# def test_browser(browser, url):

#     if browser == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser == 'chrome':
#         driver = webdriver.Chrome()

#     driver.get(url)
#     driver.maximize_window()
#     print(driver.title)
#     driver.quit()

    
# ------------------------------------------------pytest-fixtures--------------------------------------------------

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

def test_validProduct(test_setup_and_teardown):
    driver.find_element(By.NAME, value = "search").send_keys("HP")
    driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH, value = "//h4/a[contains(text(),'HP LP3065')]").is_displayed()

def test_invalid_product(test_setup_and_teardown):
    driver.find_element(By.NAME, value = "search").send_keys("Honda")
    driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH, value = "//input[@id='button-search']/following::h2").is_displayed()

def test_empty_product(test_setup_and_teardown):
    driver.find_element(By.NAME, value = "search").send_keys("")
    driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH, value = "//input[@id='button-search']/following::h2").is_displayed()






