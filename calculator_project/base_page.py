from appium import webdriver

from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.platform_version = "15"
            options.device_name = "emulator-5554"
            options.app = "C:\\Users\\v-puritynjau\\MobileApps\\com.miui.calculator_15.3.3-315003003_minAPI29(arm64-v8a)(nodpi)_apkmirror.com.apk"
            options.automation_name = "UiAutomator2"
            self.driver = webdriver.Remote("http://localhost:4723", options=options)

    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def click(self, locator):
        self.find(*locator).click()

    def send_keys(self, locator, text):
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)

    def teardown(self):
        self.driver.quit()

