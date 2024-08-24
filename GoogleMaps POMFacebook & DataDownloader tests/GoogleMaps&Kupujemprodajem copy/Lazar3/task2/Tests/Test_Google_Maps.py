import time

import pytest
from Lazar3.task2.Pages.home_page_maps import HomePage
from Lazar3.task2.config.config import MapsURL


class TestGoogleMaps:

    def test_google_maps(self, driver):
        #creating object for URL, click and visibility methods
        home = HomePage(driver)
        #callinf funcions
        home.driver.get(MapsURL)
        home.verify_url()
        home.visibility_of_elements()
        home.destination_route('Budapest, Hungary', 'Belgrade')
        home.option_parameters()
        time.sleep(7)


