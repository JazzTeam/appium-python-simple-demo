from appium_page_object.main_page import MainPage
from appium_steps.base_steps import BaseSteps
from appium import webdriver

class MainSteps(BaseSteps):
    def __init__(self):
        capabilities = {}
        capabilities['platformName'] = 'iOS'
        capabilities['platformVersion'] = '11.4'
        capabilities['automationName'] = 'XCUITest'
        capabilities['deviceName'] = 'iPhone 6s'
        capabilities['app'] = '/Users/admin/Library/Developer/Xcode/DerivedData/UICatalog-afswgjckpnkqtebkoffqyuhqtgqq/Build/Products/Release-iphonesimulator/UICatalog.app'
        capabilities['newCommandTimeout'] = '0'

        driver = webdriver.Remote('http://192.168.1.126:4723/wd/hub', capabilities)

        super(MainSteps, self).__init__(driver)
        self.main_page = MainPage(driver)

    def open_alert_views_page(self):
        return self.main_page.open_alert_views_page()






