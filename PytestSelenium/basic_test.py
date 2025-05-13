
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
                        
# # --------------------------------------------------------------------------------------#
# import pytest

# from selenium.webdriver.common.by import By

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

# @pytest.fixture()
# def test_setup_and_teardown():
#     global driver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://tutorialsninja.com/demo/")
#     yield
#     driver.quit()

# def test_validProduct(test_setup_and_teardown):
#     driver.find_element(By.NAME, value = "search").send_keys("HP")
#     driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
#     assert driver.find_element(By.XPATH, value = "//h4/a[contains(text(),'HP LP3065')]").is_displayed()

# def test_invalid_product(test_setup_and_teardown):
#     driver.find_element(By.NAME, value = "search").send_keys("Honda")
#     driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
#     assert driver.find_element(By.XPATH, value = "//input[@id='button-search']/following::h2").is_displayed()

# def test_empty_product(test_setup_and_teardown):
#     driver.find_element(By.NAME, value = "search").send_keys("")
#     driver.find_element(By.XPATH, value = "//button[@class='btn btn-default btn-lg']").click()
#     assert driver.find_element(By.XPATH, value = "//input[@id='button-search']/following::h2").is_displayed()

# ----------------------------------------------------by using conftest.py------------------------------------------------

# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.by import By




# @pytest.mark.usefixtures("setup_and_tear_down")
# class TestSearch:
#     @pytest.mark.parametrize("search_term", [('Selenium'), ('pytest')])
#     def test_google_search(self, search_term):
#         self.driver.find_element(By.NAME, value="q").send_keys(search_term)
#         time.sleep(6)
#         self.driver.find_element(By.CLASS_NAME, value = "gNO89b").click()
#         time.sleep(6)

#--------------------------------Pytest Function------------------------------------------------


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import read_config


# def setup_function(function):
#     global driver
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get("https://parabank.parasoft.com/parabank/index.htm")

# def teardown_function(function):
#     driver.quit()

# def test_register_page():
#     driver.find_element(By.LINK_TEXT, value = "Register").click()
#     driver.find_element(By.NAME, value = "customer.firstName").send_keys("karan")
#     driver.find_element(By.NAME, value = "customer.lastName").send_keys("karan")
#     driver.find_element(By.NAME, value = "customer.address.street").send_keys("1234")
#     driver.find_element(By.NAME, value = "customer.address.city").send_keys("IND")
#     driver.find_element(By.NAME, value = "customer.address.state").send_keys("TN")
#     driver.find_element(By.NAME, value = "customer.address.zipCode").send_keys("10001")
#     driver.find_element(By.NAME, value = "customer.phoneNumber").send_keys("1234567890")
#     driver.find_element(By.NAME, value = "customer.ssn").send_keys("12312")
#     driver.find_element(By.NAME, value = "customer.username").send_keys("karan123485wd")
#     driver.find_element(By.NAME, value = "customer.password").send_keys("k@0715")
#     driver.find_element(By.NAME, value = "repeatedPassword").send_keys("k@0715")
#     driver.find_element(By.XPATH, value = "//input[@value='Register']").click()
#     assert driver.title == "ParaBank | Customer Created"

# def test_login_page():
#     driver.find_element(By.NAME, value = "username").send_keys("karan123485wd")
#     driver.find_element(By.NAME, value = "password").send_keys("k@0715")
#     driver.find_element(By.XPATH, value = "//input[@value='Log In']").click()
#     assert driver.find_element(By.XPATH, value = "//div[@id='showOverview']/h1").is_displayed()

# ---------------------------------Data driven -------------------------------------------------
@pytest.mark.usefixtures("setup_and_tear_down")
class TestSearch:
    def test_valid_login(self):
        self.driver.find_element(By.ID, value = "login2").click()
        username = read_config.get_config("Login details", "uname")
        password = read_config.get_config("Login details", "pass")
        self.driver.find_element(By.ID, value="loginusername").send_keys(username)
        self.driver.find_element(By.ID, value="loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, value = "//button[text()='Log in']").click() 
        time.sleep(5)
        assert self.driver.find_element(By.ID, value="logout2").is_displayed()

