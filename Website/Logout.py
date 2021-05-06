from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class Flickerlogout(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        login = inst.driver.find_element_by_link_text("Log In")
        login.click()
        email = inst.driver.find_element_by_id("login-email")
        email.send_keys("mohamedamr866@gmail.com")
        login = inst.driver.find_element_by_xpath("//button")
        login.click()
        time.sleep(3)
        password = inst.driver.find_element_by_id("login-password")
        password.send_keys("abcd12345678")
        signin = inst.driver.find_element_by_xpath("//button")
        signin.click()
        time.sleep(3)

    def test_logout(self):
        account = self.driver.find_element_by_xpath("//div[contains(@class,'avatar person tiny')]")
        account.click()
        logout = self.driver.find_element_by_link_text("Log out")
        logout.click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath("//h6")
        self.assertTrue(result)






    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()