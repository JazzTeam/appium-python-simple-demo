from appium_page_object.base_page import BasePage
from appium_page_object.alert_views_page import AlertViewsPage

class MainPage(BasePage):

    alert_views_selector = '//XCUIElementTypeStaticText[@name=\"Alert Views\"]'

    def open_alert_views_page(self):
        self.click(self.alert_views_selector)
        alert_page = AlertViewsPage(self.driver)
        return alert_page

    def open_page_by_name(self, name):
        self.click('//XCUIElementTypeStaticText[@name=\"' + name + '\"]')
        alert_page = AlertViewsPage(self.driver)
        return alert_page


