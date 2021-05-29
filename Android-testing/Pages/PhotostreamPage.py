from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.PhotostreamPageLocator import PhotostreamPageLocator
from Locators.PhotoviewPageLocator import PhotoviewPageLocator
from Locators.HomePageLocator import HomePageLocator
import time

class PhotostreamPage:
    def __init__(self, d):
        self.driver = d

    def check_last_uploaded_title_matches(self, title):
        time.sleep(10)
        picture_box = self.driver.find_element(*PhotostreamPageLocator.PICTURE_BOX)
        picture_box.click()
        self.driver.implicitly_wait(10)
        picture_title = self.driver.find_element(*PhotoviewPageLocator.TITLE)
        return title in picture_title.text

    def close_photo_view(self):
        close = self.driver.find_element(*PhotoviewPageLocator.CLOSE_BUTTON)
        close.click()
        self.driver.implicitly_wait(5)
        upload_icon = self.driver.find_element(*HomePageLocator.UPLOAD_ICON)
        upload_icon.click()

    def is_uploading(self):
        self.driver.implicitly_wait(5)
        status = self.driver.find_element(*PhotostreamPageLocator.MESSAGE_BAR)
        return "Uploading" in status.text