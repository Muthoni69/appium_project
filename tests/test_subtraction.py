from calculator_project.base_page import BasePage
from calculator_project.calculator_page import CalculatorPage
from calculator_project.main_page import MainPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from calculator_project.locators import MyLocators

def test_subtraction():
    base_page = BasePage()
    driver = base_page.driver

    try:
        main_page = MainPage(driver)
        main_page.handle_popup()

        calculator_project = CalculatorPage(driver)

        first_number = input("Enter the first number: ")
        first_number_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyLocators.numbers[first_number]))

        calculator_project.click_number(first_number)
        calculator_project.click_operator("subtract")

        second_number = input("Enter the second number: ")
        calculator_project.click_number(second_number)

        calculator_project.click_operator("equal")

        expected_result = input("Enter the expected result: ")
        result = calculator_project.get_result()

        assert result.replace("=", "").strip() == expected_result, f"Assertion failed: Expected '{expected_result}', but got '{result.replace("=", "").strip()}'"

        print("Test Passed: Calculation successful!")

    finally:
        base_page.teardown()

if __name__ == "__main__":
    test_subtraction()