from Pages.BasePage import BasePage
from Locators.SearchPeopleLocator import SearchPeoplePageLocators
import  time

class SearchPeoplePage(BasePage):
    def open_profile(self):
        time.sleep(3)
        profile = self.driver.find_element(*SearchPeoplePageLocators.PROFILE_BOX)
        profile.click()
        time.sleep(5)
    
    def search_people_title(self):
        result = self.driver.title
        return "Search" in result
    
    def search_results_match(self, searchedFor):
        matchings = 0
        
        people_from_search = self.driver.find_elements(*SearchPeoplePageLocators.PEOPLE_NAME) #we get all search results and check it matcher searched
      
        for i in range(0, len(people_from_search)):
            people_from_search[i] = people_from_search[i].text
        
        for i in range(0, len(people_from_search)):
            if searchedFor in people_from_search[i]:
                matchings+=1
        
        return matchings       