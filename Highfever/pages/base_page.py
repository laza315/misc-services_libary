from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from config.config import Confiq


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def page_opens(self, end_point):
        config = Confiq
        return self.driver.get(config.high_fiver_url + end_point)

    def get_element(self, by, locator, condition=ec.presence_of_element_located, timeout=10):
        wait = WebDriverWait(self.driver, timeout).until(condition((by, locator)))
        return wait

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).click()
