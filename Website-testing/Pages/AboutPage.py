from Pages.BasePage import BasePage
from Locators.HomePageLocators import HomePageLocators
from Locators.AboutPageLocators import AboutPageLocators
from Locators.SearchPeopleLocator import SearchPeoplePageLocators
from Locators.SearchGroupsLocators import SearchGroupsPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class AboutPage(BasePage):
    #In each function of the following after reaching the about page we click the edit profile info button, then we choose the required textbox to update, then we check that the info is updated
    def edit_occupation(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        occupation = self.driver.find_element(*AboutPageLocators.OCCUPATION_TEXTBOX)  #Locating the occupation textbox
        occupation.clear()  #clearing the occupation textbox
        time.sleep(1)
        occupation.send_keys("Engineer")  #Edit the occupation
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(5)
        occupation_info = self.driver.find_element(*AboutPageLocators.OCCUPATION_INFO)  #Locating the occupation info
        result = "Engineer" in occupation_info.text  #Checking that the info is updated
        return result

    def edit_home_town(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        home_town = self.driver.find_element(*AboutPageLocators.HOME_TOWN_TEXTBOX)  #Locating the home town textbox
        home_town.clear()  #clearing the textbox
        time.sleep(1)
        home_town.send_keys("Giza")  #Edit the home town
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        home_town_info = self.driver.find_element(*AboutPageLocators.HOME_TOWN_INFO)  #Locating the home town info
        print(home_town_info.text)
        result = "Giza" in home_town_info.text  #Checking that the info is updated
        return result

    def edit_city(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        city = self.driver.find_element(*AboutPageLocators.CITY_TEXTBOX)  #Locating the city textbox
        city.clear()  #clearing the textbox
        time.sleep(1)
        city.send_keys("Giza")  #Edit the city
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        city_info = self.driver.find_element(*AboutPageLocators.CITY_INFO)  #Locating the city info
        result = "Giza" in city_info.text  #Checking that the info is updated
        return result

    def edit_country(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        country = self.driver.find_element(*AboutPageLocators.COUNTRY_TEXTBOX)  #Locating the country textbox
        country.clear()  #clearing the textbox
        time.sleep(1)
        country.send_keys("Egypt")  #Edit the country
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        country_info = self.driver.find_element(*AboutPageLocators.COUNTRY_INFO)  #Locating the country info
        result = "Egypt" in country_info.text  #Checking that the info is updated
        return result

    def edit_facebook(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        facebook = self.driver.find_element(*AboutPageLocators.FACEBOOK_TEXTBOX)  #Locating the facebook textbox
        facebook.clear()  #clearing the textbox
        time.sleep(1)
        facebook.send_keys("MohamedAmr")  #Edit the facebook info
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        facebook_info = self.driver.find_element(*AboutPageLocators.FACEBOOK_INFO)  #Locating the facebook info
        result = "MohamedAmr" in facebook_info.text  #Checking that the info is updated
        return result

    def edit_twitter(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        twitter = self.driver.find_element(*AboutPageLocators.TWITTER_TEXTBOX)  #Locating the twitter textbox
        twitter.clear()  #clearing the textbox
        time.sleep(1)
        twitter.send_keys("MohamedAmr1")   #Edit the twitter info
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        twitter_info = self.driver.find_element(*AboutPageLocators.TWITTER_INFO)  #Locating the twitter info
        result = "MohamedAmr1" in twitter_info.text  #Checking that the info is updated
        return result

    def edit_instagram(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        instagram = self.driver.find_element(*AboutPageLocators.INSTAGRAM_TEXTBOX)  #Locating the instagram textbox
        instagram.clear()  #clearing the textbox
        time.sleep(1)
        instagram.send_keys("MohamedAmr2")  #Edit the instagram info
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        instagram_info = self.driver.find_element(*AboutPageLocators.INSTAGRAM_INFO)  #Locating the instagram info
        result = "MohamedAmr2" in instagram_info.text  #Checking that the info is updated
        return result

    def edit_pinterest(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        pinterest = self.driver.find_element(*AboutPageLocators.PINTEREST_TEXTBOX)  #Locating the pinterest textbox
        pinterest.clear()  #clearing the textbox
        time.sleep(1)
        pinterest.send_keys("MohamedAmr3")  #Edit the pinterest info
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)  #Locating the done button
        done.click()
        time.sleep(3)
        pinterest_info = self.driver.find_element(*AboutPageLocators.PINTEREST_INFO)  #Locating the pinterest info
        result = "MohamedAmr3" in pinterest_info.text  #Checking that the info is updated
        return result

    def edit_tumblr(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)  #Locating the edit button
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        tumblr = self.driver.find_element(*AboutPageLocators.TUMBLR_TEXTBOX)  #Locating the tumblr textbox
        tumblr.clear()  #clearing the textbox
        time.sleep(1)
        tumblr.send_keys("MohamedAmr4")  #Edit the tumblr info
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)   #Locating the done button
        done.click()
        time.sleep(3)
        tumblr_info = self.driver.find_element(*AboutPageLocators.TUMBLR_INFO)  #Locating the tumblr info
        result = "MohamedAmr4" in tumblr_info.text  #Checking that the info is updated
        return result






