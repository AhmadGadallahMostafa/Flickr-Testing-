from Locators.ProfilePageLocators import ProfilePageLocators
from Pages.BasePage import BasePage
import time

class ProfilePage(BasePage):
    def profile_name_matches_search(self, searchedString):
        result = self.driver.title
        return searchedString in result
    
    def follow_opened_profile(self):
        follow_button = self.driver.find_element(*ProfilePageLocators.FOLLOW_BUTTON)
        follow_button.click()
        time.sleep(3)
        follow_status = self.driver.find_element(*ProfilePageLocators.FOLLOW_TEXT)
        follow_status = follow_status.text
        return "Following" in follow_status
    
    
    
