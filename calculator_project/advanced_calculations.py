from appium.webdriver.common.appiumby import AppiumBy

from calculator_project.base_page import BasePage
from calculator_project.calculator_page import CalculatorPage
from calculator_project.locators import MyLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdvancedCalculatorInput(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.calculator_page = CalculatorPage(driver)

    def input_numbers(self, numbers_string):
        numbers = numbers_string.split(',')

        for number in numbers:
            number = number.strip()

            if number:  #Handle potential empty strings
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(MyLocators.numbers[number])
                )
                self.calculator_page.click_number(number)

    def input_operators(self, operators_string):
        operators = operators_string.split(',')

        for operator in operators:
            operator = operator.strip().lower()

            if operator:
                if operator in self.calculator_page.operators: #Access operators through the calculator_page
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(self.calculator_page.operators[operator])
                    )
                    self.calculator_page.click_operator(operator)

                else:
                    print(f"Warning: Operator '{operator}' not found in operators' list.")

                    





