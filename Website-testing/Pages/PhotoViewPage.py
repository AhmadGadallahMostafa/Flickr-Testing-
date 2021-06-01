from Pages.BasePage import BasePage
from Locators.PhotoviewPageLocators import PhotoViewLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class PhotoViewPage(BasePage):
    def comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXTBOX)
        comment.send_Keys("Nice pic")
        comment_button = self.driver.find_element(*PhotoViewLocators.COMMENT_BUTTON)
        comment_button.click()

    def check_comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXT)
        result = "Nice pic" in comment.text