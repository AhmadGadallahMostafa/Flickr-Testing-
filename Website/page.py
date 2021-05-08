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

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def wrong_email_format(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("aaaa")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        time.sleep(2)
        email_warning = self.driver.find_element(*LoginPageLocators.EMAIL_WARNING)
        result = "Hmm… that's not an email address" in email_warning.text
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def no_email(self):
        self.driver.refresh()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        time.sleep(2)
        email_required = self.driver.find_element(*LoginPageLocators.EMAIL_REQUIRED)
        return "Required" in email_required.text 

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def right_email(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        time.sleep(2)
        result = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without the password we will check that the page isn't the home pag
    def no_password(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        login.click()
        time.sleep(5)
        result = self.driver.title
        return "Home" in result

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong password "Invalid password" will appear
    def wrong_password(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password.send_keys("aaaaaaaaaaaa")
        login.click()
        time.sleep(2)
        password_required = self.driver.find_element(*LoginPageLocators.PASSWORD_REQUIRED)
        return "Invalid password" in password_required.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong email and wrong password "Invalid email or password." will appear
    def wrong_email_and_wrong_password(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("karimamr3009@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password.send_keys("abcd12345678")
        login.click()
        time.sleep(2)
        invalid_email_or_password = self.driver.find_element(*LoginPageLocators.INVALID_EMAIL_OR_PASSWORD)
        return "Invalid email or password." in invalid_email_or_password.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a right email and right password the home page will be reached
    def right_email_and_right_password(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password.send_keys("abcd12345678")
        login.click()
        time.sleep(5)
        result = self.driver.title
        return "Home" in result


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

    def go_to_prints(self):
        self.driver.get("https://www.flickr.com/prints")

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
        

class LogoutPage(BasePage):
    # Tester: Mohamed Amr
    # In this function when we choose the log out button a block contains "Choose an account" will appear
    def logout(self):
        account = self.driver.find_element(*LogoutLocators.ACCOUNT)
        account.click()
        logout = self.driver.find_element(*LogoutLocators.LOGOUT)
        logout.click()
        time.sleep(5)
        result = self.driver.find_element(*LogoutLocators.CHOOSE_AN_ACCOUNT)
        return "Choose an account" in result.text


class SignupPage(BasePage):
    # Tester: Mohamed Amr
    # This function tests if we try to signup without the first name it must show the word required to the user
    def firstname(self):
        lastname = self.driver.find_element(*SignupPageLocators.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocators.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocators.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element(*SignupPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        firstname_required = self.driver.find_element(*SignupPageLocators.FIRST_NAME_REQUIRED)
        return firstname_required.text == "Required"

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def lastname(self):
        self.driver.refresh()
        firstname = self.driver.find_element(*SignupPageLocators.FIRST_NAME)
        firstname.send_keys("Mohamed")
        age = self.driver.find_element(*SignupPageLocators.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocators.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element(*SignupPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        lastname_required = self.driver.find_element(*SignupPageLocators.LAST_NAME_REQUIRED)
        return lastname_required.text == "Required"

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the age it must show the word required to the user
    def age(self):
        self.driver.refresh()
        firstname = self.driver.find_element(*SignupPageLocators.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocators.LAST_NAME)
        lastname.send_keys("Amr")
        email = self.driver.find_element(*SignupPageLocators.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        password = self.driver.find_element(*SignupPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        age_required = self.driver.find_element(*SignupPageLocators.AGE_REQUIRED)
        return age_required.text == "Required"

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the email it must show the word required to the user
    def email(self):
        self.driver.refresh()
        firstname = self.driver.find_element(*SignupPageLocators.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocators.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocators.AGE)
        age.send_keys("20")
        password = self.driver.find_element(*SignupPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        email_required = self.driver.find_element(*SignupPageLocators.EMAIL_REQUIRED)
        return email_required.text == "Required"

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the password it must show the word required to the user
    def password(self):
        self.driver.refresh()
        firstname = self.driver.find_element(*SignupPageLocators.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*SignupPageLocators.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*SignupPageLocators.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*SignupPageLocators.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        password_required = self.driver.find_element(*SignupPageLocators.PASSWORD_REQUIRED)
        return password_required.text == "Required"

    # Tester: Mohamed Amr
    # This function tests if we try to signup with age less than 13 years it must show "In order to use Flickr, you must be 13 or older"  to the user
    def valid_age(self):
        self.driver.refresh()
        age = self.driver.find_element(*SignupPageLocators.AGE)
        age.send_keys("9")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        age_warning = self.driver.find_element(*SignupPageLocators.AGE_WARNING)
        return age_warning.text == "In order to use Flickr, you must be 13 or older"

    # Tester: Mohamed Amr
    # This function tests if we try to signup with an email in a wrong format it must show "Invalid email"  to the user
    def valid_email(self):
        self.driver.refresh()
        email = self.driver.find_element(*SignupPageLocators.EMAIL)
        email.send_keys("mohamedamr866gmail.com")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        email_warning = self.driver.find_element(*SignupPageLocators.EMAIL_WARNING)
        return email_warning.text == "Invalid email"

    # Tester: Mohamed Amr
    # This function tests if we try to signup with a password less than 12 charachters  it must show "Invalid password"  to the user
    def valid_password(self):
        self.driver.refresh()
        password = self.driver.find_element(*SignupPageLocators.PASSWORD)
        password.send_keys("aaaaaaaaaaa")
        signup = self.driver.find_element(*SignupPageLocators.SIGNUP)
        signup.click()
        time.sleep(5)
        password_warning = self.driver.find_element(*SignupPageLocators.PASSWORD_WARNING)
        return password_warning.text == "Invalid password"

class PrintsPage(BasePage):
    # Tester: Mohamed Amr
    #In this function when we click on the choose photos button "Drag and drop your photo to upload or browse." will appear
    def choose_photo(self):
        choose_photo = self.driver.find_element(*PrintsPageLocators.CHOOSE_PHOTO)
        choose_photo.click()
        time.sleep(2)
        get_started = self.driver.find_element(*PrintsPageLocators.GET_STARTED)
        get_started.click()
        time.sleep(5)
        result = self.driver.find_element(*PrintsPageLocators.RESULT)
        return "Drag and drop your photo to upload or browse." in result.text
    
    def title_matches(self):
        time.sleep(2)
        result = self.driver.title
        return "Prints" in result

