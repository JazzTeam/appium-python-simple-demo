from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):

        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_web_element(self, selector):
            return self.driver.find_element(By.CSS_SELECTOR, selector)

    def find_web_element_by_name(self, selector):
        return self.driver.find_element(By.NAME, selector)