from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
class SearchPage(PageFactory):
    def __init__(self,driver):
        self.driver=driver

    locators={
        'display_status_valid_produc':('xpath','//a[text()="HP LP3065"]')
    }

    def display_status_valid_product(self):
        displayed_product=self.display_status_valid_produc.get_text()
        assert displayed_product=="HP LP3065"