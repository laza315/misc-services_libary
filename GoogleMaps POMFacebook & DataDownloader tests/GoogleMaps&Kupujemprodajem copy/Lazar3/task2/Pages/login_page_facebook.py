from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username_id = "email"
    password_id = "pass"
    button = "login"
    wrong_mail_pass = "//div[@class='_9ay7']"

    def __init__(self, driver):
        self.driver = driver

    def log(self, username, password):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        self.driver.find_element(By.NAME, self.button).click()

    def wrong_mail_n_pass(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.wrong_mail_pass)))
