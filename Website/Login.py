from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class FlickerLogin(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        login = inst.driver.find_element_by_link_text("Log In")
        login.click()

    def test_email_1(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("aaaa")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        email_warning = self.driver.find_element_by_xpath("//div[contains(@class,'flickr-modal bg-white elevation-2 b-rad-1 flex column pa-3')]")
        result = email_warning.text.find("Hmm… that's not an email address")
        self.assertGreaterEqual(result, 0)

    def test_email_2(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        email_required = self.driver.find_element_by_xpath("//form[@id='login-form']//div[2]//div[2]")
        self.assertTrue(email_required.text == "Required")

    def test_email_4(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        result = self.driver.find_element_by_id("login-password")
        self.assertTrue(result)

    def test_password_1(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        password = self.driver.find_element_by_id("login-password")
        time.sleep(2)
        result = self.driver.title
        self.assertFalse("Home" in result)

    def test_password_2(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("aaaaaaaaaaaa")
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(2)
        password_required = self.driver.find_element_by_xpath("//form[@id='login-form']//div[3]//div[1]//div[2]")
        self.assertTrue(password_required.text == "Invalid password")

    """def test_clear_email_and_wrong_password(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("aaaaaaaaaaaa")
        email.clear()
        time.sleep(2)
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        email_required = self.driver.find_element_by_xpath("//form[@id='login-form']//div[2]//div[2]")
        self.assertTrue(email_required.text == "Required")"""

    def test_email_and_password(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(5)
        result = self.driver.title
        self.assertTrue("Home" in result)
        #success = result.find("Home")
        #self.assertGreaterEqual(success, 0)



    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()