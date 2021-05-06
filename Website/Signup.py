from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



class FlickerSignup(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        signup = inst.driver.find_element_by_link_text("Sign Up")
        signup.click()

    def test_firstname(self):
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        firstname_required = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[1]//div[2]")
        self.assertTrue(firstname_required.text == "Required")

    def test_lastname(self):
        self.driver.refresh()
        time.sleep(2)
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        lastname_required = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[2]//div[2]")
        self.assertTrue(lastname_required.text == "Required")

    def test_age(self):
        self.driver.refresh()
        time.sleep(2)
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        age_required = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[3]//div[2]")
        self.assertTrue(age_required.text == "Required")

    def test_email(self):
        self.driver.refresh()
        time.sleep(2)
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        email_required = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[4]//div[2]")
        self.assertTrue(email_required.text == "Required")

    def test_password(self):
        self.driver.refresh()
        time.sleep(2)
        firstname = self.driver.find_element_by_id("sign-up-first-name")
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element_by_id("sign-up-last-name")
        lastname.send_keys("Amr")
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("20")
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866@gmail.com")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        password_required = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[5]//div[2]")
        self.assertTrue(password_required.text == "Required")

    def test_valid_age(self):
        self.driver.refresh()
        age = self.driver.find_element_by_id("sign-up-age")
        age.send_keys("9")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        age_warning = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[3]//div[2]")
        self.assertTrue(age_warning.text == "In order to use Flickr, you must be 13 or older")

    def test_valid_email_1(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("sign-up-email")
        email.send_keys("mohamedamr866gmail.com")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        email_warning = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[4]//div[2]")
        self.assertTrue(email_warning.text == "Invalid email")

    """def test_valid_email_2(self):
        self.driver.refresh()
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
        time.sleep(60)
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        email_warning = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[4]//div[2]")
        self.assertTrue(email_warning.text == "Email unavailable")"""

    def test_valid_password(self):
        self.driver.refresh()
        password = self.driver.find_element_by_id("sign-up-password")
        password.send_keys("aaaaaaaaaaa")
        signup = self.driver.find_element_by_xpath("//button")
        signup.click()
        time.sleep(5)
        password_warning = self.driver.find_element_by_xpath("//form[@id='sign-up-form']//div[5]//div[2]")
        self.assertTrue(password_warning.text == "Invalid password")


    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()
