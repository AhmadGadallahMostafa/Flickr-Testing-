
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