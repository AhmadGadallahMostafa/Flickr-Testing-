from Locators.GroupPageLocator import GroupPageLocator
import time

class GroupPage():
    def __init__(self, driver):
        self.driver = driver

    def join_group(self):
        join = self.driver.find_element(*GroupPageLocator.JOIN_BTN)
        join.click()
        time.sleep(2)
        join = self.driver.find_element(*GroupPageLocator.JOIN_BTN)
    
    def leave_group(self):
        three_dots = self.driver.find_element(*GroupPageLocator.THREE_DOTS)
        three_dots.click()
        time.sleep(1)
        leave = self.driver.find_element(*GroupPageLocator.LEAVE)
        leave.click()
        time.sleep(1)
        confirm_leave = self.driver.find_element(*GroupPageLocator.CONFIRM_LEAVE)
        confirm_leave.click()
        join_status = self.driver.find_element(*GroupPageLocator.JOIN_STATUS)
        return "Join" in join_status.text
    
    def add_photo_to_group(self):
        three_dots = self.driver.find_element(*GroupPageLocator.THREE_DOTS)
        three_dots.click()
        add_photo = self.driver.find_element(*GroupPageLocator.ADD_PHOTO)
        add_photo.click()
        time.sleep(1)
        photo_to_upload = self.driver.find_element(*GroupPageLocator.PHOTO_LIST)
        photo_to_upload = photo_to_upload.find_element_by_xpath('.//android.view.View')
        photo_to_upload.click()
        add_btn = self.driver.find_element(*GroupPageLocator.ADD)
        add_btn.click()
        time.sleep(2)
        photo_in_group = self.driver.find_element(*GroupPageLocator.GROUP_PHOTO_LIST)
        photo_in_group = photo_in_group.find_element_by_xpath('.//android.widget.ListView/android.widget.LinearLayout/android.view.View')
        photo_in_group.click()
        time.sleep(1)
        photo_title = self.driver.find_element(*GroupPageLocator.PHOTO_ADDED_TITLE)
        return "IMG_0009" in photo_title.text