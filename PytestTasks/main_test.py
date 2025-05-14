import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import excelRead

@pytest.mark.parametrize("username,password", excelRead.get_data("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/PytestTasks/Sausedata.xlsx", "Sheet1"))
@pytest.mark.usefixtures("setup_and_tear_down")
class TestLogin2:
    def test_validation1(self,username,password):
        self.driver.find_element(By.ID,value="user-name").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,value="password").send_keys(password)
        self.driver.find_element(By.ID,value="login-button").click()
        time.sleep(5)
        if username in ("standard_user", "problem_user", "performance_glitch_user"):
          expected = "Products"

          assert self.driver.find_element(By.XPATH,value="//div[@class='product_label']").text.__eq__(expected)
        else:
           expected="Sorry, this user has been locked out."
           assert expected in self.driver.find_element(By.XPATH,value="//h3[@data-test='error']").text
        self.driver.quit()



