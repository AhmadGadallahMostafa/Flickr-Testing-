from Pages.BasePage import BasePage
from Locators.SearchPhotosPageLocators import SearchPhotosPagesLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  time

class SearchPhotosPage(BasePage):
    def title_mactches(self):
        page_title = self.driver.title
        return "Search" in page_title
    
    def search_results_match(self, searchedFor):
        matchings = 0
        
        photos_from_search = self.driver.find_elements(*SearchPhotosPagesLocators.PHOTO_TITLES) #we get all search results and check it matcher searched

        for i in range(0, len(photos_from_search)):                 #we get all titles of resulting photos
            photos_from_search[i] = photos_from_search[i].get_attribute("title")
        
        for i in range(0, len(photos_from_search)):                 #we count how many time we find the word search for in the title
            if searchedFor in photos_from_search[i]:
                matchings+=1
        
        return matchings

