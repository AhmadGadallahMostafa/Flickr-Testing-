from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.WelcomePageLocator import WelcomePageLocator
import time

class WelcomePage:
    def __init__(self, d):
        self.driver = d

    def go(self):
        a = self.driver.find_element(*WelcomePageLocator.GET_STARTED)
        a.click()
