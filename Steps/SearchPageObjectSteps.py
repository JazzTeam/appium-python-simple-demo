from Steps.BaseSteps import BaseSteps

class SearchRobotSteps(BaseSteps):

    def search(self, value):
        self.page.search(value)

    def get_text_first_result(self):
        result_element = self.page.find_web_element(".r h3")
        return result_element.text