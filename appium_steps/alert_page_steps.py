from appium_page_object.alert_views_page import AlertViewsPage
from appium_steps.base_steps import BaseSteps



class AlertPageSteps(BaseSteps):
    def __init__(self, driver):
        super(AlertPageSteps, self).__init__(driver)
        self.alert_page = AlertViewsPage(driver)

    def open_alert_views_page(self):
        return self.alert_page.open_okay_cancel_alert()


