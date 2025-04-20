from calculator_project.base_page import BasePage
from calculator_project.main_page import MainPage

def test_navigation():
    base_page = BasePage()  # This initializes the driver
    driver = base_page.driver  # Get the driver instance

    try:
        main_page = MainPage(driver)  # Pass the driver to MainPage
        main_page.handle_popup()

        main_page.navigate_to_calc()
        assert main_page.find(*MainPage.CALCULATOR_BUTTON).is_displayed(), "Calculator page did not open!"

        main_page.navigate_to_converter()
        assert main_page.find(*MainPage.CONVERTER_BUTTON).is_displayed(), "Converter page did not open!"

        print("Test Passed: Navigation to Calculator and Converter was successful!")


    finally:
        base_page.teardown()  # Ensure the driver quits

if __name__ == "__main__":
    test_navigation()




