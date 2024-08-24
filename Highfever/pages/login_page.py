import time
from pyotp import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    login_page_logo = 'brand_logo'
    pleaseSignInText = 'signtext'
    google_button = 'buttonDiv'
    click_anywhere_on_page = 'signtext'
    welcomeMsg = 'moto_text'
    username_input_field = 'input[type="email"]'
    pass_input_field = 'input[type="password"]'
    auth_field = 'input[type="tel"]'
    auth_button = 'totpNext'
    next_button = 'identifierNext'
    pass_next_button = 'passwordNext'
    home_page_logo = 'logo'
    user_profile_icon = '//div[@class="header"]//img[@class="icon"][2]'  # old locator, will be used again '//img[@class="icon"][3]'
    sign_out_btn = '//button[text()="Sign Out"]'
    confirm_its_you = '//div[@class="fFW7wc-ibnC6b"]'
    test_dummy_dugme = '//div[@class="K4efff"]'
    confirm_button_for_private_mail = 'confirm_yes'
    close_button_for_private_mail = 'error_close'
    recbox ='textarea'
    employee_with_given_mail_does_not_exist = '//div[@class = "alert alert-danger error"]'

    @property
    def get_the_logo_of_login_page(self):
        return self.get_element(By.CLASS_NAME, self.login_page_logo)

    @property
    def get_please_signin_text_of_login_page(self):
        return self.get_element(By.CLASS_NAME, self.pleaseSignInText)

    @property
    def get_welcome_message_of_login_page(self):
        return self.get_element(By.CLASS_NAME, self.welcomeMsg)

    @property
    def get_google_button_of_login_page(self):
        return self.get_element(By.ID, self.google_button, timeout= 5)

    @property
    def is_google_button_on_login_page_clickable(self):
        return self.get_element(By.ID, self.google_button, condition=ec.element_to_be_clickable, timeout=7)

    def username_input(self, username):
        self.get_element(By.CSS_SELECTOR, self.username_input_field).send_keys(username)
        time.sleep(2)
        self.get_element(By.ID, self.next_button).click()

    def password_input(self, password):
        self.get_element(By.CSS_SELECTOR, self.pass_input_field).send_keys(password)
        time.sleep(2)
        self.get_element(By.ID, self.pass_next_button).click()

    def private_mail_google_steps(self):
        self.get_element(By.ID, self.confirm_button_for_private_mail).click()
        self.get_element(By.ID, self.close_button_for_private_mail).click()

    def sign_in_with_private_mail(self, username, password):
        self.get_google_button_of_login_page.click()
        time.sleep(3)
        window_first = self.driver.window_handles[0]
        self.driver.implicitly_wait(3)
        window_sec = self.driver.window_handles[1]
        self.driver.switch_to.window(window_sec)
        time.sleep(3)
        self.username_input(username)
        time.sleep(3)
        self.password_input(password)
        self.private_mail_google_steps()
        self.driver.switch_to.window(window_first)

    def sign_in_when_user_is_already_signed_first_time(self):
        window_first = self.driver.window_handles[0]
        time.sleep(3)
        hoverable = self.driver.find_element(By.CLASS_NAME, self.click_anywhere_on_page)
        action = ActionChains(self.driver)
        action.move_to_element(hoverable).click_and_hold().perform()
        self.get_element(By.ID, self.google_button, timeout=5).click()
        window_sec = self.driver.window_handles[1]
        self.driver.switch_to.window(window_sec)
        time.sleep(3)
        self.get_element(By.XPATH, self.confirm_its_you).click()
        self.driver.implicitly_wait(3)
        self.driver.switch_to.window(window_first)
        time.sleep(2)

    def credentials_and_token(self, input_mail, input_pass, secret):
        self.get_google_button_of_login_page.click()
        time.sleep(3)
        window_first = self.driver.window_handles[0]
        self.driver.implicitly_wait(3)
        window_sec = self.driver.window_handles[1]
        self.driver.switch_to.window(window_sec)
        self.username_input(input_mail)
        time.sleep(3)
        self.password_input(input_pass)
        time.sleep(3)
        auth_field = self.get_element(By.CSS_SELECTOR, self.auth_field)
        totp = TOTP(secret)
        token = totp.now()
        auth_field.send_keys(token)
        self.get_element(By.ID, self.auth_button).click()
        self.driver.switch_to.window(window_first)
        time.sleep(5)

    def click_on_user_profile_icon(self):
        self.get_element(By.XPATH, self.user_profile_icon).click()

    def sign_out_click(self):
        return self.get_element(By.XPATH, self.sign_out_btn).click()

    @property
    def employee_does_not_exist_message(self):
        return self.get_element(By.XPATH, self.employee_with_given_mail_does_not_exist, ec.visibility_of_element_located)

    @property
    def click_on_text_area(self):
        return self.driver.find_element(By.NAME, self.recbox).click()


