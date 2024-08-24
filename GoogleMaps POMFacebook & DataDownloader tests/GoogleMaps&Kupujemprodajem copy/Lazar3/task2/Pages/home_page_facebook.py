from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    welcome = "//a[@aria-current='page']"

    def __init__(self, driver):
        self.driver = driver

    def welcome_func(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.welcome)))


