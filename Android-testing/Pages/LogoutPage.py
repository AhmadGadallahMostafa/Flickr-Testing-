from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.LogoutPageLocator import LogoutPageLocator
import time

class LogoutPage:
    def __init__(self, d):
        self.driver = d

    # Tester: Mohamed Amr
    # In this function when we choose the log out button Get Started button will appear
    def logout(self):
        profile = self.driver.find_element(*LogoutPageLocator.PROFILE)
        profile.click()
        settings = self.driver.find_element(*LogoutPageLocator.SETTINGS)
        settings.click()
        time.sleep(5)
        self.driver.swipe(470, 1400, 470, 1000, 400)
        signout = self.driver.find_element(*LogoutPageLocator.SIGNOUT)
        signout.click()
        result = self.driver.find_element(*LogoutPageLocator.GET_STARTED)
        return result
