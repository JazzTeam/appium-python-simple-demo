import unittest
import HtmlTestRunner
from appium import webdriver
from selenium.webdriver.common.by import By

class SimpleAppiumTest(unittest.TestCase):
    def setUp(self):
        capabilities = {}
        capabilities['platformName'] = 'iOS'
        capabilities['platformVersion'] = '11.4'
        capabilities['automationName'] = 'XCUITest'
        capabilities['deviceName'] = 'iPhone 6s'
        capabilities['app'] = '/Users/admin/Library/Developer/Xcode/DerivedData/UICatalog-afswgjckpnkqtebkoffqyuhqtgqq/Build/Products/Release-iphonesimulator/UICatalog.app'
        capabilities['newCommandTimeout'] = '0'

        self.driver = webdriver.Remote('http://192.168.1.126:4723/wd/hub', capabilities)

    def test_simple(self):
        expected_text = 'A Short Title Is Best'

        self.driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="Alert Views"]').click()
        self.driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="Okay / Cancel"]').click()
        self.assertEqual(self.driver.find_element(By.XPATH, '//XCUIElementTypeStaticText[@name="A Short Title Is Best"]').text, expected_text)
        self.driver.find_element(By.XPATH, '//XCUIElementTypeButton[@name="Cancel"]').click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))


