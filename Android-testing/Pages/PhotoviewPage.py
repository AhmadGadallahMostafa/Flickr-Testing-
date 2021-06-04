from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.PhotostreamPageLocator import PhotostreamPageLocator
from Locators.PhotoviewPageLocator import PhotoviewPageLocator
from Locators.HomePageLocator import HomePageLocator
import time

class PhotoViewPage:
    def __init__(self, d):
        self.driver = d

    def comment(self):
        comment = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXTBOX)
        comment.send_keys("Nice pic")
        time.sleep(3)
        post_button = self.driver.find_element(*PhotoviewPageLocator.POST_BUTTON)
        post_button.click()
        time.sleep(3)

    def check_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)
        result = "Nice pic" in comment_text.text
        return result