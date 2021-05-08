from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
import AndroidLocator
import time


class WelcomePage:
    def __init__(self, d):
        self.driver = d

    def go(self):
        a = self.driver.find_element(*AndroidLocator.WelcomePageLocator.GET_STARTED)
        a.click()


class LoginPage:
    def __init__(self, d):
        self.driver = d

    def enter_email(self):
        email_field = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email_field.send_keys("karimamr9@outlook.com")
        next_button = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        next_button.click()
        self.driver.implicitly_wait(10)
        password = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        password.send_keys(",Q#8zUvxmSVJ-L^")
        sign_in = self.driver.find_element(*AndroidLocator.LoginPageLocator.SIGN_IN)
        sign_in.click()

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a wrong format an error message will appear to the user "Hmm… that's not an email address"
    def wrong_email_format(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("aaaa")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_warning = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_WARNING)
        result = "Hmm… that's not an email address" in email_warning.text
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without an email the word "Required" will appear
    def no_email(self):
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        email_required = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_REQUIRED)
        return "Required" in email_required.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with an email in a right format the password text box will appear
    def right_email(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        return result

    # Tester: Mohamed Amr
    # In this function if we try to log in without the password we will check that the page isn't the home page
    def no_password(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        login.click()
        self.driver.implicitly_wait(2)
        result = self.driver.find_element(*AndroidLocator.LoginPageLocator.PROFILE)

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong password "Invalid password" will appear
    def wrong_password(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        login.click()
        self.driver.implicitly_wait(2)
        password_required = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD_REQUIRED)
        return "Invalid password" in password_required.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a wrong email and wrong password "Invalid email or password." will appear
    def wrong_email_and_wrong_password(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("karimamr3009@gmail.com")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        password.send_keys("abcd12345678")
        login.click()
        self.driver.implicitly_wait(5)
        invalid_email_or_password = self.driver.find_element(*AndroidLocator.LoginPageLocator.INVALID_EMAIL_OR_PASSWORD)
        return "Invalid email or password." in invalid_email_or_password.text

    # Tester: Mohamed Amr
    # In this function if we try to log in with a right email and right password the home page will be reached
    def right_email_and_right_password(self):
        email = self.driver.find_element(*AndroidLocator.LoginPageLocator.EMAIL_FIELD)
        email.send_keys("mohamedamr866@gmail.com")
        login = self.driver.find_element(*AndroidLocator.LoginPageLocator.NEXT_BUTTON)
        login.click()
        self.driver.implicitly_wait(2)
        password = self.driver.find_element(*AndroidLocator.LoginPageLocator.PASSWORD)
        password.send_keys("abcd12345678")
        login.click()
        self.driver.implicitly_wait(5)
        result = self.driver.find_element(*AndroidLocator.LoginPageLocator.PROFILE)
        return result

class HomePage:
    def __init__(self, d):
        self.driver = d

    def go_to_upload(self):
        self.driver.implicitly_wait(5)
        upload_button = self.driver.find_element(*AndroidLocator.HomePageLocator.UPLOAD_ICON)
        upload_button.click()

    def go_to_photo_stream(self):
        profile_button = self.driver.find_element(*AndroidLocator.HomePageLocator.PHOTO_STREAM_ICON)
        profile_button.click()


class UploadPage:
    def __init__(self, d):
        self.driver = d

    def check_and_accept_permission(self):
        permission_block = self.driver.find_elements(*AndroidLocator.UploadPageLocator.PERMISSION_BLOCK)
        if permission_block:
            allow_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.ALLOW)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()
            self.driver.implicitly_wait(5)
            allow_button.click()

    def is_upload_page(self):
        camera_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.CAMERA_BUTTON)

    def take_picture(self):
        self.driver.implicitly_wait(5)
        camera_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.CAMERA_BUTTON)
        camera_button.click()
        self.driver.implicitly_wait(5)
        next_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.NEXT_BUTTON)
        next_button.click()
        title_text = self.driver.find_element(*AndroidLocator.UploadPageLocator.TITLE_TEXT)
        title_text.send_keys("Android camera upload")
        post_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.POST_BUTTON)
        post_button.click()

    def choose_from_gallery(self):
        time.sleep(1)
        gallery_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.GALLERY_BUTTON)
        gallery_button.click()
        time.sleep(1)
        downloads = self.driver.find_element(*AndroidLocator.UploadPageLocator.DOWNLOADS)
        downloads.click()
        time.sleep(1)
        picture = self.driver.find_element(*AndroidLocator.UploadPageLocator.PICKER_GRID)
        picture.click()
        time.sleep(1)
        done = self.driver.find_element(*AndroidLocator.UploadPageLocator.DONE)
        done.click()
        time.sleep(1)
        next_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.NEXT_BUTTON)
        next_button.click()
        time.sleep(1)
        title_text = self.driver.find_element(*AndroidLocator.UploadPageLocator.TITLE_TEXT)
        title_text.send_keys("Android gallery upload")
        time.sleep(1)
        post_button = self.driver.find_element(*AndroidLocator.UploadPageLocator.POST_BUTTON)
        post_button.click()
        


