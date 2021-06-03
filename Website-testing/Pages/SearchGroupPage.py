from Pages.BasePage import BasePage
from Locators.SearchGroupsLocators import SearchGroupsPageLocators
import time

class SearchGroupsPage(BasePage):
    def open_group(self): #opens first group in search paage and watis 5s 
        group = self.driver.find_element(*SearchGroupsPageLocators.GROUP_BOX)
        group.click()
        time.sleep(10)



