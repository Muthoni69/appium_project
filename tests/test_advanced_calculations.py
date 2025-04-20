from calculator_project.base_page import BasePage
from calculator_project.main_page import MainPage
from calculator_project.advanced_calculations import AdvancedCalculatorInput

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Handle edge cases eg "Division by zero", negative numbers
def test_advanced_calculations():
    base_page = BasePage()
    driver = base_page.driver

    try:
        main_page = MainPage(driver)
        main_page.handle_popup()

        advanced_input = AdvancedCalculatorInput(driver)

        numbers_input = input("Enter the sequence of numbers (comma-separated, e.g., 10,200,-5): ")
        advanced_input.input_numbers(numbers_input)


        operators_input = input("Enter the sequence of operators (comma-separated, e.g., add,multiply,subtract): ")
        advanced_input.input_operators(operators_input)

        numbers_input = input("Enter the other sequence of numbers (comma-separated, e.g., 10,200,-5): ")
        advanced_input.input_numbers(numbers_input)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(advanced_input.calculator_page.operators["equal"])
            # Access operators through calculator_page
        )
        advanced_input.calculator_page.click_operator("equal")

        expected_result = input("Enter the expected final result: ")
        result = advanced_input.calculator_page.get_result()

        assert result.replace("=",
                              "").strip() == expected_result, f"Assertion failed: Expected '{expected_result}', but got '{result.replace('=', '').strip()}' for input: numbers='{numbers_input}', operators='{operators_input}'"

        print("Test Passed: Advanced calculation successful!")

    finally:
        base_page.teardown()

if __name__ == "__main__":
    test_advanced_calculations()










