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

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def wrong_email_format(self):
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("aaaa")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_warning = self.driver.find_element(*LoginPageLocators.EMAIL_WARNING)
        result = "Hmm… that's not an email address" in email_warning.text

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def no_email(self):
        self.driver.refresh()
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_required = self.driver.find_element(*LoginPageLocators.EMAIL_REQUIRED)
        return email_required.text == "Required"

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def right_email(self):
        self.driver.refresh()
        email = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
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
        self.driver.implicitly_wait(2)
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
        self.driver.implicitly_wait(2)
        password_required = self.driver.find_element(*LoginPageLocators.PASSWORD_REQUIRED)
        return password_required.text == "Invalid password"

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
        self.driver.implicitly_wait(5)
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
        self.driver.implicitly_wait(5)
        result = self.driver.title
        return "Home" in result


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