class PhotoStreamPage:
    def __init__(self, d):
        self.driver = d

    def check_last_uploaded_title_matches(self, title):
        time.sleep(10)
        picture_box = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.PICTURE_BOX)
        picture_box.click()
        self.driver.implicitly_wait(10)
        picture_title = self.driver.find_element(*AndroidLocator.PhotoViewPageLocator.TITLE)
        return title in picture_title.text

    def close_photo_view(self):
        close = self.driver.find_element(*AndroidLocator.PhotoViewPageLocator.CLOSE_BUTTON)
        close.click()
        self.driver.implicitly_wait(5)
        upload_icon = self.driver.find_element(*AndroidLocator.HomePageLocator.UPLOAD_ICON)
        upload_icon.click()

    def is_uploading(self):
        self.driver.implicitly_wait(5)
        status = self.driver.find_element(*AndroidLocator.PhotoStreamPageLocator.MESSAGE_BAR)
        return "Uploading" in status.text

class LogoutPage:
    def __init__(self, d):
        self.driver = d

    # Tester: Mohamed Amr
    # In this function when we choose the log out button Get Started button will appear
    def logout(self):
        profile = self.driver.find_element(*AndroidLocator.LogoutPageLocator.PROFILE)
        profile.click()
        settings = self.driver.find_element(*AndroidLocator.LogoutPageLocator.SETTINGS)
        settings.click()
        time.sleep(5)
        self.driver.swipe(470, 1400, 470, 1000, 400)
        signout = self.driver.find_element(*AndroidLocator.LogoutPageLocator.SIGNOUT)
        signout.click()
        result = self.driver.find_element(*AndroidLocator.LogoutPageLocator.GET_STARTED)
        return result

class SignupPage:
    def __init__(self, d):
        self.driver = d

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def first_name(self):
        lastname = self.driver.find_element(*AndroidLocator.SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        firstname_required = self.driver.find_element(*AndroidLocator.SignupPageLocator.FIRST_NAME_REQUIRED)
        return "Required" in firstname_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the last name it must show the word required to the user
    def last_name(self):
        firstname = self.driver.find_element(*AndroidLocator.SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        age = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        self.driver.implicitly_wait(5)
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        lastname_required = self.driver.find_element(*AndroidLocator.SignupPageLocator.LAST_NAME_REQUIRED)
        return "Required" in lastname_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the age it must show the word required to the user
    def age(self):
        firstname = self.driver.find_element(*AndroidLocator.SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*AndroidLocator.SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        email = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        self.driver.implicitly_wait(5)
        age_required = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE_REQUIRED)
        return "Required" in age_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the email it must show the word required to the user
    def email(self):
        firstname = self.driver.find_element(*AndroidLocator.SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*AndroidLocator.SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE)
        age.send_keys("20")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        email_required = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL_REQUIRED)
        return "Required" in email_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup without the password it must show the word required to the user
    def password(self):
        firstname = self.driver.find_element(*AndroidLocator.SignupPageLocator.FIRST_NAME)
        firstname.send_keys("Mohamed")
        lastname = self.driver.find_element(*AndroidLocator.SignupPageLocator.LAST_NAME)
        lastname.send_keys("Amr")
        age = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE)
        age.send_keys("20")
        email = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866@gmail.com")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(10)
        password_required = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD_REQUIRED)
        return "Required" in password_required.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with age less than 13 years it must show "In order to use Flickr, you must be 13 or older"  to the user
    def valid_age(self):
        age = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE)
        age.send_keys("9")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        age_warning = self.driver.find_element(*AndroidLocator.SignupPageLocator.AGE_WARNING)
        return "In order to use Flickr, you must be 13 or older" in age_warning.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with an email in a wrong format it must show "Invalid email"  to the user
    def valid_email(self):
        email = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL)
        email.send_keys("mohamedamr866gmail.com")
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        email_warning = self.driver.find_element(*AndroidLocator.SignupPageLocator.EMAIL_WARNING)
        return "Invalid email" in email_warning.text

    # Tester: Mohamed Amr
    # This function tests if we try to signup with a password less than 12 charachters  it must show "Invalid password"  to the user
    def valid_password(self):
        down = self.driver.find_element(*AndroidLocator.SignupPageLocator.DOWN)
        down.click()
        password = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD)
        password.send_keys("aaaaaaaaaaa")
        down.click()
        signup = self.driver.find_element(*AndroidLocator.SignupPageLocator.SIGNUP)
        signup.click()
        time.sleep(5)
        password_warning = self.driver.find_element(*AndroidLocator.SignupPageLocator.PASSWORD_WARNING)
        print(password_warning.text)
        return "Invalid password" in password_warning.text
