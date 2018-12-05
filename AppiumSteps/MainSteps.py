from AppiumPageObject.MainPage import MainPage
from AppiumSteps.BaseSteps import BaseSteps



class MainSteps(BaseSteps):
    def __init__(self, driver):
        self.page = MainPage(driver)

    def set_values(self, value1, value2):
        self.page.set_text_A(value1)
        self.page.set_text_B(value2)


    def calculate(self):
        self.page.click_calculate()
        self.page.sleep(1)
        return self.page.get_answer()
