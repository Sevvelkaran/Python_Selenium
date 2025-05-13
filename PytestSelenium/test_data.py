import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import excelReader

@pytest.mark.parametrize("username,password", excelReader.get_data("PytestSelenium/loginData.xlsx","login"
))
class TestLog:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_validlogin(self, username, password):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(5)
        assert self.driver.find_element(By.ID , value ="logout2").is_displayed()
        time.sleep(5)
        self.driver.quit()
