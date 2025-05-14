from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from Utils import consolelogger


class HomePage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
    
    locators={
        'user_name':('CSS',"#username input"),
        'password':('CSS',"#password input"),
        'login_btn':('ID','login-btn'),
        'search_box_field':('name','search'),
        'search_button':('xpath',"//button[@class='btn btn-default btn-lg']")
    }

    def enter_product(self,product_name):
        logger = consolelogger.get_logger()
        self.search_box_field.click()
        logger.info("Clicked on search box")
        self.search_box_field.clear()
        logger.info("Cleared search box")
        self.search_box_field.set_text(product_name)
        logger.info(f"Entered product name: {product_name}")
        
    def click_search_button(self):
        self.search_button.click()
        logger = connsolelogger.get_logger()