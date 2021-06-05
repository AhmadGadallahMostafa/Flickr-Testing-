from Locators.SearchPageLocators import SearchPageLocators
import time

class SearchPage():
    def __init__(self, driver):
        self.driver = driver

    def search_people(self):
        people = self.driver.find_element(*SearchPageLocators.PEOPLE_SEARCH)
        people.click()
        time.sleep(2)
        
    def search_groups(self):
        groups = self.driver.find_element(*SearchPageLocators.GROUP_SEARCH)
        groups.click()
        time.sleep(2)
    
    def open_profile(self):
        profile = self.driver.find_element(*SearchPageLocators.PROFILE_BOX)
        profile.click()
        time.sleep(4)

    def open_group(self):
        group = self.driver.find_element(*SearchPageLocators.GROUPS)
        first_group = group.find_element_by_xpath('.//android.widget.FrameLayout[1]')
        first_group.click()
        time.sleep(5)
    
    
    

       