import pytest
from Lazar3.task2.Pages.login_page_facebook import LoginPage
from Lazar3.task2.Pages.home_page_facebook import HomePage

"""
Test Scenario:
1.Go to Facebook Login Page
2.Verify tittle and insert dummy mail and password. At the end, click to submit 
button and close driver
"""


class TestLogin:

    @pytest.fixture
    def get_url(self, driver):
        driver.get('https://www.facebook.com/')
        yield driver

    def test_log(self, driver, get_url):
        login = LoginPage(driver)
        login.log('maricmatej71@gmail.com', 'loginfacedemo')
        home = HomePage(driver)
        assert home.welcome_func().is_displayed()

    def test_wrong_mail(self, driver, get_url):
        login = LoginPage(driver)
        login.log('maricmatej7@gmail.com', 'loginfacedemo')
        assert login.wrong_mail_n_pass().is_displayed()


