import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class AwardPage(BasePage):

    points_to_redeem = 'p[class="points-number redeem"]'
    find_award_button = '//*[text()=" Find award "]'
    categories = '//*[@class="gifts_wrapper"]'
    right_arrow = '//div[@class="gifts_wrapper"][1]//img[@src="../../assets/static/arrow_right.png"]'
    left_arrow = '//div[@class="gifts_wrapper"][1]//img[@src="../../assets/static/arrow_left.png"]'
    search_loop = '//img[@class="slider_icon"][1]'
    search_filter = '//img[@class="slider_icon"][1]'



    def __init__(self, driver):
        super().__init__(driver)

    def get_the_number_of_points(self):
        points = self.get_element(By.CSS_SELECTOR, self.points_to_redeem).text
        print(points)

    def go_to_award_page(self):
        self.get_element(By.XPATH, self.find_award_button).click()

    def get_category(self):
        categories = self.get_element(By.XPATH, self.categories).text
        print(categories)

    def swipe_right_left_through_category(self):
        arrowright = self.get_element(By.XPATH, self.right_arrow)
        action = ActionChains(self.driver)
        action.double_click(arrowright)
        arrowleft = self.get_element(By.XPATH, self.left_arrow)
        action.double_click(arrowleft)
        time.sleep(2)

    def search_and_filter_buttons(self):
        self.get_element(By.XPATH, self.search_loop, ec.element_to_be_clickable).is_enabled()
        self.get_element(By.XPATH, self.search_filter, ec.element_to_be_clickable).is_enabled()

    def behavior_of_find_award_button(self):
        self.get_element(By.XPATH, self.find_award_button, ec.visibility_of_element_located)
        self.go_to_award_page()
        self.get_element(By.XPATH, self.find_award_button, ec.invisibility_of_element_located)


