from Locators.ProfilePageLocator import ProfilePageLocator
import time

class ProfilePage():
    def __init__(self, driver):
        self.driver = driver
    
    def follow_profile(self):
        follow = self.driver.find_element(*ProfilePageLocator.FOLLOW_BTN)
        follow.click()
        time.sleep(2)
        follow_status = self.driver.find_element(*ProfilePageLocator.FOLLOW_STATUS)
        return "" in follow_status.text
    
    def unfollow(self):
        unfollow = self.driver.find_element(*ProfilePageLocator.FOLLOW_BTN)
        unfollow.click()
        time.sleep(2)
        follow_status = self.driver.find_element(*ProfilePageLocator.FOLLOW_STATUS)
        return "Follow" in follow_status.text


    
    

       