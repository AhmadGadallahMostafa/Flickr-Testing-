from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.UploadPageLocator import UploadPageLocator
import time

class UploadPage:
    def __init__(self, d):
        self.driver = d

    def check_and_accept_permission(self):
        permission_block = self.driver.find_elements(*UploadPageLocator.PERMISSION_BLOCK)
        if permission_block:
            allow_button = self.driver.find_element(*UploadPageLocator.ALLOW)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()

    def is_upload_page(self):
        camera_button = self.driver.find_element(*UploadPageLocator.CAMERA_BUTTON)

    def take_picture(self):
        self.driver.implicitly_wait(5)
        camera_button = self.driver.find_element(*UploadPageLocator.CAMERA_BUTTON)
        camera_button.click()
        self.driver.implicitly_wait(5)
        next_button = self.driver.find_element(*UploadPageLocator.NEXT_BUTTON)
        next_button.click()
        title_text = self.driver.find_element(*UploadPageLocator.TITLE_TEXT)
        title_text.send_keys("Android camera upload")
        post_button = self.driver.find_element(*UploadPageLocator.POST_BUTTON)
        post_button.click()

    def choose_from_gallery(self):
        time.sleep(1)
        gallery_button = self.driver.find_element(*UploadPageLocator.GALLERY_BUTTON)
        gallery_button.click()
        time.sleep(1)
        downloads = self.driver.find_element(*UploadPageLocator.DOWNLOADS)
        downloads.click()
        time.sleep(1)
        picture = self.driver.find_element(*UploadPageLocator.PICKER_GRID)
        picture.click()
        time.sleep(1)
        done = self.driver.find_element(*UploadPageLocator.DONE)
        done.click()
        time.sleep(1)
        next_button = self.driver.find_element(*UploadPageLocator.NEXT_BUTTON)
        next_button.click()
        time.sleep(1)
        title_text = self.driver.find_element(*UploadPageLocator.TITLE_TEXT)
        title_text.send_keys("Android gallery upload")
        time.sleep(1)
        post_button = self.driver.find_element(*UploadPageLocator.POST_BUTTON)
        post_button.click()
        