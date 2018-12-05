from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, xpath_selector):
        self.find_web_element(xpath_selector).click()

    def set_text(self, xpath_selector, text):
        self.find_web_element(xpath_selector).send_keys(text)

    def get_text(self, xpath_selector):
        return self.find_web_element(xpath_selector).text

    def sleep(self, value):
        time.sleep(value)

    def quit(self):
        self.driver.quit()

    def find_web_element(self, selector):
            return self.driver.find_element(By.XPATH, selector)