from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from values import strings
from values import integers
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        with allure.step("Finding components of the main page"):
            self.driver = driver
            webdriver_waiter = WebDriverWait(self.driver.instance, integers.default_timeout)
            self.body = webdriver_waiter.until(
                EC.presence_of_element_located((
                    By.ID, strings.main_page_id_body)),
                strings.id_is_not_present_timeout_message.format(strings.main_page_id_body))
            self.image = WebDriverWait(self.body, integers.default_timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, strings.main_page_tag_img)),
                strings.main_page_tag_timeout_message.format(strings.main_page_id_body, strings.main_page_tag_img))
            self.form_searching = webdriver_waiter.until(EC.presence_of_element_located(
                (By.ID, strings.main_page_id_searchform)),
                strings.id_is_not_present_timeout_message.format(strings.main_page_id_searchform))
            self.input_searching = self.find_input_searching()
            self.div_main_buttons = webdriver_waiter.until(EC.presence_of_element_located(
                (By.CLASS_NAME, strings.main_page_class_FPdoLc)),
                strings.class_is_not_present_timeout_message.format(strings.main_page_class_FPdoLc))
            self.searching_button = BasePage.find_button(self.div_main_buttons, (By.NAME, strings.main_page_name_btnK))
            self.luck_button = BasePage.find_button(self.div_main_buttons, (By.NAME, strings.main_page_name_btnI))
            self.drop_down_element = None

    def find_input_searching(self):
        list_inputs = WebDriverWait(self.form_searching, integers.default_timeout).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, strings.main_page_tag_input)),
            strings.main_page_inputs_timeout_message)
        input_with_defined_class = None
        for temp_input in list_inputs:
            temp_string = temp_input.get_attribute(strings.main_page_attribute_class)
            if temp_string:
                input_with_defined_class = temp_input
                break
        assert input_with_defined_class, strings.main_page_input_with_defined_class_is_not_found_assert_message
        return input_with_defined_class

    @allure.step("Verify a visibility of the main image")
    def validate_image_is_visible(self):
        assert self.image.is_displayed(), strings.main_page_img_is_not_displayed_assert_message

    @allure.step("Verify the attribute 'alt = Google'")
    def validate_images_attribute_by_eth_string(self, string_eth_alt_attribute="Google"):
        string_value_of_alt = self.image.get_attribute(strings.main_page_attribute_alt)
        assert string_value_of_alt == string_eth_alt_attribute, \
            strings.main_page_img_assert_message.format(strings.main_page_attribute_alt,
                                                        string_eth_alt_attribute, string_value_of_alt)

    @allure.step("Verify the input of searching")
    def validate_input_searching(self):
        assert self.input_searching.is_enabled(), strings.main_page_input_enabling_assert_message

    @allure.step("Verify main buttons (searching, luck)")
    def validate_buttons_of_searching_and_luck(self):
        for temp_button in [self.searching_button, self.luck_button]:
            BasePage.validate_element_is_displayed_and_enabled(self, temp_button)

    @allure.step("Searching")
    def searching(self, string_query="TEST"):
        with allure.step("Define a query: {}".format(string_query)):
            self.input_searching.send_keys(string_query)
        with allure.step("Verify a value of input"):
            current_value = self.input_searching.get_attribute(strings.main_page_attribute_value)
            assert current_value == string_query, strings.main_page_difference_in_values_assert_message.\
                format(string_query, current_value)
        with allure.step("Wait a drop-down list"):
            self.drop_down_element = WebDriverWait(self.form_searching, integers.default_timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, strings.main_page_class_UUbT9)),
                strings.main_page_element_with_class_is_not_visible_assert_message.format(
                    strings.main_page_class_UUbT9))
            with allure.step("Reassigning of the search's button"):
                self.searching_button = BasePage.find_button(self.drop_down_element,
                                                             (By.NAME, strings.main_page_name_btnK))
        with allure.step("Click on the 'Search' button"):
            self.searching_button.click()

