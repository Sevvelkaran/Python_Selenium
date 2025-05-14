import pytest
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage  

@pytest.mark.usefixtures("setupandteardown")
class TestSearch:

    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product("HP LP3065")
        home_page.click_search_button()
        search_page = SearchPage(self.driver)
        # assert search_page.display_status_of_valid_product().is_displayed(), "Valid product was not displayed"

