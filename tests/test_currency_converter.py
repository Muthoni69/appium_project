from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from calculator_project.base_page import BasePage
from calculator_project.main_page import MainPage
from calculator_project.ConverterPage import ConverterPage
from calculator_project.locators import MyLocators

from calculator_project.calculator_page import CalculatorPage

from selenium.webdriver.support import expected_conditions as EC

import time

def test_currency_conversion():
    base_page = BasePage()
    driver = base_page.driver

    try:
        main_page = MainPage(driver)
        main_page.handle_popup()

        time.sleep(5)
        main_page.navigate_to_converter()
        calculator_project = ConverterPage(driver)

        #Select source currency
        calculator_project.click_currency_button()

        assert calculator_project.scroll_and_select_currency("British Pound GBP"), "Source currency not found"

        #Select the target currency

        assert calculator_project.scroll_and_select_currency("Kenyan Shilling KES"), "Target currency not found"

        #Enter amount to convert
        first_digit = input("Enter first currency digit: ")
        calculator_project.enter_number(first_digit)

        second_digit = input("Enter second currency digit: ")
        calculator_project.enter_number(second_digit)

        third_digit = input("Enter second currency digit: ")
        calculator_project.enter_number(third_digit)

        #Get conversion results by first locating the result container
        result_container_locator = (AppiumBy.ID, "com.miui.calculator:id/unit_view_container")
        wait = WebDriverWait(driver, 10)
        result_element = wait.until(EC.visibility_of_element_located(result_container_locator))


        #Extract the dynamic conversion result text
        conversion_result_text = result_element.text.strip()
        print(f"Extracted conversion result: {conversion_result_text}")

        #Assert against the expected result
        expected_rate = 135.0  # Example exchange rate
        expected_result = 100 * expected_rate
        tolerance = 5.0  # Allow for some rounding difference

        try:
            actual_result = float(conversion_result_text)
            assert abs(actual_result - expected_result) <= tolerance, \
                f"Assertion failed: Expected KES result for 100 USD to be within +/- {tolerance} of {expected_result}, but got '{actual_result}'"
        except ValueError:
            assert False, f"Assertion failed: Could not convert result '{conversion_result_text}' to a float."

        print("Test Passed: Currency conversion successful!")

    finally:
        base_page.teardown()

if __name__ == "__main__":
    test_currency_conversion()






