import time

import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    url = 'https://sbgenomics.bamboohr.com/login.php?r=%2Fhome'
    card = 'fab-Button__text'
    emailinput = 'identifier'
    passinput = 'password'

    def __init__(self, driver):
        self.driver = driver

    def verify_url(self):
        response = requests.get(self.url)
        return response.status_code == 200

    def visibility_of_el(self):
        guidemetogmail = self.driver.find_element(By.CLASS_NAME, self.card)
        guidemetogmail.click()
        ukucaj = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.NAME, self.emailinput)))
        ukucaj.send_keys('lazar.djokovic-in@sbgenomics.com' + Keys.ENTER)
        ukucaj = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.NAME, self.passinput)))
        ukucaj.send_keys('' + Keys.ENTER)
        time.sleep(5)


