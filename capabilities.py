from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

CAPABILITIES = {
    'platformName': 'Android',
    'platformVersion': '15.0',
    'deviceName': 'sdk_gphone64_arm64',
    'app': '/Users/carlosmartinez/Documents/PythonAppium/resources/apps/android.apk',
    'automationName': 'UiAutomator2',
    'appActivity': 'com.swaglabsmobileapp.MainActivity'
}


def initialize_driver() -> webdriver.Remote:
    """Driver initialisation"""
    try:
        return webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(CAPABILITIES))
    except Exception as e:
        print(f"Error to initialise the driver: {e}")
        raise


def login(driver: webdriver.Remote, username: str, password: str) -> None:
    """Login into the application"""
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='test-Username').send_keys(username)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='test-Password').send_keys(password)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()
    except Exception as e:
        print(f"Error during login session: {e}")
        raise


def verify_home_page(driver: webdriver.Remote) -> bool:
    """Verify the home page is visible."""
    try:
        return driver.find_element(AppiumBy.XPATH, value='//*[@text="PRODUCTS"]').is_displayed()
    except Exception as e:
        print(f"Error during the verification of the home page: {e}")
        return False


def main() -> None:
    """Function to run the test"""
    driver = initialize_driver()
    try:
        login(driver, 'standard_user', 'secret_sauce')
        if verify_home_page(driver):
            print("Login was successful.")
        else:
            print("Home page was not visible.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
