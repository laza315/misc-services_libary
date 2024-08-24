import time
import unittest

from selenium import webdriver
#from Lazar.POMFacebook.Pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setupclass(cls):
        cls.driver = webdriver.Chrome()

    def test_success_login(self):
        driver = self.driver
        self.driver.get("https://www.facebook.com/login/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'facebook').is_displayed()
        time.sleep(3)

        # login = LoginPage(driver)
        # login.enter_username()
        # login.enter_password()
        # login.click_On_Login_Button()

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

# if __name__ == '__main__':
#     unittest.main



