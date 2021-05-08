from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
        self.driver.implicitly_wait(10)
        you = self.driver.find_element(*HomePageLocators.YOU)
        you.click()
    
    def go_to_groups(self):
        self.driver.implicitly_wait(10)
        you = self.driver.find_element(*HomePageLocators.YOU)
        action = ActionChains(self.driver)
        action.move_to_element(you)
        groups = self.driver.find_element(*HomePageLocators.GROUPS_ICON)
        action.move_to_element(groups)
        action.click(groups)
        action.perform()

    def check_push_notifications(self):
        time.sleep(10)
        push_notifications = self.driver.find_element(*HomePageLocators.PUSH_NOTIFICATION)
        return len(push_notifications.text) != 0 
        #if not zero => true then we got a notification
    
    def send_notification(self):
        search = self.driver.find_element(*HomePageLocators.SEARCH_FIELD)
        search.send_keys("karimamr9")
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        search_people = self.driver.find_element(*HomePageLocators.SEARCH_PEOPLE)
        search_people.click()
        time.sleep(5)
        follow_button = self.driver.find_element(*SearchPeoplePageLocators.FOLLOW_BUTTON)
        follow_button.click()
        time.sleep(5)
        


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


class GroupsPage(BasePage):
    def title_matches(self):
        time.sleep(1)
        page_title = self.driver.title
        return "groups" in page_title

    def create_group_no_name(self):
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(1)
        next1.click()
        time.sleep(1)
        error_message = self.driver.find_element(*GroupsPageLocators.ERROR_TEXT)
        return "Please enter a group name" in error_message.text

    def create_group(self):
        self.driver.refresh()
        time.sleep(5)
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(2)
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("TESTGROUP12341256456741589")
        next1.click() #2nd next
        next1.click() #create group
        time.sleep(5)
        return "TESTGROUP12341256456741589" in self.driver.title

    def create_group_that_exists(self):
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("TESTGROUP12341256456741589")
        next1.click() #2nd next
        next1.click() #create group
        time.sleep(1)
        error_message = self.driver.find_element(*GroupsPageLocators.ERROR_TEXT)
        return "There is already a group with this name" in error_message.text

    def create_18_age_group(self):
        self.driver.refresh()
        time.sleep(5)
        create_group = self.driver.find_element(*GroupsPageLocators.CREATE_GROUP)
        create_group.click()
        time.sleep(2)
        next1 = self.driver.find_element(*GroupsPageLocators.NEXT)
        next1.click()
        time.sleep(2)
        group_name = self.driver.find_element(*GroupsPageLocators.GROUP_NAME_TEXT)
        group_name.send_keys("This is a test group20111 18+")
        #This is a test group 18+
        next1.click()
        check_adult = self.driver.find_element(*GroupsPageLocators.ADULT_GROUP_SELECTOR)
        check_adult.click()
        next1.click()
        time.sleep(5)
        group_text = self.driver.find_element(*GroupsPageLocators.GROUP_MESSAGE)
        return "group is 18+" in group_text.text

    def add_photo_to_group(self):
        time.sleep(5)
        group_link = self.driver.find_element(*GroupsPageLocators.GROUP_LINK)
        group_link.click()
        time.sleep(5)
        photo_pool = self.driver.find_element(*GroupsPageLocators.PHOTO_POOL)
        photo_pool.click()
        time.sleep(2)
        add_photo = self.driver.find_element(*GroupsPageLocators.ADD_PHOTO)
        add_photo.click()
        time.sleep(2)
        photo_box = self.driver.find_element(*GroupsPageLocators.PHOTO_BOX)
        photo_box.click()
        photo_box_selected = self.driver.find_element(*GroupsPageLocators.PHOTO_BOX_SELECTED)
        selected_title = photo_box_selected.get_attribute("title")
        add_to_group_button = self.driver.find_element(*GroupsPageLocators.ADD_TO_GROUP)
        add_to_group_button.click()
        time.sleep(5)
        uploaded_title = self.driver.find_element(*GroupsPageLocators.PHOTO_UPLOADED_TITLE)
        return selected_title in uploaded_title.text


class NotificationPage(BasePage):
    def check_last_notficiation(self):
        notification_icon = self.driver.find_element(*HomePageLocators.NOTIFICATIONS_ICON)
        notification_icon.click()
        time.sleep(1)
        last_notification = self.driver.find_element(*HomePageLocators.NOTIFICATION)
        return "karim amr is now following you" in last_notification.text
        






