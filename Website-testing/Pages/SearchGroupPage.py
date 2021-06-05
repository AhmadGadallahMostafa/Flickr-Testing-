from Pages.BasePage import BasePage
from Locators.SearchGroupsLocators import SearchGroupsPageLocators
import time

class SearchGroupsPage(BasePage):
    def open_group(self): #opens first group in search paage and watis 5s 
        group = self.driver.find_element(*SearchGroupsPageLocators.GROUP_BOX)
        group.click()
        time.sleep(10)

    def search_results_match(self, searchedFor):
        matchings = 0
        
        groups_from_search = self.driver.find_elements(*SearchGroupsPageLocators.GROUP_NAMES) #we get all search results and check it matcher searched
      
        for i in range(0, len(groups_from_search)):
            groups_from_search[i] = groups_from_search[i].text
        
        for i in range(0, len(groups_from_search)):
            if searchedFor in groups_from_search[i]:
                matchings+=1
        
        return matchings       


