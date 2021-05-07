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

    #Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def test_wrong_email_format(self):
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("aaaa")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        email_warning = self.driver.find_element_by_xpath("//div[contains(@class,'flickr-modal bg-white elevation-2 b-rad-1 flex column pa-3')]")
        result = email_warning.text.find("Hmm… that's not an email address")
        self.assertGreaterEqual(result, 0)

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def test_no_email(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        email_required = self.driver.find_element_by_xpath("//form[@id='login-form']//div[2]//div[2]")
        self.assertTrue(email_required.text == "Required")

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def test_right_email(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        result = self.driver.find_element_by_id("login-password")
        self.assertTrue(result)

    # Tester: Mohamed Amr
    # In this function if we try to log in without the password we will check that the page isn't the home page
    def test_no_password(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(2)
        result = self.driver.title
        self.assertFalse("Home" in result)

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong password "Invalid password" will appear
    def test_wrong_password(self):
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

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong email and wrong password "Invalid email or password." will appear
    def test_wrong_email_and_wrong_password(self):
        self.driver.refresh()
        email = self.driver.find_element_by_id("login-email")
        email.send_keys("karimamr3009@gmail.com")
        login = self.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(2)
        password = self.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = self.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(5)
        result = self.driver.find_element_by_xpath("//p")
        self.assertTrue("Invalid email or password." in result.text)


    # Tester: Mohamed Amr
    # In this function if we try to log in with a right email and right password the home page will be reached
    def test_right_email_and_right_password(self):
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




    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()