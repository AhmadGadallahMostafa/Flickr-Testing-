from selenium.webdriver.support import expected_conditions as EC
from Locators.HomePageLocator import HomePageLocator
from appium.webdriver.common.touch_action import TouchAction

import time

class HomePage:
    def __init__(self, d):
        self.driver = d

    def go_to_upload(self):
        self.driver.implicitly_wait(5)
        upload_button = self.driver.find_element(*HomePageLocator.UPLOAD_ICON)
        upload_button.click()
        time.sleep(2)

    def go_to_photo_stream(self):
        profile_button = self.driver.find_element(*HomePageLocator.PHOTO_STREAM_ICON)
        profile_button.click()
        time.sleep(2)
    
    def go_to_notifications(self):
        notification_tab = self.driver.find_element(*HomePageLocator.NOTIFICATION)
        notification_tab.click()
        time.sleep(2)

    def search_for_profile(self, acc):
        search_icon = self.driver.find_element(*HomePageLocator.SEARCH_ICON)
        search_icon.click()
        time.sleep(1)
        search_field = self.driver.find_element(*HomePageLocator.SEARCH_BOX)
        search_field.clear()
        search_field.send_keys(acc)
        TouchAction(self.driver).tap(x=968, y=1706).perform()
        time.sleep(2)
    
    def search_for_group(self, groupName):
        search_icon = self.driver.find_element(*HomePageLocator.SEARCH_ICON)
        search_icon.click()
        time.sleep(1)
        search_field = self.driver.find_element(*HomePageLocator.SEARCH_BOX)
        search_field.clear()
        search_field.send_keys(groupName)
        TouchAction(self.driver).tap(x=968, y=1706).perform()
        time.sleep(2)


