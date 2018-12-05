from selenium import webdriver
from Steps.SearchSteps import SearchSteps
import unittest

import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.steps = SearchSteps(driver)
        self.steps.open("https://google.com")

    def test_search_python(self):
        str_request = "python"
        self.steps.search(str_request)
        self.assertIn("Welcome to Python.org", self.steps.get_text_first_result())

    def test_search_java(self):
        str_request = "java"
        self.steps.search(str_request)
        self.assertIn(str_request, self.steps.get_text_first_result())

    def test_fail_search(self):
        str_request = "java"
        self.steps.search(str_request)
        self.assertIn("fail_str", self.steps.get_text_first_result())

    def tearDown(self):
        self.steps.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))


