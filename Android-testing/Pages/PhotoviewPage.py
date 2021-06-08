
from Locators.PhotoviewPageLocator import PhotoviewPageLocator

import time

class PhotoViewPage:
    def __init__(self, d):
        self.driver = d
    # In this function we click the comment button then write a comment and post it
    def comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        comment = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXTBOX)  #Locating the comment textbox
        comment.send_keys("Nice pic")  #writing the comment
        time.sleep(3)
        post_button = self.driver.find_element(*PhotoviewPageLocator.POST_BUTTON)  #Locating the post button
        post_button.click()
        time.sleep(3)
    # After executing the above function we use this one to check that the comment is written
    def check_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)  #Locating the comment textbox
        result = "Nice pic" in comment_text.text  #Check that the comment in the comment textbox
        return result

    # In this function we click the edit button then edit a comment
    def edit_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(1)
        options = self.driver.find_element(*PhotoviewPageLocator.OPTIONS_BUTTON)  #Locating the options button button
        options.click()
        time.sleep(1)
        edit = self.driver.find_element(*PhotoviewPageLocator.EDIT_BUTTON)  #Locating the edit button
        edit.click()
        comment = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TO_EDIT_TEXTBOX)  #Locating the comment textbox
        comment.clear()  #Clear the textbox
        comment.send_keys("Nice pic Karim")  #Writing the new comment
        time.sleep(3)
        okay_button = self.driver.find_element(*PhotoviewPageLocator.OKAY_BUTTON)  #Locating the okay button
        okay_button.click()
        time.sleep(3)

    # After executing the above function we use this one to check that the comment is edited
    def check_edit_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)  #Locating the comment textbox
        result = "Nice pic Karim" in comment_text.text  #Check that the comment in the comment textbox
        return result

    # In this function we click the delete button to delete a comment
    def delete_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(1)
        options = self.driver.find_element(*PhotoviewPageLocator.OPTIONS_BUTTON)  #Locating the options button
        options.click()
        time.sleep(1)
        delete = self.driver.find_element(*PhotoviewPageLocator.DELETE_BUTTON)  #Locating the delete button
        delete.click()
        yes_button = self.driver.find_element(*PhotoviewPageLocator.YES_BUTTON)  #Locating the yes button
        yes_button.click()
        time.sleep(3)

    # After executing the above function we use this one to check that the comment is deleted
    def check_delete_comment(self):
        comment_button = self.driver.find_element(*PhotoviewPageLocator.COMMENT_BUTTON)  #Locating the comment button
        comment_button.click()
        time.sleep(2)
        comment_text = self.driver.find_element(*PhotoviewPageLocator.COMMENT_TEXT)  #Locating the comment textbox
