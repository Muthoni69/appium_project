import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder #For creating an action sequence


from calculator_project.base_page import BasePage
from calculator_project.locators import MyLocators

class ConverterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locate = MyLocators

    def click_currency_button(self):
        self.click(self.locate.currency_button)

    def scroll_and_select_currency(self, currency_name, timeout=10, max_scrolls=10):
        """Scrolls through the currency list and selects the given currency."""
        currency_icon = self.find(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/icon1").instance(0)')
        currency_icon.click()
        time.sleep(2)

        currency_list = AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('android:id/list')"

        scrollable_element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(currency_list))
        start_y = scrollable_element.location['y'] + int(scrollable_element.size['height'] * 0.8)
        end_y = scrollable_element.location['y'] + int(scrollable_element.size['height'] * 0.2)
        start_x = scrollable_element.location['x'] + int(scrollable_element.size['width'] * 0.5)

        found = False
        for i in range(max_scrolls):
            try:
                currency_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'text("{currency_name}")')
                currency_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(currency_locator)
                )
                currency_element.click()
                found = True
                break
            except Exception:
                actions = ActionChains(self.driver)
                action_builder = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "finger"))
                action_builder.pointer_action.move_to_location(start_x, start_y)
                action_builder.pointer_action.pointer_down()
                action_builder.pointer_action.pause(0.2)  # Reduced pause
                action_builder.pointer_action.move_to_location(start_x, end_y)
                action_builder.pointer_action.release()
                actions.perform()
                WebDriverWait(self.driver, 0.5).until(lambda d: False) # Small delay after scroll

        if not found:
            print(f"Currency '{currency_name}' not found after scrolling {max_scrolls} times.")
            return False
        return True

    def enter_number(self, number):
        """Enters a number using the calculator's number buttons."""
        if str(number) in self.locate.numbers:
            self.click(self.locate.numbers[str(number)])
        else:
            print(f"Warning: Number '{number}' not found in locators.")

    def convert_length(self,length):
        self.click(self.locate.length_button)
        self.click(self.locate.numbers[length])

    def convert_mass(self, mass):
        self.click(self.locate.mass_button)
        self.click(self.locate.numbers[mass])

    def calculate_BMI(self, age, weight, height, gender):
        self.click(self.locate.BMI_button)
        self.send_keys(self.locate.age_button, str(age))
        self.send_keys(self.locate.weight_button, str(weight))
        self.send_keys(self.locate.height_button, str(height))

        if gender == "Female":
            self.click(self.locate.female_gender_button)

        elif gender == "Male":
            self.click(self.locate.male_gender_button)

        else:
            print("Invalid gender. Please specify 'Male' or 'Female'.")

        self.click(self.locate.bmi_calculate)

