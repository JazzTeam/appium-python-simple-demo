from appium_page_object.base_page import BasePage

class BaseAlert(BasePage):

    cancel_button_selector = '//XCUIElementTypeButton[@name=\"Cancel\"]'

    def cancel_alert(self):
        self.click(self.cancel_button_selector)

    def click_button_by_name(self, name):
        self.click('//XCUIElementTypeButton[@name=\"' + name + '\"]')

