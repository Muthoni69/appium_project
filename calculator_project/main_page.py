from appium.webdriver.common.appiumby import AppiumBy

from calculator_project.base_page import BasePage

class MainPage(BasePage):
    CALCULATOR_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Calculator']")
    CONVERTER_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Converter']")
    POPUP_BUTTON = (AppiumBy.ID, "android:id/button1")

    def __init__(self, driver):
        super().__init__(driver)

    def handle_popup(self):
        popup_button = self.find(*self.POPUP_BUTTON)
        popup_button.click()

    def navigate_to_calc(self):
        self.click(self.CALCULATOR_BUTTON)

    def navigate_to_converter(self):
        self.click(self.CONVERTER_BUTTON)

