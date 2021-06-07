
from Locators.PhotoviewPageLocator import PhotoviewPageLocator

import time

class PhotoViewPage:
    def __init__(self, d):
        self.driver = d

    def comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        comment = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXTBOX)
        comment.send_keys("Nice pic")
        time.sleep(3)
        post_button = self.driver.find_element(*PhotoviewPageLocator.POST_BUTTON)
        post_button.click()
        time.sleep(3)

    def check_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)
        result = "Nice pic" in comment_text.text
        return result

    def edit_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(1)
        options = self.driver.find_element(*PhotoviewPageLocator.OPTIONS_BUTTON)
        options.click()
        time.sleep(1)
        edit = self.driver.find_element(*PhotoviewPageLocator.EDIT_BUTTON)
        edit.click()
        comment = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TO_EDIT_TEXTBOX)
        comment.clear()
        comment.send_keys("Nice pic Karim")
        time.sleep(3)
        okay_button = self.driver.find_element(*PhotoviewPageLocator.OKAY_BUTTON)
        okay_button.click()
        time.sleep(3)

    def check_edit_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)
        result = "Nice pic Karim" in comment_text.text
        return result

    def delete_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(1)
        options = self.driver.find_element(*PhotoviewPageLocator.OPTIONS_BUTTON)
        options.click()
        time.sleep(1)
        delete = self.driver.find_element(*PhotoviewPageLocator.DELETE_BUTTON)
        delete.click()
        yes_button = self.driver.find_element(*PhotoviewPageLocator.YES_BUTTON)
        yes_button.click()
        time.sleep(3)

    def check_delete_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)
