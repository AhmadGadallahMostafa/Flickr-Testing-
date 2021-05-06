import unittest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class FlickrSignupAndroid(unittest.TestCase):

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
        profile = self.driver.find_element_by_accessibility_id("Profile")
        profile.click()
        settings = self.driver.find_element_by_id("com.flickr.android:id/profile_header_overflow")
        settings.click()
        signout = self.driver.find_element_by_id("com.flickr.android:id/profile_settings_logout")
        signout.click()
        result = self.driver.find_element_by_accessibility_id("Get Started")
        self.assertTrue(result)

