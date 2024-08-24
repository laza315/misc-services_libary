from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        return wait

    def field_inputs(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(
          ec.visibility_of_element_located(by_locator)).send_keys(text)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(by_locator)).click()

    def is_visible(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(by_locator))
        return bool

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

        # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

