import time
import pytest
from pages.home_page import HomePage
from config.config import Confiq
from pages.login_page import LoginPage


class TestHomeAndUserFE:
    def test_visibility_and_responsiveness_of_elements(self, driver):
        """This tests case covers functionality
        of every visible element, displayed on Home Page

        1.Login
        2.Verify HomePage
        3.Verify displayed nav bar
        4.Verify elements in nav bar(Logo,gift,notification bell, profile)
        5.Mouse hover profile button
        6.Verify that picture is getting zoomed
        7.Check is profile button is clickable and click on it
        8.Assert that pop up form  is showing up
        9.Verify elements at pop up(profile picture, account, 'x' button, and Sign out button)
        10.Check click ability of buttons and click on Sign out button
        11.Verify success sign out by  displayed Login pages
        """
        config = Confiq
        home = HomePage(driver)
        home.page_opens(config.end_point_login)
        login = LoginPage(driver)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        home.verify_displayed_nav_bar()
        time.sleep(4)

    def test_giving_a_recognition_to_someone(self, driver):
        """ Giving someone recognition in best possible scenario

        1. Initial setup
        2. Click on add person field
        3. Click on text area before enter any data
        3.Make sure field is clear
        4. Insert 'Bo'
        5. Verify all offered options in a list
        6.Choose one of them
        7.Verify that is correctly entered in field
        8.Click the Select button
        9.Click on add points field
        10. Click on text area before enter any data
        11.Make sure field is clear
        12.Enter corect points(1 to 20)
        13. Click Confirm button
        14.Click on TextArea right below
        15.Make sure it is clear
        16.Check if is 'Recognize' button enabled
        17.Click on it
        18.Verify properly displayed recognition on feed
        """
        config = Confiq
        home = HomePage(driver)
        home.page_opens(config.end_point_login)
        login = LoginPage(driver)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        home.giving_recognition("Bo", "7", "test")
        time.sleep(4)

    def test_assign_myself_recognition(self, driver):
        """ This test tries to give itself a recognition
        and shows that it is not possible

        1. Initial setup
        2. Click on add person field
        3. Click on text area before enter any data
        3.Make sure field is clear
        4.Insert 'Test Du'
        5.Verify all offered options in a list
        6.Choose 'Test Dummy'
        7.Verify displayed alert massage 'You can't HighFiver yourself!'
        8.Verify that Select button is disabled
        9.One click on field
        10.Verify that the alert has disappeared
        11.Enter some other person
        """
        config = Confiq
        home = HomePage(driver)
        home.page_opens(config.end_point_login)
        login = LoginPage(driver)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        home.giving_rec_to_myself('Test Dummy', 'ic')

    def test_iterate_through_list_of_recognition(self, driver):
        """ As a user, I  want to set the number of recognitions
        that will be shown to me on Home Page.
        At the end, are we getting exact number of recognitions we were set?

        1.Initial setup
        2.Scroll to the bottom of page
        3.Set 10 recognition in items per page
        4.Extract list of recognition
        5.Assert that length of list is the same as we set in paginator container
        """
        config = Confiq
        home = HomePage(driver)
        home.page_opens(config.end_point_login)
        login = LoginPage(driver)
        login.credentials_and_token(config.mail_intern, config.password,config.test_dummy_in_secret)
        home.scroll_down()
        time.sleep(5)

    def test_giving_a_recognition_in_inverted_order(self, driver):
        """ Here we're checking whether user may send some recognition
        if he, for instance start from text field,
        then he adds points and at the end add person
        In essence, the user may click at recognize button
        only when all three conditions are met, points, person and text

        1.Initial setup
        2.Insert some text in recognition field
        3.Check is recognize button disabled
        4.Click on add person
        5.Insert any person
        6.Check is recognize button disabled
        7.Click on add points
        8.Insert some number of points
        9.Check is recognize button enabled
        """
        config = Confiq
        home = HomePage(driver)
        home.page_opens(config.end_point_login)
        login = LoginPage(driver)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        home.recognize_someone_in_inverted_order("opis", "Bo", "7")
        time.sleep(2)

    @pytest.mark.manual
    def test_recognition_session_remember_values(self, driver):
        """ Hypothetically we have a situation where the user enters all the data
        and forgets to click the button.
        We check whether the application saves the entered values
        so that the user can end the session multiple times

        1.Initial setup
        2.Click on add person button
        3.Enter someone
        4.Click Select button
        5.Close the popup
        6.Click again on add person button
        7.Verify does the field remebers the user we choose
        """

    @pytest.mark.manual
    def test_choose_a_person(self, driver):
        """
        1.Initial setup
        2.Click on add person field
        3.Enter one character
        4.Verify behavior
        5.Enter two correct name characters
        6.Verify full list
        7.Put a dot in between two characters
        8.Verify behavior
        9.Delete input
        9.Insert number
        10. Verify behavior
        11.Insert valid person, add some number at the end of name
        12. Verify behavior
        """

    @pytest.mark.manual
    def test_points_feature_field(self, driver):

        """
        1.Initial setup
        2.Click on add points field
        3.Click at text area
        4.Make sure it clear
        2. Enter valid number(1 to 20)
        3.Delete
        4.Try to insert float number
        5.Verify proper message ' Please enter a value between 1 and 20.' and disablity of select button
        6.Delete
        7.Try to insert negative number
        8.Verify proper message ' Please enter a value between 1 and 20.', and disablity of select button
        9. Delete
        10.Try to insert some latter or invalid character, for example('e')
        11.Verify proper message ' Please enter a value between 1 and 20.' and disablity of select button
        """

    @pytest.mark.manual
    def test_closing_pop_up_frame(self, driver):
        """This tests case handles functionality
        of User profile frame

        1.Login
        2.Verify HomePage
        3.Go to profile on nav bar and click on user
        4.Assert that pop up form  is showing up
        5.Click on "X" button and verify that pop up window is closed with displayed HomePage
        6.Go to profile on nav bar and click on user
        7.Assert that pop up form  is showing up
        8.Click somewhere else, out of pop up frame
        9.Verify that pop up window is closed with displayed HomePage
        """
        pass

    @pytest.mark.manual
    def test_functionality_of_recognition_text_area(self, driver):
        """ Checking whether User can give any recognition
        to someone by entering some proper amount of
        text into the field followed by a check does
        User receiving message if he tries
        to send empty recognition to some employee

        1.Login
        2.Verify HomePage
        3.Verify recognition form container
        4.Check if recognition nav bar is displayed so as elements itself
        5.Verify input field is displayed
        6.Click on input field form
        7.Make sure that "Add Text" is deleted by clicking into  the field
        8.Verify clear input frame
        9.Check if button is clickable
        10.Click on "recognize" button(without entering anything into  the field)
        11.Check if proper massage for mandatory input is displayed
        12.Close message alert window
        13.Enter some data into the text area(one letter)
        14.Check if button is clickable
        15.Verify responsiveness of "recognize" button by click on it
        """
        pass

    @pytest.mark.manual
    def test_functionality_of_emoji_box(self, driver):
        """Checking whether user can enter more than one smiley face
        in an attempt not to open emoji box twice

        1.Login
        2.Verify Home Page
        3.Verify recognition form container
        4.Check if recognition nav bar is displayed so as elements itself
        5.Verify input field is displayed
        6.Click on input field form
        7.Open the emoji box form
        8.Insert some emoji
        9.Verify that emoji box has closed by entering one emoji character
        10.Open the emoji box form again
        11.Insert some emoji
        12.Verify two entered characters in text area
        """
        pass

    @pytest.mark.manual
    def test_input_field_max_data(self, driver):
        """If we say that total amount of character
        you can send to the field is 360
        (90 character per row times 4 rows).
        At this point we want to check are we still able to give recognition
        to someone and considering that maximum limit of characters,
        we jus checking can we enter above 360
        letters into the text field area intended for recognition

        1.Login
        2.Verify HomePage
        3.Verify input field is displayed
        4.Click on input field form
        5.Make sure that "Add Text" is deleted by clicking into  the field
        6.Verify clear input frame
        7.Enter maximum number of character(which is 360)
        8.Verify is  "recognition" button still clickable
        9.Verify responsiveness of "recognize" button by click on it
        10.Go one step back and clear input text area
        11.Try to enter above 360 characters
        12 .Verify is  "recognition" button still clickable
        """
        pass

    @pytest.mark.manual
    def test_toggle_functionality(self, driver):
        """ Handling switch functionality of
        "I want to make this recognition private " output which covers next topics:

        -If it's not switched to left, User are sending public recognition
         that is displayed on feed of  all users at the system
         and on profile of user who receives the recognition
        -If it's switched to right, User are sending private recognition
         that is displayed only at feed of  user who receives recognition
        as well as on the user's profile

        1.Login
        2.Verify HomePage
        3.Verify recognition form container
        4.Verify if "I want to make this recognition private" switch button is set to public(turned off) by default
        5.Send some data into field
        6.Switch to private
        7.Verify is  "recognition" button still clickable
        8.Delete and clear input field box
        9.Try to move switch button without entering any data
        10.Verify responsiveness of "recognize" button by click on it
        """
        pass

    @pytest.mark.manual
    def test_public_recognition(self, driver):
        """At first, we want to be sure that everyone who is a member of the system
        sees the recognition from one user to the other, on their home pages

        1.Login User No.1
        2.Make sure that toggle button is set to off state
        3.Send public recognition to User No.2
        4.Log out from User No.1
        5.Login User No.2
        6.Verify that recognition given from User No.1 is displayed on my feed
        7.Go to User profile pages
        8.Verify that I have received recognition displayed on my profile as well
        9.Logout from User No.2
        10.Login with User No.3
        11. Verify that recognition given from User No.1 to User No.2 is shown only on my feed
        """
        pass

    @pytest.mark.manual
    def test_private_recognition(self, driver):
        """Secondly, we want to be sure if User who gives recognition to someone
        as well as the one who has receives it
        can see  that recognition on each other Home and Profile pages.
        Accompanied by the condition that no one but them can see the said post

        1.Login User No.1
        2.Make sure that toggle button is set to off state
        3.Switch toggle button on and send private recognition to User No.2
        4.Log out from User No.1
        5.Login User No.2
        6.Verify that recognition given from User No.1 is displayed on my feed
        7.Go to User profile pages
        8.Verify that I have received recognition displayed on my profile as well
        9.Logout from User No.2
        10.Login with User No.3
        11. Check that recognition given from User No.1 to User No.2 is NOT shown on my feed by verifying  something else if any
        """
    @pytest.mark.manual
    def test_hashtags(self):
        """ Check whether user can add a hashtag in recognition area
        1.Initial setup
        2. Click on text area
        3. Enter '#' character
        4.Verify displayed list of  hashtags
        5.Choose  any hashtag in order to insert
        """
