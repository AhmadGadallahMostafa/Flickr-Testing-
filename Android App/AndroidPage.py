from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import AndroidLocator
import time


class WelcomePage:
    def __init__(self, d):
        self.driver = d

    def go(self):
        a = self.driver.find_element(*AndroidLocator.WelcomePageLocator.GET_STARTED)
        a.click()


class LoginPage:
    def __init__(self, d):
        self.driver = d

    def enter_email(self):
        email_field = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email_field.send_keys("karimamr9@outlook.com")
        next_button = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        next_button.click()
        self.driver.implicitly_wait(10)
        password = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        password.send_keys(",Q#8zUvxmSVJ-L^")
        sign_in = self.driver.find_element(*AndroidLocator.LoginPageLocator.SIGN_IN)
        sign_in.click()


class HomePage:
    def __init__(self, d):
        self.driver = d

    def go_to_upload(self):
        upload_button = self.driver.find_element(*AndroidLocator.HomePageLocator.UPLOAD_ICON)
        upload_button.click()

    def go_to_photo_stream(self):
        profile_button = self.driver.find_element(*AndroidLocator.HomePageLocator.PHOTO_STREAM_ICON)
        profile_button.click()


class UploadPage:
    def __init__(self, d):
        self.driver = d

    def check_and_accept_permission(self):
        permission_block = self.driver.find_elements(*AndroidLocator.UploadPageLocator.PERMISSION_BLOCK)
        if permission_block:
            allow_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.ALLOW)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()

    def is_upload_page(self):
        camera_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.CAMERA_BUTTON)

    def take_picture(self):
        self.driver.implicitly_wait(5)
        camera_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.CAMERA_BUTTON)
        camera_button.click()
        self.driver.implicitly_wait(5)
        next_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.NEXT_BUTTON)
        next_button.click()
        title_text = self.driver.find_element(*AndroidLocator.UploadPageLocator.TITLE_TEXT)
        title_text.send_keys("Android upload")
        post_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.POST_BUTTON)
        post_button.click()


class PhotoStreamPage:
    def __init__(self, d):
        self.driver = d

    def check_last_uploaded_title_matches(self, title):
        time.sleep(5)
        picture_box = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.PICTURE_BOX)
        picture_box.click()
        picture_title = self.driver.find_element(*AndroidLocator.PhotoViewPageLocator.TITLE)
        return title in picture_title.text

    def close_photo_view(self):
        close = self.driver.find_element(*AndroidLocator.PhotoViewPageLocator.ClOSE)
        close.click()
        self.driver.implicitly_wait(5)
        upload_icon = self.driver.find_element(*AndroidLocator.HomePageLocator.UPLOAD_ICON)
        upload_icon.click()

    def is_uploading(self):
        self.driver.implicitly_wait(5)
        status = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.MESSAGE_BAR)
        return "Uploading" in status.text
