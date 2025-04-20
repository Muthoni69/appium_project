from appium.webdriver.common.appiumby import AppiumBy

from calculator_project.base_page import BasePage
from calculator_project.locators import MyLocators


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = MyLocators

        self.operators = {
            "add" : (AppiumBy.ACCESSIBILITY_ID, "plus"),
            "subtract" : (AppiumBy.ACCESSIBILITY_ID, "minus"),
            "division" : (AppiumBy.ACCESSIBILITY_ID, "divide"),
            "multiplication" : (AppiumBy.ACCESSIBILITY_ID, "multiply"),
            "equal" : (AppiumBy.ACCESSIBILITY_ID, "equals"),
            "point": (AppiumBy.ACCESSIBILITY_ID, "point")
        }

        self.clear = (AppiumBy.ACCESSIBILITY_ID, "clear")
        self.display = (AppiumBy.ID, "com.miui.calculator:id/result")
        #self.zero = (AppiumBy.ACCESSIBILITY_ID, "= Can't divide by zero")

    def click_number(self, number):
        self.click(self.locate.numbers[number])

    def click_operator(self, operator):
        self.click(self.operators[operator])

    def clear_function(self):
        self.click(self.clear)

    def get_result(self):
        return self.find(*self.display).text