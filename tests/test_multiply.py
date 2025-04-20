import time

from calculator_project.base_page import BasePage
from calculator_project.main_page import MainPage
from calculator_project.locators import MyLocators
from calculator_project.calculator_page import CalculatorPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiply():
    base_page = BasePage()
    driver = base_page.driver

    try:
        main_page = MainPage(driver)
        main_page.handle_popup()

        calculator_project = CalculatorPage(driver)

        first_number = input("Enter the first number: ")
        first_number_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyLocators.numbers[first_number]))

        calculator_project.click_number(first_number)
        other_number = input("Enter other number: ")
        calculator_project.click_number(other_number)
        time.sleep(2)

        calculator_project.click_operator("multiplication")
        last_number = input("Enter the last number: ")

        calculator_project.click_number(last_number)
        calculator_project.click_operator("equal")

        expected_result = input("Enter the expected result: ")
        result = calculator_project.get_result()

        assert result.replace("=", "").strip() == expected_result, f"Assertion failed: Expected '{expected_result}', but got '{result.replace("=", "").strip()}'"

        print("Test Passed: Calculation successful!")

    finally:
        base_page.teardown()

if __name__ == "__main__":
    test_multiply()



