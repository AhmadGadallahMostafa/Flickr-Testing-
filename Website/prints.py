from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class Flickerlprints(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        path = "C:\Program Files (x86)\chromedriver.exe"
        inst.driver = webdriver.Chrome(path)
        inst.driver.get("https://www.flickr.com/")
        inst.driver.maximize_window()
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
        time.sleep(5)

    def test_prints_page(self):
        prints = self.driver.find_element_by_xpath("//ul[@class='nav-menu desktop-only']//li[3]")
        prints.click()
        time.sleep(2)
        result = self.driver.title
        self.assertTrue("Prints" in result)

    def test_choose_photo(self):
        choose_photo = self.driver.find_element_by_xpath("//Button[@class='unfluid hero-button bordered-button-black']")
        choose_photo.click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath("//div[@class='fluid-modal-overlay no-stack-flip']")
        self.assertTrue("Drag and drop your photo to upload or browse." in result)





    @classmethod
    def tearDownClass(inst):
        inst.driver.close()


if __name__ == "__main__":
    unittest.main()