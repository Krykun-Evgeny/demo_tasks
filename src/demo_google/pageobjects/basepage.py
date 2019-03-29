from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import integers
from values import strings
import allure


class BasePage:
    def validate_element_is_displayed_and_enabled(self, element):
        string_html = self.html_from_element(element)
        with allure.step("Validate that element is displayed and enabled. HTML: {}".format(string_html)):
            assert element.is_displayed(), strings.assert_element_is_not_displayed_message.format(string_html)
            assert element.is_enabled(), strings.assert_element_is_not_enabled_message.format(string_html)

    def validate_title(self, string_eth_title="Google"):
        string_title = self.driver.instance.title
        with allure.step("Validate a current title wth '{}'".format(string_eth_title)):
            assert string_title == string_eth_title, \
                strings.assert_difference_in_titles_message.format(string_eth_title, string_title)

    def validate_url(self, string_eth_url="https://www.google.com.ua/"):
        string_url = self.driver.instance.current_url
        with allure.step("Validate a current URL with '{}'".format(string_eth_url)):
            assert string_eth_url in string_url, strings.assert_url_message.\
                format(string_eth_url, string_url)

    def html_from_element(self, element):
        string_html = ""
        for temp_string in ['innerHTML', 'outerHTML']:
            temp = self.driver.instance.execute_script("return arguments[0].{};".format(temp_string), element)
            if temp:
                string_html = temp
                break
        assert string_html, strings.assert_html_of_element_is_not_defined_message
        return string_html

    @staticmethod
    def find_button(parent_element, locator):
        return WebDriverWait(parent_element, integers.default_timeout).until(
                EC.element_to_be_clickable(locator), strings.assert_element_is_not_clickable_message.format(str(locator)))

