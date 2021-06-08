from Pages.BasePage import BasePage
from Locators.PhotoviewPageLocators import PhotoViewLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class PhotoViewPage(BasePage):
    #In this function we locate the comment textbox then write a comment
    def comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXTBOX)  #Locating the comment textbox
        comment.send_keys("Nice pic")  #Write a comment
        time.sleep(3)
        comment_button = self.driver.find_element(*PhotoViewLocators.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(3)
    #After executing the above function we check that the comment is written
    def check_comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXT)  #Locating the comment textbox
        result = "Nice pic" in comment.text  #Checking that the comment is written
        return result

