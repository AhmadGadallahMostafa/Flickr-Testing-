import unittest

import AndroidPage
from appium import webdriver
import unittest


def login(driver):
    login = AndroidPage.LoginPage(driver)
    login.enter_email()


class FlickrUploadAndroid(unittest.TestCase):

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

    def test_go_to_upload(self):
        home = AndroidPage.HomePage(self.driver)
        home.go_to_upload()
        upload_page = AndroidPage.UploadPage(self.driver)
        upload_page.check_and_accept_permission()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()