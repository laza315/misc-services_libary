import time
from pages.login_page import LoginPage
from config.config import Confiq
import requests


class TestLoginFE:

    def test_get_pages_url(self, driver):
        """ User  requests access to the app
        by calling proper URL

        Test Steps:
        1.Verify call response of given URL
        """
        config = Confiq()
        login = LoginPage(driver)
        # Open the URL pages
        login.page_opens(config.end_point_login)
        #  1.Verify call response of given URL
        response = requests.get(config.high_fiver_url)
        assert response.status_code == 200

    def test_functionality_of_elements(self, driver):
        """This tests case covers functionality
        of every visible element, displayed on LoginPage

        Test Steps:
        1.Go to Login Page
        2.Verifying if pages's Logo is displayed
        3.Verifying if 'Please sign in' output is displayed
        4.Verifying if 'Sign in with Gmail' button is displayed
        5.Verifying is it 'Let's give each other a high five!'output displayed
        6.Verifying that 'Sign in' button is clickable
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to Login Page
        login.page_opens(config.end_point_login)
        # Verifying if pages's Logo is displayed
        assert login.get_the_logo_of_login_page.is_displayed()
        # Verifying if 'Please sign in' output is displayed
        assert login.get_please_signin_text_of_login_page.is_displayed()
        # Verifying is it 'Let's give each other a high five!'output displayed
        assert login.get_welcome_message_of_login_page.is_displayed()
        # Verifying if 'Sign in with Gmail' button is displayed
        assert login.get_google_button_of_login_page.is_displayed()
        # Verifying that 'Sign in' button is clickable
        assert login.is_google_button_on_login_page_clickable

    def test_sign_in_first_time_intern(self, driver):
        """This tests case consists of three well connected parts:
        At first phrase we check whether the user will be allowed to go the Home pages
        on the first login with the correct credentials followed by signing out
        as well as returning to the Login pages
        And, at the end of the day, we want to be sure that same employee who
        logged in a second ago now is at the database, and his user session is
        still runs as we expected

        Test Steps:
        1.Go to Login Page
        2.Click on Sign In button
        3.Assert Google's SignIn Box is displayed
        4.Verify Google's input field for gmail
        5.Insert valid gmail, by that, I mean '-in@sbgenomics.com '
        6.Click on 'Next' btn
        7.Insert valid password and click 'submit' btn
        8.Verify that we are at the HomePage
        9.Click on User profile displayed on Nav bar
        10.Verify that Sign out button is visible on pop up frame
        11.Click on Sign out button
        12.Go back to the login pages
        13.Make sure we are successfully logged out, by displayed LoginPage
        14.Assert Google's SignIn Box is displayed
        15.Verify Google's input field for gmail
        16.Verify all our credentials is displayed(-in@sbgenomics.com)
        17.Click on proper Gmail address
        18.Verify that we are at Home Page
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to Login Page
        login.page_opens(config.end_point_login)
        # enter mail, password and generate valid token in intention to log in
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        # make sure we are at home page
        assert driver.current_url == config.high_fiver_url+config.end_point_home
        # click here in intend to log out
        login.click_on_user_profile_icon()
        time.sleep(4)
        # log out from home page
        login.sign_out_click()
        # make sure we are at login page
        assert driver.current_url == config.high_fiver_url+config.end_point_login
        time.sleep(3)
        login.get_google_button_of_login_page.is_displayed()
        # Now check can you enter as already signed user, in better words, do we remain remembered
        login.sign_in_when_user_is_already_signed_first_time()
        time.sleep(3)
        # make sure we are at home page
        assert driver.current_url == config.high_fiver_url+config.end_point_home
        assert driver.current_url.title() == 'Https://Highfiver.Interns.Sbgpoc.Com/Home'
        # verify tab title
        assert driver.title == "HighFiver"
        time.sleep(3)

    def test_sign_in_first_time_regular_employee(self, driver):
        """Whether the user will be allowed to the Home pages
        on the first login with the correct credentials

        Test Steps:
        1.Go to Login Page
        2.Click on Sign In button
        3.Assert Google's SignIn Box is displayed
        4.Verify Google's input field for gmail
        5.Insert valid gmail, by that, I mean '@sbgenomics.com ' which belongs to db
        6.Clik on 'Next' btn
        7.Insert valid password and click 'submit' btn
        8.Verify that we are at the HomePage
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to  login page
        login.page_opens(config.end_point_login)
        # enter mail, password and generate valid token in intention to log in
        login.credentials_and_token(config.mail_employee, config.password, config.test_dummy_secret)
        # make sure that we are at home page
        assert driver.current_url == config.high_fiver_url+config.end_point_home
        time.sleep(2)

    def test_login_email_not_in_db_private_email(self, driver):
        """Checking if the user can access the home pages
        by sign in with private mail

        Test Steps:
        1.Assert Google's SignIn Box is displayed
        2.Verify Google's input field for gmail
        3.Insert private gmail, by that, I mean ' privatemail@gmail.com '
        4.Clik on 'Next' btn
        5.Insert password and click 'submit' btn
        6.Verify presence of proper message, error code, time stamp
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to  login page
        login.page_opens(config.end_point_login)
        # enter mail and password  in intention to log in
        login.sign_in_with_private_mail(config.private_mail, config.password)
        assert driver.current_url == config.high_fiver_url+config.end_point_login
        time.sleep(3)

    def test_login_email_not_in_db_regular_employee(self, driver):
        """ Checking if the user can access the home pages
        by sign in with @sbgenomics.com mail which doesn't belong to db

        Test Steps:
        1.Assert Google's SignIn Box is displayed
        2.Verify Google's input field for gmail
        3.Insert gmail, by that, I mean ' @sbgenomics.gmail.com '
        4.Clik on 'Next' btn
        5.Insert password and click 'submit' btn
        6.Verify presence of proper message, error code, time stamp
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to Login page
        login.page_opens(config.end_point_login)
        # enter mail, password and generate valid token in intention to log in
        login.credentials_and_token(config.mail_test_database, config.password, config.test_databasecode)
        assert driver.current_url == config.high_fiver_url+config.end_point_login
        # verify logo on login page
        assert login.get_the_logo_of_login_page.is_displayed()
        # as well as button
        assert login.is_google_button_on_login_page_clickable
        # Catching alert massage for failed attempt to enter at home page
        assert login.employee_does_not_exist_message.is_displayed()
        time.sleep(5)

    def test_sign_in_as_experience_manager(self, driver):
        """Whether the experience manager will be allowed to go to the Admin Page
        on the first login with the correct credentials

        Test Steps:
        1.Go to Login Page
        2.Click on Sign In button
        3.Assert Google's SignIn Box is displayed
        4.Verify Google's input field for gmail
        5.Insert valid gmail, by that, I mean 'experience@sbgenomics.com ' which belongs to db
        6.Clik on 'Next' btn
        7.Insert valid password and click 'submit' btn
        8.Verify that we are at the AdminPage
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to Login page
        login.page_opens(config.end_point_login)
        # enter mail, password and generate valid token in intention to log in
        login.credentials_and_token(config.experience_mail, config.password, config.experience_test_secret)
        # make sure we are here where we are as experience
        assert driver.current_url == config.high_fiver_url + config.end_point_admin
        time.sleep(5)

    def test_logging_out_with_two_browser_tabs(self, driver):
        """ Checking whether the user has permission to remain logged in on the
        first card, if he logs out from any other card

        1.Login(first tab)
        2.Verify  HighFiver home pages output is visible(first tab)
        3.Click on the User profile button displayed on NavBar(first tab)
        4.Verify that Sign out button is visible on pop up frame (first tab)
        5.Open second tab
        6.Login with same user and go to home pages
        7.Verify HighFiver home pages output is visible(sec tab)
        8.Click on the User profile button displayed on NavBar(sec tab)
        9.Verify that Sign out button is visible on pop up frame (sec tab)
        10.Click on Sign out button (second tab)
        11.Return to the first tab
        12.Make sure we are successfully logged out , by displayed LoginPage(first tab)
        """
        config = Confiq
        login = LoginPage(driver)
        # Go to Login Page
        login.page_opens(config.end_point_login)
        # enter mail, password and generate valid token in intention to log in
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        # we are at home page, tab 1
        assert driver.current_url == config.high_fiver_url + config.end_point_home
        time.sleep(3)
        # open sec tab
        driver.execute_script("window.open('');")
        # Switch to the new window and open new URL
        driver.switch_to.window(driver.window_handles[1])
        # launch home page url without having previously login
        driver.get(config.high_fiver_url)
        # assert we are at home page at second tab
        assert driver.current_url == config.high_fiver_url + config.end_point_home
        time.sleep(2)
        # click here in intend to log out from second tab
        login.click_on_text_area()
        time.sleep(3)
        login.click_on_user_profile_icon()
        time.sleep(3)
        # sign out from tab 2
        login.sign_out_click()
        # verify that we are successfully sign out from home page
        # at the second tab
        assert driver.current_url == config.high_fiver_url + config.end_point_login
        time.sleep(3)
        # now switch and get back to first tab
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(4)
        # condition is that when clicked anywhere on the page, the user is logged out
        login.click_on_text_area()
        # verify that we are successfully sign out from both tabs
        assert driver.current_url == config.high_fiver_url + config.end_point_login
        time.sleep(3)

