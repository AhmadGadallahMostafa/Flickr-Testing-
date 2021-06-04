from Pages.BasePage import BasePage
from Locators.ExplorePageLocators import ExplorePageLocators
import time

class ExplorePage(BasePage):
    def page_title_is_explore(self):
        page_title = self.driver.title
        return "Explore" in page_title

    def photos_are_loaded(self):       #check if photos appear when opening explore
        photo_list = self.driver.find_elements(*ExplorePageLocators.PHOTOS) #we get list of all photos 
        return len(photo_list)#we return their count (if 0 then explore page didn't load any pictures)
    
    def go_to_trending(self):
        trending_tab = self.driver.find_element(*ExplorePageLocators.TRENDING_TAB)
        trending_tab.click()
        time.sleep(3)
    
    #trending page is divided in trending by mutiple periods 
    #we check that they are loaded
    # if one is missing we return false
    def trending_in_are_loaded_ordered(self):
        trending_in = self.driver.find_elements(*ExplorePageLocators.TRENDING_TAG_TITLES)
        for i in range(len(trending_in)):
            trending_in[i] = trending_in[i].text
        trending_by = ["Now", "Week", "All Time"]
        for i in range(0, len(trending_in)):
            if trending_by[i] not  in trending_in[i]:
                return False
        return True

    def trending_photos_loaded(self):
        time.sleep(2)
        trending_photos = self.driver.find_element(*ExplorePageLocators.TRENDING_PHOTOS)
        trending_photos = trending_photos.find_elements_by_xpath('.//*')
        return len(trending_photos)#we return their count (if 0 then explore page didn't load any pictures)
        