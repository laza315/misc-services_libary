import time
import collections
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

SCROLL_PAUSE_TIME = 0.8


class HomePage(BasePage):

    navbar = 'header'
    logo = 'img[class="logo"]'
    icons = 'div[class="icons"]'
    gift_menu = '"//div[@class="icons"]//img[1]"'
    notification_menu = '//div[@class="icons"]//img[2]'
    profile_menu = '//div[@class="icons"]//img[3]'
    recognitionform = 'recognitionForm' # By.NAME
    # giving_points_button = '//div[@class="option_bar d-flex justify-content-between"]//img[2]'
    add_person = '//div[@class="left_icons"]//*[@class="icon"][1]'
    input_field = 'input[type="text"]'
    list_of_people = '//ul[@class="search-result"]'
    choose_person_to_add = '//ul[@class="search-result"]//*[1]'
    select_button = '//*[text()=" Select "]'
    points_to_give = '//div[@class="left_icons"]//*[@class="icon"][2]'
    points_text_field = '//input[@placeholder="Add number of points"]'
    confirm_added_points = '//*[text()=" Confirm "]'
    recbox ='textarea'
    recognize_button = 'pickAwardButton'
    last_added_recognition = '//div[@class="display_wrapper"]//h1'
    cant_highfive_yourself_alert = '//div[@class="alert alert-danger person-msg"]'
    deleting_person_pencil = '//*[local-name()="svg" and @id="pencil"]/*[local-name()="path"]'
    next_page = '//button[@aria-label="Next page"]'
    recognition_list = '//div[@class="display_wrapper"]'



    def __init__(self, driver):
        super().__init__(driver)

    def verify_displayed_nav_bar(self):
        self.get_element(By.CLASS_NAME, self.navbar)

    def add_person_for_reco(self, insert_person):
        self.get_element(By.XPATH, self.add_person,ec.element_to_be_clickable).click()
        self.get_element(By.CSS_SELECTOR, self.input_field).click()
        self.get_element(By.CSS_SELECTOR, self.input_field).send_keys(insert_person)
        time.sleep(4)
        list_of_people = self.get_element(By.XPATH, self.list_of_people)
        time.sleep(4)
        print(list_of_people.text)
        self.get_element(By.XPATH, self.choose_person_to_add).click()
        self.get_element(By.XPATH, self.select_button).click()
        time.sleep(2)

    def add_points_for_reco(self, add_points):
        self.get_element(By.XPATH, self.points_to_give).click()
        self.get_element(By.XPATH, self.points_text_field).click()
        self.get_element(By.XPATH, self.points_text_field).send_keys(add_points)
        time.sleep(2)
        self.get_element(By.XPATH, self.confirm_added_points).click()

    def send_recognition(self, send_recognition):
        self.get_element(By.NAME, self.recbox).click()
        self.get_element(By.NAME, self.recbox).send_keys(send_recognition)
        time.sleep(3)
        # self.get_element(By.ID, self.recognize_button, ec.element_to_be_clickable).click()
        # time.sleep(3)

    def giving_recognition(self, enter_name, enter_points, enter_recognition):
        self.add_person_for_reco(enter_name)
        self.add_points_for_reco(enter_points)
        time.sleep(2)
        self.send_recognition(enter_recognition)
        self.get_element(By.ID, self.recognize_button, ec.element_to_be_clickable).click()
        time.sleep(3)
        lista = self.get_element(By.XPATH, self.recognition_list)
        print(lista.text)
        textrec = self.get_element(By.XPATH, self.last_added_recognition).text
        print(textrec)
        assert textrec == 'Bogdan Mitrovic received a recognition from Test Dummy! + 7 points'
        time.sleep(4)

    def giving_rec_to_myself(self, enter_yourself, enter_someone_else):
        self.get_element(By.XPATH, self.add_person, ec.element_to_be_clickable).click()
        self.get_element(By.CSS_SELECTOR, self.input_field).click()
        self.get_element(By.CSS_SELECTOR, self.input_field).send_keys(enter_yourself)
        time.sleep(4)
        self.get_element(By.XPATH, self.choose_person_to_add).click()
        time.sleep(3)
        self.get_element(By.XPATH, self.cant_highfive_yourself_alert, ec.visibility_of_element_located)
        time.sleep(3)
        self.get_element(By.XPATH, self.deleting_person_pencil).click()
        time.sleep(3)
        self.get_element(By.CSS_SELECTOR, self.input_field).click()
        self.get_element(By.CSS_SELECTOR, self.input_field).send_keys(enter_someone_else)
        list_of_people = self.get_element(By.XPATH, self.list_of_people)
        time.sleep(4)
        print(list_of_people.text)
        self.get_element(By.XPATH, self.choose_person_to_add).click()
        self.get_element(By.XPATH, self.select_button).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        next_page = self.get_element(By.XPATH, self.next_page)
        actions = ActionChains(self.driver)
        actions.move_to_element(next_page).click().perform()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        list_length = self.driver.find_elements(By.XPATH, self.recognition_list)
        if (len(list_length)) == 5:
            print("The list is equal to 5 recognitions per page, as we expected")
        else:
            return None

    def is_recognize_button_disabled(self):
        button = self.get_element(By.ID, self.recognize_button)
        assert button.is_enabled() != True

    def recognize_someone_in_inverted_order(self, enter_recognition, enter_person, enter_points):
        self.send_recognition(enter_recognition)
        self.is_recognize_button_disabled()
        self.add_person_for_reco(enter_person)
        self.is_recognize_button_disabled()
        self.add_points_for_reco(enter_points)
        button = self.get_element(By.ID, self.recognize_button)
        assert button.is_enabled() == True
        button.click()
        time.sleep(2)













