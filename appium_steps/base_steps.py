from appium_page_object.base_page import BasePage

class BaseSteps:
    def __init__(self, driver):
        self.page = BasePage(driver)

    def quit(self):
        self.page.quit()



