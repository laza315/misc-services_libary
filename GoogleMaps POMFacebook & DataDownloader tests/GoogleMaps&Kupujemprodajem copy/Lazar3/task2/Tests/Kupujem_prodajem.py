import time

from Lazar3.task2.Pages.home_page_kupujem_prodajem import HomePage


class Test_Kupujem_prodajem:

     def test_kupujem_prodajem(self, driver):
         open = HomePage(driver)
         open.open_url()
         driver.implicitly_wait(5)
         open.insert_what_you_searh_for('Fotoaparat')
         driver.implicitly_wait(6)
         open.verify_displayed_items()
         time.sleep(4)


