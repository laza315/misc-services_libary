import time
from Lazar3.task2.config.config import MapsURL
import requests as req
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Lazar3.task2.Pages.base_page import BasePage


class HomePage(BasePage):

    searchbox = '//button[@id="hArJGc"]'
    twoinputs = '//div[@class="JuLCid"]'
    drivingmode = '//img[@aria-label="Driving"]'
    textbox1 = (By.XPATH, '//div[@id="directions-searchbox-0"]/div/div/input')
    textbox2 = (By.XPATH, '//div[@id="directions-searchbox-1"]/div/div/input')
    kontejner = '//div[@class = "MlqQ3d Hk4XGb"]'
    options = (By.XPATH, '//button[@class="OcYctc fontTitleSmall XbJon"]')
    highway = (By.XPATH, '//label[text()="Highways"]')
    KM = (By.XPATH, '//label[@for="pane.directions-options-units-km"]')
    routebox = (By.CSS_SELECTOR,'[aria-label="Directions"] > div.m6QErb .MespJc')
    back_button = '//button[@class="ysKsp"]'

    def __init__(self, driver):
        super().__init__(driver)

    def verify_url(self):
        response = req.get(MapsURL)
        assert response.status_code == 200

    def visibility_of_elements(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.searchbox))).click()
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.twoinputs)))

    def destination_route(self, wherefrom, whereto):
        self.driver.find_element(By.XPATH, self.drivingmode).click()
        self.do_click(self.textbox1)
        self.field_inputs(self.textbox1, wherefrom)
        self.do_click(self.textbox2)
        self.field_inputs(self.textbox2, whereto)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(8)

    def option_parameters(self):
        self.is_visible(self.options)
        self.do_click(self.options)
        self.do_click(self.highway)
        self.do_click(self.KM)
        time.sleep(5)
        self.is_visible(self.routebox)
        rute = (WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(self.routebox)))
        print("Available routes", rute)
        print(len(rute)) # TODO ISPISAO SI BROJ PONUDJENIH, ITERIRIAJ KROZ NJIH ZA NAJDUZU RUTU, NO HARDCODING
        get_km_value_1 = self.driver.find_element(By.XPATH, '//div[@id="section-directions-trip-0"]//*[@class="XdKEzd"]').text
        get_km_value_2 = self.driver.find_element(By.XPATH, '//div[@id="section-directions-trip-1"]//*[@class="XdKEzd"]').text
        get_km_value_3 = self.driver.find_element(By.XPATH, '//div[@id="section-directions-trip-2"]//*[@class="XdKEzd"]').text
        for results in rute:
            if get_km_value_1 > get_km_value_2 in results.text:
                self.driver.find_element(By.ID, 'section-directions-trip-title-0').click()
                time.sleep(5)
                break
            elif get_km_value_1 < get_km_value_3 in results.text:
                self.driver.find_element(By.ID, 'section-directions-trip-title-2').click()
                time.sleep(5)
                break
            else:
                action = ActionChains(self.driver)
                action.double_click(self.driver.find_element(By.ID, 'section-directions-trip-title-1').click())
                time.sleep(4)
                break
                # self.driver.find_element(By.XPATH, self.back_button).click()

        #
        #     elif get_km_value_2 > get_km_value_1 and get_km_value_2 > get_km_value_3:
        #         route_sec.click()
        #         time.sleep(5)
        #         break
        #     else:
        #         route_third.click()
        #         self.driver.find_element(By.XPATH, self.back_button).click()
        #         time.sleep(5)
    def longest_route_by_spending_time(self):
        pass



