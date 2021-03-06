from Locators.ProfilePageLocator import ProfilePageLocator
import time

class ProfilePage():
    def __init__(self, driver):
        self.driver = driver

    def follow_opened_profile(self):
        follow = self.driver.find_element(*ProfilePageLocator.FOLLOW_BTN)
        follow.click()
        time.sleep(2)

    def follow_profile(self):
        self.follow_opened_profile()
        follow_status = self.driver.find_element(*ProfilePageLocator.FOLLOW_STATUS)
        
    
    def unfollow(self):
        unfollow = self.driver.find_element(*ProfilePageLocator.FOLLOW_BTN)
        unfollow.click()
        time.sleep(2)
        follow_status = self.driver.find_element(*ProfilePageLocator.FOLLOW_STATUS)
        return "Follow" in follow_status.text


    
    

       