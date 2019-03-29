from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from values import strings
from values import integers
import allure


class SearchPage(BasePage):

    def __init__(self, driver):
        with allure.step("Finding components of the search page"):
            self.driver = driver
            webdriver_waiter = WebDriverWait(self.driver.instance, integers.default_timeout)
            self.srg = webdriver_waiter.until(EC.presence_of_element_located(
                (By.CLASS_NAME, strings.search_page_class_srg)),
                strings.class_is_not_present_timeout_message.format(strings.search_page_class_srg))
            self.list_result_of_searching = self.find_list_g_searching()
            self.foot = None
            self.foot_tbody = None
            self.update_foot_with_foot_tbody()

    def update_foot(self):
        return WebDriverWait(self.driver.instance, integers.default_timeout).until(
            EC.presence_of_element_located((By.ID, strings.search_page_id_foot)),
            strings.id_is_not_present_timeout_message.format(strings.search_page_id_foot))

    def update_foot_tbody(self):
        return WebDriverWait(self.foot, integers.default_timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, strings.search_page_tag_tbody)),
            strings.search_page_tag_is_not_defined_timeout_message.format(strings.search_page_tag_tbody))

    def update_foot_with_foot_tbody(self):
        self.foot = self.update_foot()
        self.foot_tbody = self.update_foot_tbody()

    def find_list_g_searching(self):
        return WebDriverWait(self.srg, integers.default_timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, strings.search_page_class_g)),
            strings.search_page_elements_with_class_are_not_visible_timeout_message.format(
                strings.search_page_class_g))

    def find_list_td_foot(self):
        return WebDriverWait(self.foot_tbody, integers.default_timeout).until(EC.presence_of_all_elements_located(
            (By.TAG_NAME, strings.search_page_tag_td)),
            strings.search_page_elements_with_tag_are_not_present_timeout_message.format(
            strings.search_page_tag_td))

    def find_string_number_of_active_page(self):
        list_td = self.find_list_td_foot()
        for temp_td in list_td:
            if temp_td.get_attribute(strings.search_page_attribute_class) == strings.search_page_eth_attribute_class:
                return temp_td.text

    def validate_the_page_of_searching(self, string_eth_number="1"):
        with allure.step("Verify the page's number with '{}'".format(string_eth_number)):
            string_page_number = self.find_string_number_of_active_page()
            assert string_page_number == string_eth_number, strings.search_page_difference_in_pages_assert_message.\
                format(string_eth_number, string_page_number)

    def validate_results_of_searching(self):
        with allure.step("Validate an amount of searching"):
            assert len(self.list_result_of_searching) > 0, strings.search_page_results_are_not_found_assert_message

    def find_dict_page_number_with_td_element(self):
        dict_result = {}
        for temp_td in self.find_list_td_foot():
            dict_result[temp_td.text] = temp_td
        return dict_result

    def click_on_defined_page_of_searching(self, string_defined_page='2'):
        with allure.step("Click on the {} page".format(string_defined_page)):
            dict_page_number_with_td = self.find_dict_page_number_with_td_element()
            for temp_number in list(dict_page_number_with_td.keys()):
                if temp_number == string_defined_page:
                    dict_page_number_with_td[temp_number].click()
                    break
            self.update_foot_with_foot_tbody()

    def validate_page_switching(self):
        with allure.step("Validate that previous results of searching are not state"):
            return WebDriverWait(self.driver.instance, integers.default_timeout).until(
                EC.staleness_of(self.srg), strings.search_page_the_previous_srg_is_attached.format(
                    strings.search_page_class_srg))


