from appium_page_object.base_alert import BaseAlert
from appium_steps.base_steps import BaseSteps



class BaseAlertSteps(BaseSteps):
    def __init__(self, driver):
        super(BaseAlertSteps, self).__init__(driver)
        self.alert = BaseAlert(driver)

    def cancel_alert(self):
        self.alert.cancel_alert()


