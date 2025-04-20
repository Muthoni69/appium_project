from calculator_project.main_page import MainPage
from calculator_project.base_page import BasePage
from calculator_project.calculator_page import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from calculator_project.locators import MyLocators


def test_addition():
    base_page = BasePage()
    driver = base_page.driver

    try:
        main_page = MainPage(driver) #Instantiate MainPage
        main_page.handle_popup()

        calculator_page = CalculatorPage(driver)

        #Get user input for the first number
        first_number = input("Enter the first number: ")

        # Explicit wait for the first number button to be clickable
        first_number_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyLocators.numbers[first_number]))

        calculator_page.click_number(first_number)
        calculator_page.click_operator("add")

        second_number = input("Enter the second number: ")
        calculator_page.click_number(second_number)

        calculator_page.click_operator("equal")
        expected_result = input("Enter the expected result: ")
        result = calculator_page.get_result()

        assert result.replace("=", "").strip() == expected_result, f"Assertion failed: Expected '{expected_result}', but got '{result.replace('=', '').strip()}'"

        print("Test Passed: Calculation successful!")

    finally:
        base_page.teardown()

if __name__ == "__main__":
    test_addition()
