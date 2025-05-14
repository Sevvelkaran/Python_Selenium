import pytest
import time
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
from Utils.ReadExcel import get_test_data

@pytest.mark.usefixtures("setup_andtear_down")
class TestLogin:
    @pytest.mark.parametrize("username,password,expected_result", get_test_data("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/OrangeHrm/loginData.xlsx", "login"))
    def test_login(self, username, password, expected_result):
        login_page = LoginPage(self.driver)  
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        time.sleep(4)

        if expected_result == "valid":
            assert "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" == self.driver.current_url
        else:
            assert "Invalid credentials" in login_page.error()


    @pytest.mark.parametrize("username,password", get_test_data("/Users/sevvelkaranpalanivetrivel/Desktop/Expleo_Training /Python_Selenium/OrangeHrm/loginData.xlsx","dash"))
    def test_dashboard_elements_after_login(self, username, password):
        
            login_page = LoginPage(self.driver)
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()

            dashboard_page = DashboardPage(self.driver)
            assert dashboard_page.is_assign_leave_displayed(), "Assign Leave is not visible"
            assert dashboard_page.is_apply_leave_displayed(), "Apply Leave is not visible"