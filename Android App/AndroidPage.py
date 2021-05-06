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


class UploadPage():
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
