import unittest
import HtmlTestRunner

from appium import webdriver
from appium_steps.main_page_steps import MainSteps

class ContactIphoneTest(unittest.TestCase):
    def setUp(self):
        capabilities = {}
        capabilities['platformName'] = 'iOS'
        capabilities['platformVersion'] = '11.4'
        capabilities['automationName'] = 'XCUITest'
        capabilities['deviceName'] = 'iPhone 6s'
        capabilities['app'] = '/Users/admin/Desktop/TestApp-iphonesimulator.app'
        capabilities['newCommandTimeout'] = '0'

        self.driver = webdriver.Remote('http://192.168.1.153:4723/wd/hub', capabilities)
        self.steps = MainSteps(self.driver)


    def tearDown(self):
        self.steps.quit()


    def test2(self):
        self.steps.set_values(5, 7)
        print(self.steps.calculate())

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))