import unittest
import time
import AndroidPage
from appium import webdriver
from appium.webdriver.common import touch_action
import unittest
import AndroidLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


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

class FlickrLoginAndroid(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.flickr.android',
            'appActivity': 'com.yahoo.mobile.client.android.flickr.activity.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        get_started = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Get Started"
                                            )))
        get_started.click()
        self.driver.implicitly_wait(60)

    def test_wrong_email_format(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.wrong_email_format())

    def test_no_email(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.no_email())

    def test_right_email(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.right_email())

    def test_no_password(self):
        login_page = AndroidPage.LoginPage(self.driver)
        with self.assertRaises(Exception) as context:
            login_page.no_password()

    def test_wrong_password(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.wrong_password())

    def test_wrong_email_and_wrong_password(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.wrong_email_and_wrong_password())

    def test_right_email_and_right_password(self):
        login_page = AndroidPage.LoginPage(self.driver)
        self.assertTrue(login_page.right_email_and_right_password())

    def tearDown(self):
        self.driver.close_app()


class FlickrLogoutAndroid(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.flickr.android',
            'appActivity': 'com.yahoo.mobile.client.android.flickr.activity.MainActivity'
        }
        inst.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        get_started = WebDriverWait(inst.driver, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Get Started"
        )))
        get_started.click()
        inst.driver.implicitly_wait(60)
        email = inst.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = inst.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        inst.driver.implicitly_wait(60)
        password = inst.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = inst.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        signin.click()
        inst.driver.implicitly_wait(60)

    def test_logout(self):
        logout_page = AndroidPage.LogoutPage(self.driver)
        self.assertTrue(logout_page.logout())

class FlickrSignupAndroid(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.flickr.android',
            'appActivity': 'com.yahoo.mobile.client.android.flickr.activity.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        get_started = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Get Started"
                                            )))
        get_started.click()
        self.driver.implicitly_wait(60)
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]")
        signup.click()

    def test_first_name(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.first_name())

    def test_last_name(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.last_name())

    def test_age(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.age())

    def test_email(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.email())

    def test_password(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.password())

    def test_valid_age(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.valid_age())

    def test_valid_email(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.valid_email())

    def test_valid_password(self):
        signup_page = AndroidPage.SignupPage(self.driver)
        self.assertTrue(signup_page.valid_password())

    def tearDown(self):
        self.driver.close_app()

if __name__ == "__main__":
    unittest.main()