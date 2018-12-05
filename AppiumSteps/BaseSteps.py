from PageObject.BasePage import BasePage

class BaseSteps:
    def __init__(self, driver):
        self.page = BasePage(driver)

    def open(self, url):

        self.page.open(url)

    def quit(self):
        self.page.quit()



