import unittest
import time
import AndroidPage
from appium import webdriver
import unittest
import AndroidLocator


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


    def test_photo_from_camera_in_photo_stream(self):
        time.sleep(5)
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        sort_list = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.DATE_LIST)
        sort_list.click()
        by_date = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.DATE_UPLOADED)
        by_date.click()
        time.sleep(5)
        self.assertTrue(photo_stream_page.check_last_uploaded_title_matches("Android camera upload"))

    def test_photo_from_gallery_in_photo_stream(self):
        time.sleep(5)
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        sort_list = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.DATE_LIST)
        sort_list.click()
        by_date = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.DATE_UPLOADED)
        by_date.click()
        time.sleep(5)
        self.assertTrue(photo_stream_page.check_last_uploaded_title_matches("Android gallery upload"))

    def test_from_gallery(self):
        photo_stream_page = AndroidPage.PhotoStreamPage(self.driver)
        photo_stream_page.close_photo_view()
        time.sleep(5)
        upload_page = AndroidPage.UploadPage(self.driver)
        upload_page.choose_from_gallery()
        self.assertTrue(photo_stream_page.is_uploading())


if __name__ == "__main__":
    unittest.main()