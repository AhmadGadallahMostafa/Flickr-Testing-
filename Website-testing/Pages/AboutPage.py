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
        edit.click()
        time.sleep(10)
        occupation = self.driver.find_element(*AboutPageLocators.OCCUPATION_TEXTBOX)
        occupation.send_keys("Engineer")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        occupation_info = self.driver.find_element(*AboutPageLocators.OCCUPATION_INFO)
        result = "Engineer" in occupation_info.text
        return result

    def edit_home_town(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        home_town = self.driver.find_element(*AboutPageLocators.HOME_TOWN_TEXTBOX)
        home_town.send_keys("Giza")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        home_town_info = self.driver.find_element(*AboutPageLocators.HOME_TOWN_INFO)
        print(home_town_info.text)
        result = "Giza" in home_town_info.text
        return result

    def edit_city(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        city = self.driver.find_element(*AboutPageLocators.CITY_TEXTBOX)
        city.send_keys("Giza")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        city_info = self.driver.find_element(*AboutPageLocators.CITY_INFO)
        result = "Giza" in city_info.text
        return result

    def edit_country(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        country = self.driver.find_element(*AboutPageLocators.COUNTRY_TEXTBOX)
        country.send_keys("Egypt")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        country_info = self.driver.find_element(*AboutPageLocators.COUNTRY_INFO)
        result = "Egypt" in country_info.text
        return result

    def edit_facebook(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        facebook = self.driver.find_element(*AboutPageLocators.FACEBOOK_TEXTBOX)
        facebook.send_keys("Mohamed Amr")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        facebook_info = self.driver.find_element(*AboutPageLocators.FACEBOOK_INFO)
        result = "Mohamed Amr" in facebook_info.text
        return result

    def edit_twitter(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        twitter = self.driver.find_element(*AboutPageLocators.TWITTER_TEXTBOX)
        twitter.send_keys("Mohamed Amr 1")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        twitter_info = self.driver.find_element(*AboutPageLocators.TWITTER_INFO)
        result = "Mohamed Amr 1" in twitter_info.text
        return result

    def edit_instagram(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        instagram = self.driver.find_element(*AboutPageLocators.INSTAGRAM_TEXTBOX)
        instagram.send_keys("Mohamed Amr 2")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        instagram_info = self.driver.find_element(*AboutPageLocators.INSTAGRAM_INFO)
        result = "Mohamed Amr 2" in instagram_info.text
        return result

    def edit_pinterest(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        pinterest = self.driver.find_element(*AboutPageLocators.PINTEREST_TEXTBOX)
        pinterest.send_keys("Mohamed Amr 3")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        pinterest_info = self.driver.find_element(*AboutPageLocators.PINTEREST_INFO)
        result = "Mohamed Amr 3" in pinterest_info.text
        return result

    def edit_tumblr(self):
        edit = self.driver.find_element(*AboutPageLocators.EDIT)
        edit.click()
        time.sleep(10)
        tumblr = self.driver.find_element(*AboutPageLocators.TUMBLR_TEXTBOX)
        tumblr.send_keys("Mohamed Amr 4")
        time.sleep(10)
        done = self.driver.find_element(*AboutPageLocators.DONE)
        done.click()
        time.sleep(3)
        tumblr_info = self.driver.find_element(*AboutPageLocators.TUMBLR_INFO)
        result = "Mohamed Amr 4" in tumblr_info.text
        return result






