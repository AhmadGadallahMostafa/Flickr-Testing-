from Pages.BasePage import BasePage
from Locators.GroupsPageLocators import GroupsPageLocators

import time

class GroupsPage(BasePage):
    def title_matches(self):
        time.sleep(1)
        page_title = self.driver.title
        return "groups" in page_title

    def create_group_no_name(self):
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(1)
        next1.click()
        time.sleep(1)
        error_message = self.driver.find_element(*GroupsPageLocators.ERROR_TEXT)
        return "Please enter a group name" in error_message.text

    def create_group(self):
        self.driver.refresh()
        time.sleep(5)
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(2)
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("TESTGROUP12341256456741589")
        next1.click() #2nd next
        next1.click() #create group
        time.sleep(5)
        return "TESTGROUP12341256456741589" in self.driver.title

    def create_group_that_exists(self):
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("TESTGROUP12341256456741589")
        next1.click() #2nd next
        next1.click() #create group
        time.sleep(1)
        error_message = self.driver.find_element(*GroupsPageLocators.ERROR_TEXT)
        return "There is already a group with this name" in error_message.text

    def create_18_age_group(self):
        self.driver.refresh()
        time.sleep(5)
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(2)
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("This is a test group20111 18+")
        #This is a test group 18+
        next1.click()
        check_adult = self.driver.find_element(*GroupsPageLocators.ADULT_GROUP_SELECTOR)
        check_adult.click()
        next1.click()
        time.sleep(5)
        group_text = self.driver.find_element(*GroupsPageLocators.GROUP_MESSAGE)
        return "group is 18+" in group_text.text

    def add_photo_to_group(self):
        time.sleep(5)
        group_link = self.driver.find_element(*GroupsPageLocators.GROUP_LINK)
        group_link.click()
        time.sleep(5)
        photo_pool = self.driver.find_element(*GroupsPageLocators.PHOTO_POOL)
        photo_pool.click()
        time.sleep(2)
        add_photo = self.driver.find_element(*GroupsPageLocators.ADD_PHOTO)
        add_photo.click()
        time.sleep(2)
        photo_box = self.driver.find_element(*GroupsPageLocators.PHOTO_BOX)
        photo_box.click()
        photo_box_selected = self.driver.find_element(*GroupsPageLocators.PHOTO_BOX_SELECTED)
        selected_title = photo_box_selected.get_attribute("title")
        add_to_group_button = self.driver.find_element(*GroupsPageLocators.ADD_TO_GROUP)
        add_to_group_button.click()
        time.sleep(5)
        uploaded_title = self.driver.find_element(*GroupsPageLocators.PHOTO_UPLOADED_TITLE)
        return selected_title in uploaded_title.text
