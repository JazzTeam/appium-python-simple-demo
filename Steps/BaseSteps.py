from PageObject.SearchPage import SearchPage
from selenium import webdriver

class BaseSteps:

    def open(self, url):
        self.page = SearchPage(webdriver.Chrome())
        self.page.open(url)

    def quit(self):
        self.page.quit()



