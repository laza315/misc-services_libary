import pytest

from Lazar3.task2.Pages.home_page_bamboo import HomePage
from Lazar3.task2.config.config import BambooURL


class TestBamboo:

    def test_get_url(self, driver):
        driver.implicitly_wait(4)
        # URL Launch
        driver.get(BambooURL)
        bamboo = HomePage(driver)
        bamboo.verify_url()
        bamboo.visibility_of_el()
        driver.implicitly_wait(5)



