import unittest
from driverfactory.driverfactory import DriverFactory
from values import strings
from pageobjects.mainpage import MainPage
from pageobjects.searchpage import SearchPage


class TestGoogle(unittest.TestCase):

    def setUp(self):
        factory = DriverFactory()
        self.driver = factory.get_driver(strings.browser_name_chrome)
        self.driver.navigate(strings.base_url)

    def test_google_pages(self):
        main_page = MainPage(self.driver)
        main_page.validate_title()
        main_page.validate_url()
        main_page.validate_image_is_visible()
        main_page.validate_images_attribute_by_eth_string()
        main_page.validate_input_searching()
        main_page.validate_buttons_of_searching_and_luck()
        main_page.searching()

        search_page = SearchPage(self.driver)
        search_page.validate_title(string_eth_title=strings.test_google_string_eth_title)
        search_page.validate_url()
        search_page.validate_the_page_of_searching()
        search_page.validate_results_of_searching()
        search_page.click_on_defined_page_of_searching(string_defined_page=strings.test_google_string_defined_page)
        search_page.validate_page_switching()
        search_page.validate_the_page_of_searching(string_eth_number=strings.test_google_string_defined_page)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
