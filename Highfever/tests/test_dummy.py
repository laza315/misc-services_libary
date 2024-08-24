from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_br:


    def test_dummy(self, driver):
        driver.get("https://www.youtube.com/watch?v=d4yDr3loR_I&list=PLFGoYjJG_fqr7PBCFKD9_bXN9mRusY_oC&index=9&ab_channel=NaveenAutomationLabs")
        driver.maximize_window()
        driver.close()