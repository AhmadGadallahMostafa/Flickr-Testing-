import unittest

import AndroidPage
from appium import webdriver
import unittest


def login(driver):
    login_page = AndroidPage.LoginPage(driver)
    login_page.enter_email()


class FlickrUploadAndroid(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(inst):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.flickr.android',
            'appActivity': 'com.yahoo.mobile.client.android.flickr.activity.MainActivity'
        }
        inst.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        home = AndroidPage.WelcomePage(inst.driver)
        home.go()
        inst.driver.implicitly_wait(10)
        login(inst.driver)

    def test_upload_activity(self):
        home = AndroidPage.HomePage(self.driver)
        home.go_to_upload()
        upload_page = AndroidPage.UploadPage(self.driver)
        upload_page.check_and_accept_permission()
        try:
            upload_page.is_upload_page()
        except:
            self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_take_picture(self):
        upload_page = AndroidPage.UploadPage(self.driver)
        upload_page.take_picture()
        self.driver.implicitly_wait(15)
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        self.assertTrue(photo_stream_page.is_uploading())

    def test_photo_in_photo_stream(self):
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        self.driver.implicitly_wait(10)
        self.assertTrue(photo_stream_page.check_last_uploaded_title_matches("Android upload"))

    def test_close_before_upload(self):
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        self.driver.implicitly_wait(10)
        photo_stream_page.close_photo_view()
        upload_page = AndroidPage.UploadPage(self.driver)
        upload_page.close_before_upload()
        self.driver.activate_app("com.flickr.android")
        home_page = AndroidPage.HomePage(self.driver)
        home_page.go_to_photo_stream()
        self.assertTrue(photo_stream_page.check_last_uploaded_title_matches("Cancelled upload"))


if __name__ == "__main__":
    unittest.main()