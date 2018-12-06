from appium_page_object.main_page import MainPage
from appium_steps.base_steps import BaseSteps



class MainSteps(BaseSteps):
    def __init__(self, driver):
        super(MainSteps, self).__init__(driver)
        self.main_page = MainPage(driver)

    def open_alert_views_page(self):
        return self.main_page.open_alert_views_page()


