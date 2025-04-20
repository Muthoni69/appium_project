from appium.webdriver.common.appiumby import AppiumBy

class MyLocators:
    numbers = {
        "1": (AppiumBy.ID, "com.miui.calculator:id/digit_1"),
        "2": (AppiumBy.ID, "com.miui.calculator:id/digit_2"),
        "3": (AppiumBy.ID, "com.miui.calculator:id/digit_3"),
        "4": (AppiumBy.ID, "com.miui.calculator:id/digit_4"),
        "5": (AppiumBy.ID, "com.miui.calculator:id/digit_5"),
        "6": (AppiumBy.ID, "com.miui.calculator:id/digit_6"),
        "7": (AppiumBy.ID, "com.miui.calculator:id/digit_7"),
        "8": (AppiumBy.ID, "com.miui.calculator:id/digit_8"),
        "9": (AppiumBy.ID, "com.miui.calculator:id/digit_9"),
        "0": (AppiumBy.ID, "com.miui.calculator:id/digit_0")
    }

    currency_button = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.miui.calculator:id/icon"])[1]')
    length_button = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.miui.calculator:id/icon"])[2]')
    mass_button = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.miui.calculator:id/icon"])[3]')
    BMI_button = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.miui.calculator:id/icon"])[12]')
    age_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("​Enter age")')
    male_gender_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'Gender: Male')
    female_gender_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'Gender: Female')
    height_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("​Enter height")')
    weight_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("​Enter weight")')
    bmi_calculate = (AppiumBy.ID, "com.miui.calculator:id/btn_calculate")

