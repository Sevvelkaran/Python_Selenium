import pytest
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from Utils import consolelog

class DashboardPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

        self.assign_leave = (By.XPATH, "//p[text()='Assign Leave']")
        self.apply_leave = (By.XPATH, "//p[text()='Apply Leave']")

    def is_assign_leave_displayed(self):
        return self.driver.find_element(*self.assign_leave).is_displayed()

    def is_apply_leave_displayed(self):
        return self.driver.find_element(*self.apply_leave).is_displayed()

        