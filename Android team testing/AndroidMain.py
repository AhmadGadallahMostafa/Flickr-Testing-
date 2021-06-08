import unittest
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from LoginPage import LoginPage
from SignupPage import SignupPage


class FlickrLoginAndroid(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.example.mainhomefeed',
            'appActivity': 'com.example.FlickrReplicaAndroid.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(60)


    def test_no_email(self):
        login_page = LoginPage(self.driver)
        try:
            login_page.no_email()
        except Exception:
            self.fail("successful login without email")

    def test_no_password(self):
        login_page = LoginPage(self.driver)
        try:
            login_page.no_password()
        except Exception:
            self.fail("successful login without password")

    def test_wrong_password(self):
        login_page = LoginPage(self.driver)
        try:
            login_page.wrong_password()
        except Exception:
            self.fail("successful login with wrong password")

    def test_wrong_email_and_wrong_password(self):
        login_page = LoginPage(self.driver)
        try:
            login_page.wrong_email_and_wrong_password()
        except Exception:
            self.fail("successful login with wrong password and wrong email")

    def test_right_email_and_right_password(self):
        login_page = LoginPage(self.driver)
        with self.assertRaises(Exception) as context:
           login_page.right_email_and_right_password()
        
    def tearDown(self):
        self.driver.close_app()

class FlickrSignupAndroid(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.example.mainhomefeed',
            'appActivity': 'com.example.FlickrReplicaAndroid.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(60)
        signup = self.driver.find_element_by_id("com.example.mainhomefeed:id/tv_regsiter")
        signup.click()

    def test_first_name(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.first_name()
        except Exception:
            self.fail("successful signup without firstname")

    def test_last_name(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.last_name()
        except Exception:
            self.fail("successful signup without lastname")
    
    def test_age(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.age()
        except Exception:
            self.fail("successful signup without age")
        
    def test_email(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.email()
        except Exception:
            self.fail("successful signup without email")
        
    def test_password(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.password()
        except Exception:
            self.fail("successful signup without password")

    def test_valid_password(self):
        signup_page = SignupPage(self.driver)
        try:
            signup_page.valid_password()
        except Exception:
            self.fail("successful signup with short password")
    
    '''def test_successful_signup(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup_completed()
        login_page = LoginPage(self.driver)
        try:
            login_page.login_with_new_acc()
        except Exception:
            self.fail("unsuccessful login with just created acc")'''


    def tearDown(self):
        self.driver.close_app()

if __name__ == "__main__":
    unittest.main()