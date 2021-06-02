from Pages.BasePage import BasePage
from Locators.PhotoviewPageLocators import PhotoViewLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class PhotoViewPage(BasePage):
    def comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXTBOX)
        comment.send_keys("Nice pic")
        time.sleep(3)
        comment_button = self.driver.find_element(*PhotoViewLocators.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(3)

    def check_comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXT)
        result = "Nice pic" in comment.text
        return result

    '''def edit_comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXT)
        action = ActionChains(self.driver)
        action.move_to_element(comment)
        edit = self.driver.find_element(*PhotoViewLocators.EDIT_BUTTON)
        action.move_to_element(edit)
        action.click(edit)
        action.perform()
        time.sleep(3)
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXTBOX)
        comment.send_keys(" karim")
        time.sleep(3)
        done = self.driver.find_element(*PhotoViewLocators.DONE_BUTTON)
        done.click()
        time.sleep(3)

    def check_edited_comment(self):
        comment = self.driver.find_element(*PhotoViewLocators.COMMENT_TEXT)
        result = "Nice pic karim" in comment.text
        return result'''
