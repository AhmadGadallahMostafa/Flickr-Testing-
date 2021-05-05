from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginTextElement(BasePageElement):
    def __init__(self, element_id):
        self.locator = element_id


class BasePage(object):
    driver = None

    def __init__(self, d):
        self.driver = d


class MainPage(BasePage):

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()


class LoginPage(BasePage):
    email_text = LoginTextElement("login-email")
    password_text = LoginTextElement("login-password")

    def go_next(self):
        next_button = self.driver.find_element(*LoginPageLocators.NEXT_BUTTON)
        next_button.click()


class HomePage(BasePage):
    def go_upload(self):
        upload = self.driver.find_element(*HomePageLocators.UPLOAD_ICON)
        upload.click()

    def go_to_photostream(self):
        you = self.driver.find_element(*HomePageLocators.YOU)
        you.click()


class UploadPage(BasePage):
    def title_matches(self):
        return "Upload" in self.driver.title

    def choose_file(self, files):
        choose_button = self.driver.find_element(*UploadPageLocators.CHOOSE_PHOTO)
        for i in range(0, len(files)):
            choose_button.send_keys("D:\\TV & Movies\\" + files[i])

    def confirm_upload(self):
        photostream_link = self.driver.find_element(*UploadPageLocators.PHOTOSTREAM_LINK).get_attribute("href")
        time.sleep(1)
        publish = self.driver.find_element(*UploadPageLocators.PUBLISH)
        action = ActionChains(self.driver)
        action.move_to_element(publish)
        action.click(publish)
        action.perform()
        self.driver.implicitly_wait(3)
        confirm_publish = self.driver.find_element(*UploadPageLocators.CONFRIM_PUBLISH)
        confirm_publish.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        url = self.driver.current_url
        return photostream_link in url

    def detects_invalid(self):
        user_messaging = self.driver.find_element(*UploadPageLocators.USER_MESSAGING)
        return "has-failed-files" in user_messaging.get_attribute("class")

    def remove_invalid(self):
        remove_button = self.driver.find_element(*UploadPageLocators.REMOVE_FILE_BUTTON)
        remove_button.click()

    def cancel_upload(self):
        publish = self.driver.find_element(*UploadPageLocators.PUBLISH)
        action = ActionChains(self.driver)
        action.move_to_element(publish)
        action.click(publish)
        action.perform()
        self.driver.implicitly_wait(3)
        confirm_publish = self.driver.find_element(*UploadPageLocators.CONFRIM_PUBLISH)
        confirm_publish.click()
        time.sleep(5)
        self.driver.close()


class PhotoStreamPage(BasePage):
    def picture_title_matches_upload(self, title_uploaded):
        self.driver.implicitly_wait(5)
        title_matches_upload = []
        picture_title = self.driver.find_elements(*PhotoStreamLocators.TITLE)

        for i in range(0, len(picture_title)):
            for j in range(0, len(title_uploaded)):
                if title_uploaded[j] in picture_title[i].get_attribute("title"):
                    title_matches_upload.append(True)
                    break
                else:
                    if j == len(title_uploaded)-1:
                        title_matches_upload.append(False)
        return all(title_matches_upload)


