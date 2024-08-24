import time
from pages.experience_page import ExperiencePage
from config.config import Confiq
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestExperienceManager:

    def test_visibility_and_responsiveness_of_elements(self, driver):
        """ This test case covers functionality
        of every visible element, displayed on Admin Page

        1.Initial setup
        2.Verify displayed elements and check their ability(Nav bar,User cart, Rewards Administration,
        3.View all awards, Add new Award)
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.end_point_login)
        login.credentials_and_token(config.experience_mail, config.password, config.experience_test_secret)
        assert driver.current_url == config.high_fiver_url+config.end_point_admin
        home = HomePage(driver)
        home.verify_displayed_nav_bar()
        admin = ExperiencePage(driver)
        assert admin.view_award_modal_displayed_and_functional.is_displayed()
        assert admin.add_award_modal_displayed_and_functional.is_displayed()
        time.sleep(3)

    def test_view_all_awards(self, driver):
        """ We check these whether the admin sees the displayed elements,
        such as editing and deleting them.
        We also check whether it can move freely in the modals

        1.Initial setup
        2.Click on 'Rewards administration' modal
        3.Click on 'View all awards' modal
        4.Check current url with endpoint /admin/all
        5.Click on 'back arrow' button that leading as to admin page
        6.Verify current url at end point '/admin/rewards'
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.end_point_login)
        login.credentials_and_token(config.experience_mail, config.password, config.experience_test_secret)
        assert driver.current_url == config.high_fiver_url + config.end_point_admin
        admin = ExperiencePage(driver)
        admin.click_on_rewards_administration()
        admin.click_on_view_awards_model()
        assert driver.current_url == config.high_fiver_url+ config.award_end_point
        admin.go_back()
        admin.get_admin_home_page()
        time.sleep(3)
        assert driver.current_url == config.high_fiver_url+config.end_point_admin
        time.sleep(3)

    def test_delete_an_award(self, driver):
        """ A test that checks whether the admin can delete certain award
        and whether the ordinary user can see the deleted element

        1.Initial setup
        2.Click on 'Rewards administration' modal
        3.Go to 'View all awards' modal
        4.Click on delete button for some prize
        5.Verify that pop up modal has appeared
        6.Click 'cancel' button
        7.Click on delete button for second time
        8. Do the click to confirm in order to  delete it
        9.Verify one item less then it was before
        10. Do the search by text
        11.Click on text area field
        12.Type the name of the award we just delete
        13.Verify displayed message 'Unfortunately, there are no results for your search.'
        14. Sign out as a Admin
        15.Sign in as regular employee
        16.Go to award modal
        17. Do the search by text and filter to make sure that prize was succesfully delete
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.end_point_login)
        login.credentials_and_token(config.experience_mail, config.password,config.experience_test_secret)
        assert driver.current_url == config.high_fiver_url + config.end_point_admin
        admin = ExperiencePage(driver)
        admin.click_on_rewards_administration()
        admin.click_on_view_awards_model()
        assert driver.current_url == config.high_fiver_url + config.award_end_point
        time.sleep(2)
        admin.deleting_item_from_category()
        admin.canceled_deletion()
        admin.deleting_item_from_category()
        admin.confirm()
        admin.check_if_award_was_deleted("Hat")
        time.sleep(3)

    def test_edit_award(self, driver):
        """ A test that checks whether the admin can edit certain awards
        and whether the ordinary user can see the edited element

        1.Initial setup
        2.Click on 'Rewards administration' modal
        3. Go to 'View all awards' modal
        4.Verify current URL /admin/edit
        5. Verify current category name
        6.Change it to another one
        7. Also, change an award's name
        8. Click 'Save changes' button
        9. Do the search by text and filter to make sure the changes were saved successfully
        10. Sign out as an Admin
        11.Sign in as regular employee
        12.Go to award modal
        13. Do the search by filter to make sure that fresh changes made on some item are saved
        """
        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.end_point_login)
        login.credentials_and_token(config.experience_mail, config.password,
                                    config.experience_test_secret)
        assert driver.current_url == config.high_fiver_url + 'admin/home'
        admin = ExperiencePage(driver)
        admin.click_on_rewards_administration()
        admin.click_on_view_awards_model()
        assert driver.current_url == config.high_fiver_url +'admin/all'
        admin.edit_award("Make some changes")
        time.sleep(3)

    def test_add_new_award(self, driver):
        """ Here we check all the restrictions that exist when the experience manager  wants to create a new award.
        These are messages with a guard that prevent the admin from completing the addition of non-grades
        if all conditions are not met and whether the ordinary user can see the new added element

        1.Initial setup
        2.Click on 'Rewards adminitration' modal
        3.Click on "Add new Award" modal
        4.Click 'Save changes' button
        5.Verify displayed message "Award name cannot be empty!"
        6. Enter the name
        7.Click"Save changes" button4.Verify displayed message "Award value cannot be smaller than 1!"
        8.Delete default decimal which is 0, type any number greater then zero
        9.Click "Save changes" button
        10.Verify displayed message "Award description cannot be empty!"
        11.Enter any text in description field
        12.Click "Save changes" button
        13.Verify displayed message "A category must be chosen!"
        14.Click on drop down category menu
        15.Checkbox called 'company store' let it be choosen
        16.Press "save changes" button
        17.Verify displayed message "A photo must be uploaded!"
        18. Do the click to "Choose  file " model
        19.Import an image from your machine
        20.Verify that photo is loaded by the text in the right corner
        21.Click "Save changes" button
        22.On our feed verify presents of new award
        23. Do the search by text and filter to make sure that new award is added
        24. Sign out as a Admin
        25.Sign in as regural employee
        26.Go to award modal
        27. Do the search by text to make sure that new award was added by Experience manager
        """

        config = Confiq
        login = LoginPage(driver)
        login.page_opens(config.end_point_login)
        login.credentials_and_token(config.experience_mail, config.password, config.experience_test_secret)
        assert driver.current_url == config.high_fiver_url +'admin/home'
        admin = ExperiencePage(driver)
        admin.click_on_rewards_administration()
        admin.add_new_award_modal()
        assert driver.current_url == config.high_fiver_url +'admin/rewards'
        time.sleep(3)
        admin.upload_new_award("New award", "7", "opis1")
        time.sleep(3)
        assert driver.current_url == config.high_fiver_url +'admin/all'
        time.sleep(3)


