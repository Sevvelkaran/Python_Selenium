
import pytest
from selenium.webdriver.common.by import By
import excelRead

test_data = excelRead.get_data("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/PytestTasks/Sausedata.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup_and_tear_down")
class TestLogin2:

    @pytest.mark.standard_user
    def test_standard_user_login(self):
        username, password = test_data[0]  
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='product_label']").text == "Products"

    @pytest.mark.locked_out_user
    def test_locked_out_user_login(self):
        username, password = test_data[1]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert "locked out" in self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    @pytest.mark.problem_user
    def test_problem_user_login(self):
        username, password = test_data[2]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='product_label']").text == "Products"

    @pytest.mark.performance_glitch_user
    def test_performance_glitch_user_login(self):
        username, password = test_data[3]
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='product_label']").text == "Products"
