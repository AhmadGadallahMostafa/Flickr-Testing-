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
        inst.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        get_started = WebDriverWait(inst.driver, 30).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Get Started"
        )))
        get_started.click()
        inst.driver.implicitly_wait(60)
        signup = inst.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]")
        signup.click()

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def test_first_name(self):
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        firstname_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in firstname_required.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def test_lastname(self):
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        lastname_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in lastname_required.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the age it must show the word required to the user
    def test_age(self):
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        age_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in age_required.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the email it must show the word required to the user
    def test_email(self):
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        email_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in email_required.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the password it must show the word required to the user
    def test_password(self):
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        password_required = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View")
        self.assertTrue("Required" in password_required.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup with age less than 13 years it must show "In order to use Flickr, you must be 13 or older"  to the user
    def test_valid_age(self):
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("9")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        age_warning = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View")
        self.assertTrue("In order to use Flickr, you must be 13 or older" in age_warning.text)

    # Tester: Mohamed Amr
    # This function tests if we try to signup with an email in a wrong format it must show "Invalid email"  to the user
    def test_valid_email_1(self):
        #self.driver.refresh()
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866gmail.com")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(60)
        email_warning = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[2]/android.view.View")
        self.assertTrue("Invalid email" in email_warning.text)

    """def test_valid_email_2(self):
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        email_warning = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[4]//div[2]")
        self.assertTrue(email_warning.text == "Email unavailable")"""

    # Tester: Mohamed Amr
    # This function tests if we try to signup with a password less than 12 charachters  it must show "Invalid password"  to the user
    def test_valid_password(self):
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        signup.click()
        self.driver.implicitly_wait(5)
        password_warning = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View[2]/android.view.View")
        self.assertTrue("Invalid password" in password_warning.text)
