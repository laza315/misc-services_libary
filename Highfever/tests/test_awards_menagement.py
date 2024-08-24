import time

from config.config import Confiq
from pages.login_page import LoginPage
from pages.award_page import AwardPage


class TestAwardManagement:

    def test_visibility_and_responsiveness_of_elements(self, driver):
        """ This test case covers functionality
        of every visible element, displayed on Award Page

        1.Initial setup
        2.Verify current url at end point '/awards'
        3. Verify that we carry the same number of points from the home page
        4. Verify each category is displayed by scrolling down the page: gift
        cards, company store, clothes and charity
        5.Verify Gift card category
        6.Check whether slider arrow(left) button is clickable
        7.Try clicking on  it
        8.Check whether slider arrow(right) button is clickable
        9.Click on it
        10.Verify expected behavior -New items are visible
        11.Scroll up and verify whether '  search loop' and 'filter search '
        are displayed and clickable too
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.high_fiver_url+config.end_point_login)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        assert driver.current_url == config.high_fiver_url+"home"
        award = AwardPage(driver)
        award.get_the_number_of_points()
        award.go_to_award_page()
        assert driver.current_url == config.high_fiver_url+"awards"
        award.get_the_number_of_points()
        award.get_category()
        award.swipe_right_left_through_category()
        time.sleep(3)
        award.search_and_filter_buttons()
        time.sleep(3)

    def test_pick_award_button(self, driver):
        """ This button has two behaviors,
        when it is visible and when it shouldn't be. We check that it works

        1.Login
        2.Verify Home Page
        3.Check whether 'Pick award' button is displayed at user card container
        that containing points
        4.Click on 'pick award button'
        5.Verify current url at end point '/awards'
        6.'Pick award' button shouldn't be displayed on user card container,
        verify that is so
        7.Click on HIghFiver logo to go back one step
        8.Assert current url endpoint '/home'
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.high_fiver_url + config.end_point_login)
        login.credentials_and_token(config.mail_intern, config.password, config.test_dummy_in_secret)
        assert driver.current_url == config.high_fiver_url + "home"
        award = AwardPage(driver)
        award.behavior_of_find_award_button()
        assert driver.current_url == config.high_fiver_url + "awards"
        time.sleep(3)

    def test_categories(self, driver):
        """ Here we're checking  could I, as a User redeem some award

        1.Initial setup
        2.Verify current url at end point '/awards'
        3.Click on any gift item to redeem it
        4.Verify we are at redeem page
        5.Verify that we carry the same number of points from the home page
        6. Check whether redeem button is clickable
        7.Get the current number of points we have
        8.Click on button to claim you award
        9.Verify displayed pop up to finish shopping
        10.Check responsiveness of 'cancel' and 'proceed' buttons
        11.Click on cancel button
        12.Verify that pop up frame has closed
        13.Click on pick award button to claim your award
        14.Click on 'proceed' button
        15.Verify that the number of points has decreased by the value of the
        reward we just bought
        """

    def test_receiving_the_award(self, driver):
        """ Checking can user buy more prizes than he has points
        and thus get himself into the red

        1.Initial setup
        2.Verify number of points we currently have
        3.Choose some award from any category
        4.Click on pick award button
        5.Claim the prize by clicking the button as many times as the prize is
        worth in order to reduce the number of points to zero.
        6.Then try to click again.
        7.verify the received message "you are out of points"
        """
    def test_search_for_award(self, driver):
        """ This test case covers the best possible scenario, where user can do
        the search by valid text and get all displayed items,
        as well as case where user tries to enter some award that's we do not
        offer. Also, here we're checking expected behaviors like, what happened
        if user click on search without entering any data
        or does the last search words is locked in text area since we did the
        previous search

        1. Initial setup
        2.Check is search loop button clickable
        3.Click on it
        4. Make sure pop up has showed
        5.Check whether 'search' is clickable
        6. Do the click
        7.Verify is prompt message "Unfortunately, there are no results for
        your search." displayed
        8.Click again on search loop button
        9.Do the click in text area field
        10. Type some valid text, like 'gift'
        11.Verify and collect all displayed awards containing the search we
        just did
        12. Click again on search loop and verify whether text area still hold
        and remember last search- 'gift' just by clicking it
        13.Try to enter some text
        """

    def test_filter_award(self,driver):
        """ This test case covers the best possible scenario, where the user
        can search by filter
        and get the items of the category they selected.
        Also, if he chooses the select "select all ", the checkbox menu
        automatically turns off the remaining search options

        1. Initial setup
        2. Click on filter button
        3.Verify that pop up has showed
        4.Check if filter button is clickable
        5. Clik on drop-down menu
        6. Make sure that all categories are set it to off by default
        7. Select second category
        8.Verify the number of items for that particular category has displayed
        9.Click again on filter button
        10.Click on drop down menu
        11. Checkbox  called 'select all' set to on
        12.Verify all elements has showed on your feed
        """

    def test_search_and_filter_awards(self, driver):
        """ We check how the communication between the two types of searches
        works
        The idea is to make it impossible to remember the search by search to
        the filter and vice versa.
        The bottom line is that bad text search does not transfer to filter
        search

        1. Initial setup
        2. Do the click to Filter awards button
        3. Click drop down menu
        4. Choose any category
        5. Verify displayed elements
        6. Click on search with loop button
        7. Make sure it is empty
        8. Type some invalid text
        7.Verify is prompt message "Unfortunately, there are no results for
        your search." displayed
        8. Click on filter award button
        9. Do the search by categories
        10. Verify that prompt message is gone
        11.Verify displayed items on page"""

