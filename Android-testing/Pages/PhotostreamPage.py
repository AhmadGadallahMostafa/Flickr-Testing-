from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from Locators.PhotostreamPagaLocator import PhotoStreamPageLocator
from Locators.PhotoviewPageLocator import PhotoviewPageLocator
from Locators.HomePageLocator import HomePageLocator
import time

class PhotostreamPage:
    def __init__(self, d):
        self.driver = d

    def check_last_uploaded_title_matches(self, title):
        time.sleep(10)
        picture_box = self.driver.find_element(*PhotoStreamPageLocator.PICTURE_BOX)
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
        status = self.driver.find_element(*PhotoStreamPageLocator.MESSAGE_BAR)
        return "Uploading" in status.text
    # In this function we open the photo then check that it is opened by checking its id
    def view_photo(self):
        photo = self.driver.find_element(*PhotoStreamPageLocator.PHOTO)  #Locating the photo to open it
        photo.click()
        photo_id = self.driver.find_element(*PhotoviewPageLocator.TITLE)  #Locating the photo id
        result = "IMG" in photo_id.text  #Check that IMG in the photo id
        return result
    # Open the photo in the first profile
    def open_photo_of_searched_profile(self):
        photo = self.driver.find_element(*PhotoStreamPageLocator.PHOTO_IN_SEARCHED_PROFILE)
        photo.click()
        time.sleep(5)

    # Open the photo in the second profile
    def open_photo_in_another_profile(self):
        photo = self.driver.find_element(*PhotoStreamPageLocator.PHOTO_IN_ANOTHER_PROFILE)
        photo.click()
        time.sleep(5)

