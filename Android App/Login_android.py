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
        #get_started = inst.driver.find_element_by_accessibility_id("Get Started")
        get_started.click()
        inst.driver.implicitly_wait(15)

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def test_wrong_email_format(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("aaaa")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        email_warning = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
        result = email_warning.text.find("Hmm… that's not an email address")
        self.assertGreaterEqual(result, 0)

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def test_no_email(self):
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        email_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in email_required.text)

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def test_right_email(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element_by_id("login-password")
        self.assertTrue(result)

    # Tester: Mohamed Amr
    # In this function if we try to log in without the password we will check that the page isn't the home page
    def test_no_password(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        signin = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        signin.click()
        self.driver.implicitly_wait(2)
        with self.assertRaises(Exception) as context:
            result = self.driver.find_element_by_accessibility_id("Profile")

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong password "Invalid password" will appear
    def test_wrong_password(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("aaaaaaaaaaaa")
        signin = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        signin.click()
        self.driver.implicitly_wait(2)
        password_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View[2]/android.view.View")
        self.assertTrue("Invalid password" in password_required.text)

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong email and wrong password "Invalid email or password." will appear
    def test_wrong_email_and_wrong_password(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("karimamr3009@gmail.com")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        signin.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]")
        self.assertTrue("Invalid email or password." in result.text)


    # Tester: Mohamed Amr
    # In this function if we try to log in with a right email and right password the home page will be reached
    def test_right_email_and_right_password(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"
        )))
        #signin = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.Button")
        signin.click()
        self.driver.implicitly_wait(15)
        result = self.driver.find_element_by_accessibility_id("Profile")
        self.assertTrue(result)
