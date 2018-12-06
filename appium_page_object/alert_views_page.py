from appium_page_object.base_page import BasePage
from appium_page_object.base_alert import BaseAlert

class AlertViewsPage(BasePage):

    ok_cancel_alert_selector = '//XCUIElementTypeStaticText[@name=\"Okay / Cancel\"]'

    def open_okay_cancel_alert(self):
        self.click(self.ok_cancel_alert_selector)
        base_alert = BaseAlert(self.driver)
        return base_alert

    def open_alert_by_name(self, name):
        self.click('//XCUIElementTypeStaticText[@name=\"' + name + '\"]')
        base_alert = BaseAlert(self.driver)
        return base_alert

