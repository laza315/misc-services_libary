import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class ExperiencePage(BasePage):

    home_page_logo = '//img[@class="logo"]'
    rewards_administration = '//*[text()=" Rewards administration"]'
    view_all_awards_modal = '//div[text()="View all awards"]'
    add_new_award_button = '//div[text()=" Add new award "]'
    back_arrow = '//div[@class="back-div"]'
    delete_button = '//*[@class="gifts_display row mx-0 mb-5"]//div[3]//button[2]'
    edit_button = '//*[@class="gifts_display row mx-0 mb-5"]//div[17]//button[1]'
    cancel_deletion = '//div[@class="d-flex justify-content-end button_box col-lg-12"]//button[1]'
    confirm_deletion = '//div[@class="d-flex justify-content-end button_box col-lg-12"]//button[2]'
    award_name_input = 'award_name'
    award_name_message = '//h2[@id="errorText"]'
    award_value = 'award_value' # ID
    award_desc = 'award_desc'
    drop_down_toggle = '//button[@data-toggle="dropdown"]'
    save_changes = '//*[text()=" Save changes "]'
    radio_button_category = '//ul[@class="dropdown-menu show"]//input[@id="Charity"]'
    search_loop = '//img[@class="slider_icon"][1]'
    search_filter = '//img[@class="slider_icon"][2]'
    filter_btn = '//button[text()=" Filter "]'
    input_field_search = '//*[@placeholder="Search for award"]'
    search_button = '//button[@type="submit"]'
    get_text_from__new_award = '//*[@class="award_name"]'
    no_award_message = '//*[@class="no_awards"]'
    get_text_from_filter_search = '//div[@class="gift_card_2"]//h2[text()="Make some changes"]'
    filter_edit_search = '//li[@class="filter_item"]//input[@id="Charity"]'

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def view_award_modal_displayed_and_functional(self):
        return self.get_element(By.XPATH, self.view_all_awards_modal, ec.element_to_be_clickable)

    @property
    def add_award_modal_displayed_and_functional(self):
        return self.get_element(By.XPATH, self.add_new_award_modal, ec.element_to_be_clickable)

    def click_on_rewards_administration(self):
        self.get_element(By.XPATH, self.rewards_administration).click()

    def click_on_view_awards_model(self):
        self.get_element(By.XPATH, self.view_all_awards_modal).click()

    def get_admin_home_page(self):
        self.get_element(By.XPATH, self.home_page_logo).click()

    def go_back(self):
        self.get_element(By.XPATH, self.back_arrow, ec.element_to_be_clickable).click()

    def deleting_item_from_category(self):
        button = self.driver.find_element(By.XPATH, self.delete_button)
        self.driver.execute_script("arguments[0].click();", button)

    def canceled_deletion(self):
        self.get_element(By.XPATH, self.cancel_deletion).click()

    def confirm(self):
        self.get_element(By.XPATH, self.confirm_deletion).click()

    def check_if_award_was_deleted(self, insert):
        self.get_element(By.XPATH, self.search_loop).click()
        self.get_element(By.XPATH, self.input_field_search).click()
        time.sleep(2)
        self.get_element(By.XPATH, self.input_field_search).send_keys(insert)
        self.get_element(By.XPATH, self.search_button).click()
        time.sleep(3)
        self.get_element(By.XPATH, self.no_award_message).is_displayed()

    def add_new_award_modal(self):
        self.get_element(By.XPATH, self.add_new_award_button).click()

    # add new award methods
    def upload_the_photo(self):
        self.driver.find_element(By.ID, "myFile").send_keys(
            os.getcwd() + "/assets/lama.png")

    def save_changes_button(self):
        button = self.driver.find_element(By.XPATH, self.save_changes)
        self.driver.execute_script("arguments[0].click();", button)

    def error_message(self):
        self.get_element(By.XPATH, self.award_name_message).is_displayed()

    def drop_down_select_the_category(self):
        self.driver.find_element(By.XPATH, self.drop_down_toggle).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.radio_button_category).click()

    def enter_award_name(self, insert):
        self.get_element(By.ID, self.award_name_input).click()
        time.sleep(2)
        self.get_element(By.ID, self.award_name_input).clear()
        self.get_element(By.ID, self.award_name_input).send_keys(insert)

    def enter_award_value(self, insert):
        self.get_element(By.ID, self.award_value).click()
        self.get_element(By.ID, self.award_value).clear()
        self.get_element(By.ID, self.award_value).send_keys(insert)

    def enter_award_description(self, insert):
        self.get_element(By.ID, self.award_desc).click()
        self.get_element(By.ID, self.award_desc).send_keys(insert)

    def check_if_award_was_created(self, insert):
        self.get_element(By.XPATH, self.search_loop).click()
        self.get_element(By.XPATH, self.input_field_search).click()
        time.sleep(2)
        self.get_element(By.XPATH, self.input_field_search).send_keys(insert)
        self.get_element(By.XPATH, self.search_button).click()
        time.sleep(3)
        check_value = self.get_element(By.XPATH, self.get_text_from__new_award).text
        print(check_value)
        assert check_value == insert

    def search_by_filter(self, insert):
        self.get_element(By.XPATH, self.search_filter).click()
        time.sleep(2)
        self.get_element(By.XPATH, self.drop_down_toggle).click()
        time.sleep(2)
        self.get_element(By.XPATH, self.filter_edit_search).click()
        self.get_element(By.XPATH, self.filter_btn).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        check_value = self.get_element(By.XPATH, self.get_text_from_filter_search).text
        print(check_value)
        assert check_value == insert

    def upload_new_award(self, enter_award_name, enter_value, enter_description):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.save_changes_button()
        self.error_message()
        self.enter_award_name(enter_award_name)
        self.save_changes_button()
        self.error_message()
        self.enter_award_value(enter_value)
        self.save_changes_button()
        self.error_message()
        self.enter_award_description(enter_description)
        self.save_changes_button()
        self.error_message()
        self.drop_down_select_the_category()
        self.save_changes_button()
        self.error_message()
        self.upload_the_photo()
        self.save_changes_button()
        self.check_if_award_was_created(enter_award_name)

    def edit_award(self, enter_award_name):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)
        button = self.driver.find_element(By.XPATH, self.edit_button)
        self.driver.execute_script("arguments[0].click();", button)
        self.enter_award_name(enter_award_name)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.drop_down_select_the_category()
        self.upload_the_photo()
        self.save_changes_button()
        self.search_by_filter(enter_award_name)








