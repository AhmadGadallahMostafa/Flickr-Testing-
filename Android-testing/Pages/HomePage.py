from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.HomePageLocator import HomePageLocator
import time

class HomePage:
    def __init__(self, d):
        self.driver = d

    def go_to_upload(self):
        self.driver.implicitly_wait(5)
        upload_button = self.driver.find_element(*HomePageLocator.UPLOAD_ICON)
        upload_button.click()

    def go_to_photo_stream(self):
        profile_button = self.driver.find_element(*HomePageLocator.PHOTO_STREAM_ICON)
        profile_button.click()
