from Pages.BasePage import BasePage
from Locators.HomePageLocators import HomePageLocators
from Locators.AboutPageLocators import AboutPageLocators
from Locators.SearchPeopleLocator import SearchPeoplePageLocators
from Locators.SearchGroupsLocators import SearchGroupsPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class AboutPage(BasePage):
    def edit_occupation(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        occupation = self.driver.find_element(*AboutPageLocators.OCCUPATION_TEXTBOX)
        occupation.clear()
        time.sleep(1)
        occupation.send_keys("Engineer")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(5)
        occupation_info = self.driver.find_element(*AboutPageLocators.OCCUPATION_INFO)
        result = "Engineer" in occupation_info.text
        return result

    def edit_home_town(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        home_town = self.driver.find_element(*AboutPageLocators.HOME_TOWN_TEXTBOX)
        home_town.clear()
        time.sleep(1)
        home_town.send_keys("Giza")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        home_town_info = self.driver.find_element(*AboutPageLocators.HOME_TOWN_INFO)
        print(home_town_info.text)
        result = "Giza" in home_town_info.text
        return result

    def edit_city(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        city = self.driver.find_element(*AboutPageLocators.CITY_TEXTBOX)
        city.clear()
        time.sleep(1)
        city.send_keys("Giza")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        city_info = self.driver.find_element(*AboutPageLocators.CITY_INFO)
        result = "Giza" in city_info.text
        return result

    def edit_country(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        country = self.driver.find_element(*AboutPageLocators.COUNTRY_TEXTBOX)
        country.clear()
        time.sleep(1)
        country.send_keys("Egypt")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        country_info = self.driver.find_element(*AboutPageLocators.COUNTRY_INFO)
        result = "Egypt" in country_info.text
        return result

    def edit_facebook(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        facebook = self.driver.find_element(*AboutPageLocators.FACEBOOK_TEXTBOX)
        facebook.clear()
        time.sleep(1)
        facebook.send_keys("MohamedAmr")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        facebook_info = self.driver.find_element(*AboutPageLocators.FACEBOOK_INFO)
        result = "MohamedAmr" in facebook_info.text
        return result

    def edit_twitter(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        twitter = self.driver.find_element(*AboutPageLocators.TWITTER_TEXTBOX)
        twitter.clear()
        time.sleep(1)
        twitter.send_keys("MohamedAmr1")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        twitter_info = self.driver.find_element(*AboutPageLocators.TWITTER_INFO)
        result = "MohamedAmr1" in twitter_info.text
        return result

    def edit_instagram(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        instagram = self.driver.find_element(*AboutPageLocators.INSTAGRAM_TEXTBOX)
        instagram.clear()
        time.sleep(1)
        instagram.send_keys("MohamedAmr2")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        instagram_info = self.driver.find_element(*AboutPageLocators.INSTAGRAM_INFO)
        result = "MohamedAmr2" in instagram_info.text
        return result

    def edit_pinterest(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        pinterest = self.driver.find_element(*AboutPageLocators.PINTEREST_TEXTBOX)
        pinterest.clear()
        time.sleep(1)
        pinterest.send_keys("MohamedAmr3")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        pinterest_info = self.driver.find_element(*AboutPageLocators.PINTEREST_INFO)
        result = "MohamedAmr3" in pinterest_info.text
        return result

    def edit_tumblr(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(2)
        edit.click()
        time.sleep(1)
        tumblr = self.driver.find_element(*AboutPageLocators.TUMBLR_TEXTBOX)
        tumblr.clear()
        time.sleep(1)
        tumblr.send_keys("MohamedAmr4")
        time.sleep(5)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        tumblr_info = self.driver.find_element(*AboutPageLocators.TUMBLR_INFO)
        result = "MohamedAmr4" in tumblr_info.text
        return result






