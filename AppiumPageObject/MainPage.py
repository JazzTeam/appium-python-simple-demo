from AppiumPageObject.BasePage import BasePage

class MainPage(BasePage):

    integerATextInput = '//XCUIElementTypeTextField[@name=\"IntegerA\"]'

    integerBTextInput = '//XCUIElementTypeTextField[@name=\"IntegerB\"]'

    computeSumButton = '//XCUIElementTypeButton[@name=\"ComputeSumButton\"]'

    answerTextField = '//XCUIElementTypeStaticText[@name=\"Answer\"]'

    def __init__(self, driver):
        self.driver = driver

    def is_app_installed(self, value):
        self.driver.is_app_installed(value)

    def set_text_A(self, text):
        self.set_text(self.integerATextInput, text)

    def set_text_B(self, text):
        self.set_text(self.integerBTextInput, text)

    def click_calculate(self):
        self.click(self.computeSumButton)

    def get_answer(self):
        return self.get_text(self.answerTextField)
