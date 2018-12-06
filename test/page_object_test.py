import unittest
import HtmlTestRunner

from appium import webdriver
from appium_page_object.main_page import MainPage


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        capabilities = {}
        capabilities['platformName'] = 'iOS'
        capabilities['platformVersion'] = '11.4'
        capabilities['automationName'] = 'XCUITest'
        capabilities['deviceName'] = 'iPhone 6s'
        capabilities['app'] = '/Users/admin/Library/Developer/Xcode/DerivedData/UICatalog-afswgjckpnkqtebkoffqyuhqtgqq/Build/Products/Release-iphonesimulator/UICatalog.app'
        capabilities['newCommandTimeout'] = '0'

        driver = webdriver.Remote('http://192.168.1.153:4723/wd/hub', capabilities)

        main_steps = MainPage(driver)
        self.alert_views_page = main_steps.open_alert_views_page()

    def test_search_python(self):
        alert_dialog = self.alert_views_page.open_okay_cancel_alert()
        alert_dialog.cancel_alert()

    def tearDown(self):
        self.alert_views_page.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))


