from PageObject.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

import time

class SearchPage(BasePage):

    search_field = "q"

    def __init__(self, driver):
        self.driver = driver

    def sleep(self, value):
        time.sleep(2)

    def get_search_field(self):
        return self.find_web_element_by_name(self.search_field)

    def search(self, value):
        time.sleep(1)
        imput_field = self.get_search_field()
        imput_field.send_keys(value, Keys.ENTER)
        time.sleep(1)