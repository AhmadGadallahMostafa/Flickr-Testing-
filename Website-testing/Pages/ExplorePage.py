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
    
 
    def trending_photos_loaded(self):
        time.sleep(2)
        trending_photos = self.driver.find_element(*ExplorePageLocators.TRENDING_PHOTOS)
        trending_photos = trending_photos.find_elements_by_xpath('.//*')
        return len(trending_photos)#we return their count (if 0 then explore page didn't load any pictures)
        